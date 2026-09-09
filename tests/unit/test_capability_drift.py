from __future__ import annotations

import pytest
from aimage.contracts.common import EvidenceKind
from aimage.contracts.visual_intent import IntentItem, VisualIntentState
from aimage.engine.capabilities import CapabilityDriftError, assert_resolution_capability_current
from aimage.engine.compile import compile_render_spec
from aimage.engine.requirements import derive_requirements
from aimage.engine.resolve import resolve_requirements
from aimage.providers.openai.capability import build_capability_descriptor


def test_capability_change_between_resolution_and_execution_is_rejected() -> None:
    intent = VisualIntentState(job_id="job", semantic_revision=1, intent_items=(IntentItem(semantic_path="content", visual_dimension="content", value_or_constraint="cat", source_authority_id="user"),)); render = compile_render_spec(intent); requirements = derive_requirements(render, operation="generate"); old = build_capability_descriptor(job_id="job", semantic_revision=1, evidence_kind=EvidenceKind.REPRODUCED, evidence_uri="fixture:a"); resolution = resolve_requirements(requirements, (old,)); changed = build_capability_descriptor(job_id="job", semantic_revision=1, evidence_kind=EvidenceKind.REPRODUCED, evidence_uri="fixture:b")
    with pytest.raises(CapabilityDriftError): assert_resolution_capability_current(resolution, (old,), (changed,))
