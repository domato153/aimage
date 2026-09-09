from __future__ import annotations
import base64, binascii
from datetime import datetime, timezone
from typing import Any
from aimage.contracts.common import EvidenceKind
from aimage.contracts.resolution import ProviderCapabilityDescriptor
from aimage.engine.interfaces.provider import ProviderExecutionResult
from .capability import EVIDENCE_URI, MODEL_SNAPSHOT, build_capability_descriptor
from .errors import OpenAIProviderError, normalize_openai_error
from .lowering import OpenAIRenderRequest

def build_openai_client(*, timeout_seconds: float = 120.0):
    from openai import AsyncOpenAI
    return AsyncOpenAI(max_retries=0, timeout=timeout_seconds)
class OpenAIAdapter:
    def __init__(self, client: Any | None = None, *, timeout_seconds: float = 120.0, capability_evidence_kind: EvidenceKind = EvidenceKind.DECLARED, capability_evidence_uri: str = EVIDENCE_URI, capability_evidence_observed_at: datetime | None = None) -> None:
        self._client = client if client is not None else build_openai_client(timeout_seconds=timeout_seconds); self._capability_evidence_kind = capability_evidence_kind; self._capability_evidence_uri = capability_evidence_uri; self._capability_evidence_observed_at = capability_evidence_observed_at or datetime.now(timezone.utc)
    def capability_descriptor(self, *, job_id: str, semantic_revision: int) -> ProviderCapabilityDescriptor:
        return build_capability_descriptor(job_id=job_id, semantic_revision=semantic_revision, observed_at=self._capability_evidence_observed_at, evidence_kind=self._capability_evidence_kind, evidence_uri=self._capability_evidence_uri)
    async def execute(self, request: OpenAIRenderRequest, *, input_images: tuple[bytes, ...] = ()) -> ProviderExecutionResult:
        if request.model != MODEL_SNAPSHOT:
            evidence = normalize_openai_error(ValueError("request model does not match adapter target")); raise OpenAIProviderError("OpenAI request target differs from adapter capability target", evidence)
        try:
            if request.operation == "generate": response = await self._client.images.generate(model=request.model, prompt=request.prompt, n=1, output_format=request.output_format, quality=request.quality, size=request.size)
            else:
                if not input_images: raise OpenAIProviderError("edit execution requires input image bytes", normalize_openai_error(ValueError("missing edit image")))
                files = tuple((f"input-{index}.png", data, "image/png") for index, data in enumerate(input_images)); image_arg: object = files[0] if len(files) == 1 else files; kwargs: dict[str, Any] = {"image": image_arg, "model": request.model, "prompt": request.prompt, "n": 1, "output_format": request.output_format, "quality": request.quality, "size": request.size}
                if request.input_fidelity is not None: kwargs["input_fidelity"] = request.input_fidelity
                response = await self._client.images.edit(**kwargs)
        except OpenAIProviderError: raise
        except Exception as exc:
            evidence = normalize_openai_error(exc); suffix = f" request_id={evidence.request_id}" if evidence.request_id else ""; raise OpenAIProviderError(f"OpenAI image execution failed.{suffix}", evidence) from exc
        data = getattr(response, "data", None)
        if not data or not getattr(data[0], "b64_json", None): raise OpenAIProviderError("OpenAI image response contained no base64 image", normalize_openai_error(ValueError("missing b64 image")))
        try: image_bytes = base64.b64decode(data[0].b64_json, validate=True)
        except (binascii.Error, ValueError) as exc: raise OpenAIProviderError("OpenAI image response contained invalid base64 image", normalize_openai_error(exc)) from exc
        request_id = getattr(response, "_request_id", None); usage_value = getattr(response, "usage", None); usage = usage_value.model_dump(mode="json") if hasattr(usage_value, "model_dump") else usage_value if isinstance(usage_value, dict) else {}
        return ProviderExecutionResult(artifact_bytes=image_bytes, media_type=f"image/{request.output_format}", provider_request_id=request_id, actual_target_version=MODEL_SNAPSHOT, raw_provider_result_ref=f"openai-request:{request_id}" if request_id else None, usage=usage)
