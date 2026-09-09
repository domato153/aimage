from __future__ import annotations

from collections.abc import Callable
from typing import Any

from .json_codec import UnsupportedSchemaError

Migration = Callable[[dict[str, Any]], dict[str, Any]]
_MIGRATIONS: dict[tuple[str, str, str], Migration] = {}


def register_migration(contract_type: str, from_version: str, to_version: str, migration: Migration) -> None:
    key = (contract_type, from_version, to_version)
    if key in _MIGRATIONS:
        raise ValueError(f"migration already registered: {key}")
    _MIGRATIONS[key] = migration


def migrate_payload(payload: dict[str, Any], *, to_version: str) -> dict[str, Any]:
    contract_type = str(payload.get("contract_type"))
    from_version = str(payload.get("schema_version"))
    if from_version == to_version:
        return dict(payload)
    migration = _MIGRATIONS.get((contract_type, from_version, to_version))
    if migration is None:
        raise UnsupportedSchemaError(
            f"no explicit migration for {contract_type!r} {from_version!r} -> {to_version!r}"
        )
    migrated = migration(dict(payload))
    migrated["schema_version"] = to_version
    return migrated
