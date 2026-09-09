from __future__ import annotations

from datetime import datetime, timedelta, timezone

from aimage.contracts.common import EvidenceKind
from aimage.contracts.resolution import Capability, ProviderCapabilityDescriptor

MODEL_SNAPSHOT = "gpt-image-2.5-sunburst-2026-09-08"
TARGET_ID = f"openai:{MODEL_SNAPSHOT}"
EVIDENCE_URI = "https://developers.openai.com/api/docs/models/gpt-image-2.5-sunburst"


def build_capability_descriptor(*, job_id: str, semantic_revision: int, observed_at: datetime | None = None, evidence_kind: EvidenceKind = EvidenceKind.DECLARED, evidence_uri: str = EVIDENCE_URI) -> ProviderCapabilityDescriptor:
    observed_at = observed_at or datetime.now(timezone.utc)
    common_limits = {"max_width": 3840, "max_height": 2160, "dimension_divisible_by": 16, "min_aspect": 1 / 3, "max_aspect": 3.0}
    qualities = ("low", "medium", "high", "xhigh", "max", "auto")
    output_formats = ("png", "jpeg", "webp")
    return ProviderCapabilityDescriptor(
        job_id=job_id, semantic_revision=semantic_revision, target_id=TARGET_ID, target_kind="provider",
        adapter_id="aimage.providers.openai", adapter_version="0.1.0-dev0", target_version_or_model=MODEL_SNAPSHOT,
        observed_at=observed_at, valid_until=observed_at + timedelta(hours=1), evidence_kind=evidence_kind, evidence_uri=evidence_uri,
        capabilities=(
            Capability(namespace="aimage.image", name="generate", attributes={"input_kind": ("text",), "quality": qualities, "output_format": output_formats}, limits=common_limits),
            Capability(namespace="aimage.image", name="edit", attributes={"input_kind": ("image+text",), "input_fidelity": ("high", "low"), "quality": qualities, "output_format": output_formats, "max_input_images": 16}, limits=common_limits),
        ),
        known_limits=("declared documentation is insufficient for production until credentialed generate/edit reproduction", "resolutions above 2560x1440 are documented as experimental"),
    )
