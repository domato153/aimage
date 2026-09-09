# AIMAGE Handoff Skill

Status: governing AIMAGE handoff method only when resolved from the current authoritative owner. A work-branch/candidate copy is a proposed method and cannot authorize itself.

This skill owns **handoff construction and consumption**. It does not own project authority, repository state, image-generation algorithms, engine architecture, feature behavior, or the continuity state model itself.

For continuity semantics, freshness, stale/replan behavior, durable/local state, decision preservation, and receiver acceptance, this skill delegates to `governance/CONTINUITY.md` and the applicable continuity profile.

## 1. Trigger and non-trigger

Use this skill when one of the following is true:

- the user explicitly asks for a handoff to a new thread/operator/tool/session;
- consequential work will continue across a context boundary;
- stale state, unresolved dependencies, or phase ownership could materially change the next action;
- a long-running repository or image-production task needs a bounded cold-start continuation point.

Do not create handoff ceremony for ordinary low-risk work that remains in one context and can be completed directly.

A summary is not automatically a handoff. A handoff must support a fresh receiver that has no chat memory.

## 2. Governing-method owner resolution

Before producing or consuming a consequential handoff:

1. fresh-read current AIMAGE `main` and root `AGENTS.md`;
2. resolve this skill from its current authoritative owner;
3. resolve `governance/CONTINUITY.md` and the applicable profile from their current authoritative owner;
4. only then open or derive the handoff packet.

Do not bootstrap handoff semantics from a same-path copy that merely happens to be co-located with a packet, work branch, candidate, generated artifact, or old continuity ref.

A packet/candidate may carry a proposed copy of this skill, but that copy cannot authorize itself as the governing handoff method unless current AIMAGE authority explicitly delegates that role.

## 3. Boundary with continuity

Keep these responsibilities separate.

### Handoff skill owns

- when a handoff is warranted;
- how a sender constructs a bounded transfer packet;
- how a receiver starts from that packet;
- packet organization, compression, context filtering, and practical readability;
- one canonical packet locator and derived user-facing paste/share material;
- explicit transfer of the next bounded action, finish condition, and stop/replan conditions;
- material urgency, deadlines, commitments, or ownership only when they can change continuation.

### Continuity owns

- authority vs continuity evidence;
- canonical locator semantics;
- bounded continuity dependencies;
- active situation model;
- decision and negative-boundary preservation;
- stale/replan conditions;
- durable/regenerable/unrecoverable state;
- receiver `ACCEPTED` / `STALE_REPLAN` semantics;
- domain-specific continuity profiles such as repository work and image-production jobs.

Do not duplicate the full continuity contract here. Follow its current owner.

## 4. Sender workflow

For a consequential handoff, perform these steps in order.

### 4.1 Fresh reconciliation before writing the packet

Fresh-read the minimum authoritative AIMAGE state whose movement could change:

- current objective;
- phase and authorized scope;
- next executable action;
- safety or negative boundaries;
- relevant refs/files/artifacts;
- current blocker or unresolved hypothesis;
- any deadline, external commitment, or ownership boundary that materially changes what must happen next.

Do not freeze a handoff from chat memory alone.

### 4.2 Select the continuity profile

At minimum:

- repository development/architecture/maintenance work -> `governance/continuity/REPOSITORY_WORK.md`;
- image-production job -> `governance/continuity/IMAGE_JOB.md`.

A future subsystem may add another profile only when a real recurring state shape justifies it.

### 4.3 Establish one canonical packet locator

A durable handoff must have one canonical locator whose identity is sufficient to find the exact packet version.

Record, as applicable:

- repository;
- ref or owning branch;
- exact path;
- exact commit/object identity when available.

Chat text or a copied prompt may be derived from this packet, but must not become an independently rewritten second authority/continuity source.

### 4.4 Build the packet from current state

The packet should contain only information a cold receiver needs to recover the current work safely.

For a dense or high-consequence handoff, place a short **Operational Header** near the top so a receiver can immediately recover the active control state without scanning the whole packet. The header should contain only the applicable items below:

- packet locator/status;
- immediate objective;
- phase and explicit stop boundary;
- urgency/deadline/commitment when material;
- exact next bounded action;
- completion/acceptance criterion for that action;
- stop/replan trigger.

The Operational Header is a summary inside the canonical packet, not a second authority source. Compact handoffs may integrate these items into the normal sections instead of adding a separate header.

