from __future__ import annotations

from aimage.contracts.common import new_object_id
from aimage.contracts.visual_intent import (
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
    if any(baseline.approval_decision_id == decision_id for baseline in intent.baselines):
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
    """Apply a scoped composition/semantic approval as a new semantic revision.

    Exact duplicate decision IDs are idempotent even if replayed after the resulting revision
    became current. A different late decision against an old base revision is rejected.
    """

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
    if decision.kind is not DecisionKind.REOPEN:
        raise InvalidDecisionError("reopen_baseline requires a reopen decision")
    if decision.base_semantic_revision != intent.semantic_revision:
        raise StaleDecisionError("reopen was made against a stale semantic revision")
    target = next((baseline for baseline in intent.baselines if baseline.baseline_id == baseline_id), None)
    if target is None or target.status is not BaselineStatus.ACTIVE:
        raise InvalidDecisionError("baseline is not active")
    next_revision = intent.semantic_revision + 1
    revised = tuple(
        baseline.model_copy(update={"status": BaselineStatus.REOPENED}) if baseline.baseline_id == baseline_id else baseline
        for baseline in intent.baselines
    )
    return _rebuild(intent, semantic_revision=next_revision, baselines=revised)
