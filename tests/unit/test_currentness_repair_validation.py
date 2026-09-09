from __future__ import annotations

import pytest

from aimage.contracts.validation import ValidationOutcome, ValidationResult
from aimage.engine.currentness import StaleStateError, assert_current
from aimage.engine.repair import RepairEvidence, RepairPolicy, RepairProgress, RepairStop, advance_repair
from aimage.engine.validation_service import aggregate_validation


def test_currentness_rejects_late_semantic_revision() -> None:
    with pytest.raises(StaleStateError):
        assert_current(expected_semantic_revision=1, current_semantic_revision=2)


def test_repair_partial_order_replaces_best_only_on_strict_non_regressed_improvement() -> None:
    policy = RepairPolicy(max_attempts=5, max_non_improving=2)
    progress = advance_repair(
        RepairProgress(),
        policy,
        artifact_ref="a",
        evidence=RepairEvidence(material_failures=frozenset({"identity", "expression"})),
        fingerprint="state-a",
    )
    progress = advance_repair(
        progress,
        policy,
        artifact_ref="b",
        evidence=RepairEvidence(material_failures=frozenset({"identity"})),
        fingerprint="state-b",
    )
    assert progress.best_artifact_ref == "b"
    assert progress.best_evidence is not None
    assert progress.best_evidence.material_failures == frozenset({"identity"})

    # Fixing a different failure while reintroducing another is incomparable, not "better".
    progress = advance_repair(
        progress,
        policy,
        artifact_ref="c",
        evidence=RepairEvidence(material_failures=frozenset({"expression"})),
        fingerprint="state-c",
    )
    assert progress.best_artifact_ref == "b"

    # A candidate with a preservation regression can never displace a non-regressed best.
    progress = advance_repair(
        progress,
        policy,
        artifact_ref="d",
        evidence=RepairEvidence(
            material_failures=frozenset(),
            preservation_regressions=frozenset({"composition"}),
        ),
        fingerprint="state-d",
    )
    assert progress.best_artifact_ref == "b"


def test_repair_stops_on_oscillation_and_retains_best() -> None:
    policy = RepairPolicy(max_attempts=4, max_non_improving=2)
    progress = advance_repair(
        RepairProgress(),
        policy,
        artifact_ref="a",
        evidence=RepairEvidence(material_failures=frozenset({"identity"})),
        fingerprint="state-a",
    )
    with pytest.raises(RepairStop, match="oscillation"):
        advance_repair(
            progress,
            policy,
            artifact_ref="b",
            evidence=RepairEvidence(material_failures=frozenset()),
            fingerprint="state-a",
        )
    assert progress.best_artifact_ref == "a"


def test_repair_stops_after_bounded_non_improvement() -> None:
    policy = RepairPolicy(max_attempts=4, max_non_improving=1)
    progress = advance_repair(
        RepairProgress(),
        policy,
        artifact_ref="a",
        evidence=RepairEvidence(material_failures=frozenset({"identity"})),
        fingerprint="state-a",
    )
    progress = advance_repair(
        progress,
        policy,
        artifact_ref="b",
        evidence=RepairEvidence(material_failures=frozenset({"expression"})),
        fingerprint="state-b",
    )
    with pytest.raises(RepairStop, match="not strictly improving"):
        advance_repair(
            progress,
            policy,
            artifact_ref="c",
            evidence=RepairEvidence(material_failures=frozenset({"lighting"})),
            fingerprint="state-c",
        )
    assert progress.best_artifact_ref == "a"


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
