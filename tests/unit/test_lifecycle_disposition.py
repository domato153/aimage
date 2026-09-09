from __future__ import annotations

from aimage.contracts.visual_intent import (
    ArtifactDisposition,
    ArtifactDispositionRecord,
    DecisionKind,
    DecisionRecord,
    VisualIntentState,
)
from aimage.engine.lifecycle import accepted_artifact_refs, approve_baseline, reject_artifact, reopen_baseline


def test_reopen_duplicate_is_idempotent_after_revision_advance() -> None:
    initial = VisualIntentState(job_id="job", semantic_revision=1)
    approve = DecisionRecord(
        decision_id="approve-1",
        kind=DecisionKind.APPROVE,
        base_semantic_revision=1,
        actor_authority_id="user",
        subject_ref="candidate",
        scope_paths=("composition",),
        dimensions=("composition",),
    )
    approved = approve_baseline(initial, approve, value_snapshot_ref="snapshot:composition")
    baseline_id = approved.baselines[0].baseline_id
    reopen = DecisionRecord(
        decision_id="reopen-1",
        kind=DecisionKind.REOPEN,
        base_semantic_revision=2,
        actor_authority_id="user",
        subject_ref=baseline_id,
        scope_paths=("composition",),
        dimensions=("composition",),
    )
    reopened = reopen_baseline(approved, reopen, baseline_id=baseline_id)
    assert reopened.semantic_revision == 3
    assert reopened.baselines[0].reopen_decision_id == "reopen-1"
    assert reopen_baseline(reopened, reopen, baseline_id=baseline_id) is reopened


def test_newer_rejected_artifact_does_not_resurrect_by_recency() -> None:
    state = VisualIntentState(
        job_id="job",
        semantic_revision=4,
        artifact_dispositions=(
            ArtifactDispositionRecord(
                artifact_ref="artifact-a",
                semantic_revision=4,
                status=ArtifactDisposition.ACCEPTED,
                basis_decision_id="accept-a",
            ),
        ),
    )
    rejection = DecisionRecord(
        decision_id="reject-b",
        kind=DecisionKind.REJECT,
        base_semantic_revision=4,
        actor_authority_id="user",
        subject_ref="artifact-b",
    )
    rejected = reject_artifact(state, rejection, artifact_ref="artifact-b")
    assert rejected.semantic_revision == 4
    assert accepted_artifact_refs(rejected) == ("artifact-a",)
    assert reject_artifact(rejected, rejection, artifact_ref="artifact-b") is rejected
