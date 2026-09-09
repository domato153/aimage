from __future__ import annotations

from datetime import datetime, timedelta, timezone

import pytest

from aimage.contracts.common import Strength
from aimage.contracts.resolution import ResolutionStatus
from aimage.contracts.spatial import (
    ReferenceFrame,
    ReferenceFrameKind,
    SpatialEntity,
    SpatialProfile,
    SpatialRelation,
)
from aimage.contracts.visual_intent import IntentItem, VisualIntentState
from aimage.engine.compile import SemanticCompileError, compile_render_spec
from aimage.engine.requirements import derive_requirements
from aimage.engine.resolve import resolve_requirements
from aimage.providers.openai.capability import build_capability_descriptor


def _intent(*items: IntentItem) -> VisualIntentState:
    return VisualIntentState(job_id="job", semantic_revision=1, intent_items=items)


def test_compile_fails_closed_on_contradictory_mandatory_path() -> None:
    intent = _intent(
        IntentItem(
            semantic_path="composition.subject_side",
            visual_dimension="composition",
            value_or_constraint="right",
            strength=Strength.MANDATORY,
            source_authority_id="user",
        ),
        IntentItem(
            semantic_path="composition.subject_side",
            visual_dimension="composition",
            value_or_constraint="left",
            strength=Strength.MANDATORY,
            source_authority_id="user",
        ),
    )
    with pytest.raises(SemanticCompileError):
        compile_render_spec(intent)


def test_viewer_deictic_survives_compile_as_frame_kind() -> None:
    intent_item = IntentItem(
        semantic_path="composition.subject_side",
        visual_dimension="composition",
        value_or_constraint="right",
        source_authority_id="user",
    )
    intent = _intent(intent_item)
    spatial = SpatialProfile(
        job_id="job",
        semantic_revision=1,
        entities=(
            SpatialEntity(entity_id="viewer", semantic_role="viewer"),
            SpatialEntity(entity_id="subject", semantic_role="subject"),
        ),
        frames=(
            ReferenceFrame(frame_id="viewer-frame", kind=ReferenceFrameKind.VIEWER_DEICTIC, origin_entity_id="viewer"),
        ),
        relations=(
            SpatialRelation(
                predicate="right_of",
                subject_entity_id="subject",
                object_entity_id="viewer",
                reference_frame_id="viewer-frame",
                source_intent_id=intent_item.intent_id,
            ),
        ),
    )
    render = compile_render_spec(intent, spatial)
    spatial_obligation = next(item for item in render.intent_obligations if item.semantic_path.startswith("spatial."))
    assert spatial_obligation.value_or_constraint["reference_frame_kind"] == "viewer_deictic"
    assert spatial_obligation.value_or_constraint["reference_frame_kind"] != "screen_image"


def test_resolution_checks_size_and_freshness() -> None:
    intent = _intent(
        IntentItem(
            semantic_path="content",
            visual_dimension="content",
            value_or_constraint="cat",
            source_authority_id="user",
        )
    )
    render = compile_render_spec(intent, output_contract={"media_type": "image/png", "size": "1024x1024"})
    requirements = derive_requirements(render, operation="generate")
    fresh = build_capability_descriptor(job_id="job", semantic_revision=1)
    assert resolve_requirements(requirements, (fresh,)).status is ResolutionStatus.RESOLVED

    old_time = datetime.now(timezone.utc) - timedelta(hours=2)
    stale = build_capability_descriptor(job_id="job", semantic_revision=1, observed_at=old_time)
    assert resolve_requirements(requirements, (stale,)).status is ResolutionStatus.STALE_CAPABILITIES


def test_resolution_rejects_illegal_size_instead_of_weakening() -> None:
    intent = _intent(
        IntentItem(
            semantic_path="content",
            visual_dimension="content",
            value_or_constraint="cat",
            source_authority_id="user",
        )
    )
    render = compile_render_spec(intent, output_contract={"media_type": "image/png", "size": "1025x1024"})
    requirements = derive_requirements(render, operation="generate")
    descriptor = build_capability_descriptor(job_id="job", semantic_revision=1)
    result = resolve_requirements(requirements, (descriptor,))
    assert result.status is ResolutionStatus.UNSATISFIED
    assert result.unsatisfied_mandatory
