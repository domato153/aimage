from __future__ import annotations

import base64
import json
import os
import tempfile
from pathlib import Path

from openai import OpenAI

MODEL = "gpt-image-2.5-sunburst-2026-09-08"


def _image_bytes(parsed: object) -> bytes:
    data = getattr(parsed, "data", None)
    if not data:
        raise RuntimeError("image response contained no data")
    encoded = getattr(data[0], "b64_json", None)
    if not encoded:
        raise RuntimeError("GPT Image response did not contain base64 image bytes")
    return base64.b64decode(encoded)


def _request_id(raw_response: object) -> str | None:
    headers = getattr(raw_response, "headers", None)
    return headers.get("x-request-id") if headers is not None else None


def main() -> int:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("AIMAGE_OPENAI_SMOKE_SKIPPED: OPENAI_API_KEY is not configured")
        return 0

    client = OpenAI(api_key=api_key, max_retries=0, timeout=120.0)
    generation_raw = client.images.with_raw_response.generate(
        model=MODEL,
        prompt="A plain black circle centered on a clean white background. Minimal test image.",
        size="1024x1024",
        quality="low",
        n=1,
    )
    generation = generation_raw.parse()
    generated = _image_bytes(generation)

    with tempfile.TemporaryDirectory() as temp_dir:
        source_path = Path(temp_dir) / "source.png"
        source_path.write_bytes(generated)
        with source_path.open("rb") as source:
            edit_raw = client.images.with_raw_response.edit(
                model=MODEL,
                image=source,
                prompt="Preserve the image and add one small gray square in the lower-right corner.",
                size="1024x1024",
                quality="low",
                n=1,
                input_fidelity="high",
            )
        edited = _image_bytes(edit_raw.parse())

    evidence = {
        "provider": "openai",
        "requested_model_snapshot": MODEL,
        "generation": {
            "request_id": _request_id(generation_raw),
            "image_bytes": len(generated),
        },
        "edit": {
            "request_id": _request_id(edit_raw),
            "image_bytes": len(edited),
        },
        "hidden_sdk_retries": 0,
        "timeout_seconds": 120.0,
    }
    if not evidence["generation"]["request_id"] or not evidence["edit"]["request_id"]:
        raise RuntimeError("provider smoke succeeded but x-request-id evidence was missing")

    print("AIMAGE_OPENAI_SMOKE_EVIDENCE_BEGIN")
    print(json.dumps(evidence, indent=2, sort_keys=True))
    print("AIMAGE_OPENAI_SMOKE_EVIDENCE_END")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
