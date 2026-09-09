# AIMAGE Architecture Boundaries

Status: initial governing boundary for continuity adoption. This file defines responsibility separation, not the final Image Engine architecture.

## 1. Three responsibility zones

AIMAGE is intentionally separated into three zones:

### A. Continuity Infrastructure

Owns cross-context state transfer semantics:

- canonical handoff location;
- authority/fresh-reconciliation rules;
- dependency/staleness handling;
- decision and negative-boundary preservation;
- recoverability of decision-relevant artifacts;
- cold-start acceptance and exactly-one-next-action semantics.

Continuity must not define how image generation itself works.

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

Preferred dependency direction:

`features/domain capabilities -> engine interfaces`

Continuity may transport state from both engine and feature layers, but it does not own their product semantics.

The following are architectural smells requiring review:

- engine core importing a concrete character/style/composition feature implementation;
- continuity defining composition algorithms or model-specific prompt rules;
- a feature redefining authority/continuity semantics for convenience;
- an adapter silently becoming canonical job authority;
- a Project bootstrap duplicating full engine or continuity rules and becoming a competing authority.

## 3. Authority separation

AIMAGE canonical repository authority owns long-lived rules and state definitions.

A continuity packet transports a bounded snapshot needed for continuation.

A GPT Project bootstrap points a receiver to canonical AIMAGE authority and startup procedure. It is intentionally thin and is not a second copy of the engine specification.

External source repositories and external methods used to construct or audit AIMAGE are provenance/evidence only unless AIMAGE explicitly adopts a rule into its own canonical files.

## 4. Testable boundary invariants

The continuity adoption is acceptable only if:

1. `governance/CONTINUITY.md` can be interpreted without reading `domato153/translation` at runtime.
2. repository-work and image-job continuity are profiles over the same core rather than separate incompatible handoff systems.
3. image-job continuity may carry `approved geometry`, `reference roles`, or `render spec` but does not define their production algorithms.
4. the engine layer can in principle support a new image domain without importing a domain-specific implementation into the core.
5. feature/domain documents may depend on engine interfaces, but a future engine specification must not depend on one current character, classroom scene, or model-specific prompt convention.
6. the Project bootstrap remains a locator/startup contract rather than a mirrored canonical specification.

## 5. Change rule

When later Image Engine design materially changes these boundaries, update this file explicitly and audit the dependency direction. Do not let the separation erode implicitly through convenience references.
