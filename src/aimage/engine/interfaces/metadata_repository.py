from __future__ import annotations

from typing import Protocol

from aimage.contracts.common import ContractModel
from aimage.contracts.execution import ArtifactRecord, RunRecord


class MetadataRepository(Protocol):
    def save_object(self, record: ContractModel) -> None: ...
    def save_artifact(self, record: ArtifactRecord) -> None: ...
    def save_run(self, record: RunRecord) -> None: ...
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
