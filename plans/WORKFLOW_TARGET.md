# AIMAGE End-to-End Workflow Target

Status: planning/design target. This document defines the intended production workflow and capability goals. It does not authorize implementation and does not replace `architecture/BOUNDARIES.md`, continuity, or handoff governance.

## 1. Product objective

AIMAGE is a reusable image-production system that turns a user's visual intent into an approved, reproducible image result without relying on repeated blind prompt rerolls.

The system should help the user control only the parts that need control while preserving model creativity elsewhere.

The target is not a prompt library. It is an iterative production workflow with explicit state, reference roles, approval gates, provider abstraction, review, repair, artifact lineage, and reusable character/style/project state.

## 2. Primary failure classes to solve

AIMAGE must be designed around the failure classes that motivated the project:

1. **Identity/style drift** — the subject, character, object, or art language changes across generations or edits.
2. **Composition regression to model priors** — a requested spatial relationship is replaced by a generic centered/front-facing/close-up composition.
3. **Reference-role collision** — one reference image is accidentally treated as simultaneous identity, style, pose, composition, lighting, and background authority.
4. **Lossy iteration** — fixing one defect destroys parts that were already correct.
5. **Reroll dependence** — the user must repeatedly regenerate from scratch instead of preserving accepted structure and changing only the failed variable.
6. **Context loss** — a new thread/session/operator cannot reliably recover what was approved, rejected, or supposed to happen next.
7. **Provider lock-in** — the workflow is accidentally defined by one model/API rather than by AIMAGE-owned semantics.

## 3. Global design principles

### 3.1 Geometry before aesthetics when composition matters

When spatial relationships are important, convert vague language into explicit geometry and visual hierarchy before final rendering:

- camera location and direction;
- subject placement and scale;
- same-row/front/back relationships;
- subject-to-subject and subject-to-camera distance;
- gaze and body orientation;
- foreground/background ownership;
- dominant action and intended reading order.

An approved geometry/blocking artifact becomes authority for the locked spatial decision regardless of whether it was produced by AIMAGE, the user, or another compatible tool.

### 3.2 References have explicit roles

A reference must be bound to one or more declared roles such as:

- identity;
- style;
- composition/structure;
- approved blocking/layout;
- local edit source;
- optional mood/lighting evidence.

Reference presence alone must not imply authority over every visual dimension.

### 3.3 Lock only what needs locking

Every meaningful production request should be representable as:

- **LOCK** — already correct and must be preserved;
- **GEOMETRY / COMPOSITION LOCK** — structural relationships that must remain;
- **CHANGE** — the requested delta;
- **EXCLUSIONS** — failure directions or forbidden regressions;
- **CREATIVE FREEDOM** — dimensions the model may invent.

The system should avoid over-constraining creative dimensions that do not need determinism.

### 3.4 Approval creates durable state

An approval is not a chat reaction. It is a state transition that records what artifact or decision was accepted and what exactly became locked.

### 3.5 Repair the failed variable, preserve successful parts

On failure, classify the defect before choosing a repair. Prefer the smallest edit or regeneration scope that can plausibly correct the failed variable.

Do not escalate to a heavier method simply because it exists.

### 3.6 Serious workflows are iterative; trivial requests may be direct

The full workflow is available for consequential or consistency-sensitive jobs, but ordinary one-shot generation must remain possible.

No phase exists merely for ceremony.

### 3.7 Provider capabilities are subordinate to AIMAGE semantics

AIMAGE owns job state, reference-role meaning, approvals, locks, review semantics, and repair intent.

Provider-specific controls such as image IDs, masks, ControlNet, IP-Adapter, provider conversation state, workflow graphs, or model-specific prompt syntax are adapter capabilities, not AIMAGE authority.

## 4. Adaptive workflow

The logical workflow is below. Not every job must execute every phase.

### W0 — Intent / brief capture

Goal: convert the user's request into a bounded visual job without prematurely over-specifying it.

Capture when material:

- desired scene/result;
- subject/character/object;
- intended relationship or action;
- style intent;
- output purpose/aspect constraints;
- hard constraints and explicit non-goals;
- what is allowed to remain creative.

Output: `JobBrief`.

### W1 — Authority and profile resolution

Resolve existing project state before inventing new state:

- subject/character profile;
- style profile;
- prior approved artifacts;
- current reference-role bindings;
- prior failure-specific corrective guidance;
- current job continuity state if the job crossed contexts.

Do not infer an old generation is current merely because it is visible or available.

Output: `ResolvedJobContext`.

### W2 — Creative direction exploration

For non-trivial work, propose a small set of materially distinct directions rather than several cosmetic variations of the same model prior.

Diversity axes may include:

- camera placement;
- staging relationship;
- scale and negative space;
- action timing;
- foreground ownership;
- visual hierarchy;
- lighting or atmosphere when not already locked.

Output: `DirectionCandidate[]`.

### W3 — Composition / layout exploration

Translate the selected direction into explicit spatial structure.

This stage is responsible for preventing the common failure where natural-language phrases such as "beside me" collapse into generic front-right positioning.

Outputs may be textual geometry, a layout diagram, a blocking image, a pose/depth/segmentation representation, or another provider-compatible structural artifact.

Output: `CompositionSpec` plus zero or more `StructureArtifact` objects.

### W4 — Text / graphic-layout planning when needed

Only for images containing important text, labels, panels, UI, posters, diagrams, or designed graphic regions.

Separate semantic text content from visual placement so text correction does not require unnecessary whole-image reinvention.

Output: optional `TextLayoutSpec`.

### W5 — Blocking / skeleton generation

Produce a low-cost structural artifact before aesthetic finalization when geometry is important.

