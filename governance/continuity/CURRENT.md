# AIMAGE Current Repository-Work Continuity

Status: current repository-work continuity locator for the active planning/design/research slice. This file records decision-relevant current state; it does not replace `governance/CONTINUITY.md`, `governance/continuity/REPOSITORY_WORK.md`, root `AGENTS.md`, the handoff skill, or Image Engine specifications.

## 1. Authority snapshot

- Repository: `domato153/aimage`
- Authoritative branch: `main`
- Accepted `main` used as the exact base for this bounded candidate: `49d10e1e8da54e7b42107f12a9b8d964c344054f`
- Bounded work branch: `aimage-stage/semantic-contract-tabletop`
- Governing entrypoint: `AGENTS.md`
- Continuity method: `governance/CONTINUITY.md`
- Repository-work profile: `governance/continuity/REPOSITORY_WORK.md`
- Handoff method: `.agents/skills/handoff/SKILL.md`
- Architecture boundary: `architecture/BOUNDARIES.md`
- Workflow target: `plans/WORKFLOW_TARGET.md`
- Capability reuse classification: `plans/CAPABILITY_REUSE_MATRIX.md`
- External acquisition/integration plan: `plans/EXTERNAL_REUSE_PLAN.md`
- Reuse/integration assurance: `plans/REUSE_AND_INTEGRATION_ASSURANCE.md`
- Accepted semantic fusion plan: `plans/SEMANTIC_FUSION_PLAN.md`
- Semantic contract candidate: `plans/SEMANTIC_CONTRACTS.md`
- Tabletop audit candidate: `audits/SEMANTIC_CONTRACT_TABLETOP_2026-09-10.md`

Fresh repository/platform state always governs current facts. On a work branch, candidate files cannot authorize themselves. If this exact planning set is adopted into current `main`, the merge result becomes accepted authority and future receivers must fresh-reconcile it.

## 2. Current phase and scope

Phase: **planning / design / research only**.

No provider/core production implementation, dependency installation, external-source import, runtime package selection, or provider-version pinning is authorized by this state.

The prior exact next action — define minimum contracts for the four semantic families and immediately tabletop-simulate the canonical assurance scenarios — has now been executed to design decision sufficiency on the bounded candidate.

## 3. Preserved accepted foundation

Do not reopen without new evidence or explicit user scope change:

- thin GPT Project bootstrap -> fresh root `AGENTS.md`;
- AIMAGE-owned Continuity/Handoff with fresh reconciliation and no runtime dependency on historical external repositories;
- Continuity/Handoff separate from Image Engine product semantics;
- dependency direction `features/domain capabilities -> engine interfaces`;
- adaptive `plans/WORKFLOW_TARGET.md`;
- external reuse-first policy and cross-domain abstract-problem search;
- initial provider acquisition direction: OpenAI official SDK/API first, optional Diffusers, optional external ComfyUI;
- provider-native tools perform actual image generation/editing; AIMAGE does not build a custom image editor/repair renderer;
- `plans/REUSE_AND_INTEGRATION_ASSURANCE.md` Gate A-D assurance method;
- `plans/SEMANTIC_FUSION_PLAN.md` four-family architecture using external intent/baseline/resolver/spatial/validation mechanics without forcing those external runtimes into AIMAGE.

## 4. Semantic contract result

`plans/SEMANTIC_CONTRACTS.md` now defines minimum provider-neutral objects, ownership and invariants for the four semantic families.

### Family A — Visual Intent & Authority

Canonical object: `VisualIntentState`.

Supporting semantic records:

- `IntentItem`;
- `AuthorityBinding`;
- `ReferenceBinding`;
- `DecisionRecord`;
- `BaselineRecord`;
- `ArtifactDispositionRecord`;
- derived `MutationFrame`.

Key decisions:

- `VisualIntentState` is the only semantic SSoT;
- explicit user decisions/baselines cannot be silently replaced by provider limitations or derived artifacts;
- approvals/rejections are revision-bound and idempotent;
- rejected/superseded artifact disposition is explicit;
- repairs use frame-condition semantics: only authorized paths are mutable, approved unspecified paths default preserved.

### Family C — Spatial & Composition Profile

