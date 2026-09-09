from __future__ import annotations

import json
from typing import TypeAlias

from aimage.contracts.common import ContractModel
from aimage.contracts.execution import ArtifactRecord, ExecutionPlan, RunRecord
from aimage.contracts.render import RenderSpec
from aimage.contracts.requirements import RequirementSet
from aimage.contracts.resolution import ProviderCapabilityDescriptor, ResolutionResult
from aimage.contracts.spatial import SpatialProfile
from aimage.contracts.validation import ValidationReport
from aimage.contracts.visual_intent import VisualIntentState


class UnsupportedSchemaError(ValueError):
    pass


ContractType: TypeAlias = type[ContractModel]

_MODELS: dict[str, ContractType] = {
    "visual_intent_state": VisualIntentState,
    "spatial_profile": SpatialProfile,
    "render_spec": RenderSpec,
    "requirement_set": RequirementSet,
    "provider_capability_descriptor": ProviderCapabilityDescriptor,
    "resolution_result": ResolutionResult,
    "execution_plan": ExecutionPlan,
    "artifact_record": ArtifactRecord,
    "run_record": RunRecord,
    "validation_report": ValidationReport,
}


def encode_contract(record: ContractModel) -> str:
    return json.dumps(record.model_dump(mode="json"), sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def decode_contract(document: str | bytes) -> ContractModel:
    payload = json.loads(document)
    if not isinstance(payload, dict):
        raise UnsupportedSchemaError("contract payload must be a JSON object")
    contract_type = payload.get("contract_type")
    schema_version = payload.get("schema_version")
    if schema_version != "1.0":
        raise UnsupportedSchemaError(f"unsupported schema version {schema_version!r}")
    model = _MODELS.get(str(contract_type))
    if model is None:
        raise UnsupportedSchemaError(f"unknown mandatory contract type {contract_type!r}")
    return model.model_validate(payload)
