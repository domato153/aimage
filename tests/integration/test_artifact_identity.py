from __future__ import annotations

from aimage.persistence.artifact_fs import LocalArtifactStore


def test_equal_bytes_share_blob_ref_without_claiming_same_aimage_artifact_identity(tmp_path) -> None:
    store = LocalArtifactStore(tmp_path / "blobs")
    first = store.put(b"same", media_type="image/png")
    second = store.put(b"same", media_type="image/png")
    assert first.storage_ref == second.storage_ref
    assert first.content_digest == second.content_digest
    # AIMAGE artifact IDs are assigned separately by the engine/run layer, not by the blob store.
    assert not hasattr(first, "artifact_id")
