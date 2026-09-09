from __future__ import annotations

from sqlalchemy import Column, Integer, MetaData, String, Table, Text

metadata = MetaData()

object_records = Table(
    "object_records",
    metadata,
    Column("object_id", String, primary_key=True),
    Column("job_id", String, nullable=False, index=True),
    Column("contract_type", String, nullable=False),
    Column("semantic_revision", Integer, nullable=False),
    Column("payload_json", Text, nullable=False),
)

job_current = Table(
    "job_current",
    metadata,
    Column("job_id", String, primary_key=True),
    Column("semantic_revision", Integer, nullable=False),
    Column("intent_digest", String, nullable=False),
)

artifacts = Table(
    "artifacts",
    metadata,
    Column("artifact_id", String, primary_key=True),
    Column("job_id", String, nullable=False, index=True),
    Column("semantic_revision", Integer, nullable=False),
    Column("content_digest", String, nullable=False),
    Column("media_json", Text, nullable=False),
    Column("producing_run_ref", String, nullable=False),
)

runs = Table(
    "runs",
    metadata,
    Column("run_id", String, primary_key=True),
    Column("job_id", String, nullable=False, index=True),
    Column("semantic_revision", Integer, nullable=False),
    Column("execution_plan_ref", String, nullable=False),
    Column("actual_targets_json", Text, nullable=False),
    Column("outputs_json", Text, nullable=False),
    Column("raw_provider_result_ref", String),
    Column("usage_json", Text, nullable=False),
    Column("provider_request_id", String),
)
