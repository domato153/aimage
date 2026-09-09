# AIMAGE Bounded Plan Red-Team Audit — 2026-09-10

Status: planning/design adversarial challenge of the accepted semantic architecture and assurance flow. This audit intentionally tries to break the plan from multiple directions without expanding into a full safety/security program. No production implementation, provider execution, dependency installation, or source import occurred.

## 1. Verdict

**PASS AFTER ASSURANCE HARDENING**

No new architecture-blocking contradiction was found in the accepted semantic contract architecture. The contracts already contain enough primitives to represent the attacks below, but the assurance flow did not independently require an adversarial challenge before major plan adoption.

The material result is therefore:

- keep the four-family semantic architecture;
- do not add another runtime/framework or new semantic subsystem;
- add a bounded cross-cutting Red-Team Challenge to the assurance plan;
- convert six latent implementation risks into explicit adversarial checks for the implementation plan and later Gate-D V&V;
- retain the current next phase as **implementation planning only**.

## 2. Fresh authority and scope

Exact fresh base challenged:

`main = 69e51bd3b250a20a9268a6c858a82b5862933297`

Primary AIMAGE surfaces checked:

- `AGENTS.md`;
- `architecture/BOUNDARIES.md`;
- `plans/WORKFLOW_TARGET.md`;
- `plans/CAPABILITY_REUSE_MATRIX.md`;
- `plans/EXTERNAL_REUSE_PLAN.md`;
- `plans/REUSE_AND_INTEGRATION_ASSURANCE.md`;
- `plans/SEMANTIC_FUSION_PLAN.md`;
- `plans/SEMANTIC_CONTRACTS.md`;
- `audits/SEMANTIC_CONTRACT_TABLETOP_2026-09-10.md`;
- `governance/continuity/CURRENT.md`.

No open PR was found touching this exact red-team/implementation-planning assurance surface before the bounded candidate was created.

## 3. External method basis

The red-team method is intentionally lightweight and composes mature review perspectives rather than inventing an AIMAGE-specific formalism.

### Top-down undesired-state challenge — NASA Software Fault Tree Analysis

NASA describes Software Fault Tree Analysis as a **top-down** analysis that starts from an undesired failure/state and works backward through credible causes.

Used here only as a question pattern:

> If a serious AIMAGE semantic failure occurred, what combination of otherwise plausible actions could have produced it?

Sources:

- https://swehb.nasa.gov/spaces/SWEHBVD/pages/140641657/Software%2BSafety%2Band%2BHazard%2BAnalysis
- https://swehb.nasa.gov/spaces/SWEHBVC/pages/72025075/8.7%2BSoftware%2BFault%2BTree%2BAnalysis

### Bottom-up failure-mode challenge — NASA Software FMEA

NASA describes FMEA as a **bottom-up** method that examines how individual components/interfaces can fail, how failure propagates, how it can be detected, and what corrective action is needed.

Used here to challenge semantic/compiler/resolver/adapter/validator boundaries rather than to calculate safety-critical risk scores.

Source:

- https://swehb.nasa.gov/spaces/SWEHBVD/pages/140640400/8.5%2B-%2BSW%2BFailure%2BModes%2Band%2BEffects%2BAnalysis

### Control-action challenge — MIT STPA

The STPA Handbook explicitly addresses complex systems containing software and human elements and identifies **Unsafe Control Actions** in a control structure.

Used here for actions such as approve, reject, reopen, reroute, repair, retry and finalize, with special attention to commands that are missing, duplicated, late, stale, out of order or issued under the wrong state.

Source:

- https://psas.scripts.mit.edu/home/books-and-handbooks/

### Tradeoff and complexity challenge — SEI ATAM

The existing AIMAGE assurance plan already adopts ATAM-style scenario analysis. SEI describes ATAM as exposing risks, sensitivity points and tradeoffs among quality attributes.

The red-team pass uses this specifically to attack controls that improve correctness but may damage simplicity, latency, modifiability or replacement.

Sources:

- https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-atam/
- https://www.sei.cmu.edu/library/atam-method-for-architecture-evaluation/

These methods are review evidence only; no NASA/MIT/SEI runtime or formal process is introduced.

## 4. Bounded attack lenses

The red team uses six lenses. It is intentionally not an unlimited brainstorming exercise.

