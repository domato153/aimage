from __future__ import annotations

import json

import pytest

from aimage.contracts.codec.json_codec import UnsupportedSchemaError, decode_contract, encode_contract
from aimage.contracts.common import Strength
from aimage.contracts.validation import ValidationOutcome, ValidationResult
from aimage.contracts.visual_intent import DecisionKind, DecisionRecord, IntentItem, VisualIntentState
from aimage.engine.lifecycle import StaleDecisionError, approve_baseline
from aimage.engine.validation_service import aggregate_validation


def _intent(revision: int = 1) -> VisualIntentState:
    return VisualIntentState(
        job_id="job",
        semantic_revision=revision,
        intent_items=(
            IntentItem(
                semantic_path="composition",
                visual_dimension="composition",
                value_or_constraint="approved-layout",
                strength=Strength.MANDATORY,
                source_authority_id="user",
            ),
        ),
    )


def test_approval_is_revision_bound_and_duplicate_is_idempotent() -> None:
    intent = _intent()
    decision = DecisionRecord(
        decision_id="decision-1",
        kind=DecisionKind.APPROVE,
        base_semantic_revision=1,
        actor_authority_id="user",
        subject_ref="candidate-a",
        scope_paths=("composition",),
        dimensions=("composition",),
        resulting_semantic_revision=2,
    )
    approved = approve_baseline(intent, decision, value_snapshot_ref="snapshot:composition")
    assert approved.semantic_revision == 2
    assert approved.baselines[0].approval_decision_id == "decision-1"
    assert approve_baseline(approved, decision, value_snapshot_ref="snapshot:composition") is approved

    stale_other = decision.model_copy(update={"decision_id": "decision-2"})
    with pytest.raises(StaleDecisionError):
        approve_baseline(approved, stale_other, value_snapshot_ref="snapshot:other")


def test_unknown_schema_version_fails_safe() -> None:
    encoded = encode_contract(_intent())
    payload = json.loads(encoded)
    payload["schema_version"] = "999"
    with pytest.raises(UnsupportedSchemaError):
        decode_contract(json.dumps(payload))


def test_correlated_mandatory_oracle_without_calibration_is_indeterminate() -> None:
    result = ValidationResult(
        rule_id="identity",
        outcome=ValidationOutcome.PASS,
        semantic_path="identity",
        dimension="identity",
        severity="blocker",
        evaluator_identity="same-model-family",
        evaluator_version="x",
        evidence_class="model_assisted",
        correlation_note=None,
        calibration_ref=None,
    )
    assert aggregate_validation((result,), frozenset({"identity"})) is ValidationOutcome.INDETERMINATE
