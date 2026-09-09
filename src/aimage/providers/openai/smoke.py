from __future__ import annotations
import hashlib, json
from datetime import datetime, timezone
from pydantic import BaseModel, ConfigDict
from aimage.contracts.common import EvidenceKind
from .adapter import OpenAIAdapter
from .capability import MODEL_SNAPSHOT
from .lowering import OpenAIRenderRequest
class OpenAICapabilitySmokeEvidence(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)
    model_snapshot: str; observed_at: datetime; generate_request_id: str | None; edit_request_id: str | None; operations: tuple[str, ...] = ("generate", "edit"); evidence_digest: str
    @property
    def evidence_uri(self) -> str: return f"aimage-openai-smoke:sha256:{self.evidence_digest}"
def _digest(payload: dict[str, object]) -> str: return hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(",", ":"), default=str).encode()).hexdigest()
async def reproduce_openai_image_capability(client=None) -> OpenAICapabilitySmokeEvidence:
    adapter = OpenAIAdapter(client); generated = await adapter.execute(OpenAIRenderRequest(operation="generate", model=MODEL_SNAPSHOT, prompt="A simple gray circle centered on a plain white background.", size="1024x1024", quality="low", output_format="png")); edited = await adapter.execute(OpenAIRenderRequest(operation="edit", model=MODEL_SNAPSHOT, prompt="Keep the image structure and change the circle to blue.", size="1024x1024", quality="low", output_format="png", input_fidelity="high"), input_images=(generated.artifact_bytes,)); observed_at = datetime.now(timezone.utc); payload = {"model_snapshot": MODEL_SNAPSHOT, "observed_at": observed_at.isoformat(), "generate_request_id": generated.provider_request_id, "edit_request_id": edited.provider_request_id, "operations": ["generate", "edit"]}; return OpenAICapabilitySmokeEvidence(**payload, evidence_digest=_digest(payload))
def adapter_from_reproduced_smoke(evidence: OpenAICapabilitySmokeEvidence, client=None) -> OpenAIAdapter:
    if evidence.model_snapshot != MODEL_SNAPSHOT or set(evidence.operations) != {"generate", "edit"}: raise ValueError("smoke evidence does not cover selected OpenAI target")
    return OpenAIAdapter(client, capability_evidence_kind=EvidenceKind.REPRODUCED, capability_evidence_uri=evidence.evidence_uri, capability_evidence_observed_at=evidence.observed_at)
