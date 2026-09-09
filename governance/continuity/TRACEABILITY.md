# Continuity Adoption Traceability Matrix

Purpose: prove where the decision-relevant semantics of the read-only source continuity method went during AIMAGE adoption, and make omissions/over-adoption reviewable.

Source baseline is recorded in `SOURCE_PROVENANCE.md`.

Disposition values:

- `RETAIN` — generic semantics carried into AIMAGE substantially unchanged;
- `ADAPT` — generic invariant retained but source-domain terminology/mechanism replaced;
- `DROP` — source-repository-specific mechanism intentionally not adopted;
- `PROFILE` — valid only in an AIMAGE specialization rather than the common core.

## A0. Parent-skill dependencies that materially affect handoff semantics

The source handoff contract is owned by a parent maintenance skill. Most of that skill is maintenance-specific and is not imported. The following parent-skill semantics materially affect continuity and therefore must be explicitly closed rather than left as hidden runtime dependencies.

| ID | Source parent concept | Disposition | AIMAGE location | Verification |
|---|---|---|---|---|
| PS-001 | authority before memory / fresh authoritative state before claims | RETAIN | `../CONTINUITY.md` §§1-3,11 | stale-state cold start |
| PS-002 | phase is part of scope; do not cross review/design into mutation without authorization | PROFILE | `REPOSITORY_WORK.md` Phase boundary | design-only handoff mutation negative test |
| PS-003 | candidate-modified authority cannot self-authorize; transition needs trusted authorization | ADAPT | `../CONTINUITY.md` §2; `../../bootstrap/PROJECT_SOURCE.md` | self-authorizing-policy-change negative test |
| PS-004 | procedure/ceremony is itself a risk and should be proportional | RETAIN | `../CONTINUITY.md` §§8-9,13 | low-risk no-handoff / incidental-cache tests |
| PS-005 | distinguish confirmed/supported inference/unresolved when uncertainty matters | RETAIN | `../CONTINUITY.md` §6 | stale-hypothesis scenario |
| PS-006 | practical user-facing conclusion before internal technical record | RETAIN | `../CONTINUITY.md` §12 | semantic-presentation tests |
| PS-007 | handoff is live transfer; co-located stale method copy does not own semantics | RETAIN | `../CONTINUITY.md` §§3,11 | stale-method-shadow scenario |

All other maintenance-skill behavior remains outside the AIMAGE continuity runtime unless separately adopted by AIMAGE authority.

## A. Primary continuity contract mapping

| ID | Source concept | Disposition | AIMAGE location | Verification |
|---|---|---|---|---|
| CT-001 | handoff is continuity evidence, not project authority | RETAIN | `../CONTINUITY.md` §§1-2 | authority-conflict scenario |
| CT-002 | one exact canonical packet locator | RETAIN | `../CONTINUITY.md` §4 | ambiguous-CURRENT scenario |
| CT-003 | chat/paste summary derived from canonical packet | RETAIN | `../CONTINUITY.md` §§4,14 | derivative-without-locator negative test |
| CT-004 | predecessor locator explicit supersession/historical accounting | RETAIN | `../CONTINUITY.md` §4 | old-packet-still-reachable scenario |
| CT-005 | governing shared method resolved from authoritative owner | RETAIN | `../CONTINUITY.md` §3 | stale-method-shadow scenario |
| CT-006 | construction-time method identity may be recorded, receiver resolves current owner again | RETAIN | `../CONTINUITY.md` §3; `SOURCE_PROVENANCE.md` | method-drift scenario |
| CT-007 | record only dependencies whose movement can change next action/evidence/safety | RETAIN | `../CONTINUITY.md` §5 | bounded-dependency review |
| CT-008 | receiver independently re-derives minimum dependency set | RETAIN | `../CONTINUITY.md` §§5,11 | omitted-dependency scenario |
| CT-009 | bounded discovery surface for newly superseding/upstream work | ADAPT | `../CONTINUITY.md` §5; repository profile | newer-related-work scenario |
| CT-010 | active objective/problem | RETAIN | `../CONTINUITY.md` §6 | cold-reader synthesis |
| CT-011 | material hypothesis/uncertainty with epistemic status | RETAIN | `../CONTINUITY.md` §6 | stale-hypothesis scenario |
| CT-012 | exactly-one next action plus rationale | RETAIN | `../CONTINUITY.md` §§6,11 | ambiguous-next-action scenario |
| CT-013 | expected transition and bounded falsifier/contingency | RETAIN | `../CONTINUITY.md` §6 | route-change scenario |
| CT-014 | known decision-critical hazards survive transfer | ADAPT | `../CONTINUITY.md` §§7,11 | lost-known-hazard scenario |
| CT-015 | decision compression preserves needed rationale/negative boundary | RETAIN | `../CONTINUITY.md` §7 | lossy-decision scenario |
| CT-016 | examples/rationale do not silently become universal authority | RETAIN | `../CONTINUITY.md` §7 | over-generalization review |
| CT-017 | stale packet must replan when fresh dependency/authority makes next action non-unique | RETAIN | `../CONTINUITY.md` §10 | moved-ref and contradicted-premise scenarios |
| CT-018 | time passing or unrelated movement alone does not make packet stale | RETAIN | `../CONTINUITY.md` §10 | harmless-drift scenario |
| CT-019 | competing reachable work gets explicit lifecycle state only when ambiguity matters | ADAPT | `../CONTINUITY.md` §8 | competing-state scenario |
| CT-020 | source `candidate` terminology is not mandatory in generic continuity | DROP | explicit restraint in `../CONTINUITY.md` §8 | contamination search |
| CT-021 | one next executable action; no receiver guessing between peers | RETAIN | `../CONTINUITY.md` §§6,11 | two-actions hard-fail scenario |
| CT-022 | stable identity separated from temporary availability | RETAIN | `../CONTINUITY.md` §9 | expired-artifact scenario |
| CT-023 | local/session state classified durable/regenerate/unrecoverable | RETAIN | `../CONTINUITY.md` §§9,14 | missing-chat-artifact and hidden-local-state scenarios |
| CT-024 | decision-relevant derived artifacts need source/invalidation/rebuild semantics | RETAIN | `../CONTINUITY.md` §9 | stale-derived-view scenario |
| CT-025 | incidental caches do not require provenance ceremony | RETAIN | `../CONTINUITY.md` §§9,13 | harmless-cache scenario |
| CT-026 | receiver acts as zero-chat reader and challenges packet | RETAIN | `../CONTINUITY.md` §11 | cold-start rehearsal |
| CT-027 | receiver returns `ACCEPTED` or `STALE_REPLAN` | RETAIN | `../CONTINUITY.md` §11 | receiver verdict test |
| CT-028 | packet receipt is not execution ownership | RETAIN | `../CONTINUITY.md` §11 | pre-acceptance mutation negative test |
| CT-029 | practical receiver report is plain-language first by semantic function | RETAIN | `../CONTINUITY.md` §12 | paraphrase/raw-only/ambiguous presentation tests |
| CT-030 | dense/high-risk transfer may use cold-reader rehearsal | ADAPT | `../CONTINUITY.md` §13 | proportional-assurance review |
| CT-031 | permanent adversarial probes added only for recurring confirmed failure classes | RETAIN | `../CONTINUITY.md` §13 | ceremony review |
| CT-032 | completion criteria require recoverable/current/one-action transfer | RETAIN | `../CONTINUITY.md` §14 | matrix closure + cold start |
| CT-033 | decision-relevant temporary transport retains identity/provenance/expiry/regeneration semantics when applicable | ADAPT | `../CONTINUITY.md` §9 | transport-substitution/expiry scenario |
| CT-034 | stale/unbound decision-relevant derived view is advisory until reconciled/rebuilt | RETAIN | `../CONTINUITY.md` §9 | stale-derived-view scenario |

