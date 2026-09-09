from __future__ import annotations

import base64
from datetime import datetime
from typing import Any

from aimage.contracts.resolution import ProviderCapabilityDescriptor
from aimage.engine.interfaces.provider import ProviderExecutionResult

from .capability import MODEL_SNAPSHOT, build_capability_descriptor
from .errors import OpenAIProviderError, normalize_openai_error
from .lowering import OpenAIRenderRequest


def build_openai_client(*, timeout_seconds: float = 120.0):
    """Construct the official SDK client with AIMAGE-owned retry/timeout policy."""
    from openai import AsyncOpenAI

    return AsyncOpenAI(max_retries=0, timeout=timeout_seconds)


class OpenAIAdapter:
    def __init__(self, client: Any | None = None, *, timeout_seconds: float = 120.0) -> None:
        self._client = client if client is not None else build_openai_client(timeout_seconds=timeout_seconds)

    def capability_descriptor(
        self,
        *,
        job_id: str,
        semantic_revision: int,
        observed_at: datetime | None = None,
    ) -> ProviderCapabilityDescriptor:
        return build_capability_descriptor(
            job_id=job_id,
            semantic_revision=semantic_revision,
            observed_at=observed_at,
        )

    async def execute(
        self,
        request: OpenAIRenderRequest,
        *,
        input_images: tuple[bytes, ...] = (),
    ) -> ProviderExecutionResult:
        try:
            if request.operation == "generate":
                response = await self._client.images.generate(
                    model=request.model,
                    prompt=request.prompt,
                    n=1,
                    output_format=request.output_format,
                    quality=request.quality,
                    size=request.size,
                )
            else:
                if not input_images:
                    evidence = normalize_openai_error(ValueError("missing edit image"))
                    raise OpenAIProviderError("edit execution requires input image bytes", evidence)
                files = tuple((f"input-{index}.png", data, "image/png") for index, data in enumerate(input_images))
                image_arg: object = files[0] if len(files) == 1 else files
                kwargs: dict[str, Any] = {
                    "image": image_arg,
                    "model": request.model,
                    "prompt": request.prompt,
                    "n": 1,
                    "output_format": request.output_format,
                    "quality": request.quality,
                    "size": request.size,
                }
                if request.input_fidelity is not None:
                    kwargs["input_fidelity"] = request.input_fidelity
                response = await self._client.images.edit(**kwargs)
        except OpenAIProviderError:
            raise
        except Exception as exc:
            evidence = normalize_openai_error(exc)
            suffix = f" request_id={evidence.request_id}" if evidence.request_id else ""
            raise OpenAIProviderError(f"OpenAI image execution failed.{suffix}", evidence) from exc

        data = getattr(response, "data", None)
        if not data or not getattr(data[0], "b64_json", None):
            evidence = normalize_openai_error(ValueError("missing b64 image"))
            raise OpenAIProviderError("OpenAI image response contained no base64 image", evidence)
        image_bytes = base64.b64decode(data[0].b64_json, validate=True)
        request_id = getattr(response, "_request_id", None)
        usage_value = getattr(response, "usage", None)
        if hasattr(usage_value, "model_dump"):
            usage = usage_value.model_dump(mode="json")
        elif isinstance(usage_value, dict):
            usage = usage_value
        else:
            usage = {}
        return ProviderExecutionResult(
            artifact_bytes=image_bytes,
            media_type=f"image/{request.output_format}",
            provider_request_id=request_id,
            actual_target_version=MODEL_SNAPSHOT,
            raw_provider_result_ref=f"openai-request:{request_id}" if request_id else None,
            usage=usage,
        )
