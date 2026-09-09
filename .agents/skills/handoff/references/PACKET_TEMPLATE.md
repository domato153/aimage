# AIMAGE Handoff Packet Template

Use this as a semantic checklist, not a form that must be filled mechanically.

A packet is continuity evidence, not project authority.

## Identity / locator

- Repository:
- Owning ref/branch:
- Path:
- Exact commit/object identity:
- Packet status:

## Immediate objective

State the current bounded objective in practical terms.

## Current phase and authorized scope

- Phase:
- Authorized work:
- Explicit stop boundary:

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

## Exact next bounded action

One executable next action:

Why this action is next:

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

The receiver must resolve current `AGENTS.md`, `.agents/skills/handoff/SKILL.md`, `governance/CONTINUITY.md`, and the applicable continuity profile from current AIMAGE authority, reconcile fresh live state, then return `ACCEPTED` or `STALE_REPLAN` before consequential continuation.
