from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class RepairStop(RuntimeError):
    pass


class RepairPolicy(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    max_attempts: int = Field(default=3, ge=1)
    max_cost: float | None = Field(default=None, gt=0)
    max_non_improving: int = Field(default=1, ge=0)


class RepairProgress(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    attempts: int = 0
    cumulative_cost: float = 0.0
    best_score: float | None = None
    best_artifact_ref: str | None = None
    non_improving: int = 0
    seen_fingerprints: tuple[str, ...] = ()


def advance_repair(
    progress: RepairProgress,
    policy: RepairPolicy,
    *,
    artifact_ref: str,
    score: float,
    fingerprint: str,
    cost: float = 0.0,
) -> RepairProgress:
    if fingerprint in progress.seen_fingerprints:
        raise RepairStop("repair oscillation detected")
    attempts = progress.attempts + 1
    cumulative_cost = progress.cumulative_cost + cost
    if attempts > policy.max_attempts:
        raise RepairStop("repair attempt budget exhausted")
    if policy.max_cost is not None and cumulative_cost > policy.max_cost:
        raise RepairStop("repair cost budget exhausted")

    improved = progress.best_score is None or score > progress.best_score
    non_improving = 0 if improved else progress.non_improving + 1
    if non_improving > policy.max_non_improving:
        raise RepairStop("repair is not improving")

    return RepairProgress(
        attempts=attempts,
        cumulative_cost=cumulative_cost,
        best_score=score if improved else progress.best_score,
        best_artifact_ref=artifact_ref if improved else progress.best_artifact_ref,
        non_improving=non_improving,
        seen_fingerprints=progress.seen_fingerprints + (fingerprint,),
    )
