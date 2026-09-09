# AIMAGE Semantic Fusion Final Plan

Status: final planning/design integration plan for the provider-neutral semantic layer. This document refines the previously recorded six AIMAGE semantic residues into four coherent contract families built from mature external primitives. It does **not** authorize implementation, dependency installation, source import, provider integration, or runtime package selection.

## 1. Decision

AIMAGE should not implement six independent native semantic subsystems.

The latest bounded cross-domain search shows that the remaining generic mechanics are already established in other fields. The final planning direction is therefore:

> **reuse established intent-management, baseline/change-control, requirement-capability resolution, qualitative spatial reasoning, and constraint-validation patterns; make AIMAGE authoritative only for the smallest image-production vocabulary and domain meaning that those generic systems cannot supply.**

This plan refines the semantic-residue decomposition in `plans/CAPABILITY_REUSE_MATRIX.md`. It does not reverse the already accepted concrete-provider acquisition decisions in `plans/EXTERNAL_REUSE_PLAN.md` or the assurance gates in `plans/REUSE_AND_INTEGRATION_ASSURANCE.md`.

## 2. New evidence that closes the remaining generic-mechanism gap

### 2.1 Intent lifecycle / canonical desired state

**IRTF RFC 9315 — Intent-Based Networking: Concepts and Definitions**

Useful generic pattern:

- intent is declarative desired outcome rather than low-level configuration;
- a normalized intent layer can act as a Single Source of Truth (SSoT);
- fulfillment translates high-level intent into lower-level actions/configuration;
- assurance monitors the realized system against the intended state;
- drift or non-fulfillment leads to corrective action;
- concrete execution elements may remain unaware of the higher-level intent.

Status/acquisition: informational RFC and design evidence, not a mandatory runtime or standards-track dependency. Acquisition mode `E/F` (method adaptation/reference).

Source:
- https://www.rfc-editor.org/info/rfc9315/

### 2.2 Selective approval, preservation and controlled change

**NIST configuration baseline / change control**

Useful generic pattern:

- an agreed configuration/baseline is a formally reviewed state;
- subsequent changes require controlled change rather than silent mutation.

Status/acquisition: method/reference only, `E/F`.

Source:
- https://csrc.nist.gov/glossary/term/configuration_baseline

**Frame conditions / JML `assignable` model**

Useful generic pattern:

- explicitly declare what may change;
- anything outside the declared mutable set is assumed unchanged;
- verification can therefore detect writes/modifications outside the authorized frame.

Status/acquisition: specification principle only, `E/F`; no OpenJML runtime dependency.

Source:
- https://www.openjml.org/tutorial/FrameConditions

### 2.3 Requirement ↔ capability resolution

**OSGi Requirement-Capability / Resolver model**

Useful generic pattern:

- resources expose typed capabilities;
- consumers declare requirements;
- namespaces carry domain-specific semantics;
- mandatory requirements must be satisfied by a consistent resolution;
- unsatisfied mandatory requirements produce explicit resolution failure rather than silent degradation;
- the resolver output is wiring/provisioning guidance, not the high-level requirement authority itself.

Status/acquisition: `E/F` method/model adaptation. Do not add an OSGi runtime merely to obtain this pattern.

Sources:
- https://docs.osgi.org/specification/osgi.core/8.0.0/framework.resource.html
- https://docs.osgi.org/specification/osgi.core/8.0.0/service.resolver.html

### 2.4 Spatial relation vocabulary

**Qualitative Spatial/Temporal Reasoning (QSTR/QSR)**

Useful generic pattern:

- represent human-like spatial information symbolically rather than requiring exact coordinates for every relation;
- mature calculi cover topology, orientation, distance and qualitative relations;
- directional interpretation depends on a reference frame, including viewer/deictic versus object/intrinsic frames.

Sources:
- https://www.ijcai.org/proceedings/2021/624
- https://cdn.aaai.org/FLAIRS/2007/FLAIRS07-128.pdf

**OGC GeoSPARQL / RCC8**

Useful generic pattern:

- standardized topological relation family such as equals, disconnected, externally connected, partially overlapping and proper-part relationships.

Status/acquisition: vocabulary/method adaptation only, `E/F`; no RDF/GeoSPARQL runtime is required for the AIMAGE core.

Source:
- https://docs.ogc.org/is/22-047r1/22-047r1.html

### 2.5 Domain validation and decision/enforcement separation

