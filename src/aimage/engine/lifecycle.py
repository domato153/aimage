from __future__ import annotations

from aimage.contracts.common import new_object_id
from aimage.contracts.visual_intent import (
    ArtifactDisposition,
    ArtifactDispositionRecord,
    BaselineRecord,
    BaselineStatus,
    DecisionKind,
    DecisionRecord,
    VisualIntentState,
)


class StaleDecisionError(RuntimeError):
    pass


class InvalidDecisionError(ValueError):
    pass


def _decision_already_applied(intent: VisualIntentState, decision_id: str) -> bool:
    if any(
        baseline.approval_decision_id == decision_id or baseline.reopen_decision_id == decision_id
        for baseline in intent.baselines
    ):
        return True
    return any(disposition.basis_decision_id == decision_id for disposition in intent.artifact_dispositions)


def _rebuild(intent: VisualIntentState, **updates: object) -> VisualIntentState:
    payload = intent.model_dump(mode="python")
    payload.update(updates)
    payload["object_id"] = new_object_id()
    payload["created_from"] = (intent.object_id,)
    return VisualIntentState.model_validate(payload)


def approve_baseline(
    intent: VisualIntentState,
    decision: DecisionRecord,
    *,
    value_snapshot_ref: str,
) -> VisualIntentState:
    """Apply a scoped composition/semantic approval as a new semantic revision."""

    if _decision_already_applied(intent, decision.decision_id):
        return intent
    if decision.kind is not DecisionKind.APPROVE:
        raise InvalidDecisionError("approve_baseline requires an approve decision")
    if decision.base_semantic_revision != intent.semantic_revision:
        raise StaleDecisionError("approval was made against a stale semantic revision")
    if not decision.scope_paths and not decision.dimensions:
        raise InvalidDecisionError("approval must be scoped to paths or dimensions")

    next_revision = intent.semantic_revision + 1
    if decision.resulting_semantic_revision not in {None, next_revision}:
        raise InvalidDecisionError("decision resulting revision does not match the next semantic revision")
    baseline = BaselineRecord(
        approved_at_revision=next_revision,
        approved_paths=decision.scope_paths,
        approved_dimensions=decision.dimensions,
        value_snapshot_ref=value_snapshot_ref,
        approval_decision_id=decision.decision_id,
    )
    return _rebuild(
        intent,
        semantic_revision=next_revision,
        baselines=intent.baselines + (baseline,),
    )


def reopen_baseline(
    intent: VisualIntentState,
    decision: DecisionRecord,
    *,
    baseline_id: str,
) -> VisualIntentState:
    if _decision_already_applied(intent, decision.decision_id):
        return intent
    if decision.kind is not DecisionKind.REOPEN:
        raise InvalidDecisionError("reopen_baseline requires a reopen decision")
    if decision.base_semantic_revision != intent.semantic_revision:
        raise StaleDecisionError("reopen was made against a stale semantic revision")
    target = next((baseline for baseline in intent.baselines if baseline.baseline_id == baseline_id), None)
    if target is None or target.status is not BaselineStatus.ACTIVE:
        raise InvalidDecisionError("baseline is not active")
    next_revision = intent.semantic_revision + 1
    if decision.resulting_semantic_revision not in {None, next_revision}:
        raise InvalidDecisionError("decision resulting revision does not match the next semantic revision")
    revised = tuple(
        baseline.model_copy(
            update={
                "status": BaselineStatus.REOPENED,
                "reopen_decision_id": decision.decision_id,
            }
        )
        if baseline.baseline_id == baseline_id
        else baseline
        for baseline in intent.baselines
    )
    return _rebuild(intent, semantic_revision=next_revision, baselines=revised)


def reject_artifact(
    intent: VisualIntentState,
    decision: DecisionRecord,
    *,
    artifact_ref: str,
) -> VisualIntentState:
    """Record rejection without changing desired intent or semantic revision."""

    if _decision_already_applied(intent, decision.decision_id):
        return intent
    if decision.kind is not DecisionKind.REJECT:
        raise InvalidDecisionError("reject_artifact requires a reject decision")
    if decision.base_semantic_revision != intent.semantic_revision:
        raise StaleDecisionError("rejection was made against a stale semantic revision")
    disposition = ArtifactDispositionRecord(
        artifact_ref=artifact_ref,
        semantic_revision=intent.semantic_revision,
        status=ArtifactDisposition.REJECTED,
        basis_decision_id=decision.decision_id,
    )
    return _rebuild(
        intent,
        artifact_dispositions=intent.artifact_dispositions + (disposition,),
    )


def accepted_artifact_refs(intent: VisualIntentState) -> tuple[str, ...]:
    """Return only explicitly accepted, non-superseded artifacts; recency is irrelevant."""

    accepted = {
        disposition.artifact_ref
        for disposition in intent.artifact_dispositions
        if disposition.status is ArtifactDisposition.ACCEPTED
    }
    blocked = {
        disposition.artifact_ref
        for disposition in intent.artifact_dispositions
        if disposition.status in {ArtifactDisposition.REJECTED, ArtifactDisposition.SUPERSEDED}
    }
    return tuple(sorted(accepted - blocked))
