from __future__ import annotations

from alembic import command
from alembic.config import Config
from sqlalchemy import create_engine, inspect


REQUIRED_TABLES = {
    "jobs",
    "semantic_documents",
    "semantic_support_documents",
    "derived_documents",
    "capability_descriptors",
    "decisions",
    "baselines",
    "artifact_dispositions",
    "runs",
    "artifacts",
    "validation_reports",
}


def _config(database_path) -> Config:
    config = Config("alembic.ini")
    config.set_main_option("sqlalchemy.url", f"sqlite+pysqlite:///{database_path}")
    return config


def test_empty_database_migrates_to_head_idempotently_and_downgrades(tmp_path) -> None:
    database_path = tmp_path / "migration.db"
    config = _config(database_path)

    command.upgrade(config, "head")
    command.upgrade(config, "head")

    engine = create_engine(f"sqlite+pysqlite:///{database_path}")
    tables = set(inspect(engine).get_table_names())
    assert REQUIRED_TABLES <= tables
    assert "object_records" not in tables

    command.downgrade(config, "base")
    remaining = set(inspect(engine).get_table_names())
    assert not (REQUIRED_TABLES & remaining)
