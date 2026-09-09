# AIMAGE Current Repository-Work Continuity

Status: current repository-work continuity locator for the active planning/design/research slice. This file records decision-relevant current state; it does not replace `governance/CONTINUITY.md`, `governance/continuity/REPOSITORY_WORK.md`, root `AGENTS.md`, the handoff skill, or Image Engine specifications.

## 1. Authority snapshot

- Repository: `domato153/aimage`
- Authoritative branch: `main`
- Fresh accepted `main` used as the exact base for this candidate: `61ba94bc6279fa12091baa05c30a2ce1dd4fc5d8`
- Planning candidate branch: `aimage-stage/semantic-fusion-final-plan`
- Current governing entrypoint: `AGENTS.md`
- Continuity method: `governance/CONTINUITY.md`
- Repository-work profile: `governance/continuity/REPOSITORY_WORK.md`
- Handoff method: `.agents/skills/handoff/SKILL.md`
- Architecture boundary: `architecture/BOUNDARIES.md`
- Workflow target: `plans/WORKFLOW_TARGET.md`
- Capability classification: `plans/CAPABILITY_REUSE_MATRIX.md`
- External acquisition/integration plan: `plans/EXTERNAL_REUSE_PLAN.md`
- Reuse/integration assurance: `plans/REUSE_AND_INTEGRATION_ASSURANCE.md`
- **Semantic fusion final-plan candidate:** `plans/SEMANTIC_FUSION_PLAN.md`

Fresh repository/platform state always governs current factual state. A candidate copy cannot authorize itself; after adoption, the merge result becomes the new accepted factual base and the next receiver must fresh-reconcile it.

## 2. Current phase and scope

Phase: **planning / design / research only**.

No Image Engine implementation, provider integration, package installation, external-code import, runtime dependency change, or production code adoption is authorized by this state.

The prior cross-domain reuse/acquisition plan remains accepted. New bounded research has now challenged the six remaining semantic-residue areas against mature non-image fields and found stronger reusable primitives. Therefore the prior exact next action — “design six separate AIMAGE semantic areas” — is superseded by a narrower integrated semantic-fusion plan.

## 3. Completed foundation preserved

Do not reopen without new evidence or explicit scope change:

- thin GPT Project bootstrap -> current root `AGENTS.md`;
- AIMAGE-owned Continuity/Handoff with no runtime dependency on `domato153/translation`;
- current method-hardened Handoff behavior and fresh reconciliation rules;
- Continuity/Handoff separated from Image Engine/Core and Feature/Domain semantics;
- dependency direction `features/domain capabilities -> engine interfaces`;
- adaptive `plans/WORKFLOW_TARGET.md`;
- evidence-first `ADOPT / ADAPT / DESIGN` and abstract-problem cross-domain search policy;
- provider-native editing executes actual image edits where suitable; AIMAGE does not build a custom image-edit renderer;
- accepted initial concrete provider plan: OpenAI official SDK/API, optional Hugging Face Diffusers, optional external ComfyUI backend;
- no initial Nori/GenAI/Krita/style-consistency source copying;
- external acquisition due diligence and final integrated assurance gates in `plans/REUSE_AND_INTEGRATION_ASSURANCE.md`.

## 4. New cross-domain residue re-audit result

The remaining six semantic areas were re-searched using their abstract engineering problems rather than AIMAGE/image vocabulary.

New strong evidence families:

- **IRTF RFC 9315 Intent-Based Networking** — declarative intent, normalized Single Source of Truth, fulfillment/translation, assurance against realized state, corrective action;
- **NIST configuration baseline/change control** — reviewed/accepted baseline changed only through controlled change;
- **formal frame conditions / JML `assignable`** — explicitly declare what may change; everything outside the mutable frame is preserved;
- **OSGi Requirement-Capability/Resolver** — generic typed requirements/capabilities, namespaces for domain semantics, mandatory requirements must resolve or fail explicitly;
- **QSR/QSTR + OGC RCC8** — mature qualitative spatial relation calculi, topology/orientation/distance and explicit reference-frame reasoning;
- **W3C SHACL** — rule/shape separation from validated data and structured validation reports;
- **OPA policy architecture** — decision logic separated from enforcement/execution.

These are construction/design evidence unless separately adopted as a runtime dependency. The default acquisition mode is method/schema adaptation or reference (`E/F`), not code/framework import.

## 5. Semantic residue is now four contract families, not six frameworks

`plans/SEMANTIC_FUSION_PLAN.md` refines the previous six-residue decomposition into four coherent families.

### A — Visual Intent & Authority

Generic mechanics reused:

- intent/SSoT/assurance;
- baseline/change control;
- precedence/layering;
- frame-condition preservation;
- existing artifact identity/lineage adaptation.

