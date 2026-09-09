from __future__ import annotations

import base64
from types import SimpleNamespace

import pytest
from sqlalchemy import select, update

from aimage.app.use_cases import ImageEngine
from aimage.contracts.spatial import ReferenceFrame, ReferenceFrameKind, SpatialEntity, SpatialProfile, SpatialRelation
from aimage.contracts.validation import ValidationOutcome, ValidationResult
from aimage.contracts.visual_intent import IntentItem, VisualIntentState
from aimage.engine.currentness import StaleStateError
from aimage.persistence.artifact_fs import LocalArtifactStore
from aimage.persistence.sqlite.repository import SQLiteMetadataRepository
from aimage.persistence.sqlite.schema import artifacts, job_current, runs
from aimage.persistence.sqlite.transactions import create_sqlite_engine
from aimage.providers.openai.adapter import OpenAIAdapter


class FakeImages:
    def __init__(self, on_generate=None) -> None:
        self.on_generate = on_generate

    async def generate(self, **_kwargs):
        if self.on_generate:
            self.on_generate()
        return SimpleNamespace(
            data=[SimpleNamespace(b64_json=base64.b64encode(b"image-bytes").decode())],
            _request_id="req-1",
            usage={"images": 1},
        )

    async def edit(self, **_kwargs):
        return SimpleNamespace(
            data=[SimpleNamespace(b64_json=base64.b64encode(b"edited-bytes").decode())],
            _request_id="req-2",
            usage={"images": 1},
        )


class FakeClient:
    def __init__(self, on_generate=None) -> None:
        self.images = FakeImages(on_generate=on_generate)


def _intent_and_spatial() -> tuple[VisualIntentState, SpatialProfile]:
    item = IntentItem(
        semantic_path="composition.subject_side",
        visual_dimension="composition",
        value_or_constraint="right",
        source_authority_id="user",
    )
    intent = VisualIntentState(job_id="job-1", semantic_revision=1, intent_items=(item,))
    spatial = SpatialProfile(
        job_id="job-1",
        semantic_revision=1,
        entities=(
            SpatialEntity(entity_id="viewer", semantic_role="viewer"),
            SpatialEntity(entity_id="subject", semantic_role="subject"),
        ),
        frames=(ReferenceFrame(frame_id="viewer", kind=ReferenceFrameKind.VIEWER_DEICTIC),),
        relations=(
            SpatialRelation(
                predicate="right_of",
                subject_entity_id="subject",
                object_entity_id="viewer",
                reference_frame_id="viewer",
                source_intent_id=item.intent_id,
            ),
        ),
    )
    return intent, spatial


@pytest.mark.asyncio
async def test_first_vertical_slice_persists_artifact_run_and_validation(tmp_path) -> None:
    db_engine = create_sqlite_engine(tmp_path / "aimage.db")
    repository = SQLiteMetadataRepository(db_engine, create_schema=True)
    store = LocalArtifactStore(tmp_path / "artifacts")
    image_engine = ImageEngine(
        artifact_store=store,
        metadata_repository=repository,
        openai_adapter=OpenAIAdapter(FakeClient()),
    )
    intent, spatial = _intent_and_spatial()
    validation = ValidationResult(
        rule_id="viewer-side",
        outcome=ValidationOutcome.PASS,
        semantic_path="composition.subject_side",
        dimension="composition",
        severity="blocker",
        evidence_refs=("fixture:viewer-side",),
        evaluator_identity="fixture-spatial-oracle",
        evaluator_version="1",
        evidence_class="deterministic_fixture",
    )
    result = await image_engine.render(
        intent,
        spatial_profile=spatial,
        validation_results=(validation,),
        mandatory_rule_ids=frozenset({"viewer-side"}),
        profile_versions=("composition-test-1",),
    )
    assert store.get(result.artifact.artifact_id) == b"image-bytes"
    assert result.validation.overall_outcome is ValidationOutcome.PASS
    with db_engine.connect() as connection:
        assert connection.execute(select(runs)).mappings().all()
        assert connection.execute(select(artifacts)).mappings().all()


def test_sqlite_currentness_compare_and_advance_is_fail_closed(tmp_path) -> None:
    db_engine = create_sqlite_engine(tmp_path / "current.db")
    repository = SQLiteMetadataRepository(db_engine, create_schema=True)
    repository.claim_or_assert_current("job", 1, "digest-1")
    repository.advance_current(
        "job",
        expected_revision=1,
        expected_digest="digest-1",
        new_revision=2,
        new_digest="digest-2",
    )
    with pytest.raises(StaleStateError):
        repository.assert_current("job", 1, "digest-1")
    with pytest.raises(StaleStateError):
        repository.advance_current(
            "job",
            expected_revision=1,
            expected_digest="digest-1",
            new_revision=3,
            new_digest="digest-3",
        )


@pytest.mark.asyncio
async def test_old_inflight_result_is_historical_not_current(tmp_path) -> None:
    db_engine = create_sqlite_engine(tmp_path / "race.db")
    repository = SQLiteMetadataRepository(db_engine, create_schema=True)
    store = LocalArtifactStore(tmp_path / "artifacts")

    def move_current_while_provider_is_inflight() -> None:
        with db_engine.begin() as connection:
            connection.execute(
                update(job_current)
                .where(job_current.c.job_id == "job-1")
                .values(semantic_revision=2, intent_digest="newer-semantic-state")
            )

    image_engine = ImageEngine(
        artifact_store=store,
        metadata_repository=repository,
        openai_adapter=OpenAIAdapter(FakeClient(on_generate=move_current_while_provider_is_inflight)),
    )
    intent, spatial = _intent_and_spatial()
    with pytest.raises(StaleStateError):
        await image_engine.render(intent, spatial_profile=spatial)

    # The late provider output remains immutable historical evidence, but never reaches current validation/acceptance.
    with db_engine.connect() as connection:
        assert len(connection.execute(select(runs)).mappings().all()) == 1
        assert len(connection.execute(select(artifacts)).mappings().all()) == 1
        current = connection.execute(select(job_current)).mappings().one()
        assert current["semantic_revision"] == 2
