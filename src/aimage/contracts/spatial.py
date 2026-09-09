from __future__ import annotations

from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field, model_validator

from .common import ContractModel, Strength, new_object_id


class ReferenceFrameKind(StrEnum):
    VIEWER_DEICTIC = "viewer_deictic"
    SUBJECT_INTRINSIC = "subject_intrinsic"
    SCENE_WORLD = "scene_world"
    SCREEN_IMAGE = "screen_image"


class SpatialEntity(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    entity_id: str
    semantic_role: str
    artifact_ref: str | None = None
    parent_entity_id: str | None = None


class ReferenceFrame(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    frame_id: str
    kind: ReferenceFrameKind
    origin_entity_id: str | None = None
    orientation_entity_id: str | None = None


DIRECTIONAL_PREDICATES = frozenset({"left_of", "right_of", "in_front_of", "behind", "above", "below"})


class SpatialRelation(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    relation_id: str = Field(default_factory=new_object_id)
    predicate: str
    subject_entity_id: str
    object_entity_id: str | None = None
    reference_frame_id: str | None = None
    strength: Strength = Strength.MANDATORY
    tolerance: float | None = None
    source_intent_id: str

    @model_validator(mode="after")
    def viewpoint_relation_has_frame(self) -> "SpatialRelation":
        if self.predicate in DIRECTIONAL_PREDICATES and not self.reference_frame_id:
            raise ValueError(f"directional predicate {self.predicate!r} requires a reference frame")
        return self


class SpatialProfile(ContractModel):
    contract_type: str = "spatial_profile"
    spatial_profile_id: str = Field(default_factory=new_object_id)
    entities: tuple[SpatialEntity, ...] = ()
    frames: tuple[ReferenceFrame, ...] = ()
    relations: tuple[SpatialRelation, ...] = ()

    @model_validator(mode="after")
    def relation_references_exist(self) -> "SpatialProfile":
        entity_ids = {entity.entity_id for entity in self.entities}
        frame_ids = {frame.frame_id for frame in self.frames}
        for relation in self.relations:
            if relation.subject_entity_id not in entity_ids:
                raise ValueError(f"unknown spatial subject {relation.subject_entity_id!r}")
            if relation.object_entity_id and relation.object_entity_id not in entity_ids:
                raise ValueError(f"unknown spatial object {relation.object_entity_id!r}")
            if relation.reference_frame_id and relation.reference_frame_id not in frame_ids:
                raise ValueError(f"unknown reference frame {relation.reference_frame_id!r}")
        return self
