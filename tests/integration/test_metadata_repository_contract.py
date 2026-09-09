from __future__ import annotations

from collections.abc import Callable

import pytest

from aimage.contracts.execution import RunRecord
from aimage.engine.currentness import StaleStateError
from aimage.persistence.memory import InMemoryMetadataRepository
from aimage.persistence.sqlite.repository import SQLiteMetadataRepository
from aimage.persistence.sqlite.transactions import create_sqlite_engine


@pytest.fixture(params=["memory", "sqlite"])
def repository(request, tmp_path):
    if request.param == "memory":
        return InMemoryMetadataRepository()
    return SQLiteMetadataRepository(create_sqlite_engine(tmp_path / "repository-contract.db"), create_schema=True)


def test_repository_currentness_contract_is_replaceable(repository) -> None:
    repository.claim_or_assert_current("job", 1, "digest-1")
    repository.assert_current("job", 1, "digest-1")
    repository.advance_current(
        "job",
        expected_revision=1,
        expected_digest="digest-1",
        new_revision=2,
        new_digest="digest-2",
    )
    repository.assert_current("job", 2, "digest-2")
    with pytest.raises(StaleStateError):
        repository.advance_current(
            "job",
            expected_revision=1,
            expected_digest="digest-1",
            new_revision=3,
            new_digest="digest-3",
        )


def test_repository_run_lifecycle_contract_is_replaceable(repository) -> None:
    repository.start_run(
        run_id="run-1",
        job_id="job",
        semantic_revision=1,
        source_intent_digest="digest-1",
        execution_plan_ref="plan-1",
        capability_descriptor_ref="descriptor-1",
        target_model_version="model-1",
    )
    completed = RunRecord(
        run_id="run-1",
        job_id="job",
        semantic_revision=1,
        execution_plan_ref="plan-1",
        actual_target_versions=("model-1",),
        output_artifact_refs=("artifact-1",),
    )
    repository.finish_run(
        completed,
        source_intent_digest="digest-1",
        capability_descriptor_ref="descriptor-1",
        status="completed",
    )
    with pytest.raises((ValueError, RuntimeError)):
        repository.finish_run(
            completed,
            source_intent_digest="digest-1",
            capability_descriptor_ref="descriptor-1",
            status="completed",
        )
