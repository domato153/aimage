# AIMAGE Provider-Neutral Semantic Contracts

Status: planning/design contract specification for the four semantic families defined by `plans/SEMANTIC_FUSION_PLAN.md`. This file defines minimum semantic objects, ownership, invariants and failure behavior. It does **not** authorize implementation, package selection, provider integration, source import, or runtime dependency changes.

## 1. Design rule

AIMAGE is an intent-driven image-production system, not a provider request archive.

The semantic contract must preserve the user's desired outcome, authority, approvals and constraints independently of any one provider. Mature generic mechanics remain borrowed/adapted from the external-method plan; AIMAGE owns only the image-production vocabulary and mappings that those generic systems cannot provide.

The contract follows four families:

- **A — Visual Intent & Authority**: canonical desired state, authority, approval/baseline and controlled change;
- **B — Requirement, Capability & Lowering**: compile intent, resolve a legal capability strategy and lower to provider/tool execution;
- **C — Spatial & Composition Profile**: provider-neutral spatial/visual relations with explicit reference frames;
- **D — Validation & Domain Profile**: separate conformance rules/decisions from execution and return structured evidence.

The families share one semantic revision identity and do not create four independent frameworks.

## 2. External mechanics retained without runtime coupling

The contracts intentionally reuse these generic mechanics without requiring their runtimes:

- RFC 9315 intent/SSoT/fulfillment/assurance;
- NIST baseline/change-control;
- JML-style frame conditions: explicitly listed mutable state, otherwise preserved;
- OSGi Requirement-Capability namespaces and consistent resolution of mandatory requirements;
- LLVM/MLIR-style immutable IR and target lowering/legality;
- QSR/QSTR and OGC/RCC8 qualitative spatial relations and reference frames;
- SHACL-style separate validation rules/data and structured reports;
- OPA-style decision/enforcement separation;
- JSON Schema-style versioned validation/evolution;
- existing AIMAGE PROV/OpenAssetIO-inspired artifact identity/lineage adaptation.

AIMAGE does not adopt OSGi, RDF, SHACL, OPA, JML, LLVM/MLIR, GeoSPARQL or an intent-networking runtime merely to reuse these semantics.

## 3. Common identity envelope

Every durable semantic or derived contract object has enough identity to prevent stale cross-linking.

Minimum common fields:

```text
contract_type
schema_version
object_id
job_id
semantic_revision              # exact AIMAGE desired-state revision this object belongs to
created_from[]                 # object/revision identities, not mutable aliases
```

Derived execution objects additionally carry:

```text
source_semantic_revision
source_intent_digest           # digest/identity of normalized semantic input used for compilation
```

Rules:

1. `schema_version` identifies representation/evolution rules; `semantic_revision` identifies the user's desired-state revision. They are different concepts.
2. Any change to canonical intent/authority that alters semantic meaning creates a new `semantic_revision`.
3. `RenderSpec`, `RequirementSet`, `ResolutionResult`, `ExecutionPlan`, `MutationFrame` and `ValidationReport` are immutable records for their source revision/attempt.
4. A new semantic revision invalidates older derived execution objects for future execution unless an explicit compatibility check proves they remain valid. Historical evidence stays immutable.
5. Provider-native identifiers never substitute for `job_id`, `semantic_revision`, artifact identity or AIMAGE object identity.

## 4. Family A — Visual Intent & Authority

### 4.1 Owner and non-goals

Family A owns the canonical semantic desired state and controlled changes to it.

It does **not** own:

- provider request construction;
- provider capability detection;
- image rendering/editing;
- domain-rule execution;
- generic persistence/database behavior;
- Continuity/Handoff transfer mechanics.

Continuity may transport Family A identities/state, but does not define image semantics.

### 4.2 `VisualIntentState`

`VisualIntentState` is the one semantic Single Source of Truth for a job revision.

Minimum shape:

```text
VisualIntentState
  job_id
  semantic_revision
  intent_items[]
  authority_bindings[]
  reference_bindings[]
  baselines[]
  artifact_dispositions[]
  spatial_profile_ref
  domain_profile_refs[]
```

#### `IntentItem`

```text
intent_id
semantic_path
visual_dimension
value_or_constraint
strength                    # mandatory | preferred | advisory
source_authority_id
status                      # active | superseded
```

`strength` means desired semantic importance, not provider capability support. A mandatory intent that cannot be legally lowered causes explicit unsatisfied/fallback behavior; it is never silently softened.

