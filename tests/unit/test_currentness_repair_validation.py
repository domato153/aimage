from __future__ import annotations

import pytest

from aimage.contracts.validation import ValidationOutcome, ValidationResult
from aimage.engine.currentness import StaleStateError, assert_current
from aimage.engine.repair import RepairPolicy, RepairProgress, RepairStop, advance_repair
from aimage.engine.validation_service import aggregate_validation


def test_currentness_rejects_late_semantic_revision() -> None:
    with pytest.raises(StaleStateError):
        assert_current(expected_semantic_revision=1, current_semantic_revision=2)


def test_repair_stops_on_oscillation_and_retains_best() -> None:
    policy = RepairPolicy(max_attempts=3, max_non_improving=1)
    progress = advance_repair(
        RepairProgress(), policy, artifact_ref="a", score=0.8, fingerprint="state-a"
    )
    progress = advance_repair(
        progress, policy, artifact_ref="b", score=0.7, fingerprint="state-b"
    )
    assert progress.best_artifact_ref == "a"
    with pytest.raises(RepairStop):
        advance_repair(progress, policy, artifact_ref="c", score=0.81, fingerprint="state-a")


def test_mandatory_indeterminate_is_not_pass() -> None:
    results = (
        ValidationResult(
            rule_id="identity",
            outcome=ValidationOutcome.INDETERMINATE,
            semantic_path="identity",
            dimension="identity",
            severity="blocker",
            evaluator_identity="validator-x",
            evaluator_version="1",
            evidence_class="model_assisted",
        ),
    )
    assert aggregate_validation(results, frozenset({"identity"})) is ValidationOutcome.INDETERMINATE
