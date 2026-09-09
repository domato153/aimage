from __future__ import annotations

import base64
from types import SimpleNamespace

import pytest

from aimage.providers.openai.adapter import OpenAIAdapter
from aimage.providers.openai.errors import OpenAIProviderError
from aimage.providers.openai.lowering import OpenAIRenderRequest


class FakeRateLimit(Exception):
    status_code = 429
    request_id = "req-rate"
    code = "rate_limit"
    body = {"error": "limited"}


class FailingImages:
    async def generate(self, **_kwargs):
        raise FakeRateLimit("limited")


class FailingClient:
    def __init__(self) -> None:
        self.images = FailingImages()


@pytest.mark.asyncio
async def test_provider_error_preserves_normalized_retry_evidence() -> None:
    adapter = OpenAIAdapter(FailingClient())
    request = OpenAIRenderRequest(
        operation="generate",
        model="gpt-image-2.5-sunburst-2026-09-08",
        prompt="test",
        size="1024x1024",
    )
    with pytest.raises(OpenAIProviderError) as caught:
        await adapter.execute(request)
    evidence = caught.value.evidence
    assert evidence.status_code == 429
    assert evidence.request_id == "req-rate"
    assert evidence.retryable is True
    assert evidence.provider_code == "rate_limit"