Initial visual dimensions are an extensible image-domain vocabulary, not an exhaustive ontology:

```text
identity
style
composition
camera
blocking
pose
expression
lighting
text_layout
content
finishing
```

Domain profiles may define namespaced additional dimensions without redefining core ones.

#### `AuthorityBinding`

```text
authority_id
source_ref
source_kind                  # explicit_user | approved_baseline | reference | profile | domain | inferred
scope_paths[]
dimensions[]
precedence_key
valid_from_revision
```

Authority rules:

1. explicit current user decisions outrank inferred/provider-derived values within the same semantic scope;
2. an approved baseline remains binding until explicitly reopened;
3. provider capability limits do not rewrite intent — they make an execution strategy unsatisfied or require explicit fallback/user choice;
4. domain constraints that conflict with explicit user intent produce `user_decision_conflict`; they do not silently rewrite the user's SSoT;
5. conflicts that remain unresolved after configured precedence rules are explicit semantic conflicts, never last-write-wins accidents.

#### `ReferenceBinding`

```text
binding_id
artifact_ref
role                         # identity_reference | style_reference | composition_reference | blocking | etc.
scope_paths[]
dimensions[]
authority_id
```

Replacing an identity reference must not silently replace style/composition bindings because roles and dimension scopes are separate.

### 4.3 Approval, rejection and controlled change

User/domain decisions are revision-bound records, not mutable booleans.

#### `DecisionRecord`

```text
decision_id                  # also idempotency identity
kind                         # approve | reject | reopen | supersede
base_semantic_revision
actor_authority_id
subject_ref                  # artifact, intent path, baseline or candidate
scope_paths[]
dimensions[]
reason_ref?                  # optional explanation/evidence
resulting_semantic_revision? # present when decision changes canonical meaning
```

Rules:

1. applying the same `decision_id` twice is idempotent;
2. a decision whose `base_semantic_revision` no longer matches the live semantic state is `STALE_DECISION` unless an explicit reconciliation operation revalidates it;
3. an approval over selected paths/dimensions creates or updates a `BaselineRecord` for those paths only;
4. changing an approved baseline requires an explicit `reopen` or superseding user decision;
5. rejection never modifies the desired intent merely because an artifact failed; it changes artifact disposition/evidence.

#### `BaselineRecord`

```text
baseline_id
approved_at_revision
approved_paths[]
approved_dimensions[]
value_snapshot_ref
approval_decision_id
status                       # active | reopened | superseded
```

The baseline is the reviewed/accepted semantic state for the approved scope.

#### `ArtifactDispositionRecord`

```text
artifact_ref
semantic_revision
status                       # candidate | accepted | rejected | superseded
basis_decision_id?
supersedes_artifact_ref?
```

There may be many candidates, but only explicit acceptance can make a candidate the accepted artifact for the relevant scope. Resume/retry logic must not infer acceptance from recency or provider conversation state.

### 4.4 `MutationFrame`

`MutationFrame` is a derived frame condition for a repair/change attempt. It is **not** a new semantic authority.

```text
MutationFrame
  frame_id
  semantic_revision
  reason                     # repair | explicit_change | rerender
  mutable_paths[]
  preserve_paths[]
  source_validation_results[]
  authorizing_decision_id?
```

Rules:

1. `mutable_paths ∩ preserve_paths = ∅`;
2. for repair, unspecified approved paths default to preserved rather than mutable;
3. execution that cannot honor a mandatory preserve obligation is not legal lowering;
4. successful repair does not create a new semantic revision unless desired intent changed; it creates a new artifact/run under the same semantic revision;
5. user-requested semantic change does create a new semantic revision and invalidates stale derived plans.

This is the AIMAGE adaptation of a frame-condition principle: declare what may change and treat everything outside that authorized frame as preserved for the attempt.

## 5. Family C — Spatial & Composition Semantics Profile

Family C is presented before Family B because its semantic relations become part of the compiled RenderSpec.

### 5.1 Owner and non-goals

Family C owns the compact image-production spatial vocabulary required to preserve composition meaning across natural language, blocking, providers and review.

It does not attempt a universal geometry language, CAD kernel, scene graph runtime or general spatial-reasoning engine.

### 5.2 `SpatialProfile`

```text
SpatialProfile
  spatial_profile_id
  schema_version
  semantic_revision
  entities[]
  frames[]
  relations[]
```

#### `SpatialEntity`

