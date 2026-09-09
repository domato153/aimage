# AIMAGE Bounded Red-Team Assurance

Status: cross-cutting planning/verification extension to `plans/REUSE_AND_INTEGRATION_ASSURANCE.md`. It adds a deliberately adversarial challenge before material adoption/authorization without creating a fifth heavyweight gate or a runtime subsystem.

This plan does not authorize implementation, dependency installation, source import, provider integration, or production execution.

## 1. Purpose

The existing Gate A-D assurance system already covers capability closure, acquisition due diligence, architecture scenarios, end-to-end simulation, state transitions, combinatorial coverage and fault injection.

The missing assurance question is different:

> **If a reviewer actively tries to make an apparently legal AIMAGE plan produce a wrong, stale, over-coupled, unbounded or falsely accepted result, where does the plan break?**

AIMAGE therefore uses one bounded adversarial challenge across the existing gates rather than adding a new framework.

## 2. External method basis

The challenge combines only the useful question patterns from mature methods:

- **NASA Software Fault Tree Analysis (SFTA)** — top-down: start from an undesired system state and work backward through credible causes;
- **NASA Software FMEA (SFMEA)** — bottom-up: fail a component/interface, trace propagation/effects, detection and corrective controls;
- **MIT STPA** — challenge unsafe/missing/late/out-of-order control actions in systems containing software and humans;
- **SEI ATAM** — challenge quality-attribute risks, sensitivity points and tradeoffs, including whether a correctness control harms simplicity, modifiability, cost or replacement.

Sources:

- https://swehb.nasa.gov/spaces/SWEHBVD/pages/140641657/Software%2BSafety%2Band%2BHazard%2BAnalysis
- https://swehb.nasa.gov/spaces/SWEHBVD/pages/140640400/8.5%2B-%2BSW%2BFailure%2BModes%2Band%2BEffects%2BAnalysis
- https://psas.scripts.mit.edu/home/books-and-handbooks/
- https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-atam/

These are method/reference inputs only. AIMAGE does not adopt their runtimes, full safety processes or risk-scoring bureaucracy.

## 3. Trigger boundary

Run a bounded Red-Team Challenge:

- before adopting a material architecture or semantic-contract change;
- before authorizing implementation from an implementation plan;
- before a final integrated system `PASS`;
- after a material provider/dependency/authority-boundary change invalidates prior assumptions.

Do not require it for:

- ordinary low-risk documentation edits;
- trivial one-shot image jobs;
- every provider call or repair attempt;
- unchanged reruns already covered by existing tests.

## 4. Six attack lenses

A material review checks the applicable subset of these lenses.

### R1 — Top-event / authority attack

Assume one of these happened and work backward:

- wrong semantic state became current;
- rejected/stale artifact became accepted;
- mandatory intent disappeared;
- approved baseline changed without reopen;
- provider-native state became authority.

### R2 — Component/interface failure attack

Fail or corrupt one boundary at a time:

- intent normalization/authority resolution;
- semantic compilation;
- capability descriptor/resolver;
- provider adapter/lowering;
- validation/evidence;
- persistence/migration;
- continuity/resume.

Ask how the failure propagates, how it is detected, and whether failure is bounded.

### R3 — Control-action/timing attack

For approve, reject, reopen, reroute, retry, repair and finalize, challenge:

- command omitted;
- command duplicated;
- command late/stale;
- command out of order;
- command issued against the wrong semantic revision;
- command applied after state changed while work was in flight.

### R4 — Evidence/oracle attack

Challenge whether evidence is actually trustworthy:

- declared capability differs from reproduced behavior;
- capability is conditional on model/account/input/region/size;
- descriptor becomes stale between resolution and execution;
- generator/provider effectively validates its own output;
- evaluator is uncalibrated/correlated;
- mandatory check is unevaluable.

### R5 — Tradeoff/complexity attack

Try to make the mitigation itself harmful:

- lock/baseline accumulation makes the job impossible;
- repair oscillates or consumes unbounded cost;
- composite ExecutionPlan grows into a custom workflow engine;
- correctness machinery destroys one-shot simplicity;
- fallback/replacement rules create excessive coupling.

### R6 — Replacement/resume attack

Change the environment while preserving nominal user intent:

- replace provider/dependency;
- lose optional backend;
- migrate schema;
- resume in a new process/context;
- let old in-flight execution finish after a newer semantic revision exists.

## 5. Mandatory current attack classes

Until implementation evidence proves equivalent defenses, every implementation plan and final Gate-D campaign must explicitly cover at least these current attack classes:

1. **fail-closed semantic compilation** — contradictory/incomplete mandatory intent must not produce a legal executable RenderSpec;
2. **currentness fence** — old in-flight artifact/report/decision cannot become current merely because it finishes later;
3. **conditional capability matching** — mandatory resolution checks exact target/model/version/applicability/evidence, not only a capability name;
4. **validation-oracle challenge** — evaluator identity/provenance/correlation/calibration are visible for material mandatory validation;
5. **bounded repair** — detect non-improvement/oscillation and stop/escalate under a bounded attempt/cost policy while retaining best-known good work;
6. **bounded composite execution** — ExecutionPlan remains attempt-local and acyclic; human waits/repair loops/resume stay in generic lifecycle orchestration;
7. **final-artifact regression** — full composite output is validated against preservation obligations, not only intermediate steps;
8. **capability drift race** — material capability changes after resolution trigger refresh/re-resolution or bounded failure before semantic degradation.

These are assurance obligations, not eight new semantic subsystems.

## 6. Finding classification

Each attack finding is one of:

- `BLOCKING` — architecture/authority/correctness cannot be accepted;
- `REPAIR_BEFORE_ADOPTION` — bounded plan/design repair is required before adoption;
- `DEFERRED_IMPLEMENTATION_RISK` — semantics are sound but concrete runtime/provider evidence is still required;
- `REJECTED_ATTACK` — the proposed mitigation would be unnecessary, duplicative or more harmful than the demonstrated risk.

A rejected attack should record why it was rejected when the alternative would materially expand architecture or ceremony.

## 7. Review flow

For a material planning/adoption slice:

1. complete the ordinary applicable Gate A/B/C work;
2. identify 3-7 top undesired outcomes relevant to the slice;
3. challenge the plan across all applicable R1-R6 lenses;
4. prioritize attacks that cross boundaries, exploit timing, use stale evidence, or turn a mitigation against the system;
5. classify findings;
6. repair `BLOCKING`/`REPAIR_BEFORE_ADOPTION` findings;
7. rerun only the affected lenses once;
8. continue further only if the rerun exposes a materially new failure class;
9. record exactly one red-team verdict: `PASS`, `PASS_AFTER_REPAIR`, or `FAIL_REPLAN`;
10. carry retained runtime attacks into Gate D as explicit tests/fault injections/combinatorial factors.

The target is **decision sufficiency**, not a fixed attack count or exhaustive bibliography.

## 8. Required record per material attack

Record enough to reproduce the reasoning:

```text
attack_id
lens
top_event_or_failure
preconditions
attack_sequence
expected_bad_outcome
existing_defense
finding_class
required_repair_or_test
residual_risk
verdict_after_retest
```

Do not store private chain-of-thought. Record only the review inputs, observable reasoning summary, decision and evidence needed for another reviewer to reproduce the challenge.

## 9. Relationship to existing Gate A-D

This challenge does not replace or renumber the accepted gates.

- **Gate A** answers whether requirements/capabilities are covered and native design is justified.
- **Gate B** answers whether concrete external components are safe/fit/replaceable to acquire.
- **Gate C** answers whether architecture quality-attribute scenarios and tradeoffs close.
- **Red-Team Challenge** tries to falsify those answers using adverse combinations, timing and assumption failure before adoption.
- **Gate D** executes the retained attacks against the coherent implementation with real tests, combinatorial coverage and fault/regression injection.

A component or plan that passes Gate A-C but fails the bounded Red-Team Challenge is not ready for implementation authorization.

## 10. Anti-overengineering rule

Red teaming must not become a second product architecture.

Do not add a subsystem merely because an attack can be imagined. Require a credible failure path that threatens a named AIMAGE invariant, user-visible goal, replacement boundary or final PASS criterion.

Prefer, in order:

1. prove the existing contract already blocks the attack;
2. add a contract/integration test;
3. add a small invariant/failure rule;
4. add a bounded implementation policy;
5. only then change architecture.

This ordering is itself part of the red-team discipline.