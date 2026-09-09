from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Protocol

from aimage.contracts.resolution import ProviderCapabilityDescriptor


@dataclass(frozen=True)
class ProviderExecutionResult:
    artifact_bytes: bytes
    media_type: str
    provider_request_id: str | None
    actual_target_version: str
    raw_provider_result_ref: str | None = None
    usage: dict[str, Any] | None = None


class CapabilityReportingProvider(Protocol):
    def capability_descriptor(self, *, job_id: str, semantic_revision: int) -> ProviderCapabilityDescriptor: ...
