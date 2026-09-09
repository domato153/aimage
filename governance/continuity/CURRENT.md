# AIMAGE Current Repository-Work Continuity

Status: current repository-work continuity locator for the active implementation-planning preparation. This file records decision-relevant current state; it does not replace `governance/CONTINUITY.md`, `governance/continuity/REPOSITORY_WORK.md`, root `AGENTS.md`, the handoff skill, or Image Engine specifications.

## 1. Authority / locator status

- Repository: `domato153/aimage`
- Authoritative branch: `main`
- Current factual `main` HEAD: **resolve fresh at receiver start**. Do not try to make this self-referential file encode its own eventual publication SHA.
- Last reconciled accepted repository tree before this CURRENT repair: tree `f8c5c612eede55f0ea53de6d6ba61db0b5647e44`.
- Canonical implementation-planning handoff packet:
  - immutable commit: `ecfeef00d830d65e9235832adf05b1c21d2bfc16`
  - path: `governance/continuity/handoffs/IMPLEMENTATION_PLANNING_NEXT_THREAD_2026-09-10.md`
- Governing entrypoint: `AGENTS.md`
- Handoff method: `.agents/skills/handoff/SKILL.md`
- Continuity method: `governance/CONTINUITY.md`
- Repository-work profile: `governance/continuity/REPOSITORY_WORK.md`
- Architecture boundary: `architecture/BOUNDARIES.md`
- Workflow target: `plans/WORKFLOW_TARGET.md`
- Capability reuse classification: `plans/CAPABILITY_REUSE_MATRIX.md`
- External acquisition/integration plan: `plans/EXTERNAL_REUSE_PLAN.md`
- Base assurance plan: `plans/REUSE_AND_INTEGRATION_ASSURANCE.md`
- Bounded adversarial assurance: `plans/BOUNDED_RED_TEAM_ASSURANCE.md`
- Semantic fusion plan: `plans/SEMANTIC_FUSION_PLAN.md`
- Accepted semantic contracts: `plans/SEMANTIC_CONTRACTS.md`
- Accepted semantic tabletop evidence: `audits/SEMANTIC_CONTRACT_TABLETOP_2026-09-10.md`
- Accepted bounded plan red-team evidence: `audits/BOUNDED_PLAN_RED_TEAM_2026-09-10.md`
- Handoff cross-method review evidence: `audits/HANDOFF_CROSS_METHOD_AUDIT_2026-09-10.md`

Fresh repository/platform state always governs current facts. Historical construction SHAs inside immutable packets/audits are provenance, not aliases for current `main`.

## 2. Current phase and authorization

Phase: **planning / design / research only**.

The next bounded phase is **implementation planning**, not implementation.

Authorized:

- fresh reconciliation;
- official/upstream research needed for runtime/dependency/provider selection;
- bounded non-production reproduction/probing only when strictly needed for Gate B and allowed by current authority;
- implementation architecture planning;
- Gate-B due diligence;
- concrete module/type/schema/test planning;
- first thin OpenAI vertical-slice planning;
- bounded red-team and independent plan audit;
- continuity/planning updates needed to preserve the accepted result.

Not authorized:

- production Image Engine/provider implementation;
- dependency installation or lockfile mutation;
- external source import/copy;
- live provider integration as production work;
- silently reopening accepted semantic architecture;
- treating a finished implementation plan as self-authorization to code.

## 3. Accepted foundation — do not redo without new evidence

The following remain accepted unless fresh authority or implementation evidence exposes a concrete contradiction:

- thin GPT Project bootstrap -> fresh root `AGENTS.md`;
- AIMAGE-owned Continuity/Handoff with fresh reconciliation;
- Continuity/Handoff remains separate from Image Engine product semantics;
- product dependency direction remains `features/domain capabilities -> engine interfaces`;
- adaptive workflow preserves trivial one-shot simplicity;
- provider/backend-native capabilities perform actual image generation/editing; AIMAGE does not build a custom image-edit renderer;
- first hosted provider direction remains OpenAI official SDK/API;
- Diffusers remains an optional local-provider direction;
- ComfyUI remains an optional external backend/service direction;
- broad external-reuse and cross-domain semantic search is closed at planning level unless a concrete measured gap reopens it;
- mature external methods are generally reused as method/schema/reference patterns rather than forced runtime dependencies;
- provider-neutral semantic architecture is four coherent contract families rather than custom generic frameworks;
- `VisualIntentState` is the sole semantic SSoT;
- `RenderSpec`, `RequirementSet`, `ResolutionResult`, `ExecutionPlan`, provider-native payloads/IDs/graphs, artifact/run records and validation reports are derived/evidence state;
- semantic tabletop verdict is `PASS AFTER DESIGN REPAIR`;
- bounded semantic-plan red-team verdict is `PASS AFTER ASSURANCE HARDENING`;
- bounded Red-Team Challenge is a cross-cutting falsification step over Gate A-D, not Gate E and not a runtime subsystem;
- final Gate-D integrated runtime V&V has **not** happened and no final system PASS is claimed.

## 4. Fixed semantic / authority invariants

Implementation planning must preserve:

1. one semantic SSoT (`VisualIntentState`);
2. exact semantic-revision traceability for derived objects;
3. no silent loss/softening of mandatory intent or preservation obligations during compile, resolution, lowering, fallback, repair or provider replacement;
4. approved baselines change only through explicit reopen/supersession;
5. decisions are revision-bound and idempotent; stale/late decisions cannot overwrite newer state;
6. rejected/superseded artifacts cannot resurrect through recency/resume;
7. repair mutates only inside the authorized `MutationFrame` and regression-checks preserved dimensions;
8. viewpoint-sensitive spatial relations use explicit/inherited reference frames; `viewer_deictic`, `subject_intrinsic`, `scene_world` and `screen_image` are not aliases;
9. validation remains separate from enforcement/mutation and mandatory unevaluable checks remain `indeterminate` rather than pass;
10. provider-native state never becomes semantic authority;
11. domain packages depend on engine interfaces and cannot redefine core authority;
12. historical plans/reports remain immutable evidence;
13. composite execution may be legal but `ExecutionPlan` remains bounded, attempt-local and acyclic;
14. trivial one-shot use must not inherit unnecessary planning/audit ceremony.

## 5. Accepted red-team hardening obligations

The implementation plan must explicitly cover all eight:

1. **Fail-closed semantic compilation** — contradictory/incomplete mandatory semantics cannot produce a legal executable `RenderSpec`/`RequirementSet`.
2. **Currentness fence** — old in-flight artifacts/reports/decisions cannot become current merely because they finish later than a newer semantic revision.
3. **Conditional capability matching** — mandatory resolution matches exact target/model/version/applicability/limits/evidence, not only a capability name.
4. **Validation-oracle challenge** — evaluator identity/provenance/correlation/calibration and acceptable evidence class are visible where material.
5. **Bounded repair** — non-improvement/oscillation detection, bounded attempt/cost or equivalent stop policy, best-known artifact retention, and escalation.
6. **Bounded composite execution** — `ExecutionPlan` remains attempt-local/acyclic; human waits, durable resume and repair loops stay in generic lifecycle/orchestration.
7. **Final-artifact regression validation** — preservation obligations are checked on the final externally visible composite result, not only intermediate steps.
8. **Capability-drift race handling** — material capability changes after resolution trigger freshness/compatibility check, re-resolution or bounded failure before semantic degradation.

## 6. Handoff / recoverability status

Canonical packet publication is complete and immutable at `ecfeef00...` + the path in section 1.

Decision-relevant state required for the next action is **DURABLE** in repository authority. No hidden chat-local, provider-session-only, cache-only, or machine-local artifact is required for continuation.

The packet's embedded construction snapshot is intentionally historical. Receiver currentness must come from fresh `main`, current governing methods, CURRENT, and bounded discovery for newer work touching the same implementation-planning/runtime/dependency/semantic/provider/red-team boundary.

Cross-method audit result:

- I-PASS/SBAR structured-handoff coverage: PASS;
- ReqIF-style cross-boundary semantic interchange: PASS without adopting ReqIF runtime/schema;
- NASA requirements traceability: PASS, with a nonblocking recommendation for future dense prompt derivatives to run a lightweight semantic-equivalence check;
- NASA configuration status accounting: stale CURRENT metadata was the one concrete defect and this update repairs it;
- optimistic-concurrency/currentness analogy: existing fresh reconciliation + revision fencing is adequate;
- full GSN assurance graph for handoff is rejected as unnecessary ceremony.

## 7. Exactly one next bounded action

**Prepare and independently audit one concrete implementation plan only.**

The planning action must:

1. choose and justify implementation language/runtime;
2. select the minimum concrete dependency set;
3. execute Assurance Gate B for every actual dependency/provider integration using fresh official/upstream evidence;
4. map repository/modules and concrete schemas/types directly to `plans/SEMANTIC_CONTRACTS.md` while preserving `features/domain -> engine interfaces` and keeping provider-native state below the semantic layer;
5. define a thin end-to-end first OpenAI vertical slice covering one-shot, composition approval/baseline, viewer-relative placement, RenderSpec compile, capability resolution/lowering, execution/artifact/run linkage, validation, explicit provider failure/reroute/unsatisfied behavior and minimal-delta repair;
6. define contract/integration tests for fixed semantic invariants, the four tabletop repairs and the eight red-team hardening obligations;
7. define stop/go, rollback/fallback and provider/dependency replacement boundaries;
8. run `plans/BOUNDED_RED_TEAM_ASSURANCE.md` against the completed implementation plan, repair material findings, then rerun only affected lenses;
9. independently audit the final plan against fresh `main`, `architecture/BOUNDARIES.md`, external-reuse/assurance plans, semantic contracts and concurrent work;
10. update planning/continuity authority only if the planning candidate passes and current user authority allows adoption.

Do **not** begin production implementation in this slice.

## 8. Completion / acceptance criteria

Implementation planning is complete only when:

1. runtime/language selection has comparative justification;
2. every selected concrete dependency/provider integration has Gate-B evidence with no blocking `UNRESOLVED` item;
3. concrete module/type/schema ownership maps cleanly to accepted semantic contracts without a competing semantic owner;
4. provider-native IDs/payloads remain execution/evidence state only;
5. the first OpenAI vertical slice is genuinely thin and end-to-end and does not require optional Diffusers/ComfyUI to prove the core path;
6. test inventory covers accepted semantic invariants, the prior tabletop repairs, and all eight red-team obligations;
7. stop/go, rollback/fallback and replacement boundaries are explicit;
8. implementation-plan red-team returns `PASS` or `PASS_AFTER_REPAIR`;
9. fresh independent repository/architecture audit finds no conflicting newer work or boundary inversion;
10. the result is preserved in repository planning/continuity state;
11. production implementation has still not begun.

Evidence-sufficiency exit condition: once concrete runtime/dependency/module/test/vertical-slice choices meet these criteria and the remaining uncertainties are explicit implementation-time empirical checks that do not change architecture, stop planning. Do not continue research for bibliography completeness.

## 9. Expected transition

If the next planning slice passes, AIMAGE will have:

- fixed provider-neutral semantic architecture;
- accepted tabletop + adversarial design evidence;
- concrete runtime/language and minimum dependency plan;
- Gate-B records for selected dependencies/provider integration;
- concrete module/schema/test layout;
- one bounded first OpenAI vertical-slice target;
- explicit defenses/tests for the retained adversarial attack classes.

Production implementation begins only in a separate user-authorized implementation slice.

## 10. Stop / replan conditions

Return `STALE_REPLAN` or stop/replan if:

- fresh authority or a governing method materially changes so the implementation-planning action is no longer unique;
- newer open PR/active work touches the same implementation-planning/runtime/dependency/provider/semantic/red-team boundary and changes ordering or ownership;
- a selected runtime/package cannot preserve accepted semantic contracts without leakage or architecture inversion;
- Gate B finds a material license/security/provenance/maintenance/replacement/coupling blocker;
- a provider capability essential to the first vertical slice cannot be reproduced or safely represented and no legal explicit fallback exists;
- bounded red-team finds an unrepaired `BLOCKING` issue;
- the user changes phase or scope.

Harmless movement in unrelated branches/docs does not invalidate the route.