1. **Top-event / authority attack** — assume a bad final semantic outcome happened and work backward.
2. **Component/interface failure attack** — fail one semantic/compiler/resolver/adapter/validator boundary at a time.
3. **Control-action/timing attack** — make approve/reopen/reject/reroute/repair/finalize missing, duplicated, stale, late or out of order.
4. **Evidence/oracle attack** — make capability or validation evidence stale, correlated, optimistic or unevaluable.
5. **Tradeoff/complexity attack** — make correctness controls cause lock creep, ceremony, cost explosion or a hidden workflow engine.
6. **Replacement/resume attack** — swap provider/dependency/context while old work is still in flight.

A major planning slice should run one bounded pass across all applicable lenses, repair material findings, then rerun only the affected lenses once. Repeated attacks that add no materially new failure class do not justify an unbounded review loop.

## 5. Adversarial attack matrix

### RT-01 — contradictory mandatory intent reaches a provider

Attack:

Two current authoritative inputs produce incompatible mandatory semantics, for example mutually exclusive spatial constraints or two equally authoritative values for the same semantic path.

Failure sought:

The compiler emits a RenderSpec anyway and lets a stochastic provider decide what to ignore.

Existing defenses:

- Family-A authority rules forbid accidental last-write-wins;
- unresolved authority conflicts are explicit semantic conflicts;
- unknown/unsupported mandatory semantics fail safe;
- lowering cannot silently drop mandatory obligations.

Hardening obligation:

**RenderSpec compilation must be fail-closed.** Unresolved blocking semantic conflicts, required-but-unbound reference frames, invalid baseline scopes, or other incomplete mandatory semantics must prevent an executable RenderSpec/RequirementSet from being treated as legal. Implementation may represent this with a compile-result/error type; a new AIMAGE semantic subsystem is not required.

Verdict: **PASS WITH IMPLEMENTATION-PLAN HARDENING**.

### RT-02 — old in-flight result is accepted after the user changed intent

Attack:

Render for semantic revision 17 starts. The user changes intent to revision 18. Revision-17 provider output/validation returns later and is technically valid for rev17.

Failure sought:

A late success is promoted because it is newest by wall-clock time.

Existing defenses:

- all derived objects carry source semantic revision;
- DecisionRecord is base-revision-bound;
- stale decisions are rejected;
- rejected/accepted disposition is explicit and historical records are immutable.

Hardening obligation:

Before automatic acceptance/finalization or a user decision is applied, verify that artifact/report/review context is current for the live semantic revision or perform an explicit reconciliation. **Newest completion time is never currentness authority.** Add this as a contract/integration test.

Verdict: **PASS WITH IMPLEMENTATION-PLAN HARDENING**.

### RT-03 — capability name matches but the real operating conditions do not

Attack:

A provider reports `masked_edit`, but only for another model, input type, image count, account/region, size or quality mode. Resolver matches only the capability name.

Failure sought:

A strategy is declared legal even though the exact requested job falls outside the capability's applicability envelope.

Existing defenses:

- `ProviderCapabilityDescriptor` is target/model/version-sensitive;
- capabilities carry attributes/limits;
- RequirementSet carries constraints;
- descriptor evidence distinguishes declared/probed/configured/reproduced;
- Assurance Gate B requires exact functional fit and reproduction before reliance.

Hardening obligation:

Mandatory requirement resolution must match **capability + applicability constraints + exact target/model/version + sufficiently current evidence**, not string/name presence. Stale/materially changed evidence forces re-resolution before execution.

Verdict: **PASS WITH IMPLEMENTATION-PLAN HARDENING**.

### RT-04 — the generator effectively grades its own homework

Attack:

The same provider/model family generates an image and supplies optimistic feedback or a highly correlated model-assisted validator marks the result pass.

Failure sought:

A false pass enters accepted state because evaluator provenance/correlation was ignored.

Existing defenses:

- `ValidationRule` declares evaluator class and required evidence;
- reports are tri-state;
- mandatory unevaluable checks cannot silently pass;
- concrete evaluator reliability/calibration is already deferred as an implementation obligation.

Hardening obligation:

Implementation planning must define evaluator identity/version/evidence provenance and, for material mandatory visual constraints, the acceptable evidence class. Provider self-report or an uncalibrated correlated evaluator must not be treated as independent proof unless the domain/user policy explicitly accepts that risk. Gate D must include evaluator disagreement/false-pass calibration cases.

