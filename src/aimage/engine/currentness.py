from __future__ import annotations


class StaleStateError(RuntimeError):
    pass


def assert_current(
    *,
    expected_semantic_revision: int,
    current_semantic_revision: int,
    expected_intent_digest: str | None = None,
    current_intent_digest: str | None = None,
) -> None:
    if expected_semantic_revision != current_semantic_revision:
        raise StaleStateError(
            f"stale semantic revision: expected {expected_semantic_revision}, current {current_semantic_revision}"
        )
    if expected_intent_digest is not None and expected_intent_digest != current_intent_digest:
        raise StaleStateError("semantic revision matches but intent digest changed")
