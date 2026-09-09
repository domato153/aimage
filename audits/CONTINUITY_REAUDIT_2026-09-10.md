# AIMAGE Continuity Re-audit — 2026-09-10

Status: independent re-audit of PR #1 after comparing the AIMAGE candidate again against the fresh read-only `domato153/translation` governing continuity sources. The earlier PASS was not treated as authoritative.

## 1. Scope and fresh baseline

Source repository (read only): `domato153/translation`

Fresh source `main`: `638e702d81b014fb32209c8ac44e907a7fbafe87`

Source files re-read:

- `.agents/skills/maintenance-regression-supervisor/SKILL.md`
- `.agents/skills/maintenance-regression-supervisor/references/handoff-continuity.md`
- `.agents/skills/maintenance-regression-supervisor/references/handoff-continuity-regression-cases.md`

AIMAGE candidate branch: `aimage-stage/continuity-core-adoption`

AIMAGE base at re-audit start: `main` at `d7f84a0fbf85b29623c530e008f7244b463e7b5a`

This re-audit checks:

1. semantic fidelity to generic source continuity behavior;
2. hidden dependency closure, including material parent-skill semantics;
3. removal of translation/maintenance runtime coupling;
4. authority and phase safety;
5. temporary/local/derived-state fidelity;
6. AIMAGE continuity vs. Image Engine vs. feature/domain responsibility separation;
7. Project bootstrap safety and thinness.

## 2. Re-audit findings before repair

The previous candidate was broadly sound but not yet sufficient to merge. Three material gaps were found.

### F-01 — user instruction and factual live state were collapsed into one precedence list

Previous AIMAGE wording placed `explicit current user instruction` above current live repository state for "operational truth".

Risk: a mistaken user statement such as an old SHA or stale branch fact could be interpreted as outranking a fresh repository observation. Conversely, a live ref could be confused with authorization to change a governing rule.

Source distinction: the parent source skill treats repository/live facts as factual authority while explicit user authorization can authorize an authority transition; candidate text cannot self-authorize.

Repair:

- `governance/CONTINUITY.md` §2 now separates **current factual state** from **intent/scope/authorization**.
- a user instruction may authorize a transition but does not make a false repository fact true;
- a live ref establishes state but does not self-authorize a policy transition;
- a candidate/packet/work branch cannot authorize its own promotion.
- `bootstrap/PROJECT_SOURCE.md` mirrors this distinction compactly.

Disposition: **CLOSED**.

### F-02 — repository phase was recorded but not explicitly binding

Previous `REPOSITORY_WORK.md` recorded the requested phase but did not clearly state that `design/review/evaluation` cannot cross into implementation/mutation merely because the handoff contains a mutation-ready next action.

Risk: a `DESIGN ONLY` transfer could survive as a descriptive field while the receiver nevertheless performs implementation.

Source dependency: the parent source skill explicitly treats phase as part of scope and prohibits unauthorized phase crossing.

Repair:

- `REPOSITORY_WORK.md` now has a binding Phase boundary section;
- review/design/evaluation cannot authorize mutation unless current user authorization or an authoritative AIMAGE mechanism expands the phase;
- a phase-conflicting next action cannot be executed merely because a packet says so.

Disposition: **CLOSED**.

### F-03 — temporary/local/derived artifact semantics were too compressed

Previous AIMAGE core preserved `DURABLE / REGENERATE / UNRECOVERABLE` but compressed some source transport semantics: inventory of verdict/next-action-relevant local state, immutable/digest identity when transport matters, expiry/availability facts, source/producer as provenance rather than authority, and advisory status of stale/unbound derived views.

Risk: an expiring artifact or derived view could be considered recoverable/current without sufficient identity binding.

Repair:

- `CONTINUITY.md` §9 now requires inventory of decision/next-action-relevant outgoing local/session state;
- decision-relevant transport preserves immutable identity/digest or identity-equivalent locator, provenance-only producer/source, relevant availability/expiry facts, and same-state regeneration path when applicable;
- stale/unbound/unrecoverable decision-relevant derived views are advisory until rebuilt/reconciled;
- incidental caches remain exempt from ceremony.

Disposition: **CLOSED**.

## 3. Hidden-dependency closure

The original traceability primarily mapped `handoff-continuity.md`. Re-audit confirmed that a small subset of the owning parent skill materially affects handoff semantics and therefore must not remain a hidden runtime dependency.

`governance/continuity/TRACEABILITY.md` now explicitly closes these parent-skill dependencies:

- authority before memory/fresh state;
- phase as scope;
- authority cannot self-authorize;
- proportional procedure/anti-ceremony;
- epistemic labels for material uncertainty;
- user-facing clarity;
- live-transfer / governing-owner resolution.

Maintenance-only behavior remains intentionally unadopted, including:

- R0/R1/R2/R3 taxonomy as an AIMAGE continuity requirement;
- translation semantic/literary gates;
- promotion/proof-receipt control plane;
- translation CI/runner trust routing;
- candidate terminology as a mandatory universal object model.

### Closure verdict

**PASS.** A fresh AIMAGE receiver can interpret the governing continuity contract and both AIMAGE profiles without reading `domato153/translation`.

`translation` survives only as construction provenance, historical traceability, and an optional future re-audit source.

## 4. Source continuity semantic comparison

| Generic source invariant | AIMAGE status |
|---|---|
| handoff is continuity evidence, not project authority | PRESERVED |
| one canonical immutable locator | PRESERVED |
| chat/paste derivative points back to canonical packet | PRESERVED |
| old reachable packets do not win by `CURRENT`/`FINAL` naming | PRESERVED |
| governing method resolved from current owner | PRESERVED |
| bounded dependency set | PRESERVED |
| receiver independently re-derives dependency/discovery scope | PRESERVED |
| bounded supersession discovery rather than repository-wide crawl | PRESERVED |
| active situation model rather than timeline only | PRESERVED |
| uncertainty/hypothesis does not become authority | PRESERVED |
| exactly one next action + rationale | PRESERVED |
| expected transition + stop/replan condition | PRESERVED |
| known decision-critical hazards survive compression | PRESERVED |
| decision rationale/negative boundary preserved when needed | PRESERVED |
| examples do not silently become universal authority | PRESERVED |
| stale dependency/authority/premise can force `STALE_REPLAN` | PRESERVED |
| time/unrelated movement alone is not stale | PRESERVED |
| competing-state ledger only where ambiguity matters | PRESERVED/GENERALIZED |
| stable identity separated from temporary availability | PRESERVED |
| local/session state recoverability classified | PRESERVED + STRENGTHENED |
| temporary transport identity/expiry/regeneration retained when material | PRESERVED after F-03 repair |
| decision-relevant derived view bound to source/invalidation/rebuild | PRESERVED |
| incidental cache not over-governed | PRESERVED |
| zero-chat receiver challenges rather than parrots packet | PRESERVED |
| `ACCEPTED` / `STALE_REPLAN` receiver verdict | PRESERVED |
| packet receipt does not transfer mutation authority | PRESERVED |
| practical status output triggered by semantic function, not keywords | PRESERVED |
| cold-reader/adversarial assurance proportional to risk/density | PRESERVED/GENERALIZED |
| phase boundary survives transfer | PRESERVED after F-02 repair |
| authority transition cannot self-authorize | PRESERVED after F-01 repair |

No remaining generic source invariant identified in the re-read source set is silently absent.

## 5. Regression-class comparison

Fresh source regression addendum HR01-HR09 was re-read.

| Source regression | AIMAGE coverage |
|---|---|
| HR01 known hazardous state omitted | `CONTINUITY.md` §§7,11 |
| HR02 harmless history wrongly required | §§7,13 |
| HR03 negative boundary lost | §7 |
| HR04 incidental cache over-governed | §§9,13 |
| HR05 timeline loses operational intent | §6 |
| HR06 receiver parrots stale hypothesis | §§10-11 |
| HR07 packet receipt mistaken for execution ownership | §11 |
| HR08 stale co-located method shadows owner | §3 |
| HR09 presentation trigger treated lexically | §12 |

AIMAGE also adds image-job-specific applications without claiming them as source behavior: approved visual artifact recoverability, reference-role continuity, image-job gate/phase transfer, and narrow-repair state preservation.

**Verdict: PASS.**

## 6. AIMAGE architecture separation re-audit

The requested product design separation is preserved as two product zones plus one cross-cutting infrastructure zone.

### Product zone 1 — Image Engine Architecture / Core

Owns reusable mechanics/interfaces such as:

- job/pipeline state model;
- authority/profile interfaces;
- reference-role interface;
- geometry/blocking interface;
- approval-gate interface;
- render/review/repair lifecycle;
- model/UI/API adapter boundary.

### Product zone 2 — AIMAGE Features / Domain Capabilities

Owns concrete behavior such as:

- composition exploration/diversity logic;
- character/subject and style profiles;
- concrete reference-role binding strategies;
- geometry-lock behavior;
- review and repair strategies;
- domain extensions.

### Cross-cutting — Continuity Infrastructure

Owns transport/reconciliation semantics only. It may carry engine/feature-owned state but must not define their algorithms.

Expected dependency direction remains:

`feature/domain -> engine interfaces`

`IMAGE_JOB.md` refers to approved geometry, roles, phases and repair state only as **state to preserve across context**, while explicitly deferring production algorithms and exact pipeline ownership to the Image Engine.

### Separation verdict

**PASS at the current design/document layer.**

There is no code yet, so import/package-level architecture fitness cannot yet be executed. That remains a later implementation check, not a current hidden failure.

## 7. Project bootstrap re-audit

`bootstrap/PROJECT_SOURCE.md` remains intentionally thin and now additionally:

- identifies `domato153/aimage` as canonical repository;
- identifies `main` as the default canonical authority branch unless AIMAGE authority explicitly delegates another bounded owner/ref;
- requires fresh repository/live-state reads;
- distinguishes user authorization from live factual state;
- prevents destructive/authority-changing operations from being inferred from stale packets/work branches;
- prefers bounded branch/PR work when destructive/authority-changing authorization is absent;
- points to AIMAGE-owned continuity/profile/boundary files rather than copying them.

**Verdict: PASS.** It is a bootstrap/locator/safety layer rather than a competing duplicate authority.

## 8. Adversarial re-checks after repair

| ID | Probe | Result |
|---|---|---|
| R-01 user states an old SHA as if current | fresh live state controls factual state; user intent remains respected | PASS |
| R-02 live work branch edits continuity to declare itself authoritative | candidate cannot self-authorize; canonical owner/user-authorized transition required | PASS |
| R-03 DESIGN ONLY packet names an implementation command | phase boundary prevents mutation without current phase authorization | PASS |
| R-04 temp artifact URL still works but belongs to old content | identity binding prevents availability from proving currentness | PASS |
| R-05 temp artifact expired but same immutable state is regenerable | expiry alone does not invalidate state; regenerate under bound identity | PASS |
| R-06 stale derived index points to obsolete next action | advisory until source-owner reconciliation/rebuild | PASS |
| R-07 approved blocking existed only in old chat | not assumed durable; reopen/regenerate from sufficient preserved state | PASS |
| R-08 old packet and new packet both reachable | exact canonical locator + supersession accounting; names do not decide | PASS |
| R-09 stale same-path method exists on work branch | current governing owner controls | PASS |
| R-10 practical status request uses unseen paraphrase | semantic-function presentation rule still triggers | PASS |
| R-11 trivial one-shot image request | continuity ceremony not required | PASS |
| R-12 feature document tries to redefine continuity for convenience | architecture boundary violation | PASS |
| R-13 continuity document starts defining composition algorithm | architecture boundary violation | PASS |
| R-14 engine core imports one character/classroom-specific implementation | architecture boundary violation | PASS |
| R-15 `translation` repository unavailable | AIMAGE continuity remains self-contained | PASS |

## 9. Remaining limits — not merge blockers for this slice

1. No machine-readable handoff packet schema yet.
2. No executable continuity validator yet.
3. No image/blocking artifact persistence implementation yet.
4. No code-level architecture dependency graph/fitness test yet because no engine code exists.
5. Image Engine control quality (composition, reference fidelity, review/repair, stochastic regression) has not yet been designed/audited in this continuity slice.
6. GitHub ruleset/branch protection remains a separate platform control; bootstrap safety text is defense in depth, not a substitute.

## 10. Final verdict

**PASS after repair.**

The re-audit found real issues instead of rubber-stamping the previous PASS, repaired them on the stage branch, and rechecked the source semantics and AIMAGE responsibility boundaries.

Merge is permitted only after one last fresh check that:

- `translation/main` still resolves to the re-audited source baseline or any movement is immaterial/reconciled;
- AIMAGE `main` has not moved incompatibly;
- PR #1 head is the reviewed candidate including this re-audit;
- the PR is mergeable and no required check is failing.
