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
- packet organization, compression, and practical readability;
- one canonical packet locator and derived user-facing paste/share material;
- explicit transfer of the next bounded action and stop/replan conditions.

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
- current blocker or unresolved hypothesis.

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
10. **Expected transition** — what new state/evidence should result if the next action succeeds.
11. **Stop / replan conditions** — what fresh contradiction or drift invalidates the recorded route.
12. **Cold-start read route** — smallest ordered read set needed by a fresh receiver.
13. **Hard prohibitions** — only material actions that would violate current phase, preservation, authority, or user decisions.

Optional sections are allowed when they materially reduce ambiguity. Do not fill a template mechanically when a section has no decision value.

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
- one exact next action and its expected transition.

Do not copy:

- the full conversation;
- every historical branch/ref;
- every explored alternative once its decision value is exhausted;
- incidental caches or derived views that can be regenerated and do not affect the next action;
- verbose explanations that are already owned by canonical AIMAGE files.

If omission could cause a fresh receiver to choose a materially different next action, reverse a settled decision, cross a phase boundary, or resurrect rejected state, the omitted information is not harmless.

## 6. Receiver workflow

A fresh receiver must not execute the packet immediately.

1. Resolve root `AGENTS.md`, this skill, `governance/CONTINUITY.md`, and the applicable profile from current AIMAGE authority.
2. Open the packet from its canonical locator.
3. Independently re-derive the minimum continuity dependency set needed for the recorded objective and next action.
4. Fresh-read those live dependencies.
5. Reconcile packet state against fresh authority and live facts.
6. Check current phase, preserved decisions/negative boundaries, blockers, local/temporary artifact status, and supersession/rejection state.
7. Challenge the packet's exact next action: confirm that it is still unique and executable.
8. Return the continuity verdict required by `governance/CONTINUITY.md`: `ACCEPTED` or `STALE_REPLAN`.
9. Only after `ACCEPTED`, assume operational ownership and execute the next bounded action.

Packet receipt alone is not transfer of execution authority.

## 7. Receiver synthesis

Before continuing, the receiver should be able to state in ordinary language:

- what is currently being done;
- what is already closed;
- what remains uncertain or blocked;
- what must be preserved or not crossed;
- exactly one next action;
- what would force a replan.

When the user asks for practical status, give the plain-language synthesis first and technical refs/SHAs afterward. A raw-record-only request is an explicit exception.

## 8. Supersession and stale packets

A still-existing packet or branch is not proof that it remains current.

If a newer packet replaces an older one, or live authority materially invalidates the old route:

- mark or treat the old packet as superseded/historical according to current AIMAGE continuity semantics;
- do not select packets by filename words such as `CURRENT`, `FINAL`, or timestamp alone;
- do not reuse an old successful action/proof merely because its branch or artifact still exists;
- replan from fresh authority when the continuity contract requires it.

Harmless time passage or unrelated repository movement does not by itself invalidate a handoff.

## 9. AIMAGE-specific handoff considerations

### Repository / engine-development handoff

Preserve, when material:

- current architecture/design objective;
- accepted vs candidate state;
- phase boundary such as review/design/implementation/verification/adoption;
- changed files/refs whose identity matters;
- invariants and preserved behavior;
- unresolved architecture or verification risk;
- exact next bounded engineering action.

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
- exact next image action.

Do not turn these image-job fields into the generic handoff core. Their detailed state belongs to `governance/continuity/IMAGE_JOB.md` and future image-engine/domain owners.

## 10. Derived user-facing paste/share material

When the user wants a prompt to paste into a new thread, derive it from the canonical handoff packet after the packet is finalized.

The paste/share form should:

- point the receiver to current AIMAGE authority first;
- include the canonical handoff locator;
- preserve current objective, phase, negative boundaries, exact next action, and stale/replan instruction;
- tell the receiver to perform fresh reconciliation before action;
- avoid duplicating large canonical specifications already reachable from `AGENTS.md`.

Do not independently rewrite the handoff from memory after the canonical packet is created.

## 11. Quality gate before publishing a consequential handoff

Before treating a handoff as ready, verify:

- the governing handoff method was resolved from current authority;
- the packet was built from fresh state, not stale chat memory;
- the canonical locator is unambiguous;
- continuity dependencies are bounded rather than repository-wide by default;
- current objective and phase are explicit;
- completed scope is distinguishable from remaining work;
- decision rationale/negative boundaries are preserved where material;
- known rejected/superseded/hazardous states cannot be silently resurrected;
- local/temporary artifacts are classified sufficiently for a cold receiver;
- there is exactly one next executable action;
- stop/replan conditions are explicit;
- a zero-chat receiver could recover the route without reading `domato153/translation`.

For dense/high-risk transfers, perform a cold-reader or adversarial rehearsal. Do not make that ceremony mandatory for trivial handoffs.

## 12. Dependency boundary

Runtime AIMAGE handoff execution depends only on AIMAGE-owned authority routed from root `AGENTS.md`.

`domato153/translation` is construction provenance and audit evidence only. A receiver must never need to read it to understand or execute an AIMAGE handoff.