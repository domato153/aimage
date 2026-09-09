# AIMAGE Architecture Boundaries

Status: initial governing boundary for continuity/handoff adoption. This file defines responsibility separation, not the final Image Engine architecture.

## 1. Three responsibility zones

AIMAGE is intentionally separated into three zones:

### A. Continuity & Handoff Infrastructure

This is cross-context infrastructure, not image-production product logic.

#### Continuity owns state-transfer semantics

- canonical continuity/packet location semantics;
- authority/fresh-reconciliation rules;
- bounded dependency/staleness handling;
- active situation state;
- decision and negative-boundary preservation;
- recoverability of decision-relevant artifacts;
- cold-start `ACCEPTED` / `STALE_REPLAN` and exactly-one-next-action semantics.

#### Handoff owns live transfer orchestration

- deciding when a consequential handoff is warranted;
- constructing/consuming the bounded handoff packet;
- resolving the governing handoff method before packet use;
- organizing objective, phase, current state, completed scope, blocker, cold-start route, hard prohibitions, exact next action, and stop/replan conditions;
- deriving user-facing paste/share material from the canonical packet rather than independently rewriting it from memory.

Handoff delegates state/freshness/acceptance semantics to continuity. Continuity does not need to own packet-writing procedure.

Neither continuity nor handoff may define how image generation itself works.

### B. Image Engine Architecture / Core

Owns reusable production mechanics shared across image domains, for example:

- job/pipeline state model;
- authority and profile interfaces;
- reference-role interface;
- geometry/blocking interface;
- approval-gate interface;
- render/review/repair lifecycle;
- model/UI/API adapter boundary;
- capability discovery and fallback semantics where later designed.

The exact contents remain subject to the later Image Engine architecture design/audit.

### C. AIMAGE Features / Domain Capabilities

Owns concrete behavior built on the engine, for example:

- composition exploration and diversity logic;
- character/subject profiles;
- style profiles;
- reference-role binding strategies;
- geometry-lock UX/logic;
- known-failure/success pattern handling;
- image review strategies;
- repair strategies;
- domain extensions such as character illustration, product imagery, spatial design, or storyboards.

These examples are current design directions, not frozen implementation requirements.

## 2. Dependency direction

Preferred product dependency direction:

`features/domain capabilities -> engine interfaces`

Continuity/handoff may transport state from both engine and feature layers, but they do not own product semantics.

Within cross-context infrastructure:

`handoff -> continuity contract/profiles`

Handoff uses continuity semantics. Continuity must not require the handoff skill merely to define state/freshness/acceptance semantics.

The following are architectural smells requiring review:

- engine core importing a concrete character/style/composition feature implementation;
- continuity defining composition algorithms or model-specific prompt rules;
- handoff defining engine or feature behavior instead of transporting it;
- handoff duplicating continuity freshness/acceptance semantics into a competing contract;
- a feature redefining authority/continuity/handoff semantics for convenience;
- an adapter silently becoming canonical job authority;
- a Project bootstrap duplicating full engine, continuity, or handoff rules and becoming a competing authority.

## 3. Authority separation

AIMAGE canonical repository authority owns long-lived rules and state definitions.

A continuity/handoff packet transports a bounded snapshot needed for continuation. It does not become project authority merely because it is canonical as a packet artifact.

A GPT Project bootstrap points a receiver to canonical AIMAGE authority and startup procedure. It is intentionally thin and is not a second copy of the engine, continuity, or handoff specification.

External source repositories and external methods used to construct or audit AIMAGE are provenance/evidence only unless AIMAGE explicitly adopts a rule into its own canonical files.

## 4. Testable boundary invariants

The continuity/handoff adoption is acceptable only if:

1. `governance/CONTINUITY.md` can be interpreted without reading `domato153/translation` at runtime.
2. `.agents/skills/handoff/SKILL.md` can be interpreted and executed without reading `domato153/translation` at runtime.
3. handoff packet construction/consumption routes to AIMAGE continuity rather than redefining a second freshness/acceptance system.
4. repository-work and image-job continuity are profiles over the same core rather than separate incompatible handoff systems.
5. image-job continuity/handoff may carry `approved geometry`, `reference roles`, or `render spec` but does not define their production algorithms.
6. the engine layer can in principle support a new image domain without importing a domain-specific implementation into the core.
7. feature/domain documents may depend on engine interfaces, but a future engine specification must not depend on one current character, classroom scene, or model-specific prompt convention.
8. the Project bootstrap remains a locator/startup contract rather than a mirrored canonical specification.

## 5. Change rule

When later Image Engine design materially changes these boundaries, update this file explicitly and audit the dependency direction. Do not let the separation erode implicitly through convenience references.
