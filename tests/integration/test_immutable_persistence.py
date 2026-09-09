from __future__ import annotations

import pytest

from aimage.contracts.visual_intent import VisualIntentState
from aimage.persistence.sqlite.repository import ImmutableRecordConflictError, SQLiteMetadataRepository
from aimage.persistence.sqlite.transactions import create_sqlite_engine


def test_same_record_is_idempotent_but_same_id_different_content_is_rejected(tmp_path) -> None:
    repository = SQLiteMetadataRepository(create_sqlite_engine(tmp_path / "immutable.db"), create_schema=True)
    first = VisualIntentState(object_id="fixed", job_id="job", semantic_revision=1)
    repository.save_object(first)
    repository.save_object(first)
    conflicting = first.model_copy(update={"semantic_revision": 2})
    with pytest.raises(ImmutableRecordConflictError): repository.save_object(conflicting)