Canonical semantic profile object: `SpatialProfile` with semantic entities, explicit reference frames and qualitative relations.

Key decisions:

- `viewer_deictic`, `subject_intrinsic`, `scene_world`, and `screen_image` frames are distinct;
- viewpoint-sensitive direction must carry/inherit an explicit frame;
- provider prompt/blocking/pose/depth/control artifacts are lowerings, never spatial authority;
- AIMAGE adds only compact image-specific terms such as gaze, foreground/background, screen-region and attention-order semantics over mature spatial primitives.

### Family D — Validation & Domain Profile

Objects:

- `DomainProfile` / `ValidationRule`;
- immutable `ValidationReport` / `ValidationResult`.

Key decisions:

- validation is separate from provider enforcement/mutation;
- reports are tied to exact artifact, semantic revision, RenderSpec/ExecutionPlan and profile versions;
- validation is tri-state (`pass`, `fail`, `indeterminate`) so a mandatory rule that cannot be evaluated cannot silently become success;
- domain packages own actual image/domain correctness meaning but cannot redefine engine authority or continuity semantics.

### Family B — Requirement, Capability & Lowering

Objects:

- immutable compiled `RenderSpec`;
- `RequirementSet` / `CapabilityRequirement`;
- `ProviderCapabilityDescriptor`;
- `ResolutionResult`;
- provider/tool `ExecutionPlan` with `LoweringTrace`.

Key decisions:

- mandatory semantic requirements must be satisfied or explicitly unresolved;
- `ResolutionResult` selects a capability-satisfying **strategy**, potentially a small multi-target composition rather than only one provider;
- this supports cases such as image generation followed by deterministic text composition without inventing a general workflow engine;
- `LoweringTrace` records exact / within-declared-tolerance / not-representable mappings;
- mandatory semantics may never lower to `not_representable`, and tolerance is legal only when the source semantic explicitly allowed it;
- stale capability descriptors cause re-resolution where material.

## 5. Cross-family ownership model

Accepted planning direction after the tabletop:

`VisualIntentState -> Spatial/Domain profiles -> RenderSpec -> RequirementSet -> capability strategy resolution -> ExecutionPlan -> provider/tool execution -> Artifact/Run -> ValidationReport -> accept OR MutationFrame -> re-resolution/edit -> revalidate`

Authority separation:

- `VisualIntentState` = canonical desired state;
- `RenderSpec` = immutable compiled semantic snapshot;
- `ResolutionResult` = legal target-strategy decision;
- `ExecutionPlan` = provider/tool-specific lowering;
- provider requests/conversation IDs/graphs = execution evidence;
- artifact/run records = lineage/provenance;
- validation reports = decision evidence;
- Continuity/Handoff = cross-context transport/reconciliation only.

## 6. Tabletop audit result

Companion evidence: `audits/SEMANTIC_CONTRACT_TABLETOP_2026-09-10.md`.

Bounded design verdict: **PASS AFTER DESIGN REPAIR**.

The first tabletop pass found four real contract gaps and repaired them before the final pass:

1. single-provider-only resolution could not represent composite capability strategies;
2. decisions needed base-semantic-revision binding and idempotency;
3. rejected/superseded artifact disposition needed explicit durable semantics;
4. binary validation could incorrectly treat unevaluable mandatory checks as success.

After repair, the candidate design successfully represents:

- one-shot flow;
- composition exploration/partial approval;
- user blocking authority;
- cross-provider reroute;
- minimal-delta repair with preservation regression checks;
- role-separated reference replacement;
- missing mandatory capability/fallback;
- deterministic text-layout composite strategy;
- cross-context resume;
- schema migration semantics;
- optional backend loss;
- optional provenance export;
- rejected-artifact non-resurrection;
- duplicate/late approval safety;
- dependency/provider replacement;
- viewer-relative `right_of` + `same_row` placement with explicit reference frames.

No semantic ownership conflict or architecture-blocking contradiction remained after the repairs.

## 7. Assurance status

### Gate A — semantic/capability coverage

**PASS for this bounded design slice.**

### Gate B — concrete external acquisition due diligence

**Not executed by design.** No concrete implementation language/library/provider version was selected in this slice. Gate B remains mandatory before integrating each actual dependency.

### Gate C — architecture scenarios

**PASS at design/tabletop level**, subject to implementation evidence.

### Gate D — final integrated workflow V&V

**Design coverage only.** The contracts can represent the canonical scenarios, but real provider execution, contract tests, combinatorial interaction coverage and fault injection remain future implementation evidence. A final system `PASS` is not claimed.

## 8. Semantic architecture invariants now fixed

The next phases must preserve:

1. one semantic SSoT;
2. exact semantic-revision traceability for derived objects;
3. no silent loss of mandatory intent/preservation during compilation/resolution/lowering;
4. controlled baseline reopen/change;
5. repair mutation only inside the authorized frame plus regression validation of preserved dimensions;
6. explicit reference frame for viewpoint-sensitive spatial relations;
7. validation/decision separated from enforcement/execution;
8. provider-native state never becoming authority;
9. feature/domain -> engine dependency direction;
10. revision-bound idempotent decisions and stale-decision rejection;
11. rejected artifact non-resurrection;
12. tri-state mandatory validation safety;
13. legal composite capability strategies;
14. simple one-shot path;
15. immutable historical evidence.

## 9. Deliberately deferred implementation questions

These are no longer semantic-architecture gaps, but must be decided/audited before or during implementation planning:

- implementation language/runtime;
- exact JSON Schema validator/migration library;
- exact metadata/blob storage implementation;
- exact optional constraint-solver package if required;
- provider SDK/model/version choices and empirically reproduced capability descriptors;
- concrete image/spatial/domain validation evaluators and calibration;
- provider-specific attainable preservation fidelity;
- quantitative domain QA thresholds.

## 10. Exactly one next bounded action after adoption

**Prepare and independently audit the implementation plan only: choose the implementation language/runtime and minimum concrete packages, execute Assurance Gate B for every actual dependency/provider integration, map repository/modules and contract tests directly to the accepted semantic contracts, and define the first thin OpenAI vertical slice covering one-shot, composition approval, viewer-relative placement, provider reroute/failure behavior, and minimal-delta repair. Do not begin production implementation during that planning slice.**

## 11. Completion / acceptance criteria for the next action

The implementation-planning slice is complete only when:

1. language/runtime choice is justified against semantic contracts, provider SDKs, local/optional backend needs, testing and maintainability;
2. every selected dependency has exact acquisition mode, license/provenance, version-selection policy, coupling, fallback/replacement and AIMAGE-owned contract-test obligations under Gate B;
3. no dependency is selected merely because an external method inspired the architecture;
4. module/repository boundaries preserve `features/domain -> engine interfaces` and keep provider-native state below the semantic layer;
5. concrete schemas/types map one-to-one to `plans/SEMANTIC_CONTRACTS.md` without inventing competing owners;
6. contract-test inventory covers the semantic invariants and the four tabletop repairs;
7. first OpenAI vertical slice is thin but end-to-end and does not prematurely require optional Diffusers/ComfyUI;
8. exact implementation stop/go criteria and rollback/fallback boundaries are explicit;
9. the complete implementation plan is independently audited against fresh `main`, `architecture/BOUNDARIES.md`, external-reuse plans, semantic contracts and assurance gates;
10. implementation remains unauthorized until that audit passes and current user authority allows the phase transition.

## 12. Expected transition

If the next planning slice passes, AIMAGE will have:

- provider-neutral semantic architecture fixed;
- design-tabletop evidence for intended workflow semantics;
- concrete implementation/runtime/dependency plan with Gate-B evidence;
- a bounded first vertical-slice implementation target.

Only then should production implementation begin under a separate authorized implementation slice.

## 13. Stop / replan conditions

Stop/replan if:

- fresh authority materially changes the product/phase/reuse boundary;
- newer work touches the same implementation-planning surface and makes the next action non-unique;
- implementation research shows a selected runtime/package cannot preserve the semantic contracts;
- Gate B exposes a license/security/maintenance/coupling problem requiring another architecture choice;
- a provider capability required by the first vertical slice cannot be reproduced or safely approximated;
- the user changes phase or explicitly authorizes a different next action.
