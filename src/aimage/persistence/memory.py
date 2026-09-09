from __future__ import annotations

from datetime import datetime
from threading import RLock

from aimage.contracts.common import ContractModel
from aimage.contracts.execution import ArtifactRecord, RunRecord
from aimage.contracts.visual_intent import ArtifactDispositionRecord, BaselineRecord, DecisionRecord
from aimage.engine.currentness import StaleStateError


class InMemoryMetadataRepository:
    """Reference repository implementation for replacement-contract tests.

    It intentionally models the same identity/currentness semantics as SQLite without
    becoming production authority. A lock keeps compare/advance operations atomic within
    one process.
    """

    def __init__(self) -> None:
        self._lock = RLock()
        self.objects: dict[str, ContractModel] = {}
        self.artifacts: dict[str, ArtifactRecord] = {}
        self.decisions: dict[str, DecisionRecord] = {}
        self.baselines: dict[str, BaselineRecord] = {}
        self.dispositions: dict[tuple[str, int, str], ArtifactDispositionRecord] = {}
        self.runs: dict[str, dict[str, object]] = {}
        self.current: dict[str, tuple[int, str]] = {}

    @staticmethod
    def _put_immutable(mapping: dict, key: object, value: object) -> None:  # type: ignore[type-arg]
        existing = mapping.get(key)
        if existing is None:
            mapping[key] = value
        elif existing != value:
            raise ValueError(f"immutable record key {key!r} reused with different content")

    def save_object(self, record: ContractModel) -> None:
        with self._lock:
            self._put_immutable(self.objects, record.object_id, record)

    def save_artifact(self, record: ArtifactRecord) -> None:
        with self._lock:
            self._put_immutable(self.artifacts, record.artifact_id, record)

    def save_decision(self, job_id: str, decision: DecisionRecord) -> None:
        del job_id
        with self._lock:
            self._put_immutable(self.decisions, decision.decision_id, decision)

    def save_baseline(self, job_id: str, baseline: BaselineRecord) -> None:
        del job_id
        with self._lock:
            self._put_immutable(self.baselines, baseline.baseline_id, baseline)

    def save_artifact_disposition(self, job_id: str, disposition: ArtifactDispositionRecord) -> None:
        del job_id
        key = (disposition.artifact_ref, disposition.semantic_revision, disposition.status.value)
        with self._lock:
            self._put_immutable(self.dispositions, key, disposition)

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
        value = {
            "run_id": run_id,
            "job_id": job_id,
            "semantic_revision": semantic_revision,
            "source_intent_digest": source_intent_digest,
            "execution_plan_ref": execution_plan_ref,
            "capability_descriptor_ref": capability_descriptor_ref,
            "target_model_version": target_model_version,
            "attempt_index": attempt_index,
            "started_at": started_at,
            "status": "started",
            "record": None,
        }
        with self._lock:
            self._put_immutable(self.runs, run_id, value)

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
        with self._lock:
            existing = self.runs.get(record.run_id)
            if existing is None or existing["status"] != "started":
                raise ValueError("run must exist in started state and can finish once")
            expected = (
                existing["job_id"],
                existing["semantic_revision"],
                existing["source_intent_digest"],
                existing["execution_plan_ref"],
                existing["capability_descriptor_ref"],
            )
            actual = (
                record.job_id,
                record.semantic_revision,
                source_intent_digest,
                record.execution_plan_ref,
                capability_descriptor_ref,
            )
            if expected != actual:
                raise ValueError("run completion differs from started identity/currentness fields")
            existing.update(
                {
                    "status": status,
                    "record": record,
                    "normalized_error_class": normalized_error_class,
                    "raw_provider_evidence": raw_provider_evidence or {},
                    "finished_at": finished_at,
                }
            )

    def claim_or_assert_current(self, job_id: str, semantic_revision: int, intent_digest: str) -> None:
        with self._lock:
            current = self.current.get(job_id)
            requested = (semantic_revision, intent_digest)
            if current is None:
                self.current[job_id] = requested
            elif current != requested:
                raise StaleStateError("job currentness differs from requested semantic state")

    def assert_current(self, job_id: str, semantic_revision: int, intent_digest: str) -> None:
        with self._lock:
            if self.current.get(job_id) != (semantic_revision, intent_digest):
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
        with self._lock:
            if self.current.get(job_id) != (expected_revision, expected_digest):
                raise StaleStateError("cannot advance current state from a stale preimage")
            self.current[job_id] = (new_revision, new_digest)
