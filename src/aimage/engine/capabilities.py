from __future__ import annotations

import hashlib
import json

from aimage.contracts.resolution import ProviderCapabilityDescriptor, ResolutionResult, ResolutionStatus
from aimage.engine.resolve import descriptor_is_fresh


class CapabilityDriftError(RuntimeError):
    pass


def descriptor_signature(descriptor: ProviderCapabilityDescriptor) -> str:
    payload = {
        "target_id": descriptor.target_id,
        "target_kind": descriptor.target_kind,
        "adapter_id": descriptor.adapter_id,
        "adapter_version": descriptor.adapter_version,
        "target_version_or_model": descriptor.target_version_or_model,
        "evidence_kind": descriptor.evidence_kind.value,
        "evidence_uri": descriptor.evidence_uri,
        "capabilities": [cap.model_dump(mode="json") for cap in descriptor.capabilities],
        "known_limits": descriptor.known_limits,
    }
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def assert_resolution_capability_current(
    resolution: ResolutionResult,
    resolved_descriptors: tuple[ProviderCapabilityDescriptor, ...],
    current_descriptors: tuple[ProviderCapabilityDescriptor, ...],
) -> None:
    if resolution.status is not ResolutionStatus.RESOLVED:
        raise CapabilityDriftError("cannot execute a non-resolved strategy")
    old_by_id = {descriptor.descriptor_id: descriptor for descriptor in resolved_descriptors}
    current_by_target = {descriptor.target_id: descriptor for descriptor in current_descriptors}
    for wiring in resolution.requirement_wiring:
        old = old_by_id.get(wiring.target_descriptor_ref)
        if old is None:
            raise CapabilityDriftError("resolution references an unknown capability descriptor")
        current = current_by_target.get(old.target_id)
        if current is None or not descriptor_is_fresh(current):
            raise CapabilityDriftError(f"capability target {old.target_id!r} is unavailable or stale")
        if descriptor_signature(old) != descriptor_signature(current):
            raise CapabilityDriftError(f"capability target {old.target_id!r} drifted after resolution")
