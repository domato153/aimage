from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from aimage.contracts.execution import ArtifactRecord, RunRecord
from aimage.contracts.resolution import ResolutionStatus
from aimage.contracts.spatial import SpatialProfile
from aimage.contracts.validation import ValidationReport, ValidationResult
from aimage.contracts.visual_intent import DecisionRecord, MutationFrame, VisualIntentState
from aimage.engine.capabilities import assert_resolution_capability_current
from aimage.engine.compile import compile_render_spec, visual_intent_digest
from aimage.engine.interfaces.artifact_store import ArtifactStore
from aimage.engine.interfaces.metadata_repository import MetadataRepository
from aimage.engine.lifecycle import approve_baseline as apply_baseline_approval
from aimage.engine.requirements import derive_requirements
from aimage.engine.resolve import resolve_requirements
from aimage.engine.validation_service import aggregate_validation, require_final_preservation_evidence
from aimage.providers.openai.adapter import OpenAIAdapter
from aimage.providers.openai.errors import OpenAIProviderError
from aimage.providers.openai.lowering import lower_openai


class UnsatisfiedPlanError(RuntimeError):
    pass


@dataclass(frozen=True)
class VerticalSliceResult:
    artifact: ArtifactRecord
    run: RunRecord
    validation: ValidationReport