```text
entity_id
semantic_role
artifact_ref?
parent_entity_id?
```

Examples: `viewer`, `subject_girl`, `desk`, `paper`, `camera`, `speech_text_region`.

#### `ReferenceFrame`

```text
frame_id
kind                         # viewer_deictic | subject_intrinsic | scene_world | screen_image
origin_entity_id?
orientation_entity_id?
```

`viewer_deictic` means relative to the observer/viewer; `subject_intrinsic` means relative to the object's intrinsic facing/orientation; `screen_image` means literal 2D output coordinates. They must never be silently conflated.

#### `SpatialRelation`

```text
relation_id
predicate
subject_entity_id
object_entity_id?
reference_frame_id?
strength                     # mandatory | preferred | advisory
tolerance?
source_intent_id
```

Initial generic/adapted relation classes:

```text
# topology
inside | contains | overlaps | disjoint | touches

# direction/orientation
left_of | right_of | in_front_of | behind | above | below

# distance
near | medium_distance | far

# alignment/order
same_row | same_column | aligned_with | between
```

Initial AIMAGE image-specific profile terms:

```text
gaze_at
foreground_of
background_of
screen_region
attention_precedes
camera_relation
```

Rules:

1. viewpoint-sensitive directional predicates require an explicit or unambiguously inherited reference frame;
2. `screen_image` and `viewer_deictic` are not aliases;
3. qualitative constraints may carry optional numeric/tolerance bounds when needed;
4. a blocking artifact is a derived structural representation of these semantics, not their canonical owner;
5. provider lowering may use prompt text, masks, pose/depth/control maps, scene graphs or image references, but the relation semantics remain provider-neutral.

Example:

```text
right_of(subject_girl, viewer, frame=viewer_deictic)
same_row(subject_girl, viewer, frame=scene_world)
medium_distance(subject_girl, viewer)
```

This means "to my right, on the same row, with some distance" and cannot legally become "front-right" merely because a provider prompt interpreted `right` as screen placement.

## 6. Family D — Validation & Domain Profile

### 6.1 Owner and non-goals

Family D owns validation rule/profile meaning and structured decisions/evidence.

It does not:

- mutate the artifact while evaluating it;
- change canonical intent;
- execute provider repair;
- silently accept unevaluable mandatory rules.

### 6.2 `DomainProfile`

```text
DomainProfile
  profile_id
  namespace
  profile_version
  domain
  rules[]
```

#### `ValidationRule`

```text
rule_id
semantic_path_or_dimension
requirement_level            # mandatory | preferred | advisory
severity                     # blocker | error | warning | info
evaluator_class              # deterministic | model_assisted | human | provider_feedback
meaning
required_evidence[]
```

The profile supplies actual image/domain correctness meaning, such as:

- character identity match;
- approved composition preserved;
- exact text correctness;
- no forbidden artifact;
- product/logo correctness;
- storyboard continuity;
- domain-specific threshold/severity rules.

A domain profile is a feature/domain input to engine validation interfaces; it may not redefine engine authority, resolver or Continuity mechanics.

### 6.3 `ValidationReport`

Validation is tri-state at the overall and individual-rule level so uncertainty cannot masquerade as success.

```text
ValidationReport
  report_id
  artifact_ref
  semantic_revision
  render_spec_ref
  execution_plan_ref
  profile_versions[]
  overall_outcome            # pass | fail | indeterminate
  results[]
```

#### `ValidationResult`

```text
rule_id
outcome                      # pass | fail | indeterminate | not_applicable
semantic_path
dimension
severity
evidence_refs[]
observed_summary
failure_class?
repair_advice?
```

Initial `failure_class` vocabulary:

```text
retryable_execution
semantic_drift
preservation_regression
capability_unsatisfied
user_decision_conflict
hard_domain_violation
not_evaluable
invalid_or_stale_state
```

Rules:

1. a mandatory rule that is `indeterminate` prevents automatic acceptance unless an explicit user/domain policy authorizes that uncertainty;
2. validation results are immutable evidence for an exact artifact + semantic revision + profile version;
3. `repair_advice` may identify likely mutable paths/capabilities but cannot execute a repair;
4. the validation layer must recheck both the failed target and preserved baseline dimensions after repair;
5. profile/rule version changes are explicit and cannot retroactively alter historical reports.

## 7. Family B — Requirement, Capability & Lowering

### 7.1 Owner and non-goals

