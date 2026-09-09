from __future__ import annotations

from datetime import datetime
from enum import StrEnum
from typing import Any

from pydantic import BaseModel, ConfigDict, Field

from .common import ContractModel, EvidenceKind, new_object_id


class Capability(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    namespace: str
    name: str
    attributes: dict[str, Any] = {}
    limits: dict[str, Any] = {}


class ProviderCapabilityDescriptor(ContractModel):
    contract_type: str = "provider_capability_descriptor"
    descriptor_id: str = Field(default_factory=new_object_id)
    target_id: str
    target_kind: str
    adapter_id: str
    adapter_version: str
    target_version_or_model: str
    observed_at: datetime
    valid_until: datetime | None = None
    evidence_kind: EvidenceKind
    evidence_uri: str
    capabilities: tuple[Capability, ...] = ()
    known_limits: tuple[str, ...] = ()


class ResolutionStatus(StrEnum):
    RESOLVED = "resolved"
    UNSATISFIED = "unsatisfied"
    STALE_CAPABILITIES = "stale_capabilities"


class RequirementWiring(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    requirement_id: str
    target_descriptor_ref: str
    capability_name: str


class ResolutionResult(ContractModel):
    contract_type: str = "resolution_result"
    resolution_id: str = Field(default_factory=new_object_id)
    render_spec_ref: str
    requirement_set_ref: str
    status: ResolutionStatus
    selected_strategy: tuple[str, ...] = ()
    requirement_wiring: tuple[RequirementWiring, ...] = ()
    unsatisfied_mandatory: tuple[str, ...] = ()
    unsatisfied_optional: tuple[str, ...] = ()
    considered_fallbacks: tuple[str, ...] = ()
    rationale: str = ""
