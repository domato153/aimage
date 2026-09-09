from __future__ import annotations

from enum import StrEnum
from typing import Any

from pydantic import BaseModel, ConfigDict, Field, model_validator

from .common import ContractModel, Strength, new_object_id


class IntentStatus(StrEnum):
    ACTIVE = "active"
    SUPERSEDED = "superseded"


class IntentItem(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    intent_id: str = Field(default_factory=new_object_id)
    semantic_path: str
    visual_dimension: str
    value_or_constraint: Any
    strength: Strength = Strength.MANDATORY
    source_authority_id: str
    status: IntentStatus = IntentStatus.ACTIVE


class AuthorityBinding(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    authority_id: str
    source_ref: str
    source_kind: str
    scope_paths: tuple[str, ...] = ()
    dimensions: tuple[str, ...] = ()
    precedence_key: int = 0
    valid_from_revision: int = Field(ge=1)


class ReferenceBinding(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    binding_id: str = Field(default_factory=new_object_id)
    artifact_ref: str
    role: str
    scope_paths: tuple[str, ...] = ()
    dimensions: tuple[str, ...] = ()
    authority_id: str


class BaselineStatus(StrEnum):
    ACTIVE = "active"
    REOPENED = "reopened"
    SUPERSEDED = "superseded"


class BaselineRecord(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    baseline_id: str = Field(default_factory=new_object_id)
    approved_at_revision: int = Field(ge=1)
    approved_paths: tuple[str, ...]
    approved_dimensions: tuple[str, ...]
    value_snapshot_ref: str
    approval_decision_id: str
    status: BaselineStatus = BaselineStatus.ACTIVE


class ArtifactDisposition(StrEnum):
    CANDIDATE = "candidate"
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    SUPERSEDED = "superseded"


class ArtifactDispositionRecord(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    artifact_ref: str
    semantic_revision: int = Field(ge=1)
    status: ArtifactDisposition
    basis_decision_id: str | None = None
    supersedes_artifact_ref: str | None = None


class VisualIntentState(ContractModel):
    contract_type: str = "visual_intent_state"
    intent_items: tuple[IntentItem, ...] = ()
    authority_bindings: tuple[AuthorityBinding, ...] = ()
    reference_bindings: tuple[ReferenceBinding, ...] = ()
    baselines: tuple[BaselineRecord, ...] = ()
    artifact_dispositions: tuple[ArtifactDispositionRecord, ...] = ()
    spatial_profile_ref: str | None = None
    domain_profile_refs: tuple[str, ...] = ()


class DecisionKind(StrEnum):
    APPROVE = "approve"
    REJECT = "reject"
    REOPEN = "reopen"
    SUPERSEDE = "supersede"


class DecisionRecord(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    decision_id: str = Field(default_factory=new_object_id)
    kind: DecisionKind
    base_semantic_revision: int = Field(ge=1)
    actor_authority_id: str
    subject_ref: str
    scope_paths: tuple[str, ...] = ()
    dimensions: tuple[str, ...] = ()
    reason_ref: str | None = None
    resulting_semantic_revision: int | None = None


class MutationReason(StrEnum):
    REPAIR = "repair"
    EXPLICIT_CHANGE = "explicit_change"
    RERENDER = "rerender"


class MutationFrame(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    frame_id: str = Field(default_factory=new_object_id)
    semantic_revision: int = Field(ge=1)
    reason: MutationReason
    mutable_paths: tuple[str, ...]
    preserve_paths: tuple[str, ...]
    source_validation_results: tuple[str, ...] = ()
    authorizing_decision_id: str | None = None

    @model_validator(mode="after")
    def paths_are_disjoint(self) -> "MutationFrame":
        overlap = set(self.mutable_paths) & set(self.preserve_paths)
        if overlap:
            raise ValueError(f"mutation frame overlaps mutable/preserve paths: {sorted(overlap)}")
        return self
