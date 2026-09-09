from __future__ import annotations

import hashlib
from pathlib import Path

from aimage.engine.interfaces.artifact_store import StoredArtifact


class LocalArtifactStore:
    """Content-addressed local blob store; media semantics stay in ArtifactRecord."""

    def __init__(self, root: str | Path) -> None:
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)

    def _path_for_digest(self, digest: str) -> Path:
        return self.root / "sha256" / digest[:2] / digest[2:4] / digest

    def put(self, data: bytes, *, media_type: str) -> StoredArtifact:
        digest = hashlib.sha256(data).hexdigest()
        path = self._path_for_digest(digest)
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists():
            temporary = path.with_suffix(".tmp")
            temporary.write_bytes(data)
            temporary.replace(path)
        return StoredArtifact(
            artifact_id=f"sha256:{digest}",
            content_digest=f"sha256:{digest}",
            media_type=media_type,
            size_bytes=len(data),
        )

    def get(self, artifact_id: str) -> bytes:
        algorithm, separator, digest = artifact_id.partition(":")
        if algorithm != "sha256" or not separator or len(digest) != 64:
            raise KeyError(f"unsupported artifact id {artifact_id!r}")
        path = self._path_for_digest(digest)
        if not path.exists():
            raise KeyError(artifact_id)
        return path.read_bytes()
