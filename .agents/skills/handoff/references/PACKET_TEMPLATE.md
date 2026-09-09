# AIMAGE Handoff Packet Template

Use this as a semantic checklist, not a form that must be filled mechanically.

A packet is continuity evidence, not project authority.

For a dense/high-consequence handoff, place a short **Operational Header** first. Compact handoffs may fold the same items into the normal sections.

## Operational Header — when useful

- Packet locator/status:
- Immediate objective:
- Phase / stop boundary:
- Urgency/deadline/commitment, if material:
- Exact next bounded action:
- Completion/acceptance criterion:
- Stop/replan trigger:

## Identity / locator

- Repository:
- Owning ref/branch:
- Path:
- Exact commit/object identity:
- Packet status:

## Material delta from predecessor — when applicable

If this packet supersedes a still-reachable predecessor, list only the changes that make the successor operationally different.

## Immediate objective

State the current bounded objective in practical terms.

## Current phase and authorized scope

- Phase:
- Authorized work:
- Explicit stop boundary:

## Urgency / time / commitments — when material

- Deadline/time window:
- External promise or expected response:
- Does missing the timing change the next action?:

Omit this section when timing has no decision value.

## Fresh authority snapshot

Record only state whose identity can change the next action.

- Canonical/main state:
- Active work/candidate state:
- Relevant governing files/artifacts:

Fresh live state always outranks these recorded literals if they later drift.

## Current situation

- Confirmed facts:
- Supported inference, if any:
- Unresolved question/blocker, if any:

## Completed scope

List work that is already closed and should not be repeated without new evidence.

## Preserved decisions / negative boundaries

Record decisions, rationale, exclusions, rejected/superseded directions, or successful elements whose loss could change the next action or cause regression.

## Decision-relevant dependencies / artifacts

List only bounded dependencies needed for continuation. For local/temporary/derived artifacts, record the continuity classification/rebuild path when material.

If durable state already exists in an AIMAGE-owned file/artifact/service, point to it rather than mirroring the full state into this packet. Transfer only the decision-relevant interpretation or delta.

## Ownership / external party — when material

If continuation is waiting on someone/something other than the receiver:

- Owner/external party:
- Pending action/event:
- What event returns control to the receiver:

## Exact next bounded action

One executable next action:

Why this action is next:

## Completion / acceptance criteria

What proves the bounded action is finished?

For research/review/design work, state an evidence-sufficiency or exit condition so the task cannot expand into indefinite investigation.

## Expected transition

State what new state, evidence, artifact, or decision should exist after the next action succeeds.

## Stop / replan conditions

List the fresh-state changes or contradictions that invalidate the recorded route.

## Cold-start read route

Ordered minimum read set for a zero-chat receiver:

1.
2.
3.

Do not list the entire repository by default.

## Hard prohibitions

Only material prohibitions that protect current authority, phase, preservation, or explicit user decisions.

## Receiver acceptance

The receiver must resolve current `AGENTS.md`, `.agents/skills/handoff/SKILL.md`, `governance/CONTINUITY.md`, and the applicable continuity profile from current AIMAGE authority, reconcile fresh live state, then synthesize/read back:

- objective;
- one next action;
- completion criterion;
- stop/replan trigger;
- any material deadline/ownership boundary.

Only then return `ACCEPTED` or `STALE_REPLAN` before consequential continuation.