Verdict: **PASS WITH IMPLEMENTATION-PLAN HARDENING**.

### RT-05 — repair oscillates forever or repeatedly destroys good work

Attack:

Repair A fixes expression but slightly hurts identity. Repair B fixes identity but hurts expression. The loop alternates while cost rises.

Failure sought:

The architecture has a semantically valid loop but no bounded progress/escalation behavior.

Existing defenses:

- MutationFrame bounds mutable/preserve paths;
- post-repair validation checks preserved dimensions;
- Gate D already requires repair-loop exit and escalation;
- cost/latency control is an architecture quality attribute.

Hardening obligation:

Implementation plan must define a **bounded repair policy**: attempt/cost budget or equivalent stop condition, non-improvement/oscillation detection, retention of the best-known accepted/candidate artifact, and escalation to user/reopen/rerender instead of indefinite autonomous repair.

This belongs in orchestration policy, not the semantic SSoT.

Verdict: **PASS WITH IMPLEMENTATION-PLAN HARDENING**.

### RT-06 — composite execution quietly becomes a custom workflow engine

Attack:

Because `ResolutionResult` allows a small multi-target DAG, implementation keeps adding loops, human waits, dynamic branching and durable orchestration inside ExecutionPlan.

Failure sought:

Family B grows into a second workflow engine and duplicates the generic lifecycle layer.

Existing defenses:

- current contracts explicitly call the strategy small/ordered/DAG;
- C01 already says not to build a bespoke workflow engine;
- Continuity/Handoff and workflow/state mechanics have separate owners.

Hardening obligation:

Treat an ExecutionPlan as a **bounded, attempt-local, acyclic execution composition**. Human waits, long-lived lifecycle loops, repair cycles and resume semantics stay in the generic lifecycle/orchestration layer. If implementation needs materially richer orchestration, re-open the generic workflow-engine decision rather than extending ExecutionPlan ad hoc.

Verdict: **PASS WITH BOUNDARY HARDENING**.

### RT-07 — a late composite step regresses an earlier locked dimension

Attack:

Image generation preserves approved composition, then deterministic text composition resizes/crops the canvas and changes the locked composition.

Failure sought:

Individual steps are legal but the final artifact violates the original baseline.

Existing defenses:

- preservation obligations originate in the RenderSpec;
- ExecutionPlan steps are derived, not semantic authority;
- final ValidationReport is tied to the final artifact/plan;
- repair validation must regression-check preserved dimensions.

Hardening obligation:

Gate D must validate the **final externally visible artifact after the complete composite strategy**, not just intermediate provider outputs. Preservation obligations apply across the full execution composition.

Verdict: **PASS**.

### RT-08 — approval/lock accumulation makes the job impossible

Attack:

The user approves many dimensions over repeated iterations until no provider can satisfy all locks together.

Failure sought:

The system silently weakens older locks or repeatedly retries impossible work.

Existing defenses:

- baselines require explicit reopen;
- mandatory requirements cannot silently soften;
- resolver can return explicit unsatisfied results.

Hardening obligation:

When lock accumulation produces semantic/capability unsatisfiability, expose the conflict and the minimum affected baselines/requirements needed for user-authorized reopen. Do not auto-relax approved state.

Verdict: **PASS**.

### RT-09 — a domain plugin attempts to become core authority

Attack:

A character-domain validator or plugin writes provider routing/approval state directly or redefines a core visual dimension.

Existing defenses:

- `features/domain -> engine interfaces` boundary;
- namespaced domain extensions cannot redefine core dimensions;
- user/domain conflict is reported rather than silently rewriting Family A.

Verdict: **PASS**.

### RT-10 — provider capability changes after resolution but before execution

Attack:

A valid descriptor is used to resolve a plan, then the provider/model/API capability changes before execution.

Existing defenses:

- descriptors are version-sensitive observations;
- material stale/change triggers re-resolution;
- runtime failure cannot mutate intent.

Hardening obligation:

Implementation plan must define a pre-execution freshness/compatibility fence for capabilities that are material to mandatory requirements, with bounded retry/re-resolution after drift.

Verdict: **PASS WITH IMPLEMENTATION-PLAN HARDENING**.

