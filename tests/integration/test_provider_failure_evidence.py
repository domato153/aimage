from __future__ import annotations

import pytest
from sqlalchemy import select

from aimage.app.use_cases import ImageEngine
from aimage.contracts.visual_intent import IntentItem, VisualIntentState
from aimage.persistence.artifact_fs import LocalArtifactStore
from aimage.persistence.sqlite.repository import SQLiteMetadataRepository
from aimage.persistence.sqlite.schema import runs
from aimage.persistence.sqlite.transactions import create_sqlite_engine
from aimage.providers.openai.adapter import OpenAIAdapter
from aimage.providers.openai.errors import OpenAIProviderError


class RateLimitError(Exception):
    status_code = 429
    request_id = "req-rate"
    code = "rate_limit"
    body = {"message": "limited"}


class FailingImages:
    async def generate(self, **_kwargs):
        raise RateLimitError("limited")


class FailingClient:
    def __init__(self) -> None:
        self.images = FailingImages()


@pytest.mark.asyncio
async def test_provider_failure_is_persisted_as_run_evidence(tmp_path) -> None:
    db_engine = create_sqlite_engine(tmp_path / "failure.db")
    repository = SQLiteMetadataRepository(db_engine, create_schema=True)
    engine = ImageEngine(
        artifact_store=LocalArtifactStore(tmp_path / "artifacts"),
        metadata_repository=repository,
        openai_adapter=OpenAIAdapter(FailingClient()),
    )
    intent = VisualIntentState(
        job_id="job-failure",
        semantic_revision=1,
        intent_items=(
            IntentItem(
                semantic_path="content",
                visual_dimension="content",
                value_or_constraint="test",
                source_authority_id="user",
            ),
        ),
    )
    with pytest.raises(OpenAIProviderError):
        await engine.render(intent)
    with db_engine.connect() as connection:
        row = connection.execute(select(runs)).mappings().one()
    assert row["provider_request_id"] == "req-rate"
    assert "provider_error" in row["usage_json"]
    assert "429" in row["usage_json"]
