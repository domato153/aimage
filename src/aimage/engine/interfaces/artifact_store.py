from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
from typing import Protocol


@dataclass(frozen=True)
class StoredArtifact:
    storage_ref: str
    content_digest: str
    media_type: str
    size_bytes: int


class ArtifactDeletePolicy(StrEnum):
    RETAIN = "retain"
    PURGE_UNREFERENCED = "purge_unreferenced"


class ArtifactStore(Protocol):
    """Provider-neutral immutable blob-store boundary.

    Artifact identity/lineage belongs to ArtifactRecord.  ``storage_ref`` identifies only
    content-addressed bytes.  Destructive deletion is explicit and may only target a blob
    that the metadata owner has already proved unreferenced.
    """

    def put(self, data: bytes, *, media_type: str) -> StoredArtifact: ...
    def get(self, storage_ref: str) -> bytes: ...
    def exists(self, storage_ref: str) -> bool: ...
    def metadata(self, storage_ref: str) -> StoredArtifact: ...
    def delete(
        self,
        storage_ref: str,
        *,
        policy: ArtifactDeletePolicy,
        is_referenced: bool,
    ) -> bool: ...