### RT-11 — schema migration silently drops a mandatory extension

Attack:

An old job contains a mandatory namespaced semantic unknown to the new reader.

Existing defenses:

- unknown mandatory semantics fail safe;
- incompatible migration is explicit;
- historical source version remains identifiable.

Verdict: **PASS**.

### RT-12 — correctness machinery ruins the one-shot use case

Attack:

Every simple prompt is forced through blocking, explicit approval, all validation profiles and full red-team ceremony.

Failure sought:

The architecture is correct but unusably heavy.

Existing defenses:

- one-shot simplicity is a fixed invariant;
- W0-W13 are logical functions rather than mandatory user-visible phases;
- Gate C/D already include one-shot scenarios.

Red-team rule:

The red-team process itself must also be **triggered only for material architecture/implementation/adoption boundaries**, not ordinary image jobs or trivial repository edits.

Verdict: **PASS**.

## 6. What the attack did *not* justify

The following were explicitly rejected as overreaction:

- adding a new general-purpose fault-tree/FMEA/STPA engine to AIMAGE;
- turning every image generation job into a formal hazard-analysis exercise;
- adding a second semantic authority just for red-team state;
- adding arbitrary security gates unrelated to the current image-production correctness problem;
- requiring independent human review of every generated image;
- banning composite provider/tool strategies merely because they add orchestration complexity;
- reopening the four-family semantic architecture without a concrete failed invariant.

The red-team method is a planning/assurance challenge, not a product runtime subsystem.

## 7. Red-team process deficiency found in the existing plan

The existing Assurance Gate C and D already contain adversarial scenarios, fault injection, replacement, stale-state and regression tests. That is strong coverage.

The missing element was **an explicit adversarial role and bounded pre-adoption challenge** that asks:

- how can apparently legal components combine into an illegal result;
- what if timing/order/currentness is wrong;
- what if the evidence/oracle is wrong rather than the provider call;
- what if the mitigation itself creates deadlock, cost explosion or a second framework;
- what if normal operation, not an obvious exception, causes the failure.

Therefore red teaming should be added as a **cross-cutting challenge over Gates A-D**, not as a fifth heavyweight implementation gate.

## 8. Required integration into the assurance flow

For any material architecture, semantic-contract, dependency/runtime or implementation-plan adoption:

1. run the ordinary applicable Gate A/B/C checks;
2. perform one bounded Red-Team Challenge across applicable attack lenses;
3. classify findings as `BLOCKING`, `REPAIR_BEFORE_ADOPTION`, `DEFERRED_IMPLEMENTATION_RISK`, or `REJECTED_ATTACK`;
4. repair blocking/material findings;
5. rerun only the affected lenses once;
6. if a materially new failure class appears, continue only until that class is closed; do not iterate for bibliography/attack-count completeness;
7. record a red-team verdict: `PASS`, `PASS_AFTER_REPAIR`, or `FAIL_REPLAN`;
8. after implementation, feed retained adversarial cases into Gate D fault/regression/combinatorial V&V.

Red-team completion is based on **decision sufficiency**, not number of attacks.

## 9. Red-team trigger boundary

Required:

- before adopting a material architecture or semantic-contract change;
- before authorizing implementation from an implementation plan;
- before final system PASS after coherent implementation;
- after a material provider/dependency/authority-boundary change that invalidates previous assumptions.

Not required:

- ordinary low-risk documentation edits;
- trivial one-shot image jobs;
- unchanged reruns of already covered tests;
- every provider request or every repair attempt.

This keeps the process adversarial without turning AIMAGE into audit ceremony.

## 10. Result for the current plan

The accepted semantic architecture survives the bounded red-team without a new structural subsystem.

The following six checks become explicit obligations for the next implementation-planning slice:

1. fail-closed semantic compilation before executable RenderSpec;
2. currentness fence for in-flight artifacts/reports/acceptance;
3. conditional/evidence-backed capability matching rather than name matching;
4. evaluator provenance/correlation/calibration policy for material validation;
5. bounded repair progress/termination/escalation;
6. attempt-local acyclic scope for composite ExecutionPlan.

Additional Gate-D adversarial scenarios must cover final-artifact regression after composite steps and provider capability drift between resolution and execution.

No production implementation is authorized by this audit.