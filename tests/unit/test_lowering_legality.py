from __future__ import annotations

import pytest

from aimage.contracts.common import EvidenceKind
from aimage.contracts.visual_intent import IntentItem, VisualIntentState
from aimage.engine.compile import compile_render_spec
from aimage.engine.lower import LoweringLegalityError, validate_lowering_legality
from aimage.engine.requirements import derive_requirements
from aimage.engine.resolve import resolve_requirements
from aimage.providers.openai.capability import build_capability_descriptor
from aimage.providers.openai.lowering import lower_openai


def test_missing_mandatory_lowering_trace_fails_closed() -> None:
    intent = VisualIntentState(job_id="job", semantic_revision=1, intent_items=(IntentItem(semantic_path="content", visual_dimension="content", value_or_constraint="cat", source_authority_id="user"),)); render = compile_render_spec(intent); requirements = derive_requirements(render, operation="generate"); descriptor = build_capability_descriptor(job_id="job", semantic_revision=1, evidence_kind=EvidenceKind.REPRODUCED, evidence_uri="fixture:reproduced"); resolution = resolve_requirements(requirements, (descriptor,)); lowered = lower_openai(render, requirements, resolution, descriptor, operation="generate"); validate_lowering_legality(render, requirements, lowered.execution_plan)
    broken = lowered.execution_plan.model_copy(update={"lowering_trace": ()})
    with pytest.raises(LoweringLegalityError): validate_lowering_legality(render, requirements, broken)