Family B compiles a validated semantic revision into execution requirements, resolves a legal execution **strategy**, and lowers that strategy to provider/tool steps.

It does not own desired intent, approvals, domain meaning or provider-native truth.

### 7.2 `RenderSpec`

`RenderSpec` is an immutable compiled view, never the SSoT.

```text
RenderSpec
  render_spec_id
  schema_version
  job_id
  source_semantic_revision
  source_intent_digest
  authority_snapshot_ref
  spatial_profile_snapshot_ref
  domain_profile_refs[]
  intent_obligations[]
  preservation_obligations[]
  creative_freedoms[]
  input_artifact_refs[]
  output_contract
```

`creative_freedoms` are explicit areas the provider may vary; absence of a lock must not be interpreted as a hidden mandatory lock.

### 7.3 `RequirementSet`

```text
RequirementSet
  requirement_set_id
  render_spec_ref
  requirements[]
```

#### `CapabilityRequirement`

```text
requirement_id
namespace                    # e.g. aimage.image.edit
action_or_capability
necessity                    # mandatory | optional
constraints{}
source_semantic_paths[]
allowed_representation       # exact | within_declared_tolerance
```

The namespace carries image-domain semantics; the matching/resolution mechanic is generic.

### 7.4 `ProviderCapabilityDescriptor`

A descriptor is a version-sensitive observation of a target, not permanent truth.

```text
ProviderCapabilityDescriptor
  descriptor_id
  target_id
  target_kind                # provider | local_backend | compositor | utility
  adapter_id
  adapter_version
  target_version_or_model
  observed_at
  evidence_kind              # declared | probed | configured | reproduced
  capabilities[]
  known_limits[]
```

Each capability has namespace/name/attributes/limits sufficient for requirement matching.

Stale/changed capability descriptors trigger re-resolution before execution when material to mandatory requirements.

### 7.5 `ResolutionResult`

The resolver selects a capability-satisfying **strategy**, which may contain one or multiple targets.

```text
ResolutionResult
  resolution_id
  render_spec_ref
  requirement_set_ref
  status                      # resolved | unsatisfied | stale_capabilities
  selected_strategy
  requirement_wiring[]
  unsatisfied_mandatory[]
  unsatisfied_optional[]
  considered_fallbacks[]
  rationale
```

`selected_strategy` may be a single target or a small ordered/DAG composition, for example:

```text
image_generation -> deterministic_text_compositor
```

Rules:

1. every effective mandatory requirement must be wired to at least one compatible capability or resolution is `unsatisfied`;
2. optional requirements may remain unsatisfied if the result records that fact;
3. a provider name alone is not a valid resolution — the exact descriptor/capability evidence is referenced;
4. cost/latency/privacy preferences may rank otherwise legal strategies, but cannot erase mandatory semantic constraints;
5. if no legal strategy exists, return explicit unsatisfied reasons rather than lowering a weaker hidden intent.

### 7.6 `ExecutionPlan`

```text
ExecutionPlan
  execution_plan_id
  render_spec_ref
  resolution_ref
  source_semantic_revision
  steps[]
  lowering_trace[]
```

#### `ExecutionStep`

```text
step_id
target_descriptor_ref
operation
input_refs[]
provider_or_tool_payload_ref
output_role
depends_on[]
```

#### `LoweringTraceEntry`

```text
source_semantic_path
requirement_id
target_step_id
representation
fidelity                     # exact | within_declared_tolerance | not_representable
notes?
```

Legality rules:

1. mandatory semantics may not have `not_representable` lowering entries;
2. `within_declared_tolerance` is legal only when the source semantic explicitly permits that tolerance;
3. a provider-specific prompt/graph/request is execution payload, not canonical semantics;
4. the same `RenderSpec` may be re-resolved/lowered to a different legal strategy without changing `VisualIntentState`;
5. runtime provider failure does not mutate intent — it causes retry, capability refresh, re-resolution or explicit failure.

## 8. Artifact and run linkage

Existing artifact/lineage and run/provenance capabilities remain separate generic mechanics. The semantic contracts require only these links:

```text
ArtifactRecord
  artifact_id
  content_digest
  media_metadata
  derived_from_artifact_refs[]
  producing_run_ref

RunRecord
  run_id
  execution_plan_ref
  actual_target_versions[]
  output_artifact_refs[]
  raw_provider_result_ref?
  usage_cost_latency?
```

Acceptance/rejection is **not** inferred from `ArtifactRecord` creation. Family A `ArtifactDispositionRecord` owns that semantic decision.

