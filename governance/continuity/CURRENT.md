# AIMAGE Current Repository-Work Continuity

Status: current repository-work continuity locator for the active planning/design/research slice. This file records decision-relevant current state; it does not replace `governance/CONTINUITY.md`, `governance/continuity/REPOSITORY_WORK.md`, root `AGENTS.md`, the handoff skill, or Image Engine specifications.

## 1. Authority snapshot

- Repository: `domato153/aimage`
- Authoritative branch: `main`
- Fresh accepted `main` used as the exact base for this bounded red-team candidate: `69e51bd3b250a20a9268a6c858a82b5862933297`
- Bounded work branch: `aimage-stage/bounded-red-team-assurance`
- Governing entrypoint: `AGENTS.md`
- Continuity method: `governance/CONTINUITY.md`
- Repository-work profile: `governance/continuity/REPOSITORY_WORK.md`
- Handoff method: `.agents/skills/handoff/SKILL.md`
- Architecture boundary: `architecture/BOUNDARIES.md`
- Workflow target: `plans/WORKFLOW_TARGET.md`
- Capability reuse classification: `plans/CAPABILITY_REUSE_MATRIX.md`
- External acquisition/integration plan: `plans/EXTERNAL_REUSE_PLAN.md`
- Base assurance plan: `plans/REUSE_AND_INTEGRATION_ASSURANCE.md`
- Semantic fusion plan: `plans/SEMANTIC_FUSION_PLAN.md`
- Accepted semantic contracts: `plans/SEMANTIC_CONTRACTS.md`
- Accepted semantic tabletop audit: `audits/SEMANTIC_CONTRACT_TABLETOP_2026-09-10.md`
- Red-team assurance extension candidate: `plans/BOUNDED_RED_TEAM_ASSURANCE.md`
- Current bounded red-team audit candidate: `audits/BOUNDED_PLAN_RED_TEAM_2026-09-10.md`

Fresh repository/platform state always governs current facts. Candidate files cannot authorize themselves. If this exact bounded planning set is adopted, the merge result becomes the new accepted factual base and the next receiver must fresh-reconcile it.

## 2. Current phase and authorization

Phase: **planning / design / research only**.

No provider/core production implementation, dependency installation, external-source import, runtime package selection, provider-version pinning, or production execution is authorized by this state.

The previously accepted semantic-contract/tabletop slice remains valid. The current user-authorized bounded action was to red-team the plan from multiple angles, decide whether adversarial review belongs in the real assurance flow, and integrate it if appropriate.

That bounded action has now been executed to decision sufficiency on the candidate.

## 3. Preserved accepted foundation

Do not reopen without new evidence or explicit scope change:

- thin GPT Project bootstrap -> fresh root `AGENTS.md`;
- AIMAGE-owned Continuity/Handoff with fresh reconciliation;
- Continuity/Handoff separate from Image Engine product semantics;
- dependency direction `features/domain capabilities -> engine interfaces`;
- adaptive `plans/WORKFLOW_TARGET.md` with one-shot simplicity;
- evidence-first external reuse and abstract-problem cross-domain search;
- provider-native generation/editing performs actual image manipulation; AIMAGE does not build a custom image editor;
- initial provider direction: OpenAI official SDK/API first, optional Diffusers, optional external ComfyUI;
- existing Gate A-D assurance in `plans/REUSE_AND_INTEGRATION_ASSURANCE.md`;
- four-family provider-neutral semantic architecture in `plans/SEMANTIC_FUSION_PLAN.md`;
- provider-neutral contracts in `plans/SEMANTIC_CONTRACTS.md`;
- semantic tabletop verdict `PASS AFTER DESIGN REPAIR` with the four earlier repaired gaps: composite capability strategies, revision-bound/idempotent decisions, explicit artifact disposition, and tri-state validation.

## 4. Semantic architecture remains accepted

The bounded red team did **not** find a new architecture-blocking contradiction requiring another semantic family or runtime framework.

The accepted ownership model remains:

`VisualIntentState -> Spatial/Domain profiles -> RenderSpec -> RequirementSet -> capability-strategy resolution -> ExecutionPlan -> provider/tool execution -> Artifact/Run -> ValidationReport -> accept OR MutationFrame -> re-resolution/edit -> revalidate`

Fixed authority rules remain:

- `VisualIntentState` is the semantic SSoT;
- RenderSpec/ResolutionResult/ExecutionPlan are derived;
- provider-native state never becomes semantic authority;
- decisions are revision-bound/idempotent;
- rejected artifacts cannot resurrect through recency/resume;
- mandatory semantics cannot silently disappear in compile/resolution/lowering;
- repair stays within its authorized MutationFrame and regression-checks preserved dimensions;
- viewpoint-sensitive spatial relations require an explicit/inherited frame;
- validation is tri-state and separate from enforcement;
- domain content depends on engine interfaces rather than redefining core authority.

## 5. Bounded red-team result

Companion evidence: `audits/BOUNDED_PLAN_RED_TEAM_2026-09-10.md`.

Verdict: **PASS AFTER ASSURANCE HARDENING**.

The review intentionally combined lightweight top-down/bottom-up/control-action/tradeoff lenses based on NASA SFTA/FMEA, MIT STPA and the already accepted SEI ATAM approach. These are method/reference inputs only.

The red team found that the accepted contracts can represent the attacked cases, but the assurance flow needed an explicit pre-adoption adversarial challenge rather than relying only on representative scenario coverage.

### Material hardening obligations exposed

1. **Fail-closed semantic compilation** — contradictory/incomplete mandatory semantics must not produce a legal executable RenderSpec/RequirementSet.
2. **Currentness fence** — old in-flight artifacts/reports/decisions cannot become current merely because they finish later than a newer semantic revision.
3. **Conditional capability matching** — mandatory resolution must match exact target/model/version/applicability/limits/evidence, not only a capability name.
4. **Validation-oracle challenge** — evaluator identity/provenance/correlation/calibration must be visible for material mandatory validation; provider self-report is not silently independent proof.
5. **Bounded repair policy** — detect non-improvement/oscillation and stop/escalate under a bounded attempt/cost policy while retaining best-known good work.
6. **Bounded composite execution** — ExecutionPlan remains attempt-local and acyclic; human waits, repair loops and resume belong to the generic lifecycle/orchestration layer.
7. **Final-artifact regression validation** — preservation obligations apply after the complete composite strategy, not only individual steps.
8. **Capability-drift race handling** — material capability changes after resolution require freshness check/re-resolution or bounded failure before execution.

These are mostly implementation-plan/test obligations, not reasons to add new semantic subsystems.

## 6. Attacks explicitly checked

The bounded audit challenged at least:

- contradictory equally authoritative mandatory intent;
- old rev-N render/validation finishing after rev-N+1 exists;
- provider capability name matching while exact operating conditions do not;
- generator/provider effectively grading its own output;
- repair oscillation/cost growth;
- composite strategy expanding into a second workflow engine;
- late compositor/finishing step regressing locked geometry;
- lock/baseline accumulation making the job unsatisfiable;
- domain plugin attempting to become core authority;
- provider capability changing after resolution but before execution;
- schema migration dropping unknown mandatory semantics;
- assurance ceremony destroying the trivial one-shot path.

No new semantic ownership conflict remained after applying the hardening rules above.

## 7. Assurance-flow decision

The red-team method is appropriate and is now represented by `plans/BOUNDED_RED_TEAM_ASSURANCE.md` as a **cross-cutting extension** of the existing Gate A-D system.

It does not create Gate E or a runtime subsystem.

### Trigger

Required:

- before adopting a material architecture/semantic-contract change;
- before authorizing implementation from an implementation plan;
- before final integrated system `PASS`;
- after a material provider/dependency/authority-boundary change invalidates prior assumptions.

Not required for ordinary low-risk documentation edits, trivial image jobs, every provider call, or every repair attempt.

### Method

Applicable reviews challenge six lenses:

1. top-event/authority failure;
2. component/interface failure propagation;
3. missing/duplicate/late/stale/out-of-order control actions;
4. evidence/oracle failure;
5. tradeoff/complexity failure;
6. replacement/resume/in-flight race failure.

Findings are classified `BLOCKING`, `REPAIR_BEFORE_ADOPTION`, `DEFERRED_IMPLEMENTATION_RISK`, or `REJECTED_ATTACK`.

Run one bounded pass, repair material findings, then rerun only affected lenses once. Continue further only if a materially new failure class appears. The objective is decision sufficiency, not attack-count completeness.

## 8. Anti-overengineering decision

The red team explicitly rejected adding:

- a fault-tree/FMEA/STPA runtime or general analysis engine;
- formal hazard analysis for every image request;
- a second semantic authority for adversarial state;
- mandatory independent-human validation for every artifact;
- another workflow engine inside ExecutionPlan;
- arbitrary security/audit gates unrelated to demonstrated AIMAGE invariants.

Preferred mitigation order is:

1. prove an existing contract blocks the attack;
2. add a contract/integration test;
3. add a small invariant/failure rule;
4. add bounded implementation policy;
5. only then change architecture.

## 9. Assurance status after red team

### Gate A — semantic/capability coverage

Previously **PASS** for the bounded semantic design. No new uncovered semantic family was found.

### Gate B — concrete acquisition due diligence

Still **not executed by design** for implementation dependencies. It remains mandatory in implementation planning.

### Gate C — architecture scenarios

Previously **PASS at design/tabletop level**. The red team adds adversarial falsification but does not replace Gate C.

### Cross-cutting bounded Red-Team Challenge

**PASS AFTER ASSURANCE HARDENING** for the currently accepted semantic architecture.

### Gate D — final integrated V&V

Still **design coverage only**. Retained red-team attacks must become concrete implementation tests/fault injections/combinatorial factors where applicable. Final system PASS is not claimed.

## 10. Exactly one next bounded action after adoption

**Prepare and independently audit the implementation plan only: choose the implementation language/runtime and minimum concrete packages, execute Assurance Gate B for every actual dependency/provider integration, map repository/modules and contract tests directly to the accepted semantic contracts, define the first thin OpenAI vertical slice, and run the bounded Red-Team Challenge against that implementation plan before any production implementation authorization.**

The first implementation plan must cover one-shot, composition approval, viewer-relative placement, provider reroute/failure behavior and minimal-delta repair, plus the eight red-team hardening obligations in section 5.

Do **not** begin production implementation during that planning slice.

## 11. Completion / acceptance criteria for the next action

The implementation-planning slice is complete only when:

1. language/runtime choice is justified against semantic contracts, provider SDKs, optional local/backend needs, testing and maintainability;
2. every selected dependency has exact acquisition mode, license/provenance, version-selection policy, coupling, fallback/replacement and AIMAGE-owned contract-test obligations under Gate B;
3. no dependency is selected merely because an external method inspired the architecture;
4. module boundaries preserve `features/domain -> engine interfaces` and provider-native state below the semantic layer;
5. concrete schemas/types map one-to-one to `plans/SEMANTIC_CONTRACTS.md` without competing owners;
6. contract tests cover all fixed semantic invariants and prior tabletop repairs;
7. implementation-plan tests/policies explicitly cover fail-closed compilation, currentness fencing, exact capability applicability/evidence, evaluator provenance/calibration, bounded repair, bounded attempt-local ExecutionPlan, final-artifact regression and capability-drift races;
8. the first OpenAI vertical slice is thin/end-to-end and does not prematurely require optional Diffusers/ComfyUI;
9. exact implementation stop/go and rollback/fallback boundaries are explicit;
10. the complete implementation plan passes ordinary Gate-B/C-relevant audit plus `plans/BOUNDED_RED_TEAM_ASSURANCE.md` with verdict `PASS` or `PASS_AFTER_REPAIR`;
11. a fresh independent repository/architecture audit finds no conflicting newer work or boundary inversion;
12. implementation remains unauthorized until that planning/audit slice is adopted and current user authority explicitly allows implementation.

## 12. Expected transition

If the next bounded planning slice passes, AIMAGE will have:

- fixed provider-neutral semantic architecture;
- tabletop and adversarial design evidence;
- concrete implementation/runtime/dependency plan with Gate-B evidence;
- explicit red-team defenses/tests;
- one bounded first OpenAI vertical-slice implementation target.

Only then should production implementation begin under a separate authorized implementation slice.

## 13. Stop / replan conditions

Stop/replan if:

- fresh authority materially changes product/phase/reuse boundaries;
- newer work touches the same implementation-planning/red-team surface and makes the next action non-unique;
- implementation research shows a selected runtime/package cannot preserve semantic contracts;
- Gate B exposes a license/security/maintenance/coupling problem requiring architecture change;
- bounded red-team finds a `BLOCKING` failure that cannot be repaired within the implementation plan;
- a provider capability required by the first vertical slice cannot be reproduced or safely approximated;
- the user changes phase or explicitly authorizes a different next action.
