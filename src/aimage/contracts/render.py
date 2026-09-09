from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict

from .common import DerivedContractModel, Strength


class SemanticObligation(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    semantic_path: str
    dimension: str
    value_or_constraint: Any
    strength: Strength
    source_intent_id: str


class PreservationObligation(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    baseline_id: str
    approved_paths: tuple[str, ...]
    approved_dimensions: tuple[str, ...]
    value_snapshot_ref: str


class RenderSpec(DerivedContractModel):
    contract_type: str = "render_spec"
    render_spec_id: str
    authority_snapshot_ref: str
    spatial_profile_snapshot_ref: str | None = None
    domain_profile_refs: tuple[str, ...] = ()
    intent_obligations: tuple[SemanticObligation, ...] = ()
    preservation_obligations: tuple[PreservationObligation, ...] = ()
    creative_freedoms: tuple[str, ...] = ()
    input_artifact_refs: tuple[str, ...] = ()
    output_contract: dict[str, Any] = {}