**W3C SHACL**

Useful generic pattern:

- validation rules/shapes are separate from the data being validated;
- validation produces a structured conformance/report result;
- reusable validation modules can be composed;
- validation does not mutate the subject under validation.

Planning basis: stable SHACL Recommendation concepts. SHACL 1.2 drafts may be monitored but are not a dependency decision.

Status/acquisition: `E/F` method/result-schema adaptation. AIMAGE remains JSON-family by default; RDF/SHACL runtime is not required.

Source:
- https://www.w3.org/TR/shacl/

**Open Policy Agent (OPA)**

Useful generic pattern:

- separate policy decision from enforcement;
- feed structured state into a policy/decision layer;
- return a decision that a separate execution component enforces.

Status/acquisition: `E/F` architecture pattern only initially; no OPA runtime requirement.

Source:
- https://www.openpolicyagent.org/docs

## 3. Final semantic architecture: four contract families

The previous six residue areas are folded into four families. These families are conceptual contracts, not four heavyweight frameworks.

### Family A — Visual Intent & Authority

Purpose: own the canonical, provider-neutral statement of what the user wants and what has already been approved.

External mechanics reused:

- RFC 9315 intent/SSoT/fulfillment/assurance model;
- NIST baseline/change-control concept;
- frame-condition mutable-set principle;
- previously accepted precedence/layering patterns from CSS/OpenUSD/policy systems;
- existing AIMAGE artifact identity/lineage mechanics from W3C PROV/OpenAssetIO-style adaptation.

AIMAGE owns only image-domain vocabulary and meaning, for example:

- authority dimensions such as `identity`, `style`, `composition`, `blocking`, `text_layout`;
- reference-to-dimension bindings;
- visual precedence/conflict rules when two authorities target the same dimension;
- dimension-scoped approval;
- `preserve` versus `mutable` visual dimensions;
- explicit reopen/change-control event for an approved dimension.

Canonical rule:

> **Visual Intent/Authority state is the semantic SSoT. Provider conversation IDs, ComfyUI graphs, Diffusers pipeline objects, prompts, masks, RenderSpecs and ExecutionPlans are derived/execution artifacts and may never silently become the canonical user-intent authority.**

### Family B — Requirement, Capability & Lowering

Purpose: determine whether a provider/backend can legally realize the current validated visual intent and produce an explicit provider execution plan.

External mechanics reused:

- OSGi Requirement-Capability namespaces and resolver semantics;
- LSP/Vulkan/OpenAssetIO capability-discovery patterns already accepted;
- LLVM/MLIR IR/lowering and target-legality patterns already accepted;
- JSON Schema validation/versioning already accepted.

AIMAGE owns only the image capability namespace/vocabulary, for example:

- `generate_image`;
- `image_edit`;
- `masked_edit`;
- `multi_reference`;
- `identity_reference`;
- `structural_conditioning`;
- `pose_or_depth_control`;
- `deterministic_text_layout`;
- fidelity/cost/privacy/local-execution constraints.

Planned objects:

- `VisualIntentState` — canonical desired outcome/authority, from Family A;
- `RenderSpec` — immutable, validated **compiled view** of the current intent for one render/review attempt;
- `RequirementSet` — mandatory/optional capabilities derived from that RenderSpec;
- `ProviderCapabilityDescriptor` — version-sensitive capabilities/constraints observed from an adapter;
- `ResolutionResult` — provider/strategy resolution or explicit unsatisfied reason;
- `ExecutionPlan` — provider-specific lowered request/graph/configuration.

Hard rule:

> A mandatory visual intent or preservation obligation may never be silently dropped during lowering. If no provider can satisfy it, routing must choose an explicit fallback/escalation or return an unsatisfied-plan result.

### Family C — Spatial & Composition Semantics Profile

Purpose: express the subset of spatial meaning that must remain stable across natural language, blocking, providers and review.

External mechanics reused:

- QSR/QSTR qualitative relations;
- explicit frame-of-reference concept;
- OGC/RCC8 topological relations;
- previously accepted OpenUSD transforms/relations and Cassowary/CSS constraint/layout concepts.

AIMAGE does **not** invent a general geometry language. It defines a compact image-production profile over mature primitives.

Initial semantic classes:

