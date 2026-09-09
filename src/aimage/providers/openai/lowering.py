from __future__ import annotations

import hashlib
import json
from typing import Literal

from pydantic import BaseModel, ConfigDict

from aimage.contracts.common import new_object_id
from aimage.contracts.execution import ExecutionPlan, ExecutionStep, LoweringTraceEntry
from aimage.contracts.render import RenderSpec
from aimage.contracts.requirements import RequirementSet
from aimage.contracts.resolution import ProviderCapabilityDescriptor, ResolutionResult, ResolutionStatus
from aimage.contracts.visual_intent import MutationFrame


class OpenAIRenderRequest(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    operation: Literal["generate", "edit"]
    model: str
    prompt: str
    size: str
    quality: Literal["low", "medium", "high", "xhigh", "max", "auto"] = "high"
    output_format: Literal["png", "jpeg", "webp"] = "png"
    input_fidelity: Literal["high", "low"] | None = None


class LoweredOpenAI(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True, arbitrary_types_allowed=True)

    request: OpenAIRenderRequest
    execution_plan: ExecutionPlan


def _render_prompt(render_spec: RenderSpec, mutation_frame: MutationFrame | None) -> str:
    lines = [
        "AIMAGE provider lowering. Preserve the semantic meanings below; do not reinterpret reference-frame labels.",
    ]
    for obligation in render_spec.intent_obligations:
        encoded = json.dumps(obligation.value_or_constraint, sort_keys=True, ensure_ascii=False, default=str)
        lines.append(
            f"[{obligation.strength.value.upper()}] path={obligation.semantic_path} "
            f"dimension={obligation.dimension} value={encoded}"
        )
    for preservation in render_spec.preservation_obligations:
        lines.append(
            "[PRESERVE] baseline=" + preservation.baseline_id
            + " paths=" + json.dumps(preservation.approved_paths)
            + " dimensions=" + json.dumps(preservation.approved_dimensions)
        )
    if mutation_frame:
        lines.append("[MUTATION_FRAME] mutable=" + json.dumps(mutation_frame.mutable_paths))
        lines.append("[MUTATION_FRAME] preserve=" + json.dumps(mutation_frame.preserve_paths))
    return "\n".join(lines)


def lower_openai(
    render_spec: RenderSpec,
    requirement_set: RequirementSet,
    resolution: ResolutionResult,
    descriptor: ProviderCapabilityDescriptor,
    *,
    operation: Literal["generate", "edit"],
    source_artifact_refs: tuple[str, ...] = (),
    mutation_frame: MutationFrame | None = None,
) -> LoweredOpenAI:
    if resolution.status is not ResolutionStatus.RESOLVED:
        raise ValueError("cannot lower an unresolved strategy")
    if descriptor.target_id not in resolution.selected_strategy:
        raise ValueError("descriptor is not part of the selected strategy")
    if mutation_frame and mutation_frame.semantic_revision != render_spec.semantic_revision:
        raise ValueError("mutation frame belongs to another semantic revision")
    if operation == "edit" and not source_artifact_refs:
        raise ValueError("edit lowering requires a source artifact")

    size = str(render_spec.output_contract.get("size", "1024x1024"))
    request = OpenAIRenderRequest(
        operation=operation,
        model=descriptor.target_version_or_model,
        prompt=_render_prompt(render_spec, mutation_frame),
        size=size,
        quality="high",
        output_format="png",
        input_fidelity="high" if operation == "edit" and render_spec.preservation_obligations else None,
    )
    payload = json.dumps(request.model_dump(mode="json"), sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    payload_ref = "sha256:" + hashlib.sha256(payload.encode("utf-8")).hexdigest()
    step_id = new_object_id()
    primary_requirement = requirement_set.requirements[0]
    plan = ExecutionPlan(
        job_id=render_spec.job_id,
        semantic_revision=render_spec.semantic_revision,
        source_semantic_revision=render_spec.semantic_revision,
        source_intent_digest=render_spec.source_intent_digest,
        created_from=(render_spec.object_id, requirement_set.object_id, resolution.object_id, descriptor.object_id),
        render_spec_ref=render_spec.render_spec_id,
        resolution_ref=resolution.resolution_id,
        steps=(
            ExecutionStep(
                step_id=step_id,
                target_descriptor_ref=descriptor.descriptor_id,
                operation=operation,
                input_refs=tuple(dict.fromkeys(source_artifact_refs + render_spec.input_artifact_refs)),
                provider_or_tool_payload_ref=payload_ref,
                output_role="candidate_image",
            ),
        ),
        lowering_trace=tuple(
            LoweringTraceEntry(
                source_semantic_path=obligation.semantic_path,
                requirement_id=primary_requirement.requirement_id,
                target_step_id=step_id,
                representation="openai_image_prompt",
                fidelity="exact",
            )
            for obligation in render_spec.intent_obligations
        ),
    )
    return LoweredOpenAI(request=request, execution_plan=plan)
