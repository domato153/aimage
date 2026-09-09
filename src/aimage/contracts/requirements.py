from __future__ import annotations

from enum import StrEnum
from typing import Any

from pydantic import BaseModel, ConfigDict, Field

from .common import ContractModel, new_object_id


class Necessity(StrEnum):
    MANDATORY = "mandatory"
    OPTIONAL = "optional"


class RepresentationFidelity(StrEnum):
    EXACT = "exact"
    WITHIN_DECLARED_TOLERANCE = "within_declared_tolerance"


class CapabilityRequirement(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    requirement_id: str = Field(default_factory=new_object_id)
    namespace: str
    action_or_capability: str
    necessity: Necessity
    constraints: dict[str, Any] = {}
    source_semantic_paths: tuple[str, ...] = ()
    allowed_representation: RepresentationFidelity = RepresentationFidelity.EXACT


class RequirementSet(ContractModel):
    contract_type: str = "requirement_set"
    requirement_set_id: str = Field(default_factory=new_object_id)
    render_spec_ref: str
    requirements: tuple[CapabilityRequirement, ...] = ()