- topological: inside/contains/overlap/disconnected/touching where useful;
- directional: left/right/front/behind/above/below;
- distance: near/medium/far or normalized ranges when needed;
- alignment/order: same-row/same-column/aligned/between;
- frame of reference: `viewer/deictic`, `subject/intrinsic`, `scene/world`;
- camera/image-specific relations: gaze target, foreground/background ownership, screen-region placement, reading/attention order;
- optional numeric/constraint representation when qualitative relations are insufficient.

Critical rule:

> Directional predicates that can change meaning with viewpoint must carry or inherit an explicit reference frame. For example, `right_of(subject, viewer, frame=viewer)` must not be silently interpreted as screen-right, object-right, or world-east.

Adapters may lower spatial intent into prompt wording, blocking images, masks, poses, depth/control maps, scene graphs or other provider-native mechanisms. None of those representations becomes the canonical spatial authority.

### Family D — Validation & Domain Profile

Purpose: define what “this result satisfies the current intent/domain” means and return structured evidence without coupling validation to execution.

External mechanics reused:

- SHACL-style separation of rules/shapes from data and structured validation reports;
- OPA-style decision versus enforcement separation;
- generic plugin/profile mechanics already accepted;
- existing Assurance Gate C/D scenario/V&V framework.

AIMAGE/domain packages own only the actual image-specific rule vocabulary, for example:

- character identity match;
- approved composition preserved;
- text exactness;
- no forbidden artifact;
- product/logo correctness;
- storyboard continuity;
- domain-specific severity/threshold semantics.

Planned normalized result:

`ValidationReport`

with at least:

- overall conformance/decision;
- rule/profile identity/version;
- failed semantic path/dimension;
- severity;
- evidence or measurement reference;
- whether failure is retryable execution failure, repairable semantic drift, user-decision conflict, or hard unsatisfied constraint;
- suggested repair target only as advisory diagnosis, not direct provider execution.

Validation must not mutate the artifact/intent while deciding whether it conforms.

## 4. How the four families fuse into one production loop

```text
User natural language + references + prior approved state
                    |
                    v
        [A] Visual Intent & Authority SSoT
        desired outcome / authority / baseline
        mutable vs preserve frame
                    |
                    +-------------------------------+
                    |                               |
                    v                               v
        [C] Spatial Profile                [D] Domain Profile
        qualitative relations              acceptance rules
        frame of reference                  domain semantics
                    |                               |
                    +---------------+---------------+
                                    |
                                    v
                        Compile immutable RenderSpec
                                    |
                                    v
                     [B] RequirementSet + Resolver
                                    |
                  ProviderCapabilityDescriptors
                                    |
                         resolve / reroute / fail
                                    |
                                    v
                         provider ExecutionPlan
                                    |
                    OpenAI / ComfyUI / Diffusers
                                    |
                                    v
                              Artifact + Run
                                    |
                                    v
                         [D] ValidationReport
                                    |
                    intent/baseline assurance check
                           /                 \
                        pass                 drift/fail
                         |                      |
                         v                      v
                      accept          RepairIntent / change
                                         with frame condition
                                              |
                                              +----> recompile
```

This is one semantic system with four responsibilities, not four isolated engines.

## 5. RenderSpec is demoted from authority to compiled view

The previous planning correctly treated RenderSpec as an IR, but the intent-system evidence clarifies its ownership further.

Final rule:

- `VisualIntentState` is canonical semantic authority;
- `RenderSpec` is an immutable, versioned compilation snapshot for one attempt or family of attempts;
- `ExecutionPlan` is a provider-specific lowering of a RenderSpec;
- provider request/response state is execution evidence only.

This avoids a common architecture error where an execution format becomes the user's truth merely because it is easy to persist.

## 6. Approval / repair semantics after fusion

Approval and repair do not need separate custom subsystems.

### Approval

1. user or domain process approves selected visual dimensions;
2. approved values become a baseline within Family A;
3. unapproved dimensions remain mutable;
4. an intentional change to a baseline dimension requires an explicit reopen/change-control event.

### Repair

1. Family D identifies failed dimensions/rules;
2. Family A supplies the currently approved baseline and preservation obligations;
3. create a repair frame: only failed/authorized dimensions are mutable;
4. Family B chooses the cheapest provider capability able to make that change;
5. provider executes the actual image edit;
6. Family D revalidates both the repaired variable **and regression against preserved dimensions**.

AIMAGE still does not implement an image-editing renderer.

## 7. External acquisition/application matrix for the newly added methods