class ImageEngine:
    def __init__(
        self,
        *,
        artifact_store: ArtifactStore,
        metadata_repository: MetadataRepository,
        openai_adapter: OpenAIAdapter,
    ) -> None:
        self.artifact_store = artifact_store
        self.metadata = metadata_repository
        self.openai = openai_adapter

    def approve_composition(
        self,
        intent: VisualIntentState,
        decision: DecisionRecord,
        *,
        value_snapshot_ref: str,
    ) -> VisualIntentState:
        """Persist a scoped revision-bound baseline approval and atomically advance currentness."""
        old_digest = visual_intent_digest(intent)
        self.metadata.claim_or_assert_current(intent.job_id, intent.semantic_revision, old_digest)
        approved = apply_baseline_approval(intent, decision, value_snapshot_ref=value_snapshot_ref)
        if approved is intent:
            return intent
        new_digest = visual_intent_digest(approved)
        self.metadata.save_object(approved)
        self.metadata.advance_current(
            intent.job_id,
            expected_revision=intent.semantic_revision,
            expected_digest=old_digest,
            new_revision=approved.semantic_revision,
            new_digest=new_digest,
        )
        return approved

    async def render(
        self,
        intent: VisualIntentState,
        *,
        spatial_profile: SpatialProfile | None = None,
        operation: Literal["generate", "edit"] = "generate",
        source_artifacts: tuple[tuple[str, bytes], ...] = (),
        mutation_frame: MutationFrame | None = None,
        validation_results: tuple[ValidationResult, ...] = (),
        mandatory_rule_ids: frozenset[str] = frozenset(),
        profile_versions: tuple[str, ...] = (),
        output_contract: dict[str, object] | None = None,
    ) -> VerticalSliceResult:
        render_spec = compile_render_spec(intent, spatial_profile, output_contract=output_contract)
        current_digest = visual_intent_digest(intent)
        self.metadata.save_object(intent)
        if spatial_profile:
            self.metadata.save_object(spatial_profile)
        self.metadata.save_object(render_spec)
        self.metadata.claim_or_assert_current(intent.job_id, intent.semantic_revision, current_digest)

        requirement_set = derive_requirements(render_spec, operation=operation)
        self.metadata.save_object(requirement_set)
        descriptor = self.openai.capability_descriptor(
            job_id=intent.job_id,
            semantic_revision=intent.semantic_revision,
        )
        self.metadata.save_object(descriptor)
        resolution = resolve_requirements(requirement_set, (descriptor,))
        self.metadata.save_object(resolution)
        if resolution.status is not ResolutionStatus.RESOLVED:
            raise UnsatisfiedPlanError(
                f"provider strategy is {resolution.status.value}: {resolution.unsatisfied_mandatory}"
            )

        source_refs = tuple(reference for reference, _bytes in source_artifacts)
        lowered = lower_openai(
            render_spec,
            requirement_set,
            resolution,
            descriptor,
            operation=operation,
            source_artifact_refs=source_refs,
            mutation_frame=mutation_frame,
        )
        self.metadata.save_object(lowered.execution_plan)

        current_descriptor = self.openai.capability_descriptor(
            job_id=intent.job_id,
            semantic_revision=intent.semantic_revision,
        )
        assert_resolution_capability_current(resolution, (descriptor,), (current_descriptor,))

        try:
            provider_result = await self.openai.execute(
                lowered.request,
                input_images=tuple(data for _reference, data in source_artifacts),
            )
        except OpenAIProviderError as exc:
            evidence = exc.evidence
            failed_run = RunRecord(
                job_id=intent.job_id,
                semantic_revision=intent.semantic_revision,
                created_from=(lowered.execution_plan.object_id,),
                execution_plan_ref=lowered.execution_plan.execution_plan_id,
                actual_target_versions=(descriptor.target_version_or_model,),
                output_artifact_refs=(),
                raw_provider_result_ref=(
                    f"openai-request:{evidence.request_id}" if evidence.request_id else None
                ),
                usage_cost_latency={
                    "outcome": "provider_error",
                    "exception_type": evidence.exception_type,
                    "status_code": evidence.status_code,
                    "retryable": evidence.retryable,
                    "provider_code": evidence.provider_code,
                },
                provider_request_id=evidence.request_id,
            )
            self.metadata.save_run(failed_run)
            raise

        stored = self.artifact_store.put(provider_result.artifact_bytes, media_type=provider_result.media_type)
        run = RunRecord(
            job_id=intent.job_id,
            semantic_revision=intent.semantic_revision,
            created_from=(lowered.execution_plan.object_id,),
            execution_plan_ref=lowered.execution_plan.execution_plan_id,
            actual_target_versions=(provider_result.actual_target_version,),
            output_artifact_refs=(stored.artifact_id,),
            raw_provider_result_ref=provider_result.raw_provider_result_ref,
            usage_cost_latency=dict(provider_result.usage or {}),
            provider_request_id=provider_result.provider_request_id,
        )
        artifact = ArtifactRecord(
            artifact_id=stored.artifact_id,
            job_id=intent.job_id,
            semantic_revision=intent.semantic_revision,
            created_from=source_refs,
            content_digest=stored.content_digest,
            media_metadata={"media_type": stored.media_type, "size_bytes": stored.size_bytes},
            derived_from_artifact_refs=source_refs,
            producing_run_ref=run.run_id,
        )
        # Evidence is durable even if the semantic revision changed while the provider was in flight.
        self.metadata.save_run(run)
        self.metadata.save_artifact(artifact)
        # But stale evidence can never proceed into current validation/acceptance flow.
        self.metadata.assert_current(intent.job_id, intent.semantic_revision, current_digest)

        preserve_paths = mutation_frame.preserve_paths if mutation_frame else ()
        validation_results, mandatory_rule_ids = require_final_preservation_evidence(
            render_spec,
            validation_results,
            mandatory_rule_ids,
            extra_preserve_paths=preserve_paths,
        )
        overall = aggregate_validation(validation_results, mandatory_rule_ids)
        report = ValidationReport(
            job_id=intent.job_id,
            semantic_revision=intent.semantic_revision,
            created_from=(artifact.object_id, lowered.execution_plan.object_id),
            artifact_ref=artifact.artifact_id,
            render_spec_ref=render_spec.render_spec_id,
            execution_plan_ref=lowered.execution_plan.execution_plan_id,
            profile_versions=profile_versions,
            overall_outcome=overall,
            results=validation_results,
        )
        self.metadata.save_object(report)
        # Deliberately no ArtifactDispositionRecord is auto-created here; acceptance is a separate revision-bound decision.
        return VerticalSliceResult(artifact=artifact, run=run, validation=report)
