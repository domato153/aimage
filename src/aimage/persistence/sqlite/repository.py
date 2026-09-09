from __future__ import annotations

import json

from sqlalchemy import Engine, insert, select, update

from aimage.contracts.common import ContractModel
from aimage.contracts.execution import ArtifactRecord, RunRecord
from aimage.engine.currentness import StaleStateError

from .schema import artifacts, job_current, metadata, object_records, runs


class SQLiteMetadataRepository:
    def __init__(self, engine: Engine, *, create_schema: bool = False) -> None:
        self.engine = engine
        if create_schema:
            metadata.create_all(engine)

    @staticmethod
    def _json(value: object) -> str:
        return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, default=str)

    def save_object(self, record: ContractModel) -> None:
        payload = record.model_dump(mode="json")
        with self.engine.begin() as connection:
            connection.execute(
                insert(object_records).prefix_with("OR REPLACE"),
                {
                    "object_id": record.object_id,
                    "job_id": record.job_id,
                    "contract_type": record.contract_type,
                    "semantic_revision": record.semantic_revision,
                    "payload_json": self._json(payload),
                },
            )

    def save_artifact(self, record: ArtifactRecord) -> None:
        with self.engine.begin() as connection:
            connection.execute(
                insert(artifacts).prefix_with("OR REPLACE"),
                {
                    "artifact_id": record.artifact_id,
                    "job_id": record.job_id,
                    "semantic_revision": record.semantic_revision,
                    "content_digest": record.content_digest,
                    "media_json": self._json(record.media_metadata),
                    "producing_run_ref": record.producing_run_ref,
                },
            )

    def save_run(self, record: RunRecord) -> None:
        with self.engine.begin() as connection:
            connection.execute(
                insert(runs).prefix_with("OR REPLACE"),
                {
                    "run_id": record.run_id,
                    "job_id": record.job_id,
                    "semantic_revision": record.semantic_revision,
                    "execution_plan_ref": record.execution_plan_ref,
                    "actual_targets_json": self._json(record.actual_target_versions),
                    "outputs_json": self._json(record.output_artifact_refs),
                    "raw_provider_result_ref": record.raw_provider_result_ref,
                    "usage_json": self._json(record.usage_cost_latency),
                    "provider_request_id": record.provider_request_id,
                },
            )

    def _begin_immediate(self):  # type: ignore[no-untyped-def]
        connection = self.engine.connect()
        connection.exec_driver_sql("BEGIN IMMEDIATE")
        return connection

    def claim_or_assert_current(self, job_id: str, semantic_revision: int, intent_digest: str) -> None:
        connection = self._begin_immediate()
        try:
            row = connection.execute(select(job_current).where(job_current.c.job_id == job_id)).mappings().first()
            if row is None:
                connection.execute(
                    insert(job_current),
                    {"job_id": job_id, "semantic_revision": semantic_revision, "intent_digest": intent_digest},
                )
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

    def advance_current(
        self,
        job_id: str,
        *,
        expected_revision: int,
        expected_digest: str,
        new_revision: int,
        new_digest: str,
    ) -> None:
        connection = self._begin_immediate()
        try:
            result = connection.execute(
                update(job_current)
                .where(job_current.c.job_id == job_id)
                .where(job_current.c.semantic_revision == expected_revision)
                .where(job_current.c.intent_digest == expected_digest)
                .values(semantic_revision=new_revision, intent_digest=new_digest)
            )
            if result.rowcount != 1:
                raise StaleStateError("cannot advance current state from a stale preimage")
            connection.commit()
        except Exception:
            connection.rollback()
            raise
        finally:
            connection.close()