| External source | Bring in as | Runtime coupling | AIMAGE use | Do not do |
|---|---|---|---|---|
| RFC 9315 | `E/F` method/reference | none | intent SSoT, fulfillment/assurance loop | do not treat an informational networking RFC as executable AIMAGE specification |
| NIST configuration baseline | `E/F` method/reference | none | approval baseline and explicit change control | do not import security-control bureaucracy irrelevant to image jobs |
| JML frame conditions | `E/F` method/reference | none | mutable/preserve set semantics | do not adopt JML syntax/runtime |
| OSGi Requirement-Capability | `E/F` model adaptation | none initially | generic requirement/capability/resolution structure | do not add OSGi framework/runtime |
| QSR/QSTR literature | `E/F` method/ontology evidence | none | qualitative relation families and reference frames | do not attempt a universal spatial ontology |
| OGC RCC8/GeoSPARQL | `E/F`; optional future interop only | none initially | topological relation vocabulary | do not require RDF/GeoSPARQL core storage |
| W3C SHACL | `E/F` validation/result-model adaptation | none initially | separate validation profiles and structured result pattern | do not force RDF into AIMAGE merely to use SHACL ideas |
| OPA | `E/F` architecture pattern | none initially | decision/enforcement separation | do not require OPA runtime unless a measured policy-engine need appears |

Every later concrete library selected to implement any of these concepts must independently pass `plans/REUSE_AND_INTEGRATION_ASSURANCE.md` Gate B.

## 8. Existing external-provider plan remains intact

The semantic fusion plan does not reopen accepted provider integration choices:

- OpenAI official SDK/API — first normal hosted-provider adapter;
- Hugging Face Diffusers — optional local-provider package;
- ComfyUI — optional separately installed backend/service;
- provider/source licenses remain separate from model/checkpoint/content licenses;
- no initial Nori/GenAI/Krita/style-consistency source copy;
- OpenAssetIO/OpenUSD/C2PA remain optional interoperability/evidence unless a concrete use case justifies runtime integration.

## 9. Workflow mapping

The accepted `plans/WORKFLOW_TARGET.md` remains valid; this plan tells each logical function where its semantics live.

- W0 intent/brief -> Family A intent ingestion/normalization;
- W1 authority/profile/reference -> Family A authority bindings + Family D domain profile;
- W2 creative directions -> feature strategy produces candidate intents, not new core mechanics;
- W3 composition/layout -> Family C spatial profile;
- W4 optional text/layout -> Family C layout semantics + deterministic capability requirement where needed;
- W5 blocking/skeleton -> derived artifact carrying Family C intent;
- W6 composition approval -> Family A baseline/change-control event;
- W7 optional rough -> derived artifact, same authority model;
- W8 RenderSpec lock -> compile/validate immutable RenderSpec from current SSoT;
- W9 provider capability/routing -> Family B requirement/capability resolution;
- W10 render -> ExecutionPlan through provider adapter;
- W11 review -> Family D ValidationReport;
- W12 repair/escalation -> A/D diagnosis + A frame condition + B capability selection + provider-native execution;
- W13 finalization/export -> accepted artifact plus deterministic finishing/provenance as required;
- W14 continuity/handoff -> transports identities and accepted semantic state, but remains outside Image Engine ownership.

No new user-visible ceremony is added by this plan.

## 10. Design invariants that later code must prove

1. **Single semantic authority** — canonical user intent/approval lives in AIMAGE VisualIntent/Authority state, never in provider-native state.
2. **No silent semantic loss** — mandatory intent or preservation requirements cannot disappear during compilation/lowering.
3. **Baseline protection** — approved dimensions cannot change without explicit reopen/change control.
4. **Repair frame safety** — a repair may mutate only explicitly authorized dimensions; preserved dimensions are regression obligations.
5. **Reference-frame explicitness** — ambiguous directional spatial relations must resolve a viewpoint/reference frame before execution.
6. **Provider replaceability** — changing provider cannot by itself change authority, approval or domain semantics.
7. **Validation/execution separation** — validation decides and reports; provider/repair executor enforces.
8. **Validation purity** — a validation pass does not mutate the artifact or canonical intent being validated.
9. **Domain/core direction** — domain profiles supply vocabulary/rules through engine interfaces and cannot redefine continuity, generic state machinery or provider adapters.
10. **Derived-view identity** — RenderSpec and ExecutionPlan record exactly which canonical semantic state/version they were derived from.
11. **Explicit unsatisfied result** — if mandatory requirements cannot be resolved, return an explainable unsatisfied-plan/fallback state instead of best-effort silent degradation.
12. **One-shot simplicity** — trivial image generation can compile directly through the same model without exposing production workflow ceremony to the user.

