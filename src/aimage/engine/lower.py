from __future__ import annotations

from aimage.contracts.common import Strength
from aimage.contracts.execution import ExecutionPlan
from aimage.contracts.render import RenderSpec
from aimage.contracts.requirements import Necessity, RequirementSet


class LoweringLegalityError(ValueError):
    pass


def validate_lowering_legality(render_spec: RenderSpec, requirement_set: RequirementSet, plan: ExecutionPlan) -> None:
    """Fail closed when an executable plan loses mandatory semantic/requirement coverage."""
    if plan.source_semantic_revision != render_spec.source_semantic_revision:
        raise LoweringLegalityError("execution plan belongs to another semantic revision")
    if plan.source_intent_digest != render_spec.source_intent_digest:
        raise LoweringLegalityError("execution plan source digest differs from RenderSpec")
    if plan.render_spec_ref != render_spec.render_spec_id:
        raise LoweringLegalityError("execution plan references another RenderSpec")

    traces_by_path = {}
    requirement_ids = set()
    for trace in plan.lowering_trace:
        traces_by_path.setdefault(trace.source_semantic_path, []).append(trace)
        requirement_ids.add(trace.requirement_id)

    missing_paths = []
    illegal_paths = []
    for obligation in render_spec.intent_obligations:
        if obligation.strength is not Strength.MANDATORY:
            continue
        traces = traces_by_path.get(obligation.semantic_path, [])
        if not traces:
            missing_paths.append(obligation.semantic_path)
        elif not any(trace.fidelity == "exact" for trace in traces):
            illegal_paths.append(obligation.semantic_path)

    mandatory_requirements = {
        requirement.requirement_id
        for requirement in requirement_set.requirements
        if requirement.necessity is Necessity.MANDATORY
    }
    missing_requirements = mandatory_requirements - requirement_ids
    if missing_paths or illegal_paths or missing_requirements:
        raise LoweringLegalityError(
            "illegal lowering: "
            f"missing_paths={sorted(missing_paths)} "
            f"non_exact_paths={sorted(illegal_paths)} "
            f"missing_requirements={sorted(missing_requirements)}"
        )
