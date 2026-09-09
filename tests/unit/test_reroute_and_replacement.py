from __future__ import annotations

from datetime import datetime, timedelta, timezone

from aimage.contracts.common import EvidenceKind
from aimage.contracts.resolution import Capability, ProviderCapabilityDescriptor, ResolutionStatus
from aimage.contracts.visual_intent import IntentItem, VisualIntentState
from aimage.engine.compile import compile_render_spec
from aimage.engine.requirements import derive_requirements
from aimage.engine.resolve import resolve_requirements


def _descriptor(target_id: str, *, fresh: bool) -> ProviderCapabilityDescriptor:
    observed = datetime.now(timezone.utc)
    return ProviderCapabilityDescriptor(
        job_id="job",
        semantic_revision=1,
        target_id=target_id,
        target_kind="provider",
        adapter_id=f"adapter:{target_id}",
        adapter_version="1",
        target_version_or_model=f"model:{target_id}",
        observed_at=observed,
        valid_until=observed + (timedelta(hours=1) if fresh else -timedelta(seconds=1)),
        evidence_kind=EvidenceKind.REPRODUCED,
        evidence_uri=f"fixture:{target_id}",
        capabilities=(
            Capability(
                namespace="aimage.image",
                name="generate",
                attributes={"input_kind": ("text",)},
                limits={
                    "max_width": 2048,
                    "max_height": 2048,
                    "dimension_divisible_by": 16,
                    "min_aspect": 1 / 3,
                    "max_aspect": 3.0,
                },
            ),
        ),
    )


def test_same_semantics_reroute_to_fresh_replacement_descriptor() -> None:
    intent = VisualIntentState(
        job_id="job",
        semantic_revision=1,
        intent_items=(
            IntentItem(
                semantic_path="content",
                visual_dimension="content",
                value_or_constraint="test",
                source_authority_id="user",
            ),
        ),
    )
    render = compile_render_spec(intent)
    requirements = derive_requirements(render, operation="generate")
    stale_primary = _descriptor("primary", fresh=False)
    fresh_replacement = _descriptor("replacement", fresh=True)
    result = resolve_requirements(requirements, (stale_primary, fresh_replacement))
    assert result.status is ResolutionStatus.RESOLVED
    assert result.selected_strategy == ("replacement",)
    assert render.source_semantic_revision == 1
    assert intent.semantic_revision == 1
