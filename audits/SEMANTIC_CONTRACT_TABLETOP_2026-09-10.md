# AIMAGE Semantic Contract Tabletop Audit — 2026-09-10

Status: design-only independent audit of `plans/SEMANTIC_CONTRACTS.md` against the accepted semantic-fusion architecture and existing Assurance Gate C/D scenarios. No runtime/provider execution occurred. This is not the final implementation/system V&V verdict.

## 1. Audit verdict

**PASS AFTER DESIGN REPAIR**

The first tabletop pass exposed four material contract gaps. They were repaired in the contract candidate before the final pass:

1. **single-provider resolution was too narrow** — exact text/layout and other composite workflows require a legal multi-target strategy; `ResolutionResult` now resolves a capability-satisfying strategy, potentially a small ordered/DAG composition;
2. **approval/rejection events needed revision binding** — `DecisionRecord` now carries `decision_id` + `base_semantic_revision`, making duplicate decisions idempotent and stale/late decisions rejectable;
3. **rejected artifact state was insufficiently explicit** — `ArtifactDispositionRecord` now records candidate/accepted/rejected/superseded state independently of creation time/provider state;
4. **binary validation was unsafe** — `ValidationReport`/results are now tri-state (`pass`, `fail`, `indeterminate`) so unevaluable mandatory rules cannot silently become success.

After those repairs, no architecture-blocking contradiction was found in the bounded design simulations below.

## 2. Authority and scope checked

Exact fresh base used for the candidate:

`main = 49d10e1e8da54e7b42107f12a9b8d964c344054f`

Checked against:

- `AGENTS.md`;
- `architecture/BOUNDARIES.md`;
- `plans/WORKFLOW_TARGET.md`;
- `plans/CAPABILITY_REUSE_MATRIX.md`;
- `plans/EXTERNAL_REUSE_PLAN.md`;
- `plans/REUSE_AND_INTEGRATION_ASSURANCE.md`;
- `plans/SEMANTIC_FUSION_PLAN.md`;
- `governance/continuity/CURRENT.md`.

Phase remains planning/design/research only.

No implementation language, package, provider model/version, source import or runtime dependency is selected by this audit.

## 3. External semantic-method spot checks

The contract assumptions were rechecked against primary/official sources before the tabletop:

- RFC 9315 defines intent as declarative goals/outcomes, defines an SSoT that normalizes validated intent, and uses intended-versus-operational state to detect drift and support corrective actions:
  - https://www.rfc-editor.org/rfc/rfc9315.html
- NIST configuration baseline is a formally reviewed/agreed specification changed only through change-control procedures:
  - https://csrc.nist.gov/glossary/term/Configuration_Baseline
- OpenJML frame conditions explicitly state which memory may change; anything not listed is assumed unchanged:
  - https://www.openjml.org/tutorial/FrameConditions
- OSGi Resource/Resolver defines typed Requirement/Capability namespaces and requires all mandatory requirements in a resolution to be satisfied or the resolution fails:
  - https://docs.osgi.org/specification/osgi.core/8.0.0/framework.resource.html
  - https://docs.osgi.org/specification/osgi.core/8.0.0/service.resolver.html
- SHACL validation separates a shapes graph from the data graph and produces a structured validation report with conformance/results:
  - https://www.w3.org/TR/shacl/

These remain method/schema evidence, not mandatory AIMAGE runtimes.

## 4. Tabletop method

Each scenario is simulated as semantic object/state transitions rather than provider code.

For each case the audit asks:

1. what is canonical semantic state;
2. what derived objects are produced;
3. which invariants apply;
4. what happens on failure/staleness;
5. whether provider/domain state leaks into semantic authority;
6. whether the flow can continue without inventing a missing owner or silently dropping intent.

Verdicts:

- `PASS` — current contracts represent the case without ownership conflict or silent semantic loss;
- `PASS_DEFERRED_RUNTIME` — semantics close, but actual provider/library behavior remains an implementation-time Gate-B/test obligation;
- `FAIL` — contract architecture cannot represent the case safely.

## 5. Canonical scenario simulations

### S00 — OneShot

Input: simple request with no references, approval gate or exact layout requirement.

Flow:

`VisualIntentState(rev1)` -> `RenderSpec(rev1)` -> `RequirementSet(generate_image mandatory)` -> legal provider strategy -> `ExecutionPlan` -> artifact -> lightweight `ValidationReport` -> accepted disposition if successful.

