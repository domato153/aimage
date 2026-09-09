"""Initial AIMAGE metadata schema."""

from alembic import op
import sqlalchemy as sa

revision = "0001_initial"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "object_records",
        sa.Column("object_id", sa.String(), primary_key=True),
        sa.Column("job_id", sa.String(), nullable=False),
        sa.Column("contract_type", sa.String(), nullable=False),
        sa.Column("semantic_revision", sa.Integer(), nullable=False),
        sa.Column("payload_json", sa.Text(), nullable=False),
    )
    op.create_index("ix_object_records_job_id", "object_records", ["job_id"])
    op.create_table(
        "job_current",
        sa.Column("job_id", sa.String(), primary_key=True),
        sa.Column("semantic_revision", sa.Integer(), nullable=False),
        sa.Column("intent_digest", sa.String(), nullable=False),
    )
    op.create_table(
        "artifacts",
        sa.Column("artifact_id", sa.String(), primary_key=True),
        sa.Column("job_id", sa.String(), nullable=False),
        sa.Column("semantic_revision", sa.Integer(), nullable=False),
        sa.Column("content_digest", sa.String(), nullable=False),
        sa.Column("media_json", sa.Text(), nullable=False),
        sa.Column("producing_run_ref", sa.String(), nullable=False),
    )
    op.create_index("ix_artifacts_job_id", "artifacts", ["job_id"])
    op.create_table(
        "runs",
        sa.Column("run_id", sa.String(), primary_key=True),
        sa.Column("job_id", sa.String(), nullable=False),
        sa.Column("semantic_revision", sa.Integer(), nullable=False),
        sa.Column("execution_plan_ref", sa.String(), nullable=False),
        sa.Column("actual_targets_json", sa.Text(), nullable=False),
        sa.Column("outputs_json", sa.Text(), nullable=False),
        sa.Column("raw_provider_result_ref", sa.String()),
        sa.Column("usage_json", sa.Text(), nullable=False),
        sa.Column("provider_request_id", sa.String()),
    )
    op.create_index("ix_runs_job_id", "runs", ["job_id"])


def downgrade() -> None:
    op.drop_index("ix_runs_job_id", table_name="runs")
    op.drop_table("runs")
    op.drop_index("ix_artifacts_job_id", table_name="artifacts")
    op.drop_table("artifacts")
    op.drop_table("job_current")
    op.drop_index("ix_object_records_job_id", table_name="object_records")
    op.drop_table("object_records")