## B. Source maintenance-specific mechanisms intentionally not imported

| ID | Source mechanism | Disposition | Reason / replacement |
|---|---|---|---|
| MD-001 | maintenance-only R0/R1/R2/R3 risk taxonomy | DROP | AIMAGE continuity uses proportional assurance without importing maintenance review tiers. Future repository risk policy may define its own taxonomy separately. |
| MD-002 | promotion-specific authority/evidence workflow | DROP | not a generic continuity invariant; repository profile preserves only decision-relevant phase and verification state |
| MD-003 | proof receipt identity as a mandatory handoff field | DROP | evidence identity is recorded only when the next action depends on it |
| MD-004 | `candidate SHA/tree/parent` as universal terminology | ADAPT | generic immutable artifact/work identity; exact repository fields used only when applicable |
| MD-005 | deployment/promotion refs as typical mandatory dependencies | PROFILE | repository-work profile uses only refs relevant to the actual AIMAGE task |
| MD-006 | translation semantic/literary gates and source-sensitive translation rules | DROP | outside AIMAGE continuity domain |
| MD-007 | GitHub Actions/local-CI trust routing from translation maintenance | DROP | unrelated to continuity adoption; may be designed later under AIMAGE repository verification if needed |

## C. Confirmed regression-class coverage

The source regression addendum was reviewed as construction evidence. Its generic failure classes map as follows.

| Source case | Failure class | AIMAGE coverage |
|---|---|---|
| HR01 | known decision-critical hazard omitted | `CONTINUITY.md` §§7,11; audit case A-05 |
| HR02 | harmless history wrongly required | `CONTINUITY.md` §§7,13; audit case A-11 |
| HR03 | negative boundary lost in compression | `CONTINUITY.md` §7; audit case A-06 |
| HR04 | incidental derived cache over-governed | `CONTINUITY.md` §§9,13; audit case A-11 |
| HR05 | timeline complete but operational intent missing | `CONTINUITY.md` §6; audit case A-07 |
| HR06 | receiver parrots stale hypothesis | `CONTINUITY.md` §§10-11; audit case A-04 |
| HR07 | packet receipt mistaken for execution authority | `CONTINUITY.md` §11; audit case A-08 |
| HR08 | stale co-located method shadows owner | `CONTINUITY.md` §3; audit case A-03 |
| HR09 | user-facing status trigger treated lexically | `CONTINUITY.md` §12; audit case A-10 |

## D. AIMAGE-specific extensions added during adaptation

These are not claimed to come from the source continuity contract. They are AIMAGE-specific applications of generic continuity principles.

| ID | Extension | Owner |
|---|---|---|
| AX-001 | approved visual artifact recoverability | `IMAGE_JOB.md` |
| AX-002 | reference-role continuity preserves role, not just image presence | `IMAGE_JOB.md` |
| AX-003 | image-job phase/gate continuity without redefining engine pipeline | `IMAGE_JOB.md` |
| AX-004 | repair transfer separates failed variable from successful elements | `IMAGE_JOB.md` |
| AX-005 | continuity / engine / feature-domain responsibility separation | `../../architecture/BOUNDARIES.md` |

## E. Closure rule

This matrix is considered closed for the initial adoption only when:

1. every decision-relevant source continuity concept is represented above or explicitly classified as source-specific and dropped;
2. every material parent-skill dependency needed to interpret handoff semantics is internalized or explicitly classified rather than required at runtime;
3. no AIMAGE governing continuity rule requires `domato153/translation` at runtime;
4. every AIMAGE-specific extension has an AIMAGE owner rather than being falsely attributed to the source method;
5. the audit scenarios exercise both omission and over-adoption failure modes.
