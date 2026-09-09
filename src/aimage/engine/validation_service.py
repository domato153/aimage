from __future__ import annotations

from aimage.contracts.validation import ValidationOutcome, ValidationResult


def aggregate_validation(results: tuple[ValidationResult, ...], mandatory_rule_ids: frozenset[str]) -> ValidationOutcome:
    mandatory = [result for result in results if result.rule_id in mandatory_rule_ids]
    if any(result.outcome is ValidationOutcome.FAIL for result in mandatory):
        return ValidationOutcome.FAIL
    if any(result.outcome is ValidationOutcome.INDETERMINATE for result in mandatory):
        return ValidationOutcome.INDETERMINATE
    return ValidationOutcome.PASS
