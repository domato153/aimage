from __future__ import annotations

from sqlalchemy import Column, Integer, MetaData, String, Table, Text, UniqueConstraint

metadata = MetaData()

jobs = Table(
    "jobs",
    metadata,
    Column("job_id", String, primary_key=True),
    Column("current_semantic_revision", Integer, nullable=False),
    Column("current_intent_digest", String, nullable=False),
    Column("lifecycle_state", String, nullable=False, default="active"),
    Column("accepted_artifact_id", String),
    Column("updated_at", String, nullable=False),
)
# Transitional Python alias used by first-slice tests/callers; the physical table is `jobs`.
job_current = jobs

semantic_documents = Table(
    "semantic_documents",
    metadata,
    Column("object_id", String, primary_key=True),
    Column("job_id", String, nullable=False, index=True),
    Column("semantic_revision", Integer, nullable=False),
    Column("schema_version", String, nullable=False),
    Column("intent_digest", String, nullable=False),
    Column("payload_json", Text, nullable=False),
    Column("created_at", String, nullable=False),
    UniqueConstraint("job_id", "semantic_revision", name="uq_semantic_documents_job_revision"),
)

semantic_support_documents = Table(
    "semantic_support_documents",
    metadata,
    Column("object_id", String, primary_key=True),
    Column("contract_type", String, nullable=False),
    Column("job_id", String, nullable=False, index=True),
    Column("semantic_revision", Integer, nullable=False),
    Column("schema_version", String, nullable=False),
    Column("payload_json", Text, nullable=False),
    Column("created_at", String, nullable=False),
)

derived_documents = Table(
    "derived_documents",
    metadata,
    Column("object_id", String, primary_key=True),
    Column("contract_type", String, nullable=False),
    Column("job_id", String, nullable=False, index=True),
    Column("source_semantic_revision", Integer, nullable=False),
    Column("source_intent_digest", String, nullable=False),
    Column("schema_version", String, nullable=False),
    Column("payload_json", Text, nullable=False),
    Column("created_at", String, nullable=False),
)

capability_descriptors = Table(
    "capability_descriptors",
    metadata,
    Column("descriptor_id", String, primary_key=True),
    Column("descriptor_digest", String, nullable=False, unique=True),
    Column("target_id", String, nullable=False),
    Column("adapter_id", String, nullable=False),
    Column("adapter_version", String, nullable=False),
    Column("target_model_version", String, nullable=False),
    Column("evidence_kind", String, nullable=False),
    Column("evidence_uri", String, nullable=False),
    Column("observed_at", String, nullable=False),
    Column("payload_json", Text, nullable=False),
)

decisions = Table(
    "decisions",
    metadata,
    Column("decision_id", String, primary_key=True),
    Column("job_id", String, nullable=False, index=True),
    Column("base_semantic_revision", Integer, nullable=False),
    Column("kind", String, nullable=False),
    Column("subject_ref", String, nullable=False),
    Column("resulting_semantic_revision", Integer),
    Column("payload_json", Text, nullable=False),
)

baselines = Table(
    "baselines",
    metadata,
    Column("baseline_id", String, primary_key=True),
    Column("job_id", String, nullable=False, index=True),
    Column("approved_at_revision", Integer, nullable=False),
    Column("approval_decision_id", String, nullable=False, unique=True),
    Column("status", String, nullable=False),
    Column("payload_json", Text, nullable=False),
)

artifact_dispositions = Table(
    "artifact_dispositions",
    metadata,
    Column("artifact_ref", String, primary_key=True),
    Column("semantic_revision", Integer, primary_key=True),
    Column("status", String, primary_key=True),
    Column("job_id", String, nullable=False, index=True),
    Column("basis_decision_id", String),
    Column("payload_json", Text, nullable=False),
)

runs = Table(
    "runs",
    metadata,
    Column("run_id", String, primary_key=True),
    Column("job_id", String, nullable=False, index=True),
    Column("source_semantic_revision", Integer, nullable=False),
    Column("source_intent_digest", String, nullable=False),
    Column("execution_plan_ref", String, nullable=False),
    Column("capability_descriptor_ref", String),
    Column("target_model_version", String),
    Column("actual_targets_json", Text, nullable=False),
    Column("outputs_json", Text, nullable=False),
    Column("raw_provider_result_ref", String),
    Column("usage_json", Text, nullable=False),
    Column("provider_request_id", String),
    Column("status", String, nullable=False),
    Column("attempt_index", Integer, nullable=False, default=0),
    Column("normalized_error_class", String),
    Column("raw_provider_evidence_json", Text),
    Column("started_at", String, nullable=False),
    Column("finished_at", String),
)

artifacts = Table(
    "artifacts",
    metadata,
    Column("artifact_id", String, primary_key=True),
    Column("job_id", String, nullable=False, index=True),
    Column("source_semantic_revision", Integer, nullable=False),
    Column("content_digest", String, nullable=False, index=True),
    Column("blob_key", String, nullable=False),
    Column("media_metadata_json", Text, nullable=False),
    Column("producing_run_ref", String, nullable=False),
    Column("created_at", String, nullable=False),
)

validation_reports = Table(
    "validation_reports",
    metadata,
    Column("report_id", String, primary_key=True),
    Column("artifact_ref", String, nullable=False, index=True),
    Column("job_id", String, nullable=False, index=True),
    Column("semantic_revision", Integer, nullable=False),
    Column("render_spec_ref", String, nullable=False),
    Column("execution_plan_ref", String, nullable=False),
    Column("overall_outcome", String, nullable=False),
    Column("evaluator_identity", String),
    Column("evaluator_version", String),
    Column("evidence_class", String),
    Column("evaluator_provenance_json", Text, nullable=False),
    Column("calibration_ref", String),
    Column("correlation_note", String),
    Column("payload_json", Text, nullable=False),
    Column("created_at", String, nullable=False),
)