The blocker/skeleton should prioritize:

- subject positions;
- camera perspective;
- body/action direction;
- scale;
- line of action;
- major foreground/background masses;
- reading order.

It should not accidentally become style authority unless explicitly approved for that role.

Output: `BlockingArtifact`.

### W6 — Composition approval gate

The user may:

- approve;
- reject;
- approve with a bounded change;
- replace the blocking artifact with a user sketch or another structural reference.

Approval records exactly what is locked and what remains free.

Output: `ApprovalDecision` and updated locks.

### W7 — Optional rough / staging refinement

Use only if the blocking artifact is insufficient to safely reach final render.

This stage may refine pose, overlap, camera, object placement, expression staging, or other intermediate relationships without freezing final aesthetics prematurely.

Output: optional `RoughArtifact`.

### W8 — Render Spec Lock

Before final rendering, compile current authority into a provider-neutral render contract.

The render specification should include, when material:

- brief;
- role-bound references;
- geometry/composition locks;
- character/style constraints;
- approved structural artifacts;
- requested change;
- exclusions;
- creative-freedom fields;
- output properties;
- review criteria.

Output: immutable or versioned `RenderSpec`.

### W9 — Provider capability resolution and routing

Choose a provider/model/path based on the actual render requirement, not global preference.

Capability dimensions may include:

- text-to-image;
- multi-reference generation;
- high-fidelity reference preservation;
- multi-turn edit;
- masked/regional edit;
- structural conditioning;
- identity conditioning;
- text rendering;
- transparency;
- local/private execution;
- cost/latency constraints.

Output: `ExecutionPlan`.

### W10 — Generation / render

Invoke the selected adapter with the Render Spec translated into provider-specific controls.

Record provider/model/capabilities actually used and bind outputs to the exact Render Spec and input artifact identities.

Output: one or more `GenerationArtifact` objects plus `RunRecord`.

### W11 — Review

Review happens against explicit criteria, not general preference alone.

Candidate review dimensions include:

- identity compliance;
- style compliance;
- composition/geometry compliance;
- preservation of locked elements;
- requested change success;
- accidental regressions;
- readability/text correctness when applicable;
- anatomy/material/render artifacts;
- novelty/creative quality where relevant.

Automated/agent review may filter obvious failures. Human approval remains the final authority for subjective acceptance.

Output: `ReviewReport` and optional user approval.

### W12 — Repair / escalation

If review fails:

1. identify the failed variable(s);
2. identify successful elements to preserve;
3. choose the cheapest plausible repair level;
4. change one control dimension where practical;
5. rerun only the required stage(s);
6. re-review the repaired result.

Possible repair paths include:

- prompt/guideline correction;
- better reference selection;
- delta edit;
- masked/regional edit;
- structural-control correction;
- provider/model reroute;
- asset/profile repair;
- only then heavier dataset/training mechanisms if justified.

Output: `RepairPlan`, new artifact version, and new review.

### W13 — Finalization / export

After final approval, perform only deterministic or explicitly authorized finishing steps such as:

- format conversion;
- crop/pad to exact target;
- alpha/background operations;
- metadata/provenance packaging;
- contact sheet or comparison export;
- project artifact persistence.

Output: `FinalArtifact` plus provenance.

### W14 — Cross-context continuation

Continuity and handoff are cross-cutting infrastructure rather than image-production phases.

When a job crosses context boundaries, preserve the approved artifacts, reference roles, current locks, successful elements, active failure/repair target, and exactly one next action under the existing AIMAGE continuity/handoff contracts.

## 5. Core data contracts to design

The future engine should provide provider-neutral contracts for at least:

- `ImageJob`;
- `JobBrief`;
- `ReferenceBinding`;
- `ProfileBinding`;
- `DirectionCandidate`;
- `CompositionSpec`;
- `ArtifactRecord`;
- `ApprovalDecision`;
- `RenderSpec`;
- `ProviderCapabilitySet`;
- `ExecutionPlan`;
- `RunRecord`;
- `ReviewReport`;
- `RepairPlan`.

Exact schemas are not frozen by this planning document.

## 6. Product-layer responsibility

### Image Engine / Core owns

- job lifecycle/state machine;
- artifact identity/version/provenance;
- generic reference-role interface;
- approval/lock semantics;
- provider adapter interface and capability discovery;
- Render Spec and execution records;
- generic review/repair result contracts;
- persistence/version graph interfaces;
- cost/error/observability interfaces where useful.

### Feature / Domain layer owns

- composition exploration logic;
- character/subject profile behavior;
- style profile behavior;
- reference-selection strategies;
- geometry/blocking strategies;
- consistency strategies;
- review rubrics and domain-specific defect detectors;
- repair-policy strategies;
- text/layout, storyboarding, product, character-illustration, or other domain extensions.

The dependency direction remains `features/domain capabilities -> engine interfaces`.

## 7. Acceptance goals for the eventual system

The mature workflow should make the following practical statements true:

1. A user can approve composition before committing to final detail.
2. "Keep everything except X" is represented as explicit state rather than hopeful prompt wording.
3. Identity, style, and composition references can be independently assigned and replaced.
4. A failed generation can be repaired without unnecessarily discarding successful elements.
5. A new provider can be added without redefining job authority or workflow semantics.
6. A provider that supports structural controls can use them without making those controls mandatory for providers that do not.
7. A cold receiver can determine what is approved, what failed, and what to do next.
8. A one-shot image remains cheap and simple when no production workflow is needed.
9. External reusable components remain replaceable and subordinate to AIMAGE-owned interfaces.
10. The system does not require the user to become a prompt engineer to obtain controlled results.
