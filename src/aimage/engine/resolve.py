from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from aimage.contracts.requirements import CapabilityRequirement, Necessity, RequirementSet
from aimage.contracts.resolution import (
    Capability,
    ProviderCapabilityDescriptor,
    RequirementWiring,
    ResolutionResult,
    ResolutionStatus,
)


def descriptor_is_fresh(descriptor: ProviderCapabilityDescriptor, now: datetime | None = None) -> bool:
    now = now or datetime.now(timezone.utc)
    return descriptor.valid_until is None or descriptor.valid_until >= now


def _constraint_matches(key: str, expected: Any, descriptor: ProviderCapabilityDescriptor, capability: Capability) -> bool:
    if key == "target_version_or_model":
        return descriptor.target_version_or_model == expected
    if key in capability.attributes:
        actual = capability.attributes[key]
        if isinstance(actual, (tuple, list, set, frozenset)):
            return expected in actual
        return actual == expected
    if key in capability.limits:
        limit = capability.limits[key]
        if isinstance(limit, (tuple, list, set, frozenset)):
            return expected in limit
        return limit == expected
    return False


def capability_satisfies(
    requirement: CapabilityRequirement,
    descriptor: ProviderCapabilityDescriptor,
    capability: Capability,
) -> bool:
    if capability.namespace != requirement.namespace or capability.name != requirement.action_or_capability:
        return False
    return all(_constraint_matches(key, value, descriptor, capability) for key, value in requirement.constraints.items())


def resolve_requirements(
    requirement_set: RequirementSet,
    descriptors: tuple[ProviderCapabilityDescriptor, ...],
    *,
    now: datetime | None = None,
) -> ResolutionResult:
    wiring: list[RequirementWiring] = []
    unsatisfied_mandatory: list[str] = []
    unsatisfied_optional: list[str] = []
    used_targets: list[str] = []
    stale_candidate_seen = False

    for requirement in requirement_set.requirements:
        match: tuple[ProviderCapabilityDescriptor, Capability] | None = None
        for descriptor in descriptors:
            for capability in descriptor.capabilities:
                if capability_satisfies(requirement, descriptor, capability):
                    if not descriptor_is_fresh(descriptor, now):
                        stale_candidate_seen = True
                        continue
                    match = (descriptor, capability)
                    break
            if match:
                break

        if match:
            descriptor, capability = match
            wiring.append(
                RequirementWiring(
                    requirement_id=requirement.requirement_id,
                    target_descriptor_ref=descriptor.descriptor_id,
                    capability_name=capability.name,
                )
            )
            if descriptor.target_id not in used_targets:
                used_targets.append(descriptor.target_id)
        elif requirement.necessity is Necessity.MANDATORY:
            unsatisfied_mandatory.append(requirement.requirement_id)
        else:
            unsatisfied_optional.append(requirement.requirement_id)

    if unsatisfied_mandatory and stale_candidate_seen:
        status = ResolutionStatus.STALE_CAPABILITIES
        rationale = "mandatory requirements match only stale capability evidence"
    elif unsatisfied_mandatory:
        status = ResolutionStatus.UNSATISFIED
        rationale = "one or more mandatory requirements are unsatisfied"
    else:
        status = ResolutionStatus.RESOLVED
        rationale = "all mandatory requirements are wired to fresh compatible capabilities"

    return ResolutionResult(
        job_id=requirement_set.job_id,
        semantic_revision=requirement_set.semantic_revision,
        created_from=(requirement_set.object_id,) + tuple(d.object_id for d in descriptors),
        render_spec_ref=requirement_set.render_spec_ref,
        requirement_set_ref=requirement_set.requirement_set_id,
        status=status,
        selected_strategy=tuple(used_targets),
        requirement_wiring=tuple(wiring),
        unsatisfied_mandatory=tuple(unsatisfied_mandatory),
        unsatisfied_optional=tuple(unsatisfied_optional),
        rationale=rationale,
    )
