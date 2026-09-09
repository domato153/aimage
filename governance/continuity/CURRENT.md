# AIMAGE Current Repository-Work Continuity

Status: current repository-work continuity locator for the active planning/design/research slice. This file records decision-relevant current state; it does not replace `governance/CONTINUITY.md`, `governance/continuity/REPOSITORY_WORK.md`, root `AGENTS.md`, or Image Engine specifications.

## 1. Authority snapshot

- Repository: `domato153/aimage`
- Authoritative branch: `main`
- Accepted `main` at start of this bounded slice: `877ce7dc7c48c1f0976a4ec926ece81872a1feb7`
- Active planning candidate branch: `aimage-stage/cross-domain-reuse-resolution`
- Current governing entrypoint: `AGENTS.md`
- Continuity method: `governance/CONTINUITY.md`
- Repository-work profile: `governance/continuity/REPOSITORY_WORK.md`
- Handoff method: `.agents/skills/handoff/SKILL.md` resolved from fresh current authority when a handoff is actually consumed/produced
- Architecture boundary: `architecture/BOUNDARIES.md`
- Workflow target: `plans/WORKFLOW_TARGET.md`
- Capability classification: `plans/CAPABILITY_REUSE_MATRIX.md`
- External acquisition/integration design: `plans/EXTERNAL_REUSE_PLAN.md`
- Reuse/integration assurance and final workflow simulation method: `plans/REUSE_AND_INTEGRATION_ASSURANCE.md`

Fresh repository state always governs current factual state. The user has indicated that `.agents/skills/handoff/SKILL.md` is being improved in another thread; this slice does not reopen or duplicate that work. Any future handoff operation must fresh-read whichever handoff skill is authoritative at that time.

## 2. Current phase and scope

Phase: **planning / design / research only**.

The capability-first cross-domain reuse re-audit and the external acquisition/application architecture are now represented on the bounded candidate branch. No Image Engine implementation, provider integration, package installation, external-code import, runtime dependency change, or production code adoption is authorized by this state.

## 3. Completed foundation preserved

Do not reopen without new evidence or explicit scope change:

- thin GPT Project bootstrap -> current root `AGENTS.md`;
- separate Continuity and Handoff routes;
- AIMAGE-owned continuity/handoff with no runtime dependency on `domato153/translation`;
- Continuity/Handoff separated from Image Engine/Core and Feature/Domain product semantics;
- intended dependency direction `features/domain capabilities -> engine interfaces`;
- accepted adaptive `plans/WORKFLOW_TARGET.md`;
- provider-native targeted/delta/masked/multi-turn editing as execution capability rather than a reason for an AIMAGE repair renderer;
- evidence-first `ADOPT / ADAPT / DESIGN` policy.

## 4. Cross-domain reuse re-audit result

The prior matrix over-classified several generic engineering problems as AIMAGE-native design. The candidate `plans/CAPABILITY_REUSE_MATRIX.md` now applies the required abstract-problem search and reduces native design materially.

### Generic mechanics now explicitly reused/adapted

- workflow/state/history/human gates -> SCXML/BPMN/Temporal patterns;
- artifact identity/lineage -> W3C PROV/OpenAssetIO/content-addressed/SLSA concepts, optional C2PA export;
- provider-neutral execution intent -> LLVM/MLIR IR/lowering patterns + JSON Schema;
- provider capability discovery -> LSP/Vulkan/OpenAssetIO feature/capability patterns;
- geometry/relative layout -> OpenUSD/Cassowary/CSS layout primitives;
- persistence/serialization -> generic metadata/blob separation + JSON Schema/schema-evolution methods;
- exact text/graphic layout -> SVG/CSS deterministic layout primitives;
- repair orchestration -> diagnose/analyze -> plan -> provider execution -> verify/regression loop.

These are not made AIMAGE runtime dependencies merely because their patterns are reused.

### Major reclassifications

Previously native or partially native items such as reference-role binding, approval/lock machinery, provider adapter/capability machinery, RenderSpec mechanics, persistence/serialization, geometry specification, blocking workflow and text layout are now primarily `ADAPT` or `ADAPT + small AIMAGE extension`.

The materially retained `DESIGN` surface is narrowed to:

- domain-specific QA semantics (`F21`) — actual domain correctness/rubrics;
- domain extension semantic content (`F23`) — actual new domain behavior.

Generic review/plugin machinery for those items is still reused rather than invented.

## 5. Exact AIMAGE semantic residue after reuse

The candidate planning set retains only semantics that currently pass the existence-value test:

1. **visual authority vocabulary** — which dimension a reference/profile/artifact governs and precedence/conflict meaning;
2. **dimension-scoped approval/lock/preservation intent** — what the user approved and what later execution must preserve or explicitly reopen;
3. **visual execution-intent vocabulary** — the small AIMAGE fields/invariants inside a provider-neutral RenderSpec IR;
4. **image capability taxonomy/compatibility predicates** — visual operations/constraints needed for routing;
5. **visual spatial predicates/reading hierarchy** — qualitative image-composition meaning layered over mature transform/constraint primitives;
6. **domain-specific review/extension semantics**.

If future external evidence closes any of these without loss of user-visible/cross-provider control, it should shrink further.

## 6. External acquisition/application design result

The candidate `plans/EXTERNAL_REUSE_PLAN.md` now distinguishes concrete runtime acquisition from method/schema reuse.

### Initial concrete provider/runtime integrations when implementation is later authorized

- **OpenAI official SDK/API** — normal provider dependency behind `OpenAIProviderAdapter`;
- **Hugging Face Diffusers** — optional local provider package;
- **ComfyUI** — optional separately installed service/backend; no GPL core source copied into AIMAGE.

