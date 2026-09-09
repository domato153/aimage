from __future__ import annotations

from datetime import datetime, timedelta, timezone
from aimage.contracts.common import EvidenceKind
from aimage.contracts.requirements import CapabilityRequirement, Necessity, RequirementSet
from aimage.contracts.resolution import Capability, ProviderCapabilityDescriptor, ResolutionStatus
from aimage.engine.resolve import resolve_requirements


def _descriptor(target: str, capability: str) -> ProviderCapabilityDescriptor:
    now = datetime.now(timezone.utc); return ProviderCapabilityDescriptor(job_id="job", semantic_revision=1, target_id=target, target_kind="provider" if capability == "generate" else "utility", adapter_id=f"adapter:{target}", adapter_version="1", target_version_or_model="1", observed_at=now, valid_until=now + timedelta(hours=1), evidence_kind=EvidenceKind.REPRODUCED, evidence_uri=f"fixture:{target}", capabilities=(Capability(namespace="aimage.image", name=capability),))

def test_resolution_can_compose_two_targets_without_changing_semantics() -> None:
    requirements = RequirementSet(job_id="job", semantic_revision=1, render_spec_ref="render", requirements=(CapabilityRequirement(namespace="aimage.image", action_or_capability="generate", necessity=Necessity.MANDATORY, constraints={"evidence_kind": ("reproduced",)}), CapabilityRequirement(namespace="aimage.image", action_or_capability="deterministic_text_layout", necessity=Necessity.MANDATORY, constraints={"evidence_kind": ("reproduced",)})))
    result = resolve_requirements(requirements, (_descriptor("image-provider", "generate"), _descriptor("text-compositor", "deterministic_text_layout"))); assert result.status is ResolutionStatus.RESOLVED; assert result.selected_strategy == ("image-provider", "text-compositor")
