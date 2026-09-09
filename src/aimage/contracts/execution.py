from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict, Field, model_validator

from .common import ContractModel, DerivedContractModel, new_object_id


class ExecutionStep(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    step_id: str = Field(default_factory=new_object_id)
    target_descriptor_ref: str
    operation: str
    input_refs: tuple[str, ...] = ()
    provider_or_tool_payload_ref: str
    output_role: str
    depends_on: tuple[str, ...] = ()


class LoweringTraceEntry(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    source_semantic_path: str
    requirement_id: str
    target_step_id: str
    representation: str
    fidelity: str
    notes: str | None = None


class ExecutionPlan(DerivedContractModel):
    contract_type: str = "execution_plan"
    execution_plan_id: str = Field(default_factory=new_object_id)
    render_spec_ref: str
    resolution_ref: str
    steps: tuple[ExecutionStep, ...]
    lowering_trace: tuple[LoweringTraceEntry, ...] = ()

    @model_validator(mode="after")
    def acyclic_and_closed(self) -> "ExecutionPlan":
        step_ids = {step.step_id for step in self.steps}
        deps = {step.step_id: set(step.depends_on) for step in self.steps}
        if any(not values <= step_ids for values in deps.values()):
            raise ValueError("execution plan contains unknown dependency")
        visiting: set[str] = set()
        visited: set[str] = set()

        def visit(step_id: str) -> None:
            if step_id in visiting:
                raise ValueError("execution plan must be acyclic")
            if step_id in visited:
                return
            visiting.add(step_id)
            for dep in deps[step_id]:
                visit(dep)
            visiting.remove(step_id)
            visited.add(step_id)

        for step_id in step_ids:
            visit(step_id)
        return self


class ArtifactRecord(ContractModel):
    contract_type: str = "artifact_record"
    artifact_id: str
    content_digest: str
    media_metadata: dict[str, Any] = {}
    derived_from_artifact_refs: tuple[str, ...] = ()
    producing_run_ref: str


class RunRecord(ContractModel):
    contract_type: str = "run_record"
    run_id: str = Field(default_factory=new_object_id)
    execution_plan_ref: str
    actual_target_versions: tuple[str, ...] = ()
    output_artifact_refs: tuple[str, ...] = ()
    raw_provider_result_ref: str | None = None
    usage_cost_latency: dict[str, Any] = {}
    provider_request_id: str | None = None
