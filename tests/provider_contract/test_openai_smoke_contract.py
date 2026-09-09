from __future__ import annotations

import base64
from types import SimpleNamespace
import pytest
from aimage.contracts.common import EvidenceKind
from aimage.providers.openai.smoke import adapter_from_reproduced_smoke, reproduce_openai_image_capability

class FakeImages:
    async def generate(self, **_kwargs): return SimpleNamespace(data=[SimpleNamespace(b64_json=base64.b64encode(b"generated").decode())], _request_id="gen", usage={})
    async def edit(self, **_kwargs): return SimpleNamespace(data=[SimpleNamespace(b64_json=base64.b64encode(b"edited").decode())], _request_id="edit", usage={})
class FakeClient:
    def __init__(self): self.images = FakeImages()

@pytest.mark.asyncio
async def test_smoke_evidence_is_required_to_upgrade_descriptor_to_reproduced() -> None:
    evidence = await reproduce_openai_image_capability(FakeClient()); adapter = adapter_from_reproduced_smoke(evidence, FakeClient()); descriptor = adapter.capability_descriptor(job_id="job", semantic_revision=1); assert descriptor.evidence_kind is EvidenceKind.REPRODUCED; assert descriptor.evidence_uri == evidence.evidence_uri; assert evidence.generate_request_id == "gen" and evidence.edit_request_id == "edit"
