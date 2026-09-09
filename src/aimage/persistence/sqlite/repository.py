from __future__ import annotations

import json

from sqlalchemy import Engine, insert, select, update

from aimage.contracts.common import ContractModel
from aimage.contracts.execution import ArtifactRecord, RunRecord
from aimage.engine.currentness import StaleStateError
from .schema import artifacts, job_current, metadata, object_records, runs
from .transactions import AIMAGE_BEGIN_IMMEDIATE


class ImmutableRecordConflictError(RuntimeError):
    pass


class SQLiteMetadataRepository:
    def __init__(self, engine: Engine, *, create_schema: bool = False) -> None:
        self.engine = engine
        if create_schema:
            metadata.create_all(engine)

    @staticmethod
    def _json(value: object) -> str:
        return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, default=str)

    @staticmethod
    def _insert_immutable(connection, table, key_column, key: str, values: dict[str, object]) -> None:  # type: ignore[no-untyped-def]
        result = connection.execute(insert(table).prefix_with("OR IGNORE"), values)
        if result.rowcount == 1:
            return
        existing = connection.execute(select(table).where(key_column == key)).mappings().one()
        mismatches = {name: (existing[name], value) for name, value in values.items() if existing[name] != value}
        if mismatches:
            raise ImmutableRecordConflictError(f"immutable record id {key!r} reused with different content: {sorted(mismatches)}")

    def save_object(self, record: ContractModel) -> None:
        values = {"object_id": record.object_id, "job_id": record.job_id, "contract_type": record.contract_type, "semantic_revision": record.semantic_revision, "payload_json": self._json(record.model_dump(mode="json"))}
        with self.engine.begin() as connection:
            self._insert_immutable(connection, object_records, object_records.c.object_id, record.object_id, values)

    def save_artifact(self, record: ArtifactRecord) -> None:
        values = {"artifact_id": record.artifact_id, "job_id": record.job_id, "semantic_revision": record.semantic_revision, "content_digest": record.content_digest, "media_json": self._json(record.media_metadata), "producing_run_ref": record.producing_run_ref}
        with self.engine.begin() as connection:
            self._insert_immutable(connection, artifacts, artifacts.c.artifact_id, record.artifact_id, values)

    def save_run(self, record: RunRecord) -> None:
        values = {"run_id": record.run_id, "job_id": record.job_id, "semantic_revision": record.semantic_revision, "execution_plan_ref": record.execution_plan_ref, "actual_targets_json": self._json(record.actual_target_versions), "outputs_json": self._json(record.output_artifact_refs), "raw_provider_result_ref": record.raw_provider_result_ref, "usage_json": self._json(record.usage_cost_latency), "provider_request_id": record.provider_request_id}
        with self.engine.begin() as connection:
            self._insert_immutable(connection, runs, runs.c.run_id, record.run_id, values)

    def _begin_immediate(self):  # type: ignore[no-untyped-def]
        connection = self.engine.connect().execution_options(**{AIMAGE_BEGIN_IMMEDIATE: True})
        try:
            # Starting the SQLAlchemy transaction triggers the engine's begin event,
            # which emits exactly one BEGIN IMMEDIATE for this connection.
            connection.begin()
        except Exception:
            connection.close()
            raise
        return connection

    def claim_or_assert_current(self, job_id: str, semantic_revision: int, intent_digest: str) -> None:
        connection = self._begin_immediate()
        try:
            row = connection.execute(select(job_current).where(job_current.c.job_id == job_id)).mappings().first()
            if row is None:
                connection.execute(insert(job_current), {"job_id": job_id, "semantic_revision": semantic_revision, "intent_digest": intent_digest})
            elif row["semantic_revision"] != semantic_revision or row["intent_digest"] != intent_digest:
                raise StaleStateError("job currentness differs from requested semantic state")
            connection.commit()
        except Exception:
            connection.rollback()
            raise
        finally:
            connection.close()

    def assert_current(self, job_id: str, semantic_revision: int, intent_digest: str) -> None:
        with self.engine.connect() as connection:
            row = connection.execute(select(job_current).where(job_current.c.job_id == job_id)).mappings().first()
        if row is None or row["semantic_revision"] != semantic_revision or row["intent_digest"] != intent_digest:
            raise StaleStateError("in-flight result belongs to stale semantic state")

    def advance_current(self, job_id: str, *, expected_revision: int, expected_digest: str, new_revision: int, new_digest: str) -> None:
        connection = self._begin_immediate()
        try:
            result = connection.execute(update(job_current).where(job_current.c.job_id == job_id).where(job_current.c.semantic_revision == expected_revision).where(job_current.c.intent_digest == expected_digest).values(semantic_revision=new_revision, intent_digest=new_digest))
            if result.rowcount != 1:
                raise StaleStateError("cannot advance current state from a stale preimage")
            connection.commit()
        except Exception:
            connection.rollback()
            raise
        finally:
            connection.close()