Findings:

- no baseline is required;
- no blocking/approval ceremony is forced;
- creative freedoms remain broad;
- provider payload remains derived.

Verdict: **PASS**.

### S01 — CompositionSensitive

Input: several composition directions are explored; user approves one composition while leaving expression/lighting free.

Flow:

- candidate artifacts/directions remain candidates;
- approval creates revision-bound `DecisionRecord` and active `BaselineRecord` covering composition/camera paths only;
- new `RenderSpec` carries composition preservation obligations and explicit creative freedoms for unapproved dimensions;
- later generation validates composition against the baseline.

Finding: partial approval can be represented without freezing the whole image.

Verdict: **PASS**.

### S02 — UserBlockingAuthority

Input: user supplies a blocking sketch and approves it only for structural/composition authority.

Flow:

- sketch is an `ArtifactRecord`;
- `ReferenceBinding(role=blocking, dimensions=[composition/camera/...])` scopes its authority;
- identity/style references remain separate;
- approval creates baseline over only the bound structural paths;
- provider receives derived structural controls through lowering.

Finding: blocking artifact cannot silently become identity/style authority.

Verdict: **PASS**.

### S03 — CrossProviderReroute

Input: accepted intent/geometry is initially planned for provider A; A becomes unavailable or incapable before execution.

Flow:

- `VisualIntentState` and `RenderSpec` stay unchanged;
- refresh `ProviderCapabilityDescriptor`s;
- rerun `ResolutionResult` against the same `RequirementSet`;
- lower to a new `ExecutionPlan` for provider B/strategy B;
- validation still checks the same semantic revision/baselines.

Finding: rerouting does not require rewriting canonical intent.

Verdict: **PASS_DEFERRED_RUNTIME**.

### S04 — MinimalDeltaRepair

Input: generated artifact satisfies identity/composition but expression is wrong.

Flow:

- `ValidationReport` returns failure on expression path and pass evidence on locked identity/composition;
- derived `MutationFrame.mutable_paths=[expression]`, `preserve_paths=[approved identity/composition paths]`;
- `RequirementSet` requires suitable edit capability + preservation obligations;
- resolver chooses cheapest legal edit strategy;
- provider performs actual edit;
- second validation checks expression success **and** regression on preserve paths.

Finding: repair does not need to mutate desired intent or build a custom AIMAGE editor.

Verdict: **PASS_DEFERRED_RUNTIME**.

### S05 — ReferenceRoleSeparation

Input: user replaces only the character identity reference.

Flow:

- new explicit user decision updates only `ReferenceBinding` scoped to identity;
- creates new semantic revision;
- style/composition bindings remain unchanged;
- old RenderSpecs/plans become stale for future execution;
- new compilation preserves unaffected authorities.

Finding: role/dimension scoping prevents reference replacement spillover.

Verdict: **PASS**.

### S06 — CapabilityFallback

Input: mandatory masked/local edit is required but current target cannot perform it.

Flow:

- `CapabilityRequirement(masked_edit, mandatory)` remains explicit;
- if alternate target/composite strategy exists, resolver selects it;
- otherwise `ResolutionResult.status=unsatisfied` with unresolved mandatory requirement;
- no weaker whole-image reroll is silently substituted unless user/policy explicitly authorizes a semantic fallback.

Finding: mandatory semantics cannot disappear in lowering.

Verdict: **PASS**.

### S07 — TextLayout Composite Strategy

Input: image generation plus exact deterministic text placement.

Initial gap found: a single-provider `selected_provider` model could not express hosted image generation followed by deterministic SVG/CSS composition.

Repair:

- `ResolutionResult` now selects a legal strategy with one or multiple targets;
- requirement wiring maps `generate_image` to image provider and `deterministic_text_layout` to compositor;
- `ExecutionPlan.steps[]` expresses the bounded ordered/DAG composition;
- semantic authority remains in the RenderSpec/intent, not the SVG/provider payload.

Finding: composite resolution closes the requirement without introducing a generic workflow engine.

Verdict after repair: **PASS_DEFERRED_RUNTIME**.

### S08 — CrossContextResume

Input: work pauses after composition approval and a failed expression review.

Continuity carries decision-relevant identities:

