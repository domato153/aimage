from __future__ import annotations

import pytest

from aimage.engine.interfaces.artifact_store import ArtifactDeletePolicy
from aimage.persistence.artifact_fs import LocalArtifactStore


def test_artifact_store_exposes_content_metadata_and_fail_safe_delete_policy(tmp_path) -> None:
    store = LocalArtifactStore(tmp_path / "artifacts")
    stored = store.put(b"same-bytes", media_type="image/png")

    assert store.exists(stored.storage_ref)
    assert store.get(stored.storage_ref) == b"same-bytes"
    assert store.metadata(stored.storage_ref) == stored
    assert store.delete(stored.storage_ref, policy=ArtifactDeletePolicy.RETAIN, is_referenced=False) is False
    assert store.exists(stored.storage_ref)

    with pytest.raises(ValueError):
        store.delete(
            stored.storage_ref,
            policy=ArtifactDeletePolicy.PURGE_UNREFERENCED,
            is_referenced=True,
        )
    assert store.exists(stored.storage_ref)

    assert store.delete(
        stored.storage_ref,
        policy=ArtifactDeletePolicy.PURGE_UNREFERENCED,
        is_referenced=False,
    ) is True
    assert not store.exists(stored.storage_ref)
