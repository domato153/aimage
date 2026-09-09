from __future__ import annotations

from sqlalchemy import select

from aimage.contracts.common import EvidenceKind
from aimage.contracts.spatial import SpatialProfile
from aimage.contracts.validation import ValidationOutcome, ValidationReport
from aimage.contracts.visual_intent import (
    ArtifactDisposition,
    ArtifactDispositionRecord,
    BaselineRecord,
    DecisionKind,
    DecisionRecord,
    VisualIntentState,
)
from aimage.engine.compile import compile_render_spec
from aimage.persistence.sqlite.repository import SQLiteMetadataRepository
from aimage.persistence.sqlite.schema import (
    artifact_dispositions,
    baselines,
    capability_descriptors,
    decisions,
    derived_documents,
    semantic_documents,
    semantic_support_documents,
    validation_reports,
)
from aimage.persistence.sqlite.transactions import create_sqlite_engine
from aimage.providers.openai.adapter import OpenAIAdapter


class DummyClient:
    class Images:
        pass

    images = Images()


def test_contract_families_route_to_distinct_persistence_boundaries(tmp_path) -> None:
    engine = create_sqlite_engine(tmp_path / "routing.db")
    repository = SQLiteMetadataRepository(engine, create_schema=True)
    intent = VisualIntentState(job_id="job", semantic_revision=1)
    spatial = SpatialProfile(job_id="job", semantic_revision=1)
    render_spec = compile_render_spec(intent, spatial)
    descriptor = OpenAIAdapter(
        DummyClient(),
        capability_evidence_kind=EvidenceKind.REPRODUCED,
        capability_evidence_uri="fixture:reproduced",
    ).capability_descriptor(job_id="job", semantic_revision=1)
    report = ValidationReport(
        job_id="job",
        semantic_revision=1,
        artifact_ref="artifact",
        render_spec_ref=render_spec.render_spec_id,
        execution_plan_ref="plan",
        overall_outcome=ValidationOutcome.INDETERMINATE,
    )
    decision = DecisionRecord(
        decision_id="decision",
        kind=DecisionKind.APPROVE,
        base_semantic_revision=1,
        actor_authority_id="user",
        subject_ref="candidate",
        scope_paths=("composition",),
    )
    baseline = BaselineRecord(
        baseline_id="baseline",
        approved_at_revision=2,
        approved_paths=("composition",),
        approved_dimensions=("composition",),
        value_snapshot_ref="snapshot",
        approval_decision_id=decision.decision_id,
    )
    disposition = ArtifactDispositionRecord(
        artifact_ref="artifact",
        semantic_revision=1,
        status=ArtifactDisposition.REJECTED,
        basis_decision_id="reject-decision",
    )

    repository.save_object(intent)
    repository.save_object(spatial)
    repository.save_object(render_spec)
    repository.save_object(descriptor)
    repository.save_object(report)
    repository.save_decision("job", decision)
    repository.save_baseline("job", baseline)
    repository.save_artifact_disposition("job", disposition)

    with engine.connect() as connection:
        assert len(connection.execute(select(semantic_documents)).mappings().all()) == 1
        assert len(connection.execute(select(semantic_support_documents)).mappings().all()) == 1
        assert len(connection.execute(select(derived_documents)).mappings().all()) == 1
        assert len(connection.execute(select(capability_descriptors)).mappings().all()) == 1
        assert len(connection.execute(select(validation_reports)).mappings().all()) == 1
        assert len(connection.execute(select(decisions)).mappings().all()) == 1
        assert len(connection.execute(select(baselines)).mappings().all()) == 1
        assert len(connection.execute(select(artifact_dispositions)).mappings().all()) == 1