- job id;
- current semantic revision / intent-state identity;
- active baselines/decision ids;
- accepted/rejected artifact identities;
- relevant validation report / mutation frame;
- exactly one next action.

Receiver fresh-reconciles current repository/runtime authority; execution plans may be regenerated from semantic state.

Finding: Continuity transports semantic state but does not become its owner.

Verdict: **PASS**.

### S09 — SchemaMigration

Input: stored contract uses an older schema version.

Flow:

- representation version and semantic revision remain distinct;
- compatible read uses explicit compatibility rule;
- incompatible form requires explicit migration;
- unknown mandatory semantics fail safe rather than being discarded;
- historical source version remains identifiable.

Finding: semantic meaning is preserved independently of representation migration.

Verdict: **PASS_DEFERRED_RUNTIME** (exact migration tooling deferred).

### S10 — BackendUnavailable

Input: ComfyUI/other optional backend disappears after a valid plan existed.

Flow:

- runtime execution fails;
- semantic state is untouched;
- capability descriptors are refreshed;
- same RenderSpec is re-resolved to another legal strategy or explicit unsatisfied result.

Finding: backend availability cannot corrupt canonical state.

Verdict: **PASS_DEFERRED_RUNTIME**.

### S11 — ProvenanceExport

Input: user requests exported provenance (for example future C2PA support).

Flow:

- internal artifact/run lineage remains AIMAGE-owned identity/provenance;
- optional exporter derives external provenance representation;
- external provenance format never becomes internal job authority.

Verdict: **PASS_DEFERRED_RUNTIME**.

### S12 — RejectedArtifactNonResurrection

Input: artifact B is newer than accepted artifact A but user rejected B; a restart/retry occurs.

Initial gap found: creation/lineage alone does not encode the user decision strongly enough.

Repair:

- `ArtifactDispositionRecord(B, rejected)` persists separately from artifact creation;
- accepted/current status must be derived from explicit disposition/decision, not newest timestamp/provider thread;
- Continuity can carry the relevant disposition ids;
- resume cannot promote B without a new valid decision.

Verdict after repair: **PASS**.

### S13 — DuplicateOrLateApproval

Input: an approval message is delivered twice, then an older approval arrives after intent was revised.

Initial gap found: approval needed idempotency and base revision.

Repair:

- `decision_id` makes exact duplicate processing idempotent;
- `base_semantic_revision` binds the decision to the state the user actually reviewed;
- late approval against a different live revision returns `STALE_DECISION` instead of overwriting state.

Verdict after repair: **PASS**.

### S14 — Dependency/Provider Replacement

Input: replace provider adapter/library behind the same semantic boundary.

Flow:

- new adapter emits a new `ProviderCapabilityDescriptor`;
- existing RequirementSet is resolved against it;
- only a legal strategy is lowered;
- baseline/authority/domain validation contracts remain unchanged.

Finding: replacement is bounded by capability contracts rather than provider request shape.

Verdict: **PASS_DEFERRED_RUNTIME**.

### S15 — ViewerRelativePlacement

Input: "the subject is directly to my right, on the same row, with some distance" from first-person viewer perspective.

Canonical spatial form includes, conceptually:

```text
right_of(subject, viewer, frame=viewer_deictic)
same_row(subject, viewer, frame=scene_world)
medium_distance(subject, viewer)
```

If output places subject in front-right:

- ValidationReport fails the relation/path rather than declaring general aesthetic dissatisfaction;
- repair MutationFrame may allow composition/spatial correction while preserving approved identity/style;
- provider lowering may use prompt/blocking/pose/depth/etc., but cannot reinterpret viewer-deictic right as screen-right or front-right silently.

Finding: explicit reference frame closes the recurring ambiguity class the design is intended to solve.

Verdict: **PASS_DEFERRED_RUNTIME**.

## 6. Additional architecture stress cases

### Provider field/API deprecation

A provider request field disappears. Capability descriptor/lowering adapter changes; semantic SSoT remains valid. A plan that depends on stale capabilities is re-resolved or fails explicitly.

**PASS_DEFERRED_RUNTIME**.

### Long approval pause

A baseline/decision is immutable and revision-bound; resume uses exact ids/revision rather than provider conversation memory.

**PASS**.

### Domain-rule conflict with user intent

Domain profile marks an explicit user choice invalid. Family D returns `user_decision_conflict`; it does not silently mutate Family A. Resolution requires user/domain-policy decision.