Required semantic sections:

1. **Identity / locator** — exact packet identity and provenance.
2. **Immediate objective** — what is being accomplished now, not the whole project history.
3. **Current phase and authorized scope** — including explicit stop boundary.
4. **Fresh authority snapshot** — only state whose current identity materially affects continuation.
5. **Current situation** — accepted facts, active uncertainty/hypothesis, and current blocker if any.
6. **Completed scope** — what is already closed and should not be redone without new evidence.
7. **Preserved decisions and negative boundaries** — especially decisions whose rationale prevents reversal or overgeneralization.
8. **Current dependencies / artifacts** — only decision-relevant dependencies; classify local/temporary state through the continuity contract.
9. **Exact next bounded action** — one executable next action plus why it is next.
10. **Completion / acceptance criteria** — what evidence or state proves the bounded action is finished. When completion is self-evident, this may be combined with the expected transition; for research/review/design work it must be explicit enough to prevent open-ended continuation.
11. **Expected transition** — what new state/evidence should result if the next action succeeds.
12. **Stop / replan conditions** — what fresh contradiction or drift invalidates the recorded route.
13. **Cold-start read route** — smallest ordered read set needed by a fresh receiver.
14. **Hard prohibitions** — only material actions that would violate current phase, preservation, authority, or user decisions.

Conditional sections that become required when material:

- **Urgency / time / commitments** — deadlines, expected response windows, promised follow-ups, external waits, or other timing facts that can change ordering or ownership. Absence of a deadline need not be stated for ordinary work, but a consequential time constraint must not be lost.
- **Material delta from predecessor** — when this packet supersedes another still-reachable packet, state the small set of changes that make the successor operationally different. Do not restate the whole predecessor.
- **Ownership / external party** — when an action is waiting on or assigned to someone other than the receiving operator, record who owns that dependency and what event returns control.

Optional sections are allowed when they materially reduce ambiguity. Do not fill a template mechanically when a section has no decision value.

### 4.5 Context filtering and durable-state separation

Treat a handoff as a filtered operational context, not as a dump of all prior conversation or application state.

- If durable state already exists in an AIMAGE-owned repository file, artifact, or authoritative service, point to that owner/identity and transfer only the decision-relevant interpretation or delta.
- Keep routing/transfer metadata such as reason, priority, summary, or urgency separate from durable project state and dependencies.
- Do not duplicate entire canonical specifications into the packet merely so the receiver can avoid opening the owner file.
- Do not forward tool chatter, obsolete alternatives, or incidental history that does not affect the next action.
- If filtering something out could change the next action, reverse a settled decision, hide a hazard, or make the receiver believe a dependency is complete when it is not, the omission is unsafe.

This preserves the useful property of agent handoff input filtering: the receiver gets the minimum context required for correct continuation while durable application/project state remains in its owning system.

### 4.6 Publication closeout and status accounting

Packet construction is not the final sender step for a consequential repository handoff. After the canonical packet is actually published/adopted and its immutable identity is known:

1. fresh-read the live authority and the applicable current continuity/status locator;
2. distinguish the packet's historical construction snapshot from current live state;
3. reconcile any status that changed because publication/adoption happened, such as `candidate` becoming accepted, a work branch becoming historical, or a successor packet becoming the canonical transfer locator;
4. repair stale current-status metadata when leaving it unchanged could make the receiver choose a different next action or return a false `STALE_REPLAN`;
5. confirm that all decision-relevant state the packet claims as durable is actually reachable from its recorded owner/locator;
6. only then derive or finalize user-facing paste/share material.

Do not rewrite an immutable historical packet merely because `main` moved after publication. Its construction SHA is provenance. Currentness comes from fresh authority and current continuity state.

Do not create a self-referential requirement that a mutable `CURRENT`-style file encode the commit SHA that will only exist after that file is committed. Prefer a fresh-read rule for live HEAD plus immutable identities for historical packets/evidence when self-encoding would become stale by construction.

This closeout is status accounting, not a new authority transition mechanism. A handoff packet still cannot authorize its own adoption.

### 4.7 Semantic-equivalence check for derived transfer material

For a dense or consequential handoff, a shortened paste prompt, chat bootstrap, or other derived transfer form must be checked against the finalized canonical packet before delivery.

The derivative does not need textual identity, but it must preserve every material control field whose loss or broadening could change receiver behavior. Check, when applicable:

- canonical immutable locator and authority-first/fresh-reconciliation instruction;
- immediate objective;
- current phase and stop boundary;
- exactly one next bounded action;
- completion/acceptance criterion and evidence-sufficiency exit condition;
- stop/replan conditions;
- binding decisions, negative boundaries, and known rejected/superseded states needed to prevent reversal;
- material urgency, deadline, ownership, or external-wait condition;
- exceptional permissions or prohibitions that narrow the phase boundary, including bounded research/probing permissions when material;
- recoverability/hidden-local-state facts when their omission could cause the receiver to assume an unavailable dependency exists.

A derivative may omit detail already reachable from the canonical packet when it explicitly tells the receiver to open that packet before consequential action and the omission cannot change the next action, authorization boundary, completion judgment, or stale/replan verdict.

If the derivative broadens permission, weakens a prohibition, drops a material condition, changes the finish criterion, or makes a different next action plausible, repair it before delivery. When unsure, prefer pointing back to the canonical packet rather than duplicating more state.

## 5. Compression rules

A good handoff is a selective operational state transfer, not a transcript archive.

Preserve:

- the current objective;
- the current phase/scope boundary;
- exact current facts needed for continuation;
- active blocker/uncertainty and its epistemic status;
- decisions plus rationale/negative boundary when that rationale prevents a bad reversal;
- known hazardous/rejected/superseded states that a receiver could otherwise accidentally resurrect;
- successful elements that a repair must preserve;
- one exact next action, its finish condition, and expected transition;
- material time/ownership commitments when they affect continuation;
- the material successor delta when a predecessor could still be mistaken for current.

Do not copy:

- the full conversation;
- every historical branch/ref;
- every explored alternative once its decision value is exhausted;
- incidental caches or derived views that can be regenerated and do not affect the next action;
- verbose explanations that are already owned by canonical AIMAGE files.

If omission could cause a fresh receiver to choose a materially different next action, reverse a settled decision, cross a phase boundary, miss a commitment, or resurrect rejected state, the omitted information is not harmless.

## 6. Receiver workflow

A fresh receiver must not execute the packet immediately.

1. Resolve root `AGENTS.md`, this skill, `governance/CONTINUITY.md`, and the applicable profile from current AIMAGE authority.
2. Open the packet from its canonical locator.
3. Independently re-derive the minimum continuity dependency set needed for the recorded objective and next action.
4. Fresh-read those live dependencies.
5. Reconcile packet state against fresh authority and live facts.
6. Check current phase, preserved decisions/negative boundaries, blockers, local/temporary artifact status, supersession/rejection state, and any material deadline/commitment/ownership boundary.
7. Challenge the packet's exact next action: confirm that it is still unique and executable.
8. Challenge its completion/acceptance criteria: confirm that the receiver can tell when the bounded action is done rather than silently widening the task.
9. Synthesize/read back the practical control state: objective, one next action, finish condition, material contingency/stop trigger, and any material time/ownership constraint.
10. Return the continuity verdict required by `governance/CONTINUITY.md`: `ACCEPTED` or `STALE_REPLAN`.
11. Only after `ACCEPTED`, assume operational ownership and execute the next bounded action.

Packet receipt alone is not transfer of execution authority.

If a material ambiguity cannot be resolved from fresh authority or bounded evidence, do not guess merely to complete the handoff. Return `STALE_REPLAN` or surface the blocker according to current AIMAGE authority.

## 7. Receiver synthesis

Before continuing, the receiver should be able to state in ordinary language:

- what is currently being done;
- what is already closed;
- what remains uncertain or blocked;
- what must be preserved or not crossed;
- exactly one next action;
- what proves that next action is complete;
- what would force a replan;
- any material deadline, external wait, or ownership boundary.

When the user asks for practical status, give the plain-language synthesis first and technical refs/SHAs afterward. A raw-record-only request is an explicit exception.

## 8. Supersession and stale packets

A still-existing packet or branch is not proof that it remains current.

If a newer packet replaces an older one, or live authority materially invalidates the old route:

- mark or treat the old packet as superseded/historical according to current AIMAGE continuity semantics;
- state the material delta in the successor when the predecessor remains plausibly reachable and the difference affects continuation;
- do not select packets by filename words such as `CURRENT`, `FINAL`, or timestamp alone;
- do not reuse an old successful action/proof merely because its branch or artifact still exists;
- replan from fresh authority when the continuity contract requires it.

