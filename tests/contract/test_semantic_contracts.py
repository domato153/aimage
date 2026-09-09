from __future__ import annotations

import pytest
from pydantic import ValidationError

from aimage.contracts.execution import ExecutionPlan, ExecutionStep
from aimage.contracts.spatial import ReferenceFrameKind, SpatialRelation
from aimage.contracts.visual_intent import MutationFrame, MutationReason


def test_directional_spatial_relation_requires_explicit_frame() -> None:
    with pytest.raises(ValidationError):
        SpatialRelation(
            predicate="right_of",
            subject_entity_id="subject",
            object_entity_id="viewer",
            source_intent_id="intent-1",
        )


def test_mutation_frame_cannot_mutate_and_preserve_same_path() -> None:
    with pytest.raises(ValidationError):
        MutationFrame(
            semantic_revision=1,
            reason=MutationReason.REPAIR,
            mutable_paths=("expression",),
            preserve_paths=("identity", "expression"),
        )


def test_execution_plan_rejects_cycle() -> None:
    with pytest.raises(ValidationError):
        ExecutionPlan(
            job_id="job",
            semantic_revision=1,
            source_semantic_revision=1,
            source_intent_digest="digest",
            render_spec_ref="render",
            resolution_ref="resolution",
            steps=(
                ExecutionStep(
                    step_id="a",
                    target_descriptor_ref="d",
                    operation="generate",
                    provider_or_tool_payload_ref="p1",
                    output_role="a",
                    depends_on=("b",),
                ),
                ExecutionStep(
                    step_id="b",
                    target_descriptor_ref="d",
                    operation="compose",
                    provider_or_tool_payload_ref="p2",
                    output_role="b",
                    depends_on=("a",),
                ),
            ),
        )


def test_reference_frame_kinds_are_not_aliases() -> None:
    assert ReferenceFrameKind.VIEWER_DEICTIC != ReferenceFrameKind.SCREEN_IMAGE
    assert ReferenceFrameKind.VIEWER_DEICTIC.value == "viewer_deictic"
    assert ReferenceFrameKind.SCREEN_IMAGE.value == "screen_image"
