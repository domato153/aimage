from __future__ import annotations
from datetime import datetime, timedelta, timezone
from aimage.contracts.common import EvidenceKind
from aimage.engine.resolve import descriptor_is_fresh
from aimage.providers.openai.adapter import OpenAIAdapter

class FakeClient: pass

def test_reproduced_evidence_timestamp_does_not_refresh_on_descriptor_read() -> None:
    observed = datetime.now(timezone.utc) - timedelta(minutes=30); adapter = OpenAIAdapter(FakeClient(), capability_evidence_kind=EvidenceKind.REPRODUCED, capability_evidence_uri="fixture:smoke", capability_evidence_observed_at=observed); first = adapter.capability_descriptor(job_id="job", semantic_revision=1); second = adapter.capability_descriptor(job_id="job", semantic_revision=1); assert first.observed_at == observed == second.observed_at; assert first.valid_until == second.valid_until; assert descriptor_is_fresh(first, now=observed + timedelta(minutes=59)); assert not descriptor_is_fresh(first, now=observed + timedelta(hours=1, seconds=1))
