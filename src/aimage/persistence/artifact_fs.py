from __future__ import annotations

import hashlib
from pathlib import Path

from aimage.engine.interfaces.artifact_store import ArtifactDeletePolicy, StoredArtifact


class LocalArtifactStore:
    """Content-addressed blob store; AIMAGE ArtifactRecord identity is separate."""

    def __init__(self, root: str | Path) -> None:
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)

    def _parse_ref(self, storage_ref: str) -> str:
        algorithm, separator, digest = storage_ref.partition(":")
        if algorithm != "sha256" or not separator or len(digest) != 64:
            raise KeyError(f"unsupported storage ref {storage_ref!r}")
        return digest

    def _path_for_digest(self, digest: str) -> Path:
        return self.root / "sha256" / digest[:2] / digest[2:4] / digest

    def put(self, data: bytes, *, media_type: str) -> StoredArtifact:
        digest = hashlib.sha256(data).hexdigest()
        path = self._path_for_digest(digest)
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists():
            temporary = path.with_name(f".{path.name}.tmp")
            temporary.write_bytes(data)
            temporary.replace(path)
        metadata_path = path.with_suffix(".meta")
        if not metadata_path.exists():
            metadata_path.write_text(f"{media_type}\n{len(data)}\n", encoding="utf-8")
        return StoredArtifact(
            storage_ref=f"sha256:{digest}",
            content_digest=f"sha256:{digest}",
            media_type=media_type,
            size_bytes=len(data),
        )

    def get(self, storage_ref: str) -> bytes:
        digest = self._parse_ref(storage_ref)
        path = self._path_for_digest(digest)
        if not path.exists():
            raise KeyError(storage_ref)
        return path.read_bytes()

    def exists(self, storage_ref: str) -> bool:
        try:
            digest = self._parse_ref(storage_ref)
        except KeyError:
            return False
        return self._path_for_digest(digest).exists()

    def metadata(self, storage_ref: str) -> StoredArtifact:
        digest = self._parse_ref(storage_ref)
        path = self._path_for_digest(digest)
        if not path.exists():
            raise KeyError(storage_ref)
        metadata_path = path.with_suffix(".meta")
        if not metadata_path.exists():
            raise KeyError(f"metadata missing for {storage_ref!r}")
        media_type, size_text = metadata_path.read_text(encoding="utf-8").splitlines()
        return StoredArtifact(
            storage_ref=storage_ref,
            content_digest=f"sha256:{digest}",
            media_type=media_type,
            size_bytes=int(size_text),
        )

    def delete(
        self,
        storage_ref: str,
        *,
        policy: ArtifactDeletePolicy,
        is_referenced: bool,
    ) -> bool:
        if policy is ArtifactDeletePolicy.RETAIN:
            return False
        if policy is not ArtifactDeletePolicy.PURGE_UNREFERENCED:
            raise ValueError(f"unsupported delete policy: {policy!r}")
        if is_referenced:
            raise ValueError("referenced artifact blobs cannot be deleted")
        digest = self._parse_ref(storage_ref)
        path = self._path_for_digest(digest)
        if not path.exists():
            return False
        path.unlink()
        metadata_path = path.with_suffix(".meta")
        if metadata_path.exists():
            metadata_path.unlink()
        return True