## 11. Verification plan

The existing `plans/REUSE_AND_INTEGRATION_ASSURANCE.md` remains the governing assurance plan and is sufficient as the top-level V&V framework. This semantic plan adds required checks to its Gate C/D scenarios.

### Design-level tabletop audit before implementation

Before language/runtime selection, execute the canonical scenarios as state/contract simulations using only proposed objects and transitions:

- one-shot generation;
- composition-sensitive approval;
- viewer-relative same-row/right-of case;
- user blocking authority;
- cross-provider reroute;
- minimal-delta repair with preserved dimensions;
- reference-role replacement;
- capability absence/unsatisfied mandatory requirement;
- exact text/layout requirement;
- cross-context resume;
- schema migration;
- backend unavailable;
- rejected artifact resurrection attempt;
- duplicate/late approval;
- dependency/provider replacement.

For each simulation prove the 12 invariants above and identify the exact canonical-state/derived-state objects at each step.

### Implementation-time verification

After implementation begins:

- contract/schema tests for each family;
- resolver tests for mandatory/optional capability combinations;
- lowering legality tests proving no required semantic disappears;
- state-transition and approval/change-control tests;
- spatial relation/reference-frame fixtures;
- validation-report fixtures;
- repair regression fixtures;
- provider contract tests;
- Gate D combinatorial coverage and fault injection already defined in the assurance plan.

### Final system verdict

Use the existing assurance verdicts:

- `PASS`;
- `PASS_WITH_DEFERRED_NONBLOCKERS`;
- `FAIL_REPLAN`.

Component-level success cannot substitute for integrated workflow `PASS`.

## 12. Final remaining native design surface

After this fusion, AIMAGE should not claim ownership of generic mechanisms such as intent engines, baseline engines, resolver algorithms, spatial-reasoning frameworks, policy engines or validation engines merely because it uses those ideas.

The irreducible AIMAGE-owned design surface is now primarily **image-production vocabulary and semantic profiles**:

- visual authority dimensions and their image-specific meaning;
- image capability namespace/attributes;
- compact image-production spatial predicates not already supplied directly by generic calculi;
- image/domain validation rule vocabulary and thresholds;
- mappings from those semantics to provider-neutral requirements and review evidence.

This is closer to an ontology/profile layer than a new general-purpose computer-science framework.

## 13. Planned execution sequence after this plan is adopted

Still planning/design/research only until separately authorized.

1. **Contract-schema slice** — define the minimum provider-neutral data contracts for the four families and the 12 invariants; reuse JSON Schema/versioning and existing lineage/state mechanics.
2. **Tabletop semantic simulation** — run the Assurance scenarios without provider code and audit for semantic loss, duplicated ownership and unresolvable states.
3. **Implementation planning** — choose implementation language/runtime and concrete packages only after the contract/tabletop audit passes.
4. **Gate B acquisition review** — exact version/license/security/coupling checks for every concrete dependency selected.
5. **First vertical slice** — implement the smallest end-to-end flow with the OpenAI adapter without changing the semantic contracts.
6. **Provider-replacement proof** — add/fixture an alternate provider boundary and prove the same canonical intent/approval semantics survive.
7. **Optional backends** — ComfyUI/Diffusers only after the core semantic contract is proven provider-neutral.
8. **Full integrated V&V** — run Gate C/D scenarios, combinatorial coverage, fault injection, repair regressions and cross-context resume.
9. **Final architecture/workflow audit** — return the assurance verdict; unresolved material semantic/coupling failures require replan rather than patching around the contract.

## 14. Completion criterion for this planning layer

This semantic-fusion planning layer is complete when:

- this four-family decomposition is independently audited against fresh `main`, `architecture/BOUNDARIES.md`, existing reuse plans and workflow target;
- no newer work makes the plan non-unique;
- the plan is adopted on `main` and routed from current continuity;
- `governance/continuity/CURRENT.md` advances the next bounded action to **contract-schema design + design-level tabletop simulation**, not implementation.

Implementation remains explicitly out of scope until that next design slice passes its own independent audit.