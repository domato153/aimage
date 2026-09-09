"""Initial AIMAGE metadata schema.

Human-reviewed first-slice migration. Alembic autogenerate is not correctness authority.
"""

from alembic import op
import sqlalchemy as sa

revision = "0001_initial"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "jobs",
        sa.Column("job_id", sa.String(), primary_key=True),
        sa.Column("current_semantic_revision", sa.Integer(), nullable=False),
        sa.Column("current_intent_digest", sa.String(), nullable=False),
        sa.Column("lifecycle_state", sa.String(), nullable=False),
        sa.Column("accepted_artifact_id", sa.String()),
        sa.Column("updated_at", sa.String(), nullable=False),
    )
    op.create_table(
        "semantic_documents",
        sa.Column("object_id", sa.String(), primary_key=True),
        sa.Column("job_id", sa.String(), nullable=False),
        sa.Column("semantic_revision", sa.Integer(), nullable=False),
        sa.Column("schema_version", sa.String(), nullable=False),
        sa.Column("intent_digest", sa.String(), nullable=False),
        sa.Column("payload_json", sa.Text(), nullable=False),
        sa.Column("created_at", sa.String(), nullable=False),
        sa.UniqueConstraint("job_id", "semantic_revision", name="uq_semantic_documents_job_revision"),
    )
    op.create_index("ix_semantic_documents_job_id", "semantic_documents", ["job_id"])
    op.create_table(
        "semantic_support_documents",
        sa.Column("object_id", sa.String(), primary_key=True),
        sa.Column("contract_type", sa.String(), nullable=False),
        sa.Column("job_id", sa.String(), nullable=False),
        sa.Column("semantic_revision", sa.Integer(), nullable=False),
        sa.Column("schema_version", sa.String(), nullable=False),
        sa.Column("payload_json", sa.Text(), nullable=False),
        sa.Column("created_at", sa.String(), nullable=False),
    )
    op.create_index("ix_semantic_support_documents_job_id", "semantic_support_documents", ["job_id"])
    op.create_table(
        "derived_documents",
        sa.Column("object_id", sa.String(), primary_key=True),
        sa.Column("contract_type", sa.String(), nullable=False),
        sa.Column("job_id", sa.String(), nullable=False),
        sa.Column("source_semantic_revision", sa.Integer(), nullable=False),
        sa.Column("source_intent_digest", sa.String(), nullable=False),
        sa.Column("schema_version", sa.String(), nullable=False),
        sa.Column("payload_json", sa.Text(), nullable=False),
        sa.Column("created_at", sa.String(), nullable=False),
    )
    op.create_index("ix_derived_documents_job_id", "derived_documents", ["job_id"])
    op.create_table(
        "capability_descriptors",
        sa.Column("descriptor_id", sa.String(), primary_key=True),
        sa.Column("descriptor_digest", sa.String(), nullable=False, unique=True),
        sa.Column("target_id", sa.String(), nullable=False),
        sa.Column("adapter_id", sa.String(), nullable=False),
        sa.Column("adapter_version", sa.String(), nullable=False),
        sa.Column("target_model_version", sa.String(), nullable=False),
        sa.Column("evidence_kind", sa.String(), nullable=False),
        sa.Column("evidence_uri", sa.String(), nullable=False),
        sa.Column("observed_at", sa.String(), nullable=False),
        sa.Column("payload_json", sa.Text(), nullable=False),
    )
    op.create_table(
        "decisions",
        sa.Column("decision_id", sa.String(), primary_key=True),
        sa.Column("job_id", sa.String(), nullable=False),
        sa.Column("base_semantic_revision", sa.Integer(), nullable=False),
        sa.Column("kind", sa.String(), nullable=False),
        sa.Column("subject_ref", sa.String(), nullable=False),
        sa.Column("resulting_semantic_revision", sa.Integer()),
        sa.Column("payload_json", sa.Text(), nullable=False),
    )
    op.create_index("ix_decisions_job_id", "decisions", ["job_id"])
    op.create_table(
        "baselines",
        sa.Column("baseline_id", sa.String(), primary_key=True),
        sa.Column("job_id", sa.String(), nullable=False),
        sa.Column("approved_at_revision", sa.Integer(), nullable=False),
        sa.Column("approval_decision_id", sa.String(), nullable=False, unique=True),
        sa.Column("status", sa.String(), nullable=False),
        sa.Column("payload_json", sa.Text(), nullable=False),
    )
    op.create_index("ix_baselines_job_id", "baselines", ["job_id"])
    op.create_table(
        "artifact_dispositions",
        sa.Column("artifact_ref", sa.String(), primary_key=True),
        sa.Column("semantic_revision", sa.Integer(), primary_key=True),
        sa.Column("status", sa.String(), primary_key=True),
        sa.Column("job_id", sa.String(), nullable=False),
        sa.Column("basis_decision_id", sa.String()),
        sa.Column("payload_json", sa.Text(), nullable=False),
    )
    op.create_index("ix_artifact_dispositions_job_id", "artifact_dispositions", ["job_id"])
    op.create_table(
        "runs",
        sa.Column("run_id", sa.String(), primary_key=True),
        sa.Column("job_id", sa.String(), nullable=False),
        sa.Column("source_semantic_revision", sa.Integer(), nullable=False),
        sa.Column("source_intent_digest", sa.String(), nullable=False),
        sa.Column("execution_plan_ref", sa.String(), nullable=False),
        sa.Column("capability_descriptor_ref", sa.String()),
        sa.Column("target_model_version", sa.String()),
        sa.Column("actual_targets_json", sa.Text(), nullable=False),
        sa.Column("outputs_json", sa.Text(), nullable=False),
        sa.Column("raw_provider_result_ref", sa.String()),
        sa.Column("usage_json", sa.Text(), nullable=False),
        sa.Column("provider_request_id", sa.String()),
        sa.Column("status", sa.String(), nullable=False),
        sa.Column("attempt_index", sa.Integer(), nullable=False),
        sa.Column("normalized_error_class", sa.String()),
        sa.Column("raw_provider_evidence_json", sa.Text()),
        sa.Column("started_at", sa.String(), nullable=False),
        sa.Column("finished_at", sa.String()),
    )
    op.create_index("ix_runs_job_id", "runs", ["job_id"])
    op.create_table(
        "artifacts",
        sa.Column("artifact_id", sa.String(), primary_key=True),
        sa.Column("job_id", sa.String(), nullable=False),
        sa.Column("source_semantic_revision", sa.Integer(), nullable=False),
        sa.Column("content_digest", sa.String(), nullable=False),
        sa.Column("blob_key", sa.String(), nullable=False),
        sa.Column("media_metadata_json", sa.Text(), nullable=False),
        sa.Column("producing_run_ref", sa.String(), nullable=False),
        sa.Column("created_at", sa.String(), nullable=False),
    )
    op.create_index("ix_artifacts_job_id", "artifacts", ["job_id"])
    op.create_index("ix_artifacts_content_digest", "artifacts", ["content_digest"])
    op.create_table(
        "validation_reports",
        sa.Column("report_id", sa.String(), primary_key=True),
        sa.Column("artifact_ref", sa.String(), nullable=False),
        sa.Column("job_id", sa.String(), nullable=False),
        sa.Column("semantic_revision", sa.Integer(), nullable=False),
        sa.Column("render_spec_ref", sa.String(), nullable=False),
        sa.Column("execution_plan_ref", sa.String(), nullable=False),
        sa.Column("overall_outcome", sa.String(), nullable=False),
        sa.Column("evaluator_identity", sa.String()),
        sa.Column("evaluator_version", sa.String()),
        sa.Column("evidence_class", sa.String()),
        sa.Column("evaluator_provenance_json", sa.Text(), nullable=False),
        sa.Column("calibration_ref", sa.String()),
        sa.Column("correlation_note", sa.String()),
        sa.Column("payload_json", sa.Text(), nullable=False),
        sa.Column("created_at", sa.String(), nullable=False),
    )
    op.create_index("ix_validation_reports_artifact_ref", "validation_reports", ["artifact_ref"])
    op.create_index("ix_validation_reports_job_id", "validation_reports", ["job_id"])


def downgrade() -> None:
    op.drop_index("ix_validation_reports_job_id", table_name="validation_reports")
    op.drop_index("ix_validation_reports_artifact_ref", table_name="validation_reports")
    op.drop_table("validation_reports")
    op.drop_index("ix_artifacts_content_digest", table_name="artifacts")
    op.drop_index("ix_artifacts_job_id", table_name="artifacts")
    op.drop_table("artifacts")
    op.drop_index("ix_runs_job_id", table_name="runs")
    op.drop_table("runs")
    op.drop_index("ix_artifact_dispositions_job_id", table_name="artifact_dispositions")
    op.drop_table("artifact_dispositions")
    op.drop_index("ix_baselines_job_id", table_name="baselines")
    op.drop_table("baselines")
    op.drop_index("ix_decisions_job_id", table_name="decisions")
    op.drop_table("decisions")
    op.drop_table("capability_descriptors")
    op.drop_index("ix_derived_documents_job_id", table_name="derived_documents")
    op.drop_table("derived_documents")
    op.drop_index("ix_semantic_support_documents_job_id", table_name="semantic_support_documents")
    op.drop_table("semantic_support_documents")
    op.drop_index("ix_semantic_documents_job_id", table_name="semantic_documents")
    op.drop_table("semantic_documents")
    op.drop_table("jobs")
