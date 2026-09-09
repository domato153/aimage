# AIMAGE Continuity Contract

Status: governing continuity method for AIMAGE.

This contract defines how consequential AIMAGE work crosses chat, thread, operator, tool, or session boundaries. It is continuity infrastructure, not Image Engine product authority and not a reason to add ceremony to ordinary low-risk work.

## 1. Purpose

A receiver with no chat memory must be able to recover the current relevant state from fresh AIMAGE authority, detect stale transfer state, preserve decision-critical boundaries, and identify exactly one safe next action.

A handoff is not complete merely because it contains a detailed summary. It must remain usable when refs move, old files remain reachable, temporary artifacts disappear, or a prior explanation becomes stale.

## 2. Authority precedence

For operational truth, use this precedence unless a stricter AIMAGE authority file says otherwise:

1. explicit current user instruction;
2. current AIMAGE canonical authority and live repository state;
3. current governing AIMAGE method files resolved from their authoritative owner;
4. accepted continuity packet reconciled against 1-3;
5. derived chat/paste summaries;
6. memory or historical material.

A continuity packet is evidence about prior state. It never authorizes itself and never outranks fresh authority.

## 3. Governing-method owner resolution

Before using a consequential shared procedure, resolve its current governing copy from the AIMAGE owner surface that actually owns that procedure.

- Do not infer method authority from a same-named copy co-located with a work branch, packet, generated artifact, or historical snapshot.
- If a non-owner copy differs from the current owner copy, the owner copy controls.
- Record construction-time owner/ref/path/blob when a method version can materially change receiver behavior.
- At cold start, resolve the current owner again.
- If owner identity is ambiguous or materially changed such that the next action is no longer unique, return `STALE_REPLAN`.

For this contract, the intended owner after adoption is the canonical AIMAGE repository on its authoritative branch, not `domato153/translation` or any external source used during construction.

## 4. Canonical locator and single-source derivation

A consequential handoff publishes exactly one canonical packet locator containing enough information to resolve one immutable packet version:

- repository;
- ref;
- path;
- commit SHA or equivalent immutable identity.

A human-facing paste or chat bootstrap must be derived from that packet rather than independently reconstructed from memory. A shortened derivative must retain the canonical locator and require fresh reconciliation before consequential action.

If multiple files use names such as `CURRENT`, `final`, dates, or similar aliases, filename wording does not determine currentness. The canonical locator identifies the packet; fresh AIMAGE authority determines operational truth.

When a newer locator supersedes an older still-reachable locator, the current continuity state must explicitly classify the predecessor as superseded or historical when confusion could affect the next action. Historical packets should not be rewritten merely to mark them old.

## 5. Bounded continuity dependency set

Record only dependencies whose movement can change the next action, invalidate decision-relevant evidence, or alter a preserved safety/authority boundary.

Typical dependencies include:

- live authority refs or canonical state files;
- the governing method identity when its exact semantics matter;
- active work artifacts whose identity affects the next action;
- approved image-job artifacts when replacement would alter a locked decision;
- temporary or derived artifacts only when the next action actually depends on them.

Do not turn every branch, file, image, cache, or historical record into a continuity dependency.

For each material dependency record its role and frozen identity. Also identify one bounded discovery surface capable of revealing newly created upstream or superseding work relevant to the proposed next action. The receiver must independently re-derive the minimum dependency/discovery scope from current authority rather than trusting packet omissions.

If a material dependency was omitted and that omission makes the next action ambiguous or unsafe, return `STALE_REPLAN`.

## 6. Active situation model

A consequential handoff preserves the decision-relevant current situation, not a transcript.

When material, capture:

- current problem or objective;
- current phase;
- active hypothesis or uncertainty, with an epistemic label when useful (`confirmed`, `supported_inference`, `unresolved`);
- exactly one next action;
- why that action is next;
- expected information or state transition;
- bounded stop/replan condition.

Do not invent uncertainty to fill fields. Deterministic work may use a compact objective + rationale + stop condition.

The active situation model is continuity state, not authority. A receiver must challenge it against fresh authority before accepting it.

## 7. Decision and negative-boundary preservation

Preserve explicit user or authority decisions when losing them could reverse, broaden, or otherwise change future work.

When the rationale or negative boundary is necessary to prevent semantic inversion, preserve:

- the binding decision;
- the minimum rationale needed to interpret it correctly;
- the explicit negative boundary or non-goal.

Examples and discarded discussion remain non-authoritative unless the governing decision explicitly made them normative.

Do not copy the entire deliberation merely because some decision context must survive.

## 8. Competing-state ledger — only when needed

Use lifecycle labels only when multiple still-reachable states could plausibly be mistaken for executable current work.

Allowed labels:

