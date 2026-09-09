from __future__ import annotations

from aimage.contracts.render import RenderSpec
from aimage.contracts.validation import ValidationOutcome, ValidationResult

_HIGH_CORRELATION_EVIDENCE = frozenset({"model_assisted", "provider_feedback", "provider_self_report"})


def _oracle_is_sufficient_for_mandatory_pass(result: ValidationResult) -> bool:
    if result.evidence_class not in _HIGH_CORRELATION_EVIDENCE:
        return True
    return all(
        (
            result.evaluator_identity,
            result.evaluator_version,
            result.correlation_note,
            result.calibration_ref,
        )
    )


def aggregate_validation(results: tuple[ValidationResult, ...], mandatory_rule_ids: frozenset[str]) -> ValidationOutcome:
    mandatory = [result for result in results if result.rule_id in mandatory_rule_ids]
    if any(result.outcome is ValidationOutcome.FAIL for result in mandatory):
        return ValidationOutcome.FAIL
    if any(result.outcome is ValidationOutcome.INDETERMINATE for result in mandatory):
        return ValidationOutcome.INDETERMINATE
    if any(
        result.outcome is ValidationOutcome.PASS and not _oracle_is_sufficient_for_mandatory_pass(result)
        for result in mandatory
    ):
        return ValidationOutcome.INDETERMINATE
    return ValidationOutcome.PASS


def require_final_preservation_evidence(
    render_spec: RenderSpec,
    results: tuple[ValidationResult, ...],
    mandatory_rule_ids: frozenset[str],
    *,
    extra_preserve_paths: tuple[str, ...] = (),
) -> tuple[tuple[ValidationResult, ...], frozenset[str]]:
    """Make missing final-artifact preservation evidence explicitly indeterminate.

    This runs after the complete provider/composite execution, never on an intermediate artifact.
    """

    required_paths = set(extra_preserve_paths)
    for obligation in render_spec.preservation_obligations:
        required_paths.update(obligation.approved_paths)
    observed_paths = {result.semantic_path for result in results}
    missing = sorted(required_paths - observed_paths)
    if not missing:
        return results, mandatory_rule_ids

    augmented = list(results)
    mandatory = set(mandatory_rule_ids)
    for path in missing:
        rule_id = f"final-preservation:{path}"
        mandatory.add(rule_id)
        augmented.append(
            ValidationResult(
                rule_id=rule_id,
                outcome=ValidationOutcome.INDETERMINATE,
                semantic_path=path,
                dimension="preservation",
                severity="blocker",
                observed_summary="final artifact lacks required preservation evidence",
                failure_class="not_evaluable",
                evaluator_identity="aimage.validation_service",
                evaluator_version="1",
                evidence_class="deterministic_missing_evidence",
            )
        )
    return tuple(augmented), frozenset(mandatory)