### Method/standard adaptation without mandatory runtime coupling

- SCXML/BPMN/Temporal patterns;
- W3C PROV/SLSA provenance concepts;
- LLVM/MLIR IR/lowering patterns;
- LSP/Vulkan/OpenAssetIO adapter/capability patterns;
- OpenUSD/Cassowary/CSS geometry/layout patterns;
- JSON Schema/Avro schema-evolution patterns;
- SVG/CSS deterministic text layout;
- diagnose/plan/execute/verify repair patterns.

### Optional interoperability only

- OpenAssetIO for a real external DAM/MAM system;
- OpenUSD for DCC/VFX interchange when a real use case requires it;
- C2PA for exported-content provenance;
- selected pinned ComfyUI workflow-template artifacts at the adapter edge.

### No initial source copying

Nori, GenAI Illustration Pipeline, Krita AI Diffusion and style-consistency-ai remain method/architecture/UX evidence by default. Source import is not an initial architecture dependency. Any later source import must be justified by a measured implementation gap and pass the external acquisition assurance gate.

This removes the prior uncertainty where permissive source modules were listed as likely imports before a need had been demonstrated.

## 7. External-reuse omission and due-diligence assurance

`plans/REUSE_AND_INTEGRATION_ASSURANCE.md` adds a reusable audit method derived from external professional practices.

### Gate A — capability coverage

Requires abstract-problem decomposition, cross-domain search, adoption/adaptation/composition ladder, existence-value test, and bidirectional requirement↔mechanism closure. A retained `DESIGN` without negative evidence fails.

### Gate B — external acquisition due diligence

Before implementation installs/copies/bundles a concrete component, verify exact identity/version, functional fit, license/distribution, supply-chain/maintenance risk, transitive coupling, canonical-state boundary, fallback/replacement and AIMAGE-owned tests.

Method basis includes NIST SSDF/C-SCRM, SLSA, SPDX and OpenSSF Scorecard.

### Gate C — architecture scenario audit

Uses an ATAM-style scenario review to test provider replacement, capability absence, optional backend loss, provider API drift, one-shot simplicity, long-running approval, minimal-delta repair, schema migration, license/dependency replacement and domain extension boundaries.

### Gate D — final integrated workflow validation

Uses NASA-style requirements↔verification traceability plus state-transition coverage, NIST combinatorial interaction coverage, canonical end-to-end workflow simulations and explicit fault/regression injection.

A passing component test suite alone is insufficient for final system `PASS`.

## 8. Workflow-target recheck

`plans/WORKFLOW_TARGET.md` was rechecked against the external reuse findings.

No user/control boundary currently has evidence strong enough to justify deleting a logical function from the target, so the file is intentionally not rewritten in this slice.

Interpretation after reuse:

- W0-W13 remain **logical functions**, not mandatory user-visible phases;
- W6 composition approval remains a real user decision boundary and should remain explicit;
- W8 RenderSpec lock is primarily an IR compilation/validation checkpoint, not a separate workflow-engine invention;
- W9 capability resolution is internal target selection/lowering/routing, not user ceremony;
- W12 repair is a loop back to the cheapest necessary prior operation, not a linear stage that implies a custom editor;
- W14 was already correctly modeled as cross-cutting continuity/handoff infrastructure rather than a production phase;
- trivial one-shot work continues to bypass unnecessary structure.

This preserves the accepted target while removing the assumption that every numbered item requires bespoke infrastructure or separate UI.

## 9. Remaining implementation-time deferred checks

The architecture/acquisition design is considered resolved even though the following are intentionally selected only when implementation language/runtime exists:

- exact JSON Schema validation library;
- exact Cassowary-compatible constraint-solver package, if a solver is needed rather than direct constraint evaluation;
- exact persistence database/blob-store implementation;
- exact package versions and provider model aliases;
- exact selected ComfyUI workflow artifacts for each supported advanced capability.

These are `DEFERRED_IMPLEMENTATION_CHECK` items rather than architecture gaps because acquisition mode, semantic owner, coupling, fallback and replacement boundaries are already fixed. Each concrete component must still pass Assurance Gate B before adoption.

## 10. Exactly one next bounded action

**Independently audit the bounded cross-domain reuse-resolution candidate against fresh `main`, `architecture/BOUNDARIES.md`, the prior cross-domain handoff objective, and the new Assurance Gates A/B; if coherent and clean, adopt/merge the planning candidate. After adoption, the next planning slice is to design only the narrowed AIMAGE semantic contracts listed in section 5, not to begin provider/core implementation.**

## 11. Expected transition after candidate adoption

A successful adoption leaves:

- external reuse/acquisition/application architecture resolved at planning level;
- materially reduced native-design surface;
- no unnecessary initial source imports;
- explicit implementation-time due-diligence gate for every concrete dependency;
- an externally grounded whole-system audit/simulation plan defined before implementation;
- exactly one subsequent design task: specify the remaining thin AIMAGE semantic contracts and their invariants.

## 12. Stop / replan conditions

Stop/replan if:

- fresh `main` or a newly adopted handoff/architecture change materially supersedes this candidate;
- another active branch/PR touches this exact reuse/design boundary incompatibly;
- independent audit finds a missing `DESIGN` burden-of-proof record or an external component without a replacement/canonical-state boundary;
- license/runtime/distribution evidence forces a different architecture;
- research shows one of the currently retained AIMAGE residues is actually generic and already solved;
- the user changes phase or authorizes implementation before this planning candidate is adopted.
