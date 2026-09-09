from __future__ import annotations

from datetime import datetime, timezone
from enum import StrEnum
from typing import Any
from uuid import uuid4

from pydantic import BaseModel, ConfigDict, Field


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def new_object_id() -> str:
    return uuid4().hex


class Strength(StrEnum):
    MANDATORY = "mandatory"
    PREFERRED = "preferred"
    ADVISORY = "advisory"


class EvidenceKind(StrEnum):
    DECLARED = "declared"
    PROBED = "probed"
    CONFIGURED = "configured"
    REPRODUCED = "reproduced"


class ContractModel(BaseModel):
    """Base for AIMAGE-owned durable/derived records.

    Pydantic is the representation validator, not the semantic authority.
    """

    model_config = ConfigDict(extra="forbid", frozen=True)

    contract_type: str
    schema_version: str = "1.0"
    object_id: str = Field(default_factory=new_object_id)
    job_id: str
    semantic_revision: int = Field(ge=1)
    created_from: tuple[str, ...] = ()


class DerivedContractModel(ContractModel):
    source_semantic_revision: int = Field(ge=1)
    source_intent_digest: str


JsonValue = Any