- `ACTIVE` — currently eligible to advance after remaining gates;
- `BLOCKED` — cannot advance until a named dependency or decision closes;
- `SUPERSEDED` — replaced and must not be revived by existence alone;
- `REJECTED` — failed a material requirement and is history only;
- `HISTORICAL` — reference/evidence only, never current executable work.

Record `blocked_by` or `superseded_by` when material.

Do not require a candidate ledger for a simple image job or isolated repository edit with no ambiguity. The invariant is one unambiguous next action, not mandatory lifecycle bureaucracy.

## 9. Recoverability of local, temporary, and derived state

Separate stable identity from temporary availability.

Decision-relevant state that is not self-evidently durable must be classified as:

- `DURABLE` — recoverable by the next receiver from a named immutable or authoritative location;
- `REGENERATE` — not durable, but reproducible from named inputs and a bounded regeneration step without changing the intended state;
- `UNRECOVERABLE` — cannot be trusted or recovered; dependent claims must be reopened.

For decision-relevant derived artifacts, record enough provenance to know their source owner, invalidation trigger, and rebuild/reconciliation path. Incidental caches or views that cannot affect action, eligibility, authority, or safety do not need provenance ceremony.

For image jobs, visual artifacts shown only in an outgoing chat are not automatically durable. If an approved blocking/reference/render is required for the next action, its recoverability must be explicit.

## 10. Staleness and invalidation

Return `STALE_REPLAN` when fresh reconciliation shows that the recorded next action is no longer uniquely valid.

Typical triggers include:

- a material authority/dependency moved beyond the packet's recorded preimage;
- a newer upstream/superseding state changes ordering or eligibility;
- a material dependency was omitted;
- the governing method materially changed;
- a decision-critical premise is contradicted;
- a required visual or repository artifact is unrecoverable or no longer identity-equivalent;
- the packet relies on an ambiguous alias without an immutable locator;
- preserved hazards or negative boundaries conflict with newer authority.

A packet is not stale merely because time passed, an unrelated branch moved, wording changed without semantic impact, or a disposable artifact expired when the same state can be safely regenerated.

## 11. Receiver cold-start acceptance

The receiver behaves as though chat memory is unavailable.

Before consequential continuation:

1. open the canonical packet locator;
2. resolve the current governing AIMAGE continuity/shared-method owner;
3. read the packet's authority/non-authority boundary;
4. independently derive the minimum dependency and supersession-discovery scope from the proposed next action;
5. fresh-read the reconciled dependencies and relevant authority;
6. reconcile competing states, preserved decisions/negative boundaries, and recoverability entries;
7. verify identity of decision-relevant repository, image, or derived artifacts;
8. challenge the active situation model against fresh authority/evidence;
9. synthesize the current objective, exactly one next action and rationale, expected transition, stop/replan condition, and critical preserved constraints;
10. state why any still-reachable alternate state is not executable when ambiguity exists;
11. return exactly one verdict:
   - `ACCEPTED` — one next action remains valid and its rationale survived fresh challenge;
   - `STALE_REPLAN` — drift, omission, contradiction, or ambiguity changed or de-uniqued the next action.

Receiving a packet, opening a new thread, or seeing a branch does not itself transfer authority to mutate state. Reads and reconciliation needed to decide acceptance are allowed before acceptance; consequential continuation requires `ACCEPTED` or a stronger AIMAGE gate.

## 12. User-facing receiver report

When reporting practical status after reconciliation, give the plain-language conclusion first:

1. what is true now and whether work can advance;
2. the material problem or uncertainty that remains;
3. the one concrete next action;
4. any stop/replan condition the user needs to know.

Technical refs, SHAs, lifecycle labels, and traceability details may follow.

If the user explicitly requests only raw machine/receiver fields, the raw record may be returned without the plain-language preface. Ambiguous requests default to plain-language-first.

## 13. Proportional assurance

Do not turn continuity into mandatory ceremony for every image generation or trivial edit.

Use a cold-reader rehearsal and adversarial probes when transfer state is dense, authority-sensitive, destructive, hard to reconstruct, or semantically easy to invert. A compact low-risk transfer with obvious authority and no ambiguous alternatives does not need a separate rehearsal.

Permanent probes should be added only for confirmed recurring failure classes.

## 14. Completion criteria

A consequential AIMAGE handoff is complete when:

- one canonical immutable locator exists;
- the current governing method is resolved from the AIMAGE owner;
- material dependencies are bounded and recoverable;
- the active objective/phase and exactly one next action are preserved;
- decision-critical rationale and negative boundaries survive compression;
- ambiguous competing states are explicitly classified when needed;
- stale state cannot silently authorize continuation;
- decision-relevant derived/temporary artifacts have appropriate recoverability semantics;
- a cold-start receiver can challenge and reconstruct the next action from fresh AIMAGE authority;
- chat/paste derivatives point back to the canonical packet;
- runtime use of this contract requires no access to the construction-source repository `domato153/translation`.
