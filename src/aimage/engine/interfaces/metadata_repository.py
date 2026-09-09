from __future__ import annotations

from datetime import datetime
from typing import Protocol

from aimage.contracts.common import ContractModel
from aimage.contracts.execution import ArtifactRecord, RunRecord
from aimage.contracts.visual_intent import ArtifactDispositionRecord, BaselineRecord, DecisionRecord


class MetadataRepository(Protocol):
    def save_object(self, record: ContractModel) -> None: ...
    def save_artifact(self, record: ArtifactRecord) -> None: ...
    def save_decision(self, job_id: str, decision: DecisionRecord) -> None: ...
    def save_baseline(self, job_id: str, baseline: BaselineRecord) -> None: ...
    def save_artifact_disposition(self, job_id: str, disposition: ArtifactDispositionRecord) -> None: ...
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
    ) -> None: ...
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
    ) -> None: ...
    def claim_or_assert_current(self, job_id: str, semantic_revision: int, intent_digest: str) -> None: ...
    def assert_current(self, job_id: str, semantic_revision: int, intent_digest: str) -> None: ...
    def advance_current(
        self,
        job_id: str,
        *,
        expected_revision: int,
        expected_digest: str,
        new_revision: int,
        new_digest: str,
    ) -> None: ...
