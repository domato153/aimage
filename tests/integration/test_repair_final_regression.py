from __future__ import annotations

import base64
from types import SimpleNamespace

import pytest

from aimage.app.use_cases import ImageEngine
from aimage.contracts.validation import ValidationOutcome, ValidationResult
from aimage.contracts.visual_intent import (
    BaselineRecord,
    IntentItem,
    MutationFrame,
    MutationReason,
    VisualIntentState,
)
from aimage.persistence.artifact_fs import LocalArtifactStore
from aimage.persistence.sqlite.repository import SQLiteMetadataRepository
from aimage.persistence.sqlite.transactions import create_sqlite_engine
from aimage.providers.openai.adapter import OpenAIAdapter


class FakeImages:
    async def edit(self, **_kwargs):
        return SimpleNamespace(
            data=[SimpleNamespace(b64_json=base64.b64encode(b"repaired").decode())],
            _request_id="repair-1",
            usage={},
        )


class FakeClient:
    def __init__(self) -> None:
        self.images = FakeImages()


def _approved_intent() -> VisualIntentState:
    return VisualIntentState(
        job_id="repair-job",
        semantic_revision=2,
        intent_items=(
            IntentItem(
                semantic_path="expression",
                visual_dimension="expression",
                value_or_constraint="subtle smile",
                source_authority_id="user",
            ),
        ),
        baselines=(
            BaselineRecord(
                approved_at_revision=2,
                approved_paths=("identity", "composition"),
                approved_dimensions=("identity", "composition"),
                value_snapshot_ref="snapshot:approved",
                approval_decision_id="approve-1",
            ),
        ),
    )


@pytest.mark.asyncio
async def test_repair_cannot_pass_without_final_preservation_evidence(tmp_path) -> None:
    engine = create_sqlite_engine(tmp_path / "repair.db")
    repository = SQLiteMetadataRepository(engine, create_schema=True)
    image_engine = ImageEngine(
        artifact_store=LocalArtifactStore(tmp_path / "artifacts"),
        metadata_repository=repository,
        openai_adapter=OpenAIAdapter(FakeClient()),
    )
    mutation = MutationFrame(
        semantic_revision=2,
        reason=MutationReason.REPAIR,
        mutable_paths=("expression",),
        preserve_paths=("identity", "composition"),
    )
    expression_pass = ValidationResult(
        rule_id="expression",
        outcome=ValidationOutcome.PASS,
        semantic_path="expression",
        dimension="expression",
        severity="blocker",
        evaluator_identity="human-fixture",
        evaluator_version="1",
        evidence_class="human",
    )
    result = await image_engine.render(
        _approved_intent(),
        operation="edit",
        source_artifacts=(("sha256:source", b"source"),),
        mutation_frame=mutation,
        validation_results=(expression_pass,),
        mandatory_rule_ids=frozenset({"expression"}),
    )
    assert result.validation.overall_outcome is ValidationOutcome.INDETERMINATE
    missing_paths = {
        item.semantic_path
        for item in result.validation.results
        if item.outcome is ValidationOutcome.INDETERMINATE
    }
    assert {"identity", "composition"} <= missing_paths


@pytest.mark.asyncio
async def test_repair_passes_only_when_final_preserved_paths_are_revalidated(tmp_path) -> None:
    engine = create_sqlite_engine(tmp_path / "repair-pass.db")
    repository = SQLiteMetadataRepository(engine, create_schema=True)
    image_engine = ImageEngine(
        artifact_store=LocalArtifactStore(tmp_path / "artifacts-pass"),
        metadata_repository=repository,
        openai_adapter=OpenAIAdapter(FakeClient()),
    )
    mutation = MutationFrame(
        semantic_revision=2,
        reason=MutationReason.REPAIR,
        mutable_paths=("expression",),
        preserve_paths=("identity", "composition"),
    )
    results = tuple(
        ValidationResult(
            rule_id=path,
            outcome=ValidationOutcome.PASS,
            semantic_path=path,
            dimension=path,
            severity="blocker",
            evaluator_identity="human-fixture",
            evaluator_version="1",
            evidence_class="human",
        )
        for path in ("expression", "identity", "composition")
    )
    result = await image_engine.render(
        _approved_intent(),
        operation="edit",
        source_artifacts=(("sha256:source", b"source"),),
        mutation_frame=mutation,
        validation_results=results,
        mandatory_rule_ids=frozenset({"expression", "identity", "composition"}),
    )
    assert result.validation.overall_outcome is ValidationOutcome.PASS
