from __future__ import annotations

import hashlib
import json

from aimage.contracts.common import Strength, new_object_id
from aimage.contracts.render import PreservationObligation, RenderSpec, SemanticObligation
from aimage.contracts.spatial import SpatialProfile
from aimage.contracts.visual_intent import BaselineStatus, IntentStatus, VisualIntentState


class SemanticCompileError(ValueError):
    pass


def _canonical(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, default=str)


def _digest(value: object) -> str:
    return hashlib.sha256(_canonical(value).encode("utf-8")).hexdigest()


def _semantic_payload(intent: VisualIntentState) -> dict[str, object]:
    payload = intent.model_dump(mode="json")
    for field in ("contract_type", "schema_version", "object_id", "created_from"):
        payload.pop(field, None)
    return payload


def visual_intent_digest(intent: VisualIntentState) -> str:
    """Digest canonical Family-A semantic content, excluding record/provenance envelope."""
    return _digest(_semantic_payload(intent))


def compiled_semantic_input_digest(intent: VisualIntentState, spatial_profile: SpatialProfile | None) -> str:
    spatial_payload = spatial_profile.model_dump(mode="json") if spatial_profile else None
    if spatial_payload:
        for field in ("contract_type", "schema_version", "object_id", "created_from"):
            spatial_payload.pop(field, None)
    return _digest({"visual_intent": _semantic_payload(intent), "spatial_profile": spatial_payload})


def compile_render_spec(
    intent: VisualIntentState,
    spatial_profile: SpatialProfile | None = None,
    *,
    output_contract: dict[str, object] | None = None,
) -> RenderSpec:
    if spatial_profile and spatial_profile.semantic_revision != intent.semantic_revision:
        raise SemanticCompileError("spatial profile belongs to another semantic revision")

    active = [item for item in intent.intent_items if item.status is IntentStatus.ACTIVE]
    mandatory_by_path: dict[str, set[str]] = {}
    for item in active:
        if item.strength is Strength.MANDATORY:
            mandatory_by_path.setdefault(item.semantic_path, set()).add(_canonical(item.value_or_constraint))
    conflicts = sorted(path for path, values in mandatory_by_path.items() if len(values) > 1)
    if conflicts:
        raise SemanticCompileError(f"contradictory mandatory semantics: {conflicts}")

    normalized_output = dict(output_contract or {"media_type": "image/png", "size": "1024x1024"})
    source_digest = compiled_semantic_input_digest(intent, spatial_profile)
    authority_digest = _digest([binding.model_dump(mode="json") for binding in intent.authority_bindings])
    spatial_dump = spatial_profile.model_dump(mode="json") if spatial_profile else None

    obligations: list[SemanticObligation] = [
        SemanticObligation(
            semantic_path=item.semantic_path,
            dimension=item.visual_dimension,
            value_or_constraint=item.value_or_constraint,
            strength=item.strength,
            source_intent_id=item.intent_id,
        )
        for item in active
    ]
    if spatial_profile:
        frame_kinds = {frame.frame_id: frame.kind.value for frame in spatial_profile.frames}
        for relation in spatial_profile.relations:
            obligations.append(
                SemanticObligation(
                    semantic_path=f"spatial.{relation.relation_id}",
                    dimension="composition",
                    value_or_constraint={
                        "predicate": relation.predicate,
                        "subject_entity_id": relation.subject_entity_id,
                        "object_entity_id": relation.object_entity_id,
                        "reference_frame_id": relation.reference_frame_id,
                        "reference_frame_kind": frame_kinds.get(relation.reference_frame_id),
                        "tolerance": relation.tolerance,
                    },
                    strength=relation.strength,
                    source_intent_id=relation.source_intent_id,
                )
            )

    preservation = tuple(
        PreservationObligation(
            baseline_id=baseline.baseline_id,
            approved_paths=baseline.approved_paths,
            approved_dimensions=baseline.approved_dimensions,
            value_snapshot_ref=baseline.value_snapshot_ref,
        )
        for baseline in intent.baselines
        if baseline.status is BaselineStatus.ACTIVE
    )
    return RenderSpec(
        render_spec_id=new_object_id(),
        job_id=intent.job_id,
        semantic_revision=intent.semantic_revision,
        source_semantic_revision=intent.semantic_revision,
        source_intent_digest=source_digest,
        created_from=(intent.object_id,) + ((spatial_profile.object_id,) if spatial_profile else ()),
        authority_snapshot_ref=f"sha256:{authority_digest}",
        spatial_profile_snapshot_ref=f"sha256:{_digest(spatial_dump)}" if spatial_profile else None,
        domain_profile_refs=intent.domain_profile_refs,
        intent_obligations=tuple(obligations),
        preservation_obligations=preservation,
        creative_freedoms=tuple(item.semantic_path for item in active if item.strength is Strength.ADVISORY),
        input_artifact_refs=tuple(dict.fromkeys(binding.artifact_ref for binding in intent.reference_bindings)),
        output_contract=normalized_output,
    )
