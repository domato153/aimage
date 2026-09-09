# AIMAGE Handoff Migration Traceability

Purpose: prove that the generic maintenance-handoff behavior was deliberately retained, adapted, or excluded rather than copied mechanically from `domato153/translation`.

| ID | Source concept | Decision | AIMAGE owner / treatment |
|---|---|---|---|
| H-001 | Handoff is a live transfer, not a static summary | RETAIN | `.agents/skills/handoff/SKILL.md` trigger/purpose |
| H-002 | Resolve handoff method from authoritative owner before packet use | RETAIN | `SKILL.md` §2 |
| H-003 | Same-path packet/candidate copy does not become governing method by co-location | RETAIN | `SKILL.md` §2 |
| H-004 | Fresh authority/live-state snapshot before handoff construction | RETAIN | `SKILL.md` §4.1 |
| H-005 | Immediate objective | RETAIN | `SKILL.md` §4.4 + packet template |
| H-006 | Explicit user intent / hard constraints | ADAPT | current phase/scope + preserved decisions/negative boundaries |
| H-007 | Phase boundary must survive handoff | RETAIN | `SKILL.md` §4.4, receiver workflow |
| H-008 | Preserve only current decision-relevant state, not full history | RETAIN | `SKILL.md` §5 |
| H-009 | Completed scope is distinct from remaining work | RETAIN | `SKILL.md` §4.4 |
| H-010 | Current blocker/uncertainty must be explicit | RETAIN | `SKILL.md` §4.4 |
| H-011 | Fresh refs override recorded literal snapshot | RETAIN | receiver reconciliation via AIMAGE continuity |
| H-012 | One bounded cold-start read route | RETAIN | `SKILL.md` §4.4/§6 |
| H-013 | Exact next task/action | RETAIN | `SKILL.md` §4.4 |
| H-014 | Expected state/evidence transition | RETAIN/GENERALIZE | `SKILL.md` §4.4 |
| H-015 | Hard prohibitions / stop boundary | RETAIN | `SKILL.md` §4.4 |
| H-016 | Continuity packet does not outrank live authority | RETAIN | delegated to `governance/CONTINUITY.md`; reinforced in `SKILL.md` |
| H-017 | Receiver must fresh-reconcile before operational ownership | RETAIN | `SKILL.md` §6 |
| H-018 | Packet receipt alone does not transfer execution authority | RETAIN | `SKILL.md` §6 |
| H-019 | Old packet/branch existence is not proof of currentness | RETAIN | `SKILL.md` §8 |
| H-020 | Derive user-facing paste from canonical packet, not memory rewrite | RETAIN | `SKILL.md` §10 |
| H-021 | Practical user status before internal records when appropriate | RETAIN | `SKILL.md` §7 |
| H-022 | Bounded dependency/freshness surface, not whole repository scan | RETAIN | continuity owner + `SKILL.md` quality gate |
| H-023 | Preserve decision rationale/negative boundary when compression could reverse decision | RETAIN | `SKILL.md` §5 |
| H-024 | Preserve hazardous/rejected/superseded state that could be resurrected | RETAIN/GENERALIZE | `SKILL.md` §5/§8 |
| H-025 | Temporary/local/derived evidence requires recoverability semantics only when decision-relevant | RETAIN | delegated to AIMAGE continuity; `SKILL.md` §4.4/§11 |
| H-026 | Cold-reader/adversarial rehearsal proportional to transfer risk | RETAIN | `SKILL.md` §11 |
| H-027 | External methods inform handoff shape but do not define repository authority | RETAIN | source provenance/audit boundary |
| H-028 | Maintenance snapshot can include large round history | NARROW | retain only completed scope and live-relevant rationale; do not transfer full adversarial history by default |
| H-029 | Risk tiers R0/R1/R2/R3 | DROP | maintenance-supervisor-specific risk taxonomy; AIMAGE handoff does not need it to function |
| H-030 | Translation CI/workflow run identities and exact test suites | DROP | domain-specific execution evidence; packet may carry analogous AIMAGE evidence only when it affects continuation |
| H-031 | Boneshaker/Coverage/Generic Core identities | DROP | source-project-specific |
| H-032 | Translation batch seam, POV, referent, manuscript/cursor state | DROP | owned by `40_seam_and_context_handoff.md`; explicitly excluded from generic AIMAGE handoff |
| H-033 | Promotion/proof-receipt/tx/work/draft branch machinery | DROP | translation-specific lifecycle; AIMAGE may independently adopt future equivalents |
| H-034 | Image-job geometry/reference/render state | AIMAGE EXTENSION | detailed ownership remains `governance/continuity/IMAGE_JOB.md`; generic handoff only transports it |
| H-035 | Engine/feature architecture state | AIMAGE EXTENSION | generic handoff can transport it but does not own architecture semantics |

## Dependency-closure result

The AIMAGE handoff method requires only:

- root `AGENTS.md`;
- `.agents/skills/handoff/SKILL.md`;
- `governance/CONTINUITY.md`;
- one applicable AIMAGE continuity profile;
- the live AIMAGE authority/artifacts needed by the concrete handoff.

No runtime edge points to `domato153/translation`, its maintenance skill, its tests, its CI, its batch workflow, or its translation seam protocol.
