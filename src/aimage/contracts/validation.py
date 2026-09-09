from __future__ import annotations

from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field

from .common import ContractModel, new_object_id


class ValidationOutcome(StrEnum):
    PASS = "pass"
    FAIL = "fail"
    INDETERMINATE = "indeterminate"
    NOT_APPLICABLE = "not_applicable"


class ValidationRule(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    rule_id: str
    semantic_path_or_dimension: str
    requirement_level: str
    severity: str
    evaluator_class: str
    meaning: str
    required_evidence: tuple[str, ...] = ()


class DomainProfile(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    profile_id: str
    namespace: str
    profile_version: str
    domain: str
    rules: tuple[ValidationRule, ...] = ()


class ValidationResult(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    result_id: str = Field(default_factory=new_object_id)
    rule_id: str
    outcome: ValidationOutcome
    semantic_path: str
    dimension: str
    severity: str
    evidence_refs: tuple[str, ...] = ()
    observed_summary: str = ""
    failure_class: str | None = None
    repair_advice: str | None = None
    evaluator_identity: str | None = None
    evaluator_version: str | None = None
    evidence_class: str | None = None
    correlation_note: str | None = None
    calibration_ref: str | None = None


class ValidationReport(ContractModel):
    contract_type: str = "validation_report"
    report_id: str = Field(default_factory=new_object_id)
    artifact_ref: str
    render_spec_ref: str
    execution_plan_ref: str
    profile_versions: tuple[str, ...] = ()
    overall_outcome: ValidationOutcome
    results: tuple[ValidationResult, ...] = ()
