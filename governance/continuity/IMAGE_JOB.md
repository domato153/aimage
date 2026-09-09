# Image-Job Continuity Profile

This profile specializes `../CONTINUITY.md` for an image-production job that crosses a chat/thread/session boundary. It transports image-job state; it does not own or redefine Image Engine behavior.

## Purpose

A fresh receiver should be able to continue the same image job without reconstructing intent from memory, reviving rejected compositions, silently changing approved geometry, or treating an old visual artifact as current merely because it is still visible.

## Minimum job state

Record only what matters to continuation:

- job identifier or canonical job path;
- current job phase;
- current objective/scene intent;
- applicable subject/character profile identity;
- applicable style profile identity;
- reference-role bindings that materially affect the next step;
- approved geometry/blocking identity, when approval has occurred;
- render-spec identity, when locked;
- explicit preserved decisions and negative boundaries;
- successful elements that a repair must preserve;
- current failure/uncertainty, if any;
- exactly one next action and rationale;
- expected state transition;
- stop/replan condition.

Do not require unused fields. A one-shot low-risk image request with no cross-context state may need no continuity packet at all.

## Reference-role continuity

When a reference is decision-relevant, preserve the role it was approved for rather than only the fact that the image existed.

Examples of roles may include:

- identity/subject;
- style/rendering language;
- composition/geometry;
- approved blocking/layout;
- scene-specific prop or environment reference.

A reference does not gain additional authority merely because it is present in the packet. If the job authority says a reference is identity-only, a future receiver must not silently reuse its pose or composition.

## Approved visual artifacts

After user approval, a geometry/blocking artifact can become decision-relevant job state. Record:

- artifact identity or recoverable locator;
- approved role;
- what is locked by the approval;
- what remains free to change;
- recoverability as `DURABLE`, `REGENERATE`, or `UNRECOVERABLE` when not self-evident.

If an approved artifact existed only in an old chat and cannot be recovered reliably, do not pretend the lock survived. Reopen the dependent step or regenerate from a sufficiently precise preserved spec.

## Phase continuity

The packet must prevent accidental phase skipping. Typical phases may include intake, composition exploration, geometry/blocking approval, render-spec lock, render, review, and repair, but the exact engine state machine is owned elsewhere.

Continuity records the current phase and the gate already satisfied; it does not define the pipeline itself.

## Rejected and superseded visual states

Use lifecycle labels only when needed to avoid ambiguity.

Examples:

- a rejected blocking that remains visible in chat must not become current again;
- a superseded render spec must not be chosen because its file name says `final`;
- an earlier successful render may remain `HISTORICAL` reference without being the current repair target.

## Repair continuity

When continuing a repair, preserve the failure variable and successful elements separately.

A fresh receiver should know:

- what failed;
- what already succeeded and should remain unchanged;
- which control variable is intended to change;
- what would count as repair success;
- what result would require abandoning the repair path and re-planning.

This prevents a narrow repair from becoming an uncontrolled full reroll solely because context was lost.

## Receiver acceptance

Before continuing a consequential image job, a fresh receiver must reconcile the packet against current AIMAGE authority and available artifacts, then determine whether the one next action remains uniquely justified.

Return `STALE_REPLAN` if, for example:

- an approved geometry/reference artifact is missing or identity-ambiguous;
- a newer user decision changes a lock or negative boundary;
- the recorded phase conflicts with current job state;
- multiple competing compositions/renders appear executable with no supersession decision;
- an adapter/model capability change invalidates the planned next operation.
