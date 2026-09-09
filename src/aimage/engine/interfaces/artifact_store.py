from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class StoredArtifact:
    storage_ref: str
    content_digest: str
    media_type: str
    size_bytes: int


class ArtifactStore(Protocol):
    def put(self, data: bytes, *, media_type: str) -> StoredArtifact: ...
    def get(self, storage_ref: str) -> bytes: ...
