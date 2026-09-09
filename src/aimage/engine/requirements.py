from __future__ import annotations

from aimage.contracts.common import EvidenceKind
from aimage.contracts.requirements import CapabilityRequirement, Necessity, RequirementSet
from aimage.contracts.render import RenderSpec


class RequirementDerivationError(ValueError):
    pass


def _parse_size(size: object) -> tuple[int, int] | None:
    if not isinstance(size, str) or size == "auto":
        return None
    try:
        width_text, height_text = size.lower().split("x", 1)
        return int(width_text), int(height_text)
    except (ValueError, AttributeError) as exc:
        raise RequirementDerivationError(f"invalid output size {size!r}") from exc


def derive_requirements(
    render_spec: RenderSpec,
    *,
    operation: str,
    acceptable_evidence_kinds: tuple[EvidenceKind, ...] = (EvidenceKind.REPRODUCED,),
) -> RequirementSet:
    if operation not in {"generate", "edit"}:
        raise RequirementDerivationError(f"unsupported operation {operation!r}")
    if not acceptable_evidence_kinds:
        raise RequirementDerivationError("at least one acceptable capability evidence kind is required")

    constraints: dict[str, object] = {
        "input_kind": "text" if operation == "generate" else "image+text",
        "evidence_kind": tuple(kind.value for kind in acceptable_evidence_kinds),
    }
    parsed = _parse_size(render_spec.output_contract.get("size"))
    if parsed:
        constraints["width"], constraints["height"] = parsed
    if operation == "edit" and render_spec.preservation_obligations:
        constraints["input_fidelity"] = "high"

    requirement = CapabilityRequirement(
        namespace="aimage.image",
        action_or_capability=operation,
        necessity=Necessity.MANDATORY,
        constraints=constraints,
        source_semantic_paths=tuple(obligation.semantic_path for obligation in render_spec.intent_obligations),
    )
    return RequirementSet(
        job_id=render_spec.job_id,
        semantic_revision=render_spec.semantic_revision,
        created_from=(render_spec.object_id,),
        render_spec_ref=render_spec.render_spec_id,
        requirements=(requirement,),
    )
