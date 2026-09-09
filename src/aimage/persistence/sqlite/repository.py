from __future__ import annotations

import json
from datetime import datetime

from sqlalchemy import Engine, insert, select, update

from aimage.contracts.common import ContractModel, DerivedContractModel, utc_now
from aimage.contracts.execution import ArtifactRecord, RunRecord
from aimage.contracts.resolution import ProviderCapabilityDescriptor
from aimage.contracts.validation import ValidationReport
from aimage.contracts.visual_intent import (
    ArtifactDispositionRecord,
    BaselineRecord,
    DecisionRecord,
    VisualIntentState,
)
from aimage.engine.capabilities import descriptor_signature
from aimage.engine.compile import visual_intent_digest
from aimage.engine.currentness import StaleStateError

from .schema import (
    artifact_dispositions,
    artifacts,
    baselines,
    capability_descriptors,
    decisions,
    derived_documents,
    jobs,
    metadata,
    runs,
    semantic_documents,
    semantic_support_documents,
    validation_reports,
)
from .transactions import AIMAGE_BEGIN_IMMEDIATE


class ImmutableRecordConflictError(RuntimeError):
    pass


class RunStateError(RuntimeError):
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
    def _now(value: datetime | None = None) -> str:
        return (value or utc_now()).isoformat()

    @staticmethod
    def _insert_immutable(connection, table, key_condition, key_label: str, values: dict[str, object]) -> None:  # type: ignore[no-untyped-def]
        result = connection.execute(insert(table).prefix_with("OR IGNORE"), values)
        if result.rowcount == 1:
            return
        existing = connection.execute(select(table).where(key_condition)).mappings().one()
        mismatches = {name: (existing[name], value) for name, value in values.items() if existing[name] != value}
        if mismatches:
            raise ImmutableRecordConflictError(
                f"immutable record {key_label!r} reused with different content: {sorted(mismatches)}"
            )

    def save_object(self, record: ContractModel) -> None:
        payload = record.model_dump(mode="json")
        encoded = self._json(payload)
        now = self._now()
        with self.engine.begin() as connection:
            if isinstance(record, VisualIntentState):
                values = {
                    "object_id": record.object_id,
                    "job_id": record.job_id,
                    "semantic_revision": record.semantic_revision,
                    "schema_version": record.schema_version,
                    "intent_digest": visual_intent_digest(record),
                    "payload_json": encoded,
                    "created_at": now,
                }
                self._insert_immutable(
                    connection,
                    semantic_documents,
                    semantic_documents.c.object_id == record.object_id,
                    record.object_id,
                    values,
                )
                return

            if isinstance(record, ProviderCapabilityDescriptor):
                values = {
                    "descriptor_id": record.descriptor_id,
                    "descriptor_digest": descriptor_signature(record),
                    "target_id": record.target_id,
                    "adapter_id": record.adapter_id,
                    "adapter_version": record.adapter_version,
                    "target_model_version": record.target_version_or_model,
                    "evidence_kind": record.evidence_kind.value,
                    "evidence_uri": record.evidence_uri,
                    "observed_at": record.observed_at.isoformat(),
                    "payload_json": encoded,
                }
                self._insert_immutable(
                    connection,
                    capability_descriptors,
                    capability_descriptors.c.descriptor_id == record.descriptor_id,
                    record.descriptor_id,
                    values,
                )
                return

            if isinstance(record, ValidationReport):
                first = record.results[0] if record.results else None
                provenance = [
                    {
                        "result_id": result.result_id,
                        "evaluator_identity": result.evaluator_identity,
                        "evaluator_version": result.evaluator_version,
                        "evidence_class": result.evidence_class,
                        "evidence_refs": result.evidence_refs,
                        "correlation_note": result.correlation_note,
                        "calibration_ref": result.calibration_ref,
                    }
                    for result in record.results
                ]
                values = {
                    "report_id": record.report_id,
                    "artifact_ref": record.artifact_ref,
                    "job_id": record.job_id,
                    "semantic_revision": record.semantic_revision,
                    "render_spec_ref": record.render_spec_ref,
                    "execution_plan_ref": record.execution_plan_ref,
                    "overall_outcome": record.overall_outcome.value,
                    "evaluator_identity": first.evaluator_identity if first else None,
                    "evaluator_version": first.evaluator_version if first else None,
                    "evidence_class": first.evidence_class if first else None,
                    "evaluator_provenance_json": self._json(provenance),
                    "calibration_ref": first.calibration_ref if first else None,
                    "correlation_note": first.correlation_note if first else None,
                    "payload_json": encoded,
                    "created_at": now,
                }
                self._insert_immutable(
                    connection,
                    validation_reports,
                    validation_reports.c.report_id == record.report_id,
                    record.report_id,
                    values,
                )
                return

            if isinstance(record, DerivedContractModel):
                values = {
                    "object_id": record.object_id,
                    "contract_type": record.contract_type,
                    "job_id": record.job_id,
                    "source_semantic_revision": record.source_semantic_revision,
                    "source_intent_digest": record.source_intent_digest,
                    "schema_version": record.schema_version,
                    "payload_json": encoded,
                    "created_at": now,
                }
                self._insert_immutable(
                    connection,
                    derived_documents,
                    derived_documents.c.object_id == record.object_id,
                    record.object_id,
                    values,
                )
                return

            values = {
                "object_id": record.object_id,
                "contract_type": record.contract_type,
                "job_id": record.job_id,
                "semantic_revision": record.semantic_revision,
                "schema_version": record.schema_version,
                "payload_json": encoded,
                "created_at": now,
            }
            self._insert_immutable(
                connection,
                semantic_support_documents,
                semantic_support_documents.c.object_id == record.object_id,
                record.object_id,
                values,
            )

    def save_decision(self, job_id: str, decision: DecisionRecord) -> None:
        values = {
            "decision_id": decision.decision_id,
            "job_id": job_id,
            "base_semantic_revision": decision.base_semantic_revision,
            "kind": decision.kind.value,
            "subject_ref": decision.subject_ref,
            "resulting_semantic_revision": decision.resulting_semantic_revision,
            "payload_json": self._json(decision.model_dump(mode="json")),
        }
        with self.engine.begin() as connection:
            self._insert_immutable(
                connection,
                decisions,
                decisions.c.decision_id == decision.decision_id,
                decision.decision_id,
                values,
            )

    def save_baseline(self, job_id: str, baseline: BaselineRecord) -> None:
        values = {
            "baseline_id": baseline.baseline_id,
            "job_id": job_id,
            "approved_at_revision": baseline.approved_at_revision,
            "approval_decision_id": baseline.approval_decision_id,
            "status": baseline.status.value,
            "payload_json": self._json(baseline.model_dump(mode="json")),
        }
        with self.engine.begin() as connection:
            self._insert_immutable(
                connection,
                baselines,
                baselines.c.baseline_id == baseline.baseline_id,
                baseline.baseline_id,
                values,
            )

    def save_artifact_disposition(self, job_id: str, disposition: ArtifactDispositionRecord) -> None:
        values = {
            "artifact_ref": disposition.artifact_ref,
            "semantic_revision": disposition.semantic_revision,
            "status": disposition.status.value,
            "job_id": job_id,
            "basis_decision_id": disposition.basis_decision_id,
            "payload_json": self._json(disposition.model_dump(mode="json")),
        }
        condition = (
            (artifact_dispositions.c.artifact_ref == disposition.artifact_ref)
            & (artifact_dispositions.c.semantic_revision == disposition.semantic_revision)
            & (artifact_dispositions.c.status == disposition.status.value)
        )
        key = f"{disposition.artifact_ref}:{disposition.semantic_revision}:{disposition.status.value}"
        with self.engine.begin() as connection:
            self._insert_immutable(connection, artifact_dispositions, condition, key, values)

    def save_artifact(self, record: ArtifactRecord) -> None:
        storage_ref = record.media_metadata.get("storage_ref")
        if not isinstance(storage_ref, str):
            raise ValueError("ArtifactRecord media_metadata must carry storage_ref")
        values = {
            "artifact_id": record.artifact_id,
            "job_id": record.job_id,
            "source_semantic_revision": record.semantic_revision,
            "content_digest": record.content_digest,
            "blob_key": storage_ref,
            "media_metadata_json": self._json(record.media_metadata),
            "producing_run_ref": record.producing_run_ref,
            "created_at": self._now(),
        }
        with self.engine.begin() as connection:
            self._insert_immutable(
                connection,
                artifacts,
                artifacts.c.artifact_id == record.artifact_id,
                record.artifact_id,
                values,
            )

    def start_run(
        self,
        *,
        run_id: str,
        job_id: str,
        semantic_revision: int,
        source_intent_digest: str,
        execution_plan_ref: str,
        capability_descriptor_ref: str | None,
        target_model_version: str | None,
        attempt_index: int = 0,
        started_at: datetime | None = None,
    ) -> None:
        values = {
            "run_id": run_id,
            "job_id": job_id,
            "source_semantic_revision": semantic_revision,
            "source_intent_digest": source_intent_digest,
            "execution_plan_ref": execution_plan_ref,
            "capability_descriptor_ref": capability_descriptor_ref,
            "target_model_version": target_model_version,
            "actual_targets_json": self._json(()),
            "outputs_json": self._json(()),
            "raw_provider_result_ref": None,
            "usage_json": self._json({}),
            "provider_request_id": None,
            "status": "started",
            "attempt_index": attempt_index,
            "normalized_error_class": None,
            "raw_provider_evidence_json": None,
            "started_at": self._now(started_at),
            "finished_at": None,
        }
        with self.engine.begin() as connection:
            self._insert_immutable(connection, runs, runs.c.run_id == run_id, run_id, values)

    def finish_run(
        self,
        record: RunRecord,
        *,
        source_intent_digest: str,
        capability_descriptor_ref: str | None,
        status: str,
        normalized_error_class: str | None = None,
        raw_provider_evidence: dict[str, object] | None = None,
        finished_at: datetime | None = None,
    ) -> None:
        with self.engine.begin() as connection:
            existing = connection.execute(select(runs).where(runs.c.run_id == record.run_id)).mappings().one_or_none()
            if existing is None:
                raise RunStateError("run must be persisted as started before completion")
            static_expected = {
                "job_id": record.job_id,
                "source_semantic_revision": record.semantic_revision,
                "source_intent_digest": source_intent_digest,
                "execution_plan_ref": record.execution_plan_ref,
                "capability_descriptor_ref": capability_descriptor_ref,
            }
            if any(existing[name] != value for name, value in static_expected.items()):
                raise RunStateError("run completion does not match immutable started identity/currentness fields")
            if existing["status"] != "started":
                raise RunStateError("run can finish exactly once")
            connection.execute(
                update(runs)
                .where(runs.c.run_id == record.run_id)
                .values(
                    target_model_version=(record.actual_target_versions[0] if record.actual_target_versions else None),
                    actual_targets_json=self._json(record.actual_target_versions),
                    outputs_json=self._json(record.output_artifact_refs),
                    raw_provider_result_ref=record.raw_provider_result_ref,
                    usage_json=self._json(record.usage_cost_latency),
                    provider_request_id=record.provider_request_id,
                    status=status,
                    normalized_error_class=normalized_error_class,
                    raw_provider_evidence_json=self._json(raw_provider_evidence or {}),
                    finished_at=self._now(finished_at),
                )
            )

    def _begin_immediate(self):  # type: ignore[no-untyped-def]
        connection = self.engine.connect().execution_options(**{AIMAGE_BEGIN_IMMEDIATE: True})
        try:
            connection.begin()
        except Exception:
            connection.close()
            raise
        return connection

    def claim_or_assert_current(self, job_id: str, semantic_revision: int, intent_digest: str) -> None:
        connection = self._begin_immediate()
        try:
            row = connection.execute(select(jobs).where(jobs.c.job_id == job_id)).mappings().first()
            if row is None:
                connection.execute(
                    insert(jobs),
                    {
                        "job_id": job_id,
                        "current_semantic_revision": semantic_revision,
                        "current_intent_digest": intent_digest,
                        "lifecycle_state": "active",
                        "accepted_artifact_id": None,
                        "updated_at": self._now(),
                    },
                )
            elif (
                row["current_semantic_revision"] != semantic_revision
                or row["current_intent_digest"] != intent_digest
            ):
                raise StaleStateError("job currentness differs from requested semantic state")
            connection.commit()
        except Exception:
            connection.rollback()
            raise
        finally:
            connection.close()

    def assert_current(self, job_id: str, semantic_revision: int, intent_digest: str) -> None:
        with self.engine.connect() as connection:
            row = connection.execute(select(jobs).where(jobs.c.job_id == job_id)).mappings().first()
        if row is None or row["current_semantic_revision"] != semantic_revision or row["current_intent_digest"] != intent_digest:
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
                update(jobs)
                .where(jobs.c.job_id == job_id)
                .where(jobs.c.current_semantic_revision == expected_revision)
                .where(jobs.c.current_intent_digest == expected_digest)
                .values(
                    current_semantic_revision=new_revision,
                    current_intent_digest=new_digest,
                    updated_at=self._now(),
                )
            )
            if result.rowcount != 1:
                raise StaleStateError("cannot advance current state from a stale preimage")
            connection.commit()
        except Exception:
            connection.rollback()
            raise
        finally:
            connection.close()