**PASS**.

### Mandatory rule cannot be evaluated

Initial binary-validation design was unsafe. Tri-state validation now returns `indeterminate`; mandatory indeterminate blocks auto-accept unless explicit policy/user authority allows uncertainty.

**PASS after repair**.

## 7. Fusion invariant matrix

| Invariant | Tabletop evidence | Verdict |
|---|---|---|
| One canonical semantic authority | S03, S08, S10, S14 | PASS |
| No silent loss in compile/lowering | S06, S07 | PASS |
| Baseline changes only by controlled decision | S01, S13 | PASS |
| Repair stays inside authorized frame | S04 | PASS |
| Viewpoint-sensitive relation has frame | S15 | PASS |
| Provider replacement preserves semantics | S03, S14 | PASS |
| Validation separate from enforcement | S04, S15 | PASS |
| Domain does not invert core dependency | domain conflict case | PASS |
| Derived objects identify source revision | S05, S08, S09 | PASS |
| Unsatisfied mandatory requirement is explicit | S06 | PASS |
| One-shot remains simple | S00 | PASS |
| Stale/duplicate decisions are safe | S13 | PASS |
| Rejected artifact cannot resurrect | S12 | PASS |
| Indeterminate is not silently pass | mandatory-evaluation case | PASS |
| Composite capability strategy supported | S07 | PASS |

## 8. Boundary audit

Confirmed against `architecture/BOUNDARIES.md`:

- Continuity/Handoff transports but does not define image-generation semantics;
- Family A/B/C are generic Image Engine semantic contracts;
- concrete DomainProfile rule content remains feature/domain-owned;
- feature/domain capability depends on engine validation/semantic interfaces, not vice versa;
- provider adapters and payloads remain below semantic authority;
- no provider request, ComfyUI graph, Diffusers object, prompt or external provenance format becomes canonical job state.

No boundary revision is required by this slice.

## 9. Assurance status

### Gate A — capability/semantic coverage

**PASS for the bounded semantic-contract design.**

All four families have owners, non-goals, exact minimum objects and cross-family invariants. The four design gaps found by simulation were repaired rather than deferred invisibly.

### Gate B — acquisition due diligence

**NOT EXECUTED BY DESIGN.**

No concrete implementation language/library/provider version was selected. Gate B remains mandatory during the next implementation-planning slice for every actual dependency.

### Gate C — architecture scenarios

**PASS at design/tabletop level**, subject to later implementation evidence.

### Gate D — integrated V&V

**DESIGN COVERAGE PASS ONLY.**

The scenario/traceability structure can be represented by the contracts, but actual integrated execution, combinatorial testing and fault injection remain future implementation V&V obligations.

A final system `PASS` is explicitly not claimed here.

## 10. Residual risks / deliberately deferred items

These are non-blocking for semantic architecture but blocking before/at implementation where applicable:

- exact implementation language/runtime;
- exact JSON Schema validator/migration library;
- exact storage/blob implementation;
- exact provider SDK/model versions and empirically reproduced capability descriptors;
- exact image/spatial validation evaluators and their reliability/calibration;
- exact solver/package if numeric constraint solving proves necessary;
- actual preservation fidelity attainable from each provider's edit capabilities;
- quantitative thresholds for domain-specific visual QA.

They do not change semantic ownership, failure behavior or provider-neutral contract shape established here.

## 11. Independent bounded verdict

**PASS AFTER DESIGN REPAIR.**

The semantic architecture is now sufficiently specified to move from semantic-design discovery into a separate **implementation-planning** slice.

This does not authorize production code yet.

## 12. Recommended next bounded action

Prepare the implementation plan only:

1. choose the implementation language/runtime using the accepted contract/adapter/storage/test requirements;
2. select the minimum concrete packages for schema validation, persistence, optional constraint solving and test harnesses;
3. execute Assurance Gate B for each actual dependency/provider integration;
4. define repository/module boundaries directly from the four semantic families and existing architecture boundary;
5. define contract tests from `plans/SEMANTIC_CONTRACTS.md`;
6. plan the first thin vertical slice: one-shot + composition approval + viewer-relative placement + provider reroute + minimal-delta repair with **OpenAI as the first provider adapter**, while keeping Diffusers/ComfyUI optional/deferred;
7. independently audit the implementation plan before implementation authorization.
