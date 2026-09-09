from __future__ import annotations
from aimage.contracts.visual_intent import DecisionKind, DecisionRecord, ReferenceBinding, VisualIntentState
from aimage.engine.lifecycle import replace_reference_binding

def test_identity_reference_replacement_does_not_mutate_style_and_is_idempotent() -> None:
    identity = ReferenceBinding(binding_id="identity", artifact_ref="artifact:id-old", role="identity_reference", dimensions=("identity",), authority_id="user"); style = ReferenceBinding(binding_id="style", artifact_ref="artifact:style", role="style_reference", dimensions=("style",), authority_id="user"); state = VisualIntentState(job_id="job", semantic_revision=1, reference_bindings=(identity, style)); decision = DecisionRecord(decision_id="replace-identity", kind=DecisionKind.SUPERSEDE, base_semantic_revision=1, actor_authority_id="user", subject_ref="identity"); revised = replace_reference_binding(state, decision, binding_id="identity", new_artifact_ref="artifact:id-new")
    assert revised.semantic_revision == 2 and revised.reference_bindings[0].artifact_ref == "artifact:id-new" and revised.reference_bindings[0].role == "identity_reference" and revised.reference_bindings[1] == style; assert replace_reference_binding(revised, decision, binding_id=revised.reference_bindings[0].binding_id, new_artifact_ref="artifact:id-new") is revised