AIMAGE owns only image-specific authority vocabulary and meaning: e.g. `identity`, `style`, `composition`, `blocking`, text/layout authority, dimension-scoped approval, precedence/conflict meaning, preserve/mutable dimensions and explicit reopen semantics.

**Canonical rule:** Visual Intent/Authority state is the semantic SSoT. Provider-native state, prompts, masks, RenderSpecs and ExecutionPlans are derived/execution artifacts only.

### B — Requirement, Capability & Lowering

Generic mechanics reused:

- OSGi-style Requirement-Capability resolution;
- existing LSP/Vulkan/OpenAssetIO capability patterns;
- LLVM/MLIR-style compilation/lowering/target legality;
- JSON Schema validation/versioning.

AIMAGE owns only the image capability namespace and image execution-intent vocabulary.

Derived object chain:

`VisualIntentState -> RenderSpec -> RequirementSet + ProviderCapabilityDescriptor -> ResolutionResult -> ExecutionPlan`

**Hard rule:** mandatory intent or preservation requirements may never be silently dropped. Unsupported mandatory semantics require reroute/fallback or an explicit unsatisfied-plan result.

### C — Spatial & Composition Semantics Profile

Generic mechanics reused:

- qualitative spatial reasoning;
- explicit frame of reference;
- OGC/RCC8 topology;
- OpenUSD/Cassowary/CSS transform/constraint/layout patterns already accepted.

AIMAGE owns only the compact image-production profile: useful direction/distance/alignment predicates, viewer/deictic versus subject/intrinsic versus scene/world reference frame, camera/gaze/screen-placement/attention-order semantics that generic spatial calculi do not directly name.

**Hard rule:** viewpoint-sensitive directional relations must carry or inherit an explicit reference frame before execution.

### D — Validation & Domain Profile

Generic mechanics reused:

- SHACL-style separate constraints + structured validation result;
- OPA-style decision/enforcement separation;
- existing plugin/profile and assurance machinery.

AIMAGE/domain packages own only actual visual/domain correctness meaning: character identity, approved composition preservation, exact text, product/logo correctness, storyboard continuity, domain severity/thresholds, etc.

Validation returns a normalized report; it does not mutate the artifact or execute repair itself.

## 6. Final fusion/ownership model

The four families form one loop:

`user intent/references -> A VisualIntent SSoT -> C spatial + D domain profiles -> compile RenderSpec -> B resolve/lower -> provider ExecutionPlan -> artifact/run -> D ValidationReport -> assurance against A baseline -> accept OR repair frame -> B select edit capability -> provider-native edit -> revalidate`

`RenderSpec` is explicitly **demoted from authority to an immutable compiled view**. `ExecutionPlan` is provider-specific. This prevents an external/provider representation from becoming canonical state by convenience.

Approval/repair also collapse into this model:

1. approval baselines selected visual dimensions in A;
2. non-approved dimensions remain mutable;
3. repair diagnostics identify failed dimensions in D;
4. A produces a mutable/preserve frame;
5. B chooses the cheapest legal provider capability;
6. provider executes the actual edit;
7. D checks both repair success and regression against preserved dimensions.

## 7. Acquisition/application boundary for newly added methods

No new mandatory runtime framework is introduced by this re-audit.

- RFC 9315 -> `E/F`, intent/fulfillment/assurance architecture only;
- NIST baseline -> `E/F`, approval/change-control semantics only;
- JML frame conditions -> `E/F`, mutable/preserve specification principle only;
- OSGi Resolver -> `E/F`, requirement/capability model only; **do not add OSGi runtime**;
- QSR/QSTR -> `E/F`, relation/reference-frame ontology evidence;
- OGC RCC8/GeoSPARQL -> `E/F`, useful topological vocabulary; **do not require RDF/GeoSPARQL storage/runtime**;
- W3C SHACL -> `E/F`, validation/profile/report pattern; AIMAGE remains JSON-family by default;
- OPA -> `E/F`, decision/enforcement separation; no runtime unless later measured need justifies it.

Every eventual concrete implementation package remains subject to Assurance Gate B: exact version/ref, license, maintenance/security, coupling, replacement, fallback and AIMAGE-owned contract tests.

## 8. Native AIMAGE design surface after fusion

AIMAGE should not claim ownership of generic intent engines, baseline engines, resolver algorithms, spatial-reasoning frameworks, policy engines or validation engines merely because it adapts their concepts.

The expected irreducible native surface is now mostly **image-production vocabulary/profile content**:

- visual authority dimensions and image-specific precedence meaning;
- image capability namespace/attributes;
- compact image-production spatial predicates/reference-frame conventions not directly supplied by generic calculi;
- image/domain validation rule vocabulary and thresholds;
- mappings from those semantic terms to provider-neutral requirements and validation evidence.

This is an ontology/profile layer over reused generic mechanics, not a new general-purpose computer-science framework.

## 9. Assurance remains accepted and is extended by fusion invariants

`plans/REUSE_AND_INTEGRATION_ASSURANCE.md` remains the top-level verification/validation plan:

- Gate A capability coverage;
- Gate B external acquisition due diligence;
- Gate C ATAM-style architecture scenarios;
- Gate D requirement-traceable integrated workflow simulation, state-transition coverage, combinatorial interaction coverage and fault/regression injection.

The semantic-fusion design must additionally prove:

1. one canonical semantic authority;
2. no silent semantic loss during compile/lowering;
3. baseline/approval cannot mutate without explicit reopen/change control;
4. repair mutates only its authorized frame and regression-checks preserved dimensions;
5. viewpoint-sensitive spatial relations resolve a reference frame;
6. provider replacement does not change authority/approval/domain semantics;
7. validation is separate from enforcement and does not mutate its subject;
8. domain profiles cannot invert `features/domain -> engine interfaces`;
9. RenderSpec/ExecutionPlan identify the semantic state/version from which they were derived;
10. unsatisfied mandatory requirements fail/reroute explicitly;
11. trivial one-shot use remains simple.

## 10. Workflow impact

`plans/WORKFLOW_TARGET.md` remains valid and does not require another stage explosion.

The fusion only clarifies ownership:

- W0-W1 -> A intent/authority + D domain profile;
- W3-W5 -> C spatial semantics and derived blocking artifacts;
- W6 -> A baseline/change-control event;
- W8 -> compile immutable RenderSpec;
- W9 -> B requirement/capability resolution and target lowering;
- W10 -> provider ExecutionPlan;
- W11 -> D ValidationReport;
- W12 -> D diagnosis + A repair frame + B capability choice + provider-native edit;
- W13 -> accepted artifact/finalization;
- W14 -> existing Continuity/Handoff transports identities/state but does not own image semantics.

No extra user-visible ceremony is introduced.

## 11. Exactly one next bounded action after adoption

**Define the minimum provider-neutral schema/contracts for the four semantic families in `plans/SEMANTIC_FUSION_PLAN.md`, then execute a design-only tabletop simulation of the existing canonical Assurance scenarios against those contracts to prove the fusion invariants before any implementation planning.**

This remains one bounded design action: contract definition and immediate design-level simulation are coupled because the schemas are not complete until representative workflows can traverse them without semantic loss or duplicated ownership.

Do **not** select implementation language/runtime packages, install dependencies, write provider/core production code, import external source, or pin concrete library versions during this slice.

## 12. Completion / acceptance criteria for the next action

The next slice is complete only when:

1. the four contract families have minimal objects/fields, owners and non-goals;
2. the image-specific vocabulary is explicitly separated from borrowed generic mechanics;
3. relationships among VisualIntentState, RenderSpec, RequirementSet, ProviderCapabilityDescriptor, ResolutionResult, ExecutionPlan, artifact/run records and ValidationReport are precise and non-duplicative;
4. baseline/change-control and mutable/preserve frame semantics are explicit;
5. reference-frame semantics for directional spatial predicates are explicit;
6. lowering has explicit legality/unsatisfied behavior and cannot silently lose mandatory semantics;
7. validation/decision remains separate from provider enforcement;
8. the design-only simulations cover at least one-shot, composition approval, viewer-relative placement, cross-provider reroute, minimal-delta repair, capability absence, cross-context resume, rejected-artifact resurrection and provider/dependency replacement;
9. all fusion invariants in section 9 pass or blocking contradictions are recorded;
10. the design is independently audited against fresh `main`, `architecture/BOUNDARIES.md`, the reuse/acquisition plan and assurance plan before implementation authorization.

## 13. Expected transition

If the next slice passes, AIMAGE will have a complete provider-neutral semantic contract architecture plus simulated evidence that the contracts survive the intended workflow.

Only after that should a separate implementation-planning slice choose language/runtime and concrete libraries, run Assurance Gate B for each actual dependency, and prepare the first OpenAI vertical slice.

## 14. Stop / replan conditions

Stop/replan if:

- fresh authority materially changes phase/product/reuse boundaries;
- newer work touches the same semantic-fusion surface and makes the next action non-unique;
- tabletop simulation shows two contract families duplicate ownership or cannot preserve user intent;
- a retained AIMAGE semantic is shown to be fully replaced by a mature external primitive after all;
- an accepted acquisition/license/distribution boundary becomes invalid;
- the user changes phase or explicitly authorizes a different next action.
