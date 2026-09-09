from __future__ import annotations
from aimage.contracts.common import new_object_id
from aimage.contracts.visual_intent import ArtifactDisposition, ArtifactDispositionRecord, BaselineRecord, BaselineStatus, DecisionKind, DecisionRecord, ReferenceBinding, VisualIntentState
class StaleDecisionError(RuntimeError): pass
class InvalidDecisionError(ValueError): pass

def _decision_already_applied(intent: VisualIntentState, decision_id: str) -> bool:
    if any(b.approval_decision_id == decision_id or b.reopen_decision_id == decision_id for b in intent.baselines): return True
    if any(binding.superseding_decision_id == decision_id for binding in intent.reference_bindings): return True
    return any(d.basis_decision_id == decision_id for d in intent.artifact_dispositions)
def _rebuild(intent: VisualIntentState, **updates: object) -> VisualIntentState:
    payload = intent.model_dump(mode="python"); payload.update(updates); payload["object_id"] = new_object_id(); payload["created_from"] = (intent.object_id,); return VisualIntentState.model_validate(payload)
def approve_baseline(intent: VisualIntentState, decision: DecisionRecord, *, value_snapshot_ref: str) -> VisualIntentState:
    if _decision_already_applied(intent, decision.decision_id): return intent
    if decision.kind is not DecisionKind.APPROVE: raise InvalidDecisionError("approve_baseline requires an approve decision")
    if decision.base_semantic_revision != intent.semantic_revision: raise StaleDecisionError("approval was made against a stale semantic revision")
    if not decision.scope_paths and not decision.dimensions: raise InvalidDecisionError("approval must be scoped to paths or dimensions")
    next_revision = intent.semantic_revision + 1
    if decision.resulting_semantic_revision not in {None, next_revision}: raise InvalidDecisionError("decision resulting revision does not match the next semantic revision")
    baseline = BaselineRecord(approved_at_revision=next_revision, approved_paths=decision.scope_paths, approved_dimensions=decision.dimensions, value_snapshot_ref=value_snapshot_ref, approval_decision_id=decision.decision_id)
    return _rebuild(intent, semantic_revision=next_revision, baselines=intent.baselines + (baseline,))
def reopen_baseline(intent: VisualIntentState, decision: DecisionRecord, *, baseline_id: str) -> VisualIntentState:
    if _decision_already_applied(intent, decision.decision_id): return intent
    if decision.kind is not DecisionKind.REOPEN: raise InvalidDecisionError("reopen_baseline requires a reopen decision")
    if decision.base_semantic_revision != intent.semantic_revision: raise StaleDecisionError("reopen was made against a stale semantic revision")
    target = next((b for b in intent.baselines if b.baseline_id == baseline_id), None)
    if target is None or target.status is not BaselineStatus.ACTIVE: raise InvalidDecisionError("baseline is not active")
    next_revision = intent.semantic_revision + 1
    if decision.resulting_semantic_revision not in {None, next_revision}: raise InvalidDecisionError("decision resulting revision does not match the next semantic revision")
    revised = tuple(b.model_copy(update={"status": BaselineStatus.REOPENED, "reopen_decision_id": decision.decision_id}) if b.baseline_id == baseline_id else b for b in intent.baselines)
    return _rebuild(intent, semantic_revision=next_revision, baselines=revised)
def replace_reference_binding(intent: VisualIntentState, decision: DecisionRecord, *, binding_id: str, new_artifact_ref: str) -> VisualIntentState:
    if _decision_already_applied(intent, decision.decision_id): return intent
    if decision.kind is not DecisionKind.SUPERSEDE: raise InvalidDecisionError("reference replacement requires a supersede decision")
    if decision.base_semantic_revision != intent.semantic_revision: raise StaleDecisionError("reference replacement was made against a stale semantic revision")
    target = next((binding for binding in intent.reference_bindings if binding.binding_id == binding_id), None)
    if target is None: raise InvalidDecisionError("reference binding not found")
    next_revision = intent.semantic_revision + 1
    replacement = ReferenceBinding(binding_id=new_object_id(), artifact_ref=new_artifact_ref, role=target.role, scope_paths=target.scope_paths, dimensions=target.dimensions, authority_id=target.authority_id, superseding_decision_id=decision.decision_id)
    return _rebuild(intent, semantic_revision=next_revision, reference_bindings=tuple(replacement if binding.binding_id == binding_id else binding for binding in intent.reference_bindings))
def reject_artifact(intent: VisualIntentState, decision: DecisionRecord, *, artifact_ref: str) -> VisualIntentState:
    if _decision_already_applied(intent, decision.decision_id): return intent
    if decision.kind is not DecisionKind.REJECT: raise InvalidDecisionError("reject_artifact requires a reject decision")
    if decision.base_semantic_revision != intent.semantic_revision: raise StaleDecisionError("rejection was made against a stale semantic revision")
    disposition = ArtifactDispositionRecord(artifact_ref=artifact_ref, semantic_revision=intent.semantic_revision, status=ArtifactDisposition.REJECTED, basis_decision_id=decision.decision_id)
    return _rebuild(intent, artifact_dispositions=intent.artifact_dispositions + (disposition,))
def accepted_artifact_refs(intent: VisualIntentState) -> tuple[str, ...]:
    accepted = {d.artifact_ref for d in intent.artifact_dispositions if d.status is ArtifactDisposition.ACCEPTED}; blocked = {d.artifact_ref for d in intent.artifact_dispositions if d.status in {ArtifactDisposition.REJECTED, ArtifactDisposition.SUPERSEDED}}; return tuple(sorted(accepted - blocked))