## 9. Cross-family invariants

The later implementation must enforce these invariants at contract boundaries.

1. **Single semantic SSoT** — `VisualIntentState` is canonical desired-state authority.
2. **Derived-state traceability** — every RenderSpec/plan/report traces to exact semantic revision and source identities.
3. **No silent semantic loss** — mandatory intent/preservation obligations cannot disappear during compile, resolution or lowering.
4. **Controlled baseline change** — approved paths cannot change without explicit reopen/superseding decision.
5. **Repair frame safety** — repair may mutate only authorized paths and must regression-check preserved paths.
6. **Explicit spatial frame** — viewpoint-sensitive relations resolve an explicit reference frame.
7. **Decision/enforcement separation** — validation decides/reports; provider/tool execution enforces/changes.
8. **Provider independence** — provider-native state cannot become authority, and provider replacement leaves semantic meaning intact.
9. **Domain direction** — domain profiles depend on engine contracts; engine contracts do not import concrete domain implementations.
10. **Revision-bound decisions** — duplicate decisions are idempotent and late/stale decisions cannot overwrite newer semantic state.
11. **Rejected artifact non-resurrection** — rejected/superseded artifacts remain historical evidence and cannot become accepted by retry/resume recency.
12. **Tri-state validation** — indeterminate mandatory checks cannot be silently interpreted as pass.
13. **Composite legal strategies** — requirement resolution may compose targets when one target cannot satisfy all requirements, without inventing a new workflow engine.
14. **Simple one-shot path** — empty/irrelevant production gates are not forced on trivial generation.
15. **Historical immutability** — old plans/reports remain historical evidence after newer revisions; they are not rewritten to match the present.

## 10. State/transition obligations

The exact implementation state machine remains generic/adapted, but the semantic transitions must support:

```text
intent_created
intent_revised
candidate_created
artifact_approved
artifact_rejected
baseline_created
baseline_reopened
render_compiled
requirements_resolved
resolution_unsatisfied
execution_started
execution_failed
artifact_generated
validation_passed
validation_failed
validation_indeterminate
repair_planned
repair_executed
finalized
```

A transition carrying a semantic decision includes the decision/revision identity required to reject stale or duplicate events.

## 11. Schema evolution rules

Planning default remains JSON-family versioned contracts with JSON Schema-style validation; the concrete library is deferred.

Rules:

1. every durable object carries `schema_version`;
2. compatible readers may accept older forms only under explicit compatibility rules;
3. incompatible changes require explicit migration, not best-effort field guessing;
4. historical source version remains identifiable after migration;
5. migration may change representation but must not silently change semantic meaning;
6. unknown mandatory semantics fail safe rather than being discarded.

## 12. Implementation-facing contract tests to plan later

When implementation is authorized, at minimum create contract tests for:

- revision-bound idempotent decisions;
- baseline reopen/change-control;
- role-separated references;
- viewer-deictic versus screen/image frame distinction;
- mandatory capability resolution failure;
- composite capability strategy;
- lowering-loss rejection;
- tri-state validation;
- rejected artifact non-resurrection;
- same RenderSpec re-resolution to different provider targets;
- repair mutation-frame preservation/regression detection;
- schema-version migration and unsupported-version failure.

Concrete packages and provider versions remain subject to Assurance Gate B before integration.

## 13. Relationship to Continuity/Handoff

Continuity/Handoff may transport these decision-relevant identities when crossing context boundaries:

- `job_id`;
- current `semantic_revision`;
- current `VisualIntentState` identity/digest;
- active baselines/DecisionRecord identities;
- accepted/rejected artifact identities as needed;
- current RenderSpec/ValidationReport identity when decision-relevant;
- active failure/MutationFrame identity;
- exactly one next action.

The receiver must fresh-reconcile repository/runtime authority. Continuity transport does not become a second owner of image semantics.

## 14. Completion definition

This contract design is acceptable only if the design-only tabletop audit can traverse the canonical assurance scenarios without:

- ambiguous semantic ownership;
- silent loss of mandatory intent;
- provider state becoming authority;
- stale/duplicate decisions mutating current state;
- repair crossing its mutation frame;
- rejected artifacts reappearing as accepted;
- viewpoint-sensitive spatial ambiguity;
- validation mutating its subject;
- domain-to-core dependency inversion.

The companion audit is `audits/SEMANTIC_CONTRACT_TABLETOP_2026-09-10.md`.