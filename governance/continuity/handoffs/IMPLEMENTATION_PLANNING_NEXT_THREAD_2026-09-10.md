# AIMAGE Implementation-Planning Next-Thread Handoff — 2026-09-10

Status: canonical repository-work handoff packet for the next bounded AIMAGE planning slice. This packet is continuity evidence, not project authority. Fresh AIMAGE `main`, current governing methods, and current user authorization always control.

## Operational Header

- Repository: `domato153/aimage`
- Construction authority snapshot: `main = 76a8ce92f743e49fff5434390c2c08cd64cba0b9`
- Canonical packet path: `governance/continuity/handoffs/IMPLEMENTATION_PLANNING_NEXT_THREAD_2026-09-10.md`
- Immediate objective: prepare and independently audit the concrete AIMAGE implementation plan.
- Phase: **planning / design / research only**.
- Stop boundary: **do not begin production implementation, install dependencies, import external source, or integrate providers during this slice**.
- Exact next bounded action: choose the implementation runtime/language and minimum concrete dependencies, execute Gate B for each actual dependency/provider integration, map implementation modules/types/tests to the accepted semantic contracts, define the first thin OpenAI vertical slice, and run the bounded Red-Team Challenge against the completed implementation plan.
- Completion criterion: one implementation plan is decision-complete, Gate-B-audited, red-team-audited, independently reconciled against fresh architecture/continuity authority, and ready for a separate explicit implementation-authorization slice.
- Stop/replan trigger: fresh authority or concurrent work makes the next action non-unique; a selected dependency/runtime cannot preserve accepted semantic contracts; Gate B exposes a blocking license/security/maintenance/coupling issue; or red-team finds an unrepaired blocking failure.

The immutable publication commit for this packet is supplied by the derived next-thread paste prompt after adoption, because a Git commit cannot encode its own final commit hash inside its content. The receiver must use that exact commit + path as the canonical packet locator, not a floating `main` alias.

## 1. Immediate objective

Do **implementation planning only** for the first executable AIMAGE slice. The purpose is to turn the already accepted provider-neutral architecture into one concrete, auditable build plan without reopening settled semantic design or crossing into production implementation.

## 2. Current phase and authorized scope

Authorized now:

- fresh repository reconciliation;
- current web/official-source research needed to choose runtime/libraries/provider SDKs;
- implementation architecture planning;
- Gate-B acquisition due diligence for concrete dependency candidates;
- module/type/schema/test mapping;
- first vertical-slice definition;
- bounded red-team and independent plan audit;
- planning/continuity documentation needed to preserve the result.

Not authorized in this packet:

- production Image Engine/provider code;
- package installation or lockfile mutation;
- external source import/copy;
- live provider integration as product implementation;
- concrete implementation beyond small non-production research/reproduction evidence strictly needed for Gate B, if current authority explicitly permits it;
- promotion to implementation phase merely because the plan becomes obvious.

## 3. Fresh authority snapshot at handoff construction

Fresh observed authoritative branch at construction:

`main = 76a8ce92f743e49fff5434390c2c08cd64cba0b9`

Construction-time open-PR discovery found no open PR touching the exact implementation-planning/red-team continuation surface. The receiver must repeat bounded discovery because this fact can become stale.

Current governing/read surfaces:

1. `AGENTS.md`
2. `.agents/skills/handoff/SKILL.md`
3. `governance/CONTINUITY.md`
4. `governance/continuity/REPOSITORY_WORK.md`
5. `governance/continuity/CURRENT.md`
6. `architecture/BOUNDARIES.md`
7. `plans/WORKFLOW_TARGET.md`
8. `plans/CAPABILITY_REUSE_MATRIX.md`
9. `plans/EXTERNAL_REUSE_PLAN.md`
10. `plans/REUSE_AND_INTEGRATION_ASSURANCE.md`
11. `plans/BOUNDED_RED_TEAM_ASSURANCE.md`
12. `plans/SEMANTIC_FUSION_PLAN.md`
13. `plans/SEMANTIC_CONTRACTS.md`
14. `audits/SEMANTIC_CONTRACT_TABLETOP_2026-09-10.md`
15. `audits/BOUNDED_PLAN_RED_TEAM_2026-09-10.md`

Do not assume the construction SHA remains current. Fresh repository/platform state wins.

## 4. Current situation

Confirmed:

- the broad external-reuse search and acquisition architecture is already closed at planning level;
- provider-neutral semantic architecture is reduced to four coherent contract families rather than custom generic frameworks;
- `VisualIntentState` is the sole semantic SSoT;
- `RenderSpec`, `RequirementSet`, `ResolutionResult`, `ExecutionPlan`, provider-native requests/IDs/graphs, artifact/run records, and validation reports are derived/evidence objects, not user-intent authority;
- semantic tabletop passed **after design repair**;
- bounded architecture red-team passed **after assurance hardening**;
- current next phase remains implementation planning only;
- actual Gate D integrated runtime V&V has not been executed and must not be claimed complete.

No active architecture blocker is known at handoff construction. The unresolved work is concrete implementation selection/evidence, not another open-ended search for core concepts.

## 5. Completed scope — do not redo without new evidence

Treat these as accepted foundations unless fresh authority materially changed them:

- AIMAGE Continuity/Handoff is repository-owned and separate from Image Engine semantics;
- dependency direction is `features/domain capabilities -> engine interfaces`;
- adaptive workflow preserves simple one-shot use;
- AIMAGE does not build a custom image-edit renderer; actual image edits are provider/backend-native where suitable;
- first hosted provider direction is OpenAI official SDK/API;
- Diffusers remains optional local provider direction;
- ComfyUI remains optional external backend/service direction;
- no initial Nori/GenAI/Krita/style-consistency source copying;
- mature external methods are generally E/F method/schema/reference adaptations rather than forced runtimes;
- four semantic contract families are accepted: Visual Intent & Authority; Requirement/Capability/Lowering; Spatial & Composition Profile; Validation & Domain Profile;
- semantic contracts and their fixed invariants are accepted;
- bounded red-team is a cross-cutting falsification step over Gate A-D, not Gate E and not a runtime subsystem.

Do not restart broad cross-domain discovery unless implementation evidence exposes a concrete semantic gap that the accepted contracts cannot represent.

## 6. Preserved decisions and negative boundaries

### Semantic authority

- `VisualIntentState` remains the only canonical semantic desired-state authority.
- Provider state must never become canonical merely because it is convenient to persist.
- Mandatory semantic obligations may not be silently weakened/dropped during compile, resolution, lowering, fallback, repair, or provider replacement.

### Approval / repair

- decisions are revision-bound and idempotent;
- stale/late decisions cannot overwrite newer semantic state;
- accepted/rejected/superseded artifact disposition is explicit;
- approved baseline changes require explicit reopen/supersession;
- repair uses an authorized mutation frame and regression-checks preserved dimensions;
- repair must be bounded rather than autonomous forever.

### Spatial semantics

- viewpoint-sensitive direction requires an explicit/inherited frame;
- `viewer_deictic`, `subject_intrinsic`, `scene_world`, and `screen_image` are not aliases;
- provider prompt/blocking/control representations are lowerings, not canonical spatial authority.

### Validation

- validation is separate from enforcement/mutation;
- mandatory unevaluable validation is `indeterminate`, not silent pass;
- evaluator/provenance/correlation/calibration must be visible where material;
- final externally visible composite output must be regression-validated, not only intermediate steps.

### Complexity boundary

- `ExecutionPlan` is bounded, attempt-local, and acyclic; do not grow it into a second durable workflow engine;
- bounded red-team is required only at material adoption/authorization/final-PASS boundaries, not ordinary image jobs or every provider call;
- do not add external runtimes merely because their design patterns were reused.

## 7. Current decision-relevant dependencies / artifacts

All decision-relevant state required for the next action is durable in the repository. No hidden chat-local or machine-local artifact is required for continuation.

Key durable evidence:

- `plans/SEMANTIC_CONTRACTS.md`
- `audits/SEMANTIC_CONTRACT_TABLETOP_2026-09-10.md`
- `plans/BOUNDED_RED_TEAM_ASSURANCE.md`
- `audits/BOUNDED_PLAN_RED_TEAM_2026-09-10.md`
- `governance/continuity/CURRENT.md`

Recoverability classification: **DURABLE** for the repository planning state above. No decision-critical temporary image, cache, local build, uncommitted file, or provider session is required.

Bounded supersession discovery for the receiver: check fresh `main` plus current open PRs/active branches touching implementation planning, runtime/dependency selection, semantic contracts, provider boundaries, or red-team assurance. Do not crawl unrelated branches.

## 8. Exact next bounded action

Prepare and independently audit **one concrete implementation plan**, without implementing it.

The plan must, as one coupled planning action:

1. choose and justify the implementation language/runtime against the accepted semantic contracts, provider SDK requirements, optional local/backend integration, maintainability, testability, and future replacement;
2. identify the minimum concrete dependency set for schema validation/evolution, persistence/metadata/blob handling, testing, provider adapter work, and any optional solver only if a measured requirement justifies it;
3. for every actual dependency/provider choice, execute `plans/REUSE_AND_INTEGRATION_ASSURANCE.md` Gate B using current official/upstream evidence: exact identity/version-selection policy, license/provenance, functional fit, maintenance/security/supply-chain, coupling, fallback/replacement, and AIMAGE-owned contract tests;
4. map repository/module boundaries and concrete schemas/types one-to-one to `plans/SEMANTIC_CONTRACTS.md`, preserving `features/domain -> engine interfaces` and keeping provider-native state below the semantic layer;
5. define the first thin OpenAI vertical slice end-to-end, covering at least one-shot generation, composition approval, viewer-relative placement, provider capability/reroute/failure behavior, validation, and minimal-delta repair;
6. define contract/integration tests for the fixed semantic invariants and all prior tabletop repairs;
7. incorporate the eight accepted red-team hardening obligations below;
8. run `plans/BOUNDED_RED_TEAM_ASSURANCE.md` against the completed implementation plan and repair material findings;
9. independently audit the final plan against fresh `main`, `architecture/BOUNDARIES.md`, external-reuse plans, semantic contracts, Gate A-D obligations, and current open/conflicting work;
10. update continuity/planning authority only if the final planning candidate passes and the current user scope allows that adoption.

### Eight red-team hardening obligations that must appear in the implementation plan

1. fail-closed semantic compilation for contradictory/incomplete mandatory semantics;
2. currentness fence preventing old in-flight artifacts/reports/decisions from becoming current after a newer semantic revision;
3. conditional capability matching using exact target/model/version/applicability/limits/evidence, not capability-name presence;
4. validation-oracle controls: evaluator identity/provenance/correlation/calibration and explicit evidence class for material mandatory validation;
5. bounded repair policy with non-improvement/oscillation detection, attempt/cost stop policy, best-known artifact retention, and escalation;
6. bounded attempt-local acyclic composite execution; human waits/resume/repair loops remain in generic lifecycle/orchestration;
7. final-artifact preservation/regression validation after the complete composite strategy;
8. capability-drift race handling with pre-execution freshness/compatibility checks and re-resolution/bounded failure.

## 9. Completion / acceptance criteria

The bounded action is complete only when all of the following are true:

1. runtime/language selection has an explicit comparative justification;
2. every chosen concrete dependency/provider integration has Gate-B evidence and no blocking `UNRESOLVED` acquisition item;
3. implementation module/type/schema ownership maps cleanly to the accepted semantic contracts without introducing a competing semantic owner;
4. provider-native IDs/payloads remain execution/evidence state only;
5. the first OpenAI vertical slice is thin, genuinely end-to-end, and does not require optional Diffusers/ComfyUI to prove the core path;
6. test inventory covers accepted semantic invariants, the four tabletop repairs, and the eight red-team hardening obligations;
7. stop/go, rollback/fallback, and provider/dependency replacement boundaries are explicit;
8. bounded red-team verdict for the implementation plan is `PASS` or `PASS_AFTER_REPAIR`;
9. fresh independent repository/architecture audit finds no conflicting newer work, boundary inversion, or hidden phase expansion;
10. the result is preserved in repository planning/continuity state;
11. production implementation has still **not** begun.

Evidence-sufficiency exit condition: once the concrete runtime/dependency/module/test/vertical-slice choices meet these criteria and remaining uncertainties are explicitly implementation-time empirical checks that do not change architecture, stop planning. Do not continue research for marginal bibliography completeness.

## 10. Expected transition

If the next slice passes, AIMAGE should have:

- fixed provider-neutral semantic architecture;
- accepted design tabletop + bounded red-team evidence;
- concrete implementation language/runtime and minimum dependency plan;
- Gate-B records for actual selected dependencies/provider integration;
- concrete repository/module/schema/test plan;
- one bounded first OpenAI vertical-slice target;
- explicit implementation tests/defenses for the retained adversarial attack classes.

The next thread must stop there unless the user separately authorizes production implementation. A successful plan does not self-authorize coding.

## 11. Stop / replan conditions

Return `STALE_REPLAN` or stop/replan if any of these become true:

- fresh `main`, governing handoff/continuity method, or implementation-planning authority materially changed so this next action is no longer unique;
- a newer open PR/active work item touches the same runtime/dependency/implementation-planning boundary and changes ordering/ownership;
- a selected runtime/package cannot preserve `plans/SEMANTIC_CONTRACTS.md` without semantic leakage or major architecture inversion;
- Gate B finds a material license, security, provenance, maintenance, replacement, or coupling blocker;
- current OpenAI/provider capabilities cannot reproduce a requirement essential to the first vertical slice and no explicit legal fallback exists;
- the bounded red-team finds a `BLOCKING` issue not repairable inside implementation planning;
- the user changes phase/scope.

Harmless movement in unrelated branches or documentation does not invalidate this handoff.

## 12. Cold-start read route

A fresh receiver should read in this order and keep the set bounded:

1. fresh `main` ref / repository state;
2. current root `AGENTS.md`;
3. current `.agents/skills/handoff/SKILL.md`;
4. current `governance/CONTINUITY.md`;
5. current `governance/continuity/REPOSITORY_WORK.md`;
6. **this packet from the immutable commit locator supplied in the paste prompt**;
7. current `governance/continuity/CURRENT.md`;
8. current `architecture/BOUNDARIES.md`;
9. `plans/SEMANTIC_CONTRACTS.md`;
10. `plans/EXTERNAL_REUSE_PLAN.md`;
11. `plans/REUSE_AND_INTEGRATION_ASSURANCE.md`;
12. `plans/BOUNDED_RED_TEAM_ASSURANCE.md`;
13. `audits/SEMANTIC_CONTRACT_TABLETOP_2026-09-10.md` and `audits/BOUNDED_PLAN_RED_TEAM_2026-09-10.md` only as decision-relevant evidence;
14. fresh open-PR/active-work discovery scoped to the next action.

Read `plans/WORKFLOW_TARGET.md`, `plans/CAPABILITY_REUSE_MATRIX.md`, or `plans/SEMANTIC_FUSION_PLAN.md` when needed to resolve a concrete planning ambiguity; do not reread the entire repository by default.

Then synthesize in plain language:

- current phase;
- what is already closed;
- exactly one next action;
- what proves it complete;
- what would force replan.

Return exactly one continuity verdict: `ACCEPTED` or `STALE_REPLAN`. Only after `ACCEPTED` proceed with the bounded implementation-planning action.

## 13. Hard prohibitions

- Do not treat this packet, its branch, or its filename as authority over fresh `main`.
- Do not use chat memory as a substitute for fresh repository reads.
- Do not implement production code in the implementation-planning slice.
- Do not install dependencies or mutate lockfiles in the planning slice.
- Do not import/copy external source merely because a method/project was useful evidence.
- Do not reopen settled semantic architecture without a concrete failed invariant or new authoritative evidence.
- Do not silently relax mandatory intent, approval baselines, preservation obligations, or capability requirements to make a provider work.
- Do not make OpenAI/ComfyUI/Diffusers request formats canonical job state.
- Do not turn `ExecutionPlan` into a durable second workflow engine.
- Do not turn bounded red-team into per-image runtime ceremony.
- Do not claim final Gate-D/system `PASS` from planning/tabletop evidence.

## 14. Handoff quality / cold-reader rehearsal

Cold-reader challenge at construction time:

- Can a zero-chat receiver identify the phase? **Yes: planning/design/research only.**
- Is there exactly one next bounded action? **Yes: prepare + Gate-B-audit + red-team + independently audit one concrete implementation plan.**
- Can the receiver know when to stop? **Yes: section 9 plus the evidence-sufficiency exit condition.**
- Could old rejected provider/semantic state be resurrected? **No: fresh authority + accepted semantic contracts + explicit negative boundaries control.**
- Is any hidden local/session artifact required? **No.**
- Does the packet duplicate canonical specifications? **No: it preserves operational decisions and points to owners.**
- Does it accidentally authorize implementation? **No: implementation remains explicitly prohibited until a separate user-authorized phase.**
