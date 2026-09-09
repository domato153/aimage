from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class ProviderErrorEvidence:
    provider: str
    exception_type: str
    status_code: int | None
    request_id: str | None
    retryable: bool
    provider_code: str | None
    provider_body: Any | None


class OpenAIProviderError(RuntimeError):
    def __init__(self, message: str, evidence: ProviderErrorEvidence) -> None:
        super().__init__(message)
        self.evidence = evidence


def normalize_openai_error(exc: Exception) -> ProviderErrorEvidence:
    status_code = getattr(exc, "status_code", None)
    request_id = getattr(exc, "request_id", None)
    body = getattr(exc, "body", None)
    provider_code = getattr(exc, "code", None)
    exception_type = type(exc).__name__
    retryable_statuses = {408, 409, 429, 500, 502, 503, 504}
    retryable = status_code in retryable_statuses or exception_type in {
        "APIConnectionError",
        "APITimeoutError",
    }
    return ProviderErrorEvidence(
        provider="openai",
        exception_type=exception_type,
        status_code=status_code if isinstance(status_code, int) else None,
        request_id=str(request_id) if request_id else None,
        retryable=retryable,
        provider_code=str(provider_code) if provider_code else None,
        provider_body=body,
    )