Harmless time passage or unrelated repository movement does not by itself invalidate a handoff. A deadline or commitment does matter when missing it changes the valid next action.

## 9. AIMAGE-specific handoff considerations

### Repository / engine-development handoff

Preserve, when material:

- current architecture/design objective;
- accepted vs candidate state;
- phase boundary such as review/design/implementation/verification/adoption;
- changed files/refs whose identity matters;
- invariants and preserved behavior;
- unresolved architecture or verification risk;
- exact next bounded engineering action and its completion criterion;
- deadline/external wait/owner only if it changes continuation.

For a **research, review, or audit** handoff, also preserve an evidence-sufficiency / exit condition. A receiver must know when enough evidence has been gathered to close the bounded action; “research this topic” is not an adequate finish condition for consequential work.

Do not import translation-specific promotion, proof-receipt, batch, manuscript, Coverage, or CI semantics unless AIMAGE independently adopts an equivalent mechanism.

### Image-production job handoff

Preserve, when material:

- current image-job phase;
- character/subject/style authority;
- reference-role bindings;
- approved geometry/blocking/layout authority;
- successful visual elements that repair must preserve;
- rejected/superseded composition directions that must not be resurrected;
- current render/review/repair target;
- exact next image action and what visual evidence counts as success.

Do not turn these image-job fields into the generic handoff core. Their detailed state belongs to `governance/continuity/IMAGE_JOB.md` and future image-engine/domain owners.

## 10. Derived user-facing paste/share material

When the user wants a prompt to paste into a new thread, derive it from the canonical handoff packet after the packet is finalized and publication closeout has reconciled live status.

The paste/share form should:

- point the receiver to current AIMAGE authority first;
- include the canonical handoff locator;
- preserve current objective, phase, negative boundaries, exact next action, finish condition, and stale/replan instruction;
- preserve material urgency/deadline/ownership when applicable;
- preserve exceptional permissions/prohibitions and recoverability facts when their omission could change receiver behavior;
- tell the receiver to perform fresh reconciliation and practical read-back before action;
- avoid duplicating large canonical specifications already reachable from `AGENTS.md`.

For dense or consequential derivatives, run the semantic-equivalence check in section 4.7 before delivery.

Do not independently rewrite the handoff from memory after the canonical packet is created.

## 11. Quality gate before publishing a consequential handoff

Before treating a handoff as ready, verify:

- the governing handoff method was resolved from current authority;
- the packet was built from fresh state, not stale chat memory;
- the canonical locator is unambiguous;
- continuity dependencies are bounded rather than repository-wide by default;
- current objective and phase are explicit;
- dense/high-consequence packets expose a concise operational header or equivalent top-level control state;
- completed scope is distinguishable from remaining work;
- decision rationale/negative boundaries are preserved where material;
- known rejected/superseded/hazardous states cannot be silently resurrected;
- a successor identifies the material delta from any still-reachable predecessor when confusion could affect execution;
- local/temporary artifacts are classified sufficiently for a cold receiver;
- there is exactly one next executable action;
- the action has a usable completion/acceptance criterion rather than an open-ended topic;
- material deadline/commitment/ownership facts are preserved when they can change ordering or responsibility;
- stop/replan conditions are explicit;
- packet context is filtered and durable state remains in its owning source rather than being redundantly mirrored;
- after actual packet publication/adoption, live continuity/status accounting has been reconciled and no accepted state remains mislabeled as a candidate/current executable branch;
- immutable packet provenance is not confused with live current-state aliases, and no self-referential current-SHA requirement becomes stale by construction;
- any dense/consequential paste/share derivative passed the section 4.7 semantic-equivalence check;
- a zero-chat receiver can recover the route without reading `domato153/translation`.

For dense/high-risk transfers, perform a cold-reader or adversarial rehearsal. Do not make that ceremony mandatory for trivial handoffs.

## 12. Dependency boundary

Runtime AIMAGE handoff execution depends only on AIMAGE-owned authority routed from root `AGENTS.md`.

`domato153/translation` and external handoff methods are construction/audit evidence only. A receiver must never need to read them to understand or execute an AIMAGE handoff.

External-method re-audits may be preserved under `audits/` for provenance and future review, but they do not outrank this current AIMAGE-owned skill.