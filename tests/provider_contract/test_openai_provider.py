from __future__ import annotations

import base64
from types import SimpleNamespace

import pytest

from aimage.contracts.spatial import ReferenceFrame, ReferenceFrameKind, SpatialEntity, SpatialProfile, SpatialRelation
from aimage.contracts.visual_intent import IntentItem, VisualIntentState
from aimage.engine.compile import compile_render_spec
from aimage.engine.requirements import derive_requirements
from aimage.engine.resolve import resolve_requirements
from aimage.providers.openai.adapter import OpenAIAdapter
from aimage.providers.openai.capability import MODEL_SNAPSHOT, build_capability_descriptor
from aimage.providers.openai.lowering import lower_openai


class FakeImages:
    def __init__(self) -> None:
        self.generate_kwargs = None
        self.edit_kwargs = None

    async def generate(self, **kwargs):
        self.generate_kwargs = kwargs
        return SimpleNamespace(
            data=[SimpleNamespace(b64_json=base64.b64encode(b"generated").decode())],
            _request_id="req-generate",
            usage={"images": 1},
        )

    async def edit(self, **kwargs):
        self.edit_kwargs = kwargs
        return SimpleNamespace(
            data=[SimpleNamespace(b64_json=base64.b64encode(b"edited").decode())],
            _request_id="req-edit",
            usage={"images": 1},
        )


class FakeClient:
    def __init__(self) -> None:
        self.images = FakeImages()


def _compiled_viewer_right():
    intent_item = IntentItem(
        semantic_path="composition.side",
        visual_dimension="composition",
        value_or_constraint="right",
        source_authority_id="user",
    )
    intent = VisualIntentState(job_id="job", semantic_revision=1, intent_items=(intent_item,))
    spatial = SpatialProfile(
        job_id="job",
        semantic_revision=1,
        entities=(
            SpatialEntity(entity_id="viewer", semantic_role="viewer"),
            SpatialEntity(entity_id="subject", semantic_role="subject"),
        ),
        frames=(ReferenceFrame(frame_id="vf", kind=ReferenceFrameKind.VIEWER_DEICTIC),),
        relations=(
            SpatialRelation(
                predicate="right_of",
                subject_entity_id="subject",
                object_entity_id="viewer",
                reference_frame_id="vf",
                source_intent_id=intent_item.intent_id,
            ),
        ),
    )
    return compile_render_spec(intent, spatial)


def test_lowering_preserves_viewer_deictic_literal() -> None:
    render = _compiled_viewer_right()
    requirements = derive_requirements(render, operation="generate")
    descriptor = build_capability_descriptor(job_id="job", semantic_revision=1)
    resolution = resolve_requirements(requirements, (descriptor,))
    lowered = lower_openai(render, requirements, resolution, descriptor, operation="generate")
    assert "viewer_deictic" in lowered.request.prompt
    assert "screen_image" not in lowered.request.prompt
    assert lowered.request.model == MODEL_SNAPSHOT


@pytest.mark.asyncio
async def test_adapter_generate_and_edit_use_provider_only_payload() -> None:
    client = FakeClient()
    adapter = OpenAIAdapter(client)
    render = _compiled_viewer_right()
    descriptor = adapter.capability_descriptor(job_id="job", semantic_revision=1)

    requirements = derive_requirements(render, operation="generate")
    resolution = resolve_requirements(requirements, (descriptor,))
    generated = lower_openai(render, requirements, resolution, descriptor, operation="generate")
    result = await adapter.execute(generated.request)
    assert result.artifact_bytes == b"generated"
    assert result.provider_request_id == "req-generate"

    edit_requirements = derive_requirements(render, operation="edit")
    edit_resolution = resolve_requirements(edit_requirements, (descriptor,))
    edited = lower_openai(
        render,
        edit_requirements,
        edit_resolution,
        descriptor,
        operation="edit",
        source_artifact_refs=("sha256:source",),
    )
    edit_result = await adapter.execute(edited.request, input_images=(b"source",))
    assert edit_result.artifact_bytes == b"edited"
    assert client.images.edit_kwargs["model"] == MODEL_SNAPSHOT
