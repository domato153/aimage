from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class RepairStop(RuntimeError):
    pass


class RepairEvidence(BaseModel):
    """Partial-order evidence for comparing repair candidates.

    AIMAGE deliberately avoids a scalar aesthetic score. A candidate is strictly better
    only when it removes at least one material failure without introducing any mandatory
    or preservation regression.
    """

    model_config = ConfigDict(extra="forbid", frozen=True)

    material_failures: frozenset[str] = frozenset()
    mandatory_regressions: frozenset[str] = frozenset()
    preservation_regressions: frozenset[str] = frozenset()

    @property
    def is_non_regressed(self) -> bool:
        return not self.mandatory_regressions and not self.preservation_regressions

    def strictly_improves(self, previous: "RepairEvidence") -> bool:
        return (
            self.is_non_regressed
            and previous.is_non_regressed
            and self.material_failures < previous.material_failures
        )


class RepairPolicy(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    max_attempts: int = Field(default=3, ge=1)
    max_cost: float | None = Field(default=None, gt=0)
    max_non_improving: int = Field(default=1, ge=0)


class RepairProgress(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    attempts: int = 0
    cumulative_cost: float = 0.0
    best_evidence: RepairEvidence | None = None
    best_artifact_ref: str | None = None
    non_improving: int = 0
    seen_fingerprints: tuple[str, ...] = ()


def advance_repair(
    progress: RepairProgress,
    policy: RepairPolicy,
    *,
    artifact_ref: str,
    evidence: RepairEvidence,
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

    if progress.best_evidence is None:
        improved = evidence.is_non_regressed
    else:
        improved = evidence.strictly_improves(progress.best_evidence)

    non_improving = 0 if improved else progress.non_improving + 1
    if non_improving > policy.max_non_improving:
        raise RepairStop("repair is not strictly improving under the partial-order policy")

    return RepairProgress(
        attempts=attempts,
        cumulative_cost=cumulative_cost,
        best_evidence=evidence if improved else progress.best_evidence,
        best_artifact_ref=artifact_ref if improved else progress.best_artifact_ref,
        non_improving=non_improving,
        seen_fingerprints=progress.seen_fingerprints + (fingerprint,),
    )
