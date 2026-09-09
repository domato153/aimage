# AIMAGE Handoff Skill Migration Audit

Status: candidate audit for `aimage-stage/handoff-skill-adoption`.

## 1. Audit question

Does AIMAGE now have a self-contained maintenance-style handoff method, derived from the generic parts of `domato153/translation`, while:

- removing translation runtime dependencies;
- keeping continuity and handoff as separate responsibilities;
- preserving the useful maintenance-handoff failure defenses;
- avoiding translation batch/seam, Boneshaker, Coverage, CI, promotion, or manuscript contamination;
- keeping root `AGENTS.md` as the single repository-native router?

## 2. Source boundary checked

Read-only construction sources are recorded in `.agents/skills/handoff/references/SOURCE_PROVENANCE.md`.

The audit distinguishes:

- generic maintenance handoff exemplars and parent-skill handoff semantics;
- AIMAGE's already-adopted continuity contract;
- translation-domain `40_seam_and_context_handoff.md`, which is explicitly excluded from generic handoff adoption.

Result: **PASS**.

## 3. Dependency-closure audit

Runtime route from root startup:

`AGENTS.md -> .agents/skills/handoff/SKILL.md -> governance/CONTINUITY.md -> applicable continuity profile -> live AIMAGE authority/artifacts`

No runtime step requires:

- `domato153/translation`;
- `maintenance-regression-supervisor/SKILL.md`;
- translation tests/evaluation corpus;
- Boneshaker/Coverage state;
- translation `work/draft/tx` conventions;
- translation CI/proof/promotion machinery;
- `40_seam_and_context_handoff.md`.

`domato153/translation` appears only in provenance, traceability, explicit exclusion language, and the quality gate that verifies independence.

Result: **PASS**.

## 4. Continuity vs handoff separation audit

### Continuity remains owner of

- authority vs packet semantics;
- canonical locator semantics;
- bounded continuity dependencies;
- situation model;
- decision/negative-boundary preservation;
- staleness/invalidation;
- local/temporary/derived-state recoverability;
- receiver `ACCEPTED` / `STALE_REPLAN` semantics.

### Handoff now owns

- handoff trigger/non-trigger;
- governing handoff-method bootstrap;
- sender packet construction workflow;
- packet compression/readability;
- cold-start read route;
- completed-scope/current-blocker/next-action organization;
- derived paste/share generation;
- receiver orchestration around the continuity acceptance gate.

The handoff skill delegates continuity semantics instead of introducing a second stale/acceptance system.

Some invariant-level overlap is intentional: both surfaces mention fresh reconciliation, one locator, one next action, and packet non-authority because those are interface contracts between the two responsibilities. The detailed semantic owner remains `governance/CONTINUITY.md`.

Result: **PASS**.

## 5. AGENTS routing audit

Root `AGENTS.md` now has explicit, separate routes:

- **Continuity routing** -> `governance/CONTINUITY.md` plus profile;
- **Handoff routing** -> `.agents/skills/handoff/SKILL.md`, which then invokes continuity.

This avoids the previous ambiguity where handoff behavior existed only implicitly inside continuity language.

`bootstrap/PROJECT_SOURCE.md` remains intentionally unchanged because it already routes all consequential work through current root `AGENTS.md`; duplicating the new handoff route into Project source would create a second specification surface.

Result: **PASS**.

## 6. Source-fidelity / traceability audit

`.agents/skills/handoff/references/TRACEABILITY.md` maps generic source concepts to `RETAIN`, `ADAPT`, `DROP`, or AIMAGE extension decisions.

Preserved generic maintenance-handoff concepts include:

- live transfer rather than static summary;
- method-owner resolution before packet use;
- fresh authority snapshot;
- immediate objective;
- phase/scope boundary;
- hard user constraints / negative boundaries;
- completed scope vs remaining work;
- current blocker/uncertainty;
- bounded cold-start route;
- one exact next action;
- expected transition;
- hard prohibitions / stop conditions;
- packet non-authority and receiver reconciliation;
- current-state-over-recorded-literal precedence;
- proportional cold-reader/adversarial rehearsal.

Result: **PASS**.

## 7. Contamination audit

Explicitly dropped or non-imported:

- translation source/target seam checks;
- POV/referent/manuscript/cursor state;
- batch sentence windows;
- Boneshaker identities;
- Coverage v2 phase names;
- exact translation CI workflow/test requirements;
- translation promotion/proof-receipt semantics;
- translation `work/draft/tx` lifecycle as a generic requirement;
- maintenance-supervisor R0-R3 taxonomy as a handoff prerequisite.

The AIMAGE skill contains a short negative statement naming some of these only to prohibit accidental import; they are not runtime mechanisms.

Result: **PASS**.

## 8. Authority/self-authorization audit

A first candidate draft described itself as canonical. That wording was corrected before adoption.

Current rule:

> the handoff skill is governing only when resolved from the current authoritative owner; work-branch/candidate copies are proposals and cannot authorize themselves.

This matches AIMAGE continuity's existing authority rule and the source handoff-method-shadowing regression lesson.

Result after repair: **PASS**.

## 9. External-method countercheck

External methods are method evidence only, not AIMAGE authority.

### Google SRE incident management

The SRE Book's `Clear, Live Handoff` guidance requires explicit live transfer and acknowledgment, and its incident-state guidance favors a living document with the most important current information near the top. This supports AIMAGE's live-transfer framing, current-state-first packet structure, and explicit receiver acceptance rather than passive summary inheritance.

### NIST configuration-management baseline principle

NIST SP 800-128 defines a baseline as a formally reviewed current configuration used for future changes and states that older approved baselines are retained for history/rollback after a new baseline becomes current. This supports resolving the current governing method/authority rather than treating an older co-located copy as current.

These sources justify the method shape only; they do not define AIMAGE repository authority.

Result: **consistent with external method evidence**.

## 10. Adversarial regression probes

The candidate design was checked conceptually against the following failures:

1. **Stale method shadowing:** packet branch carries an older/newer same-path handoff skill -> receiver must resolve authoritative owner first. **PASS**.
2. **Static-summary execution:** detailed handoff pasted into new thread -> receiver must still fresh-reconcile and return `ACCEPTED`/`STALE_REPLAN`. **PASS**.
3. **Phase loss:** design-only work packet contains an obvious implementation -> phase/stop boundary survives and blocks automatic crossing. **PASS**.
4. **Decision compression loss:** a rejected direction's rationale is omitted and could be resurrected -> material negative boundary must be preserved. **PASS**.
5. **Whole-history bloat:** large maintenance history exists -> packet keeps only completed scope and rationale that changes continuation. **PASS**.
6. **Unrelated ref movement:** irrelevant branch changes -> does not automatically stale the handoff. **PASS**.
7. **Temporary artifact loss:** next action depends on an outgoing-chat-only visual -> continuity recoverability classification is required. **PASS**.
8. **Old branch resurrection:** old successful candidate still exists -> existence alone does not restore executability. **PASS**.
9. **Translation contamination:** receiver tries to read `40_seam_and_context_handoff.md` for AIMAGE thread transfer -> no runtime route points there. **PASS**.
10. **Project-source duplication:** bootstrap copies handoff rules -> current design leaves bootstrap thin and routes through `AGENTS.md`. **PASS**.

## 11. Architecture-boundary audit

`architecture/BOUNDARIES.md` now separates:

- Continuity & Handoff Infrastructure;
- Image Engine Architecture / Core;
- AIMAGE Features / Domain Capabilities.

Within infrastructure the dependency direction is explicitly:

`handoff -> continuity contract/profiles`

Continuity does not require the handoff skill merely to define state/freshness/acceptance semantics, while handoff does not own product behavior.

Result: **PASS**.

## 12. Residual uncertainty

Not yet implemented, by design:

- automated schema/validator for packet structure;
- one fixed repository directory for every handoff packet;
- automated stale detection;
- automated cold-reader simulation;
- subsystem-specific handoff profiles beyond repository work and image jobs.

These are not required to adopt the current governing method. Add them only when real use demonstrates recurring value.

## 13. Adoption verdict

**PASS for adoption**, provided final pre-merge reconciliation confirms:

- AIMAGE `main` has not moved unexpectedly;
- candidate head matches this audited content;
- PR is mergeable/clean;
- no new authoritative AIMAGE rule conflicts with this candidate.
