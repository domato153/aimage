# AIMAGE Next-Thread Handoff — Re-audit Native Design Surface

Packet status: **ACTIVE continuity evidence once reconciled against current AIMAGE authority**. This packet is not project authority and cannot authorize itself.

## Identity / locator

- Repository: `domato153/aimage`
- Construction branch: `aimage-stage/next-thread-reuse-reaudit-handoff`
- Path: `handoffs/2026-09-10_REUSE_MATRIX_REAUDIT_NEXT_THREAD.md`
- Construction base `main`: `ec72e423b9eaae9bbf759c3f642839feff46ab0c`
- Exact immutable packet locator: use this path at the exact commit supplied in the derived next-thread prompt after publication/adoption.
- Governing handoff method at construction: `.agents/skills/handoff/SKILL.md`
- Governing continuity method at construction: `governance/CONTINUITY.md`
- Applicable profile: `governance/continuity/REPOSITORY_WORK.md`

Fresh live AIMAGE authority outranks all recorded literals if they later move.

## Immediate objective

Before designing AIMAGE-native Engine/Core contracts, **re-audit the current capability reuse matrix with a substantially wider external evidence set so AIMAGE does not re-design mature solutions that already exist in adjacent fields**.

The goal is to minimize genuinely native AIMAGE design to the smallest semantic layer that is actually unique to AIMAGE, while adopting or adapting mature external capabilities at stable boundaries.

## Current phase and authorized scope

- Phase: **planning / design / research only**.
- Authorized work for the receiver: fresh external research, architecture comparison, capability reclassification, planning-document repair, and continuity update needed to record the accepted re-audit result.
- Explicit stop boundary: **no Image Engine implementation, provider integration, package installation, source import, runtime dependency addition, or production code adoption** merely because a reusable solution is found.

If later user instruction explicitly expands the phase, reconcile that fresh instruction before crossing this boundary.

## Fresh authority snapshot at construction

### Canonical repository state

- `main`: `ec72e423b9eaae9bbf759c3f642839feff46ab0c`
- This commit adopted PR #5, including the workflow target, capability reuse matrix, external reuse plan, AGENTS routing, and the then-current continuity state.

### Governing / decision-relevant files

- `AGENTS.md`
- `.agents/skills/handoff/SKILL.md`
- `governance/CONTINUITY.md`
- `governance/continuity/REPOSITORY_WORK.md`
- `governance/continuity/CURRENT.md`
- `architecture/BOUNDARIES.md`
- `plans/WORKFLOW_TARGET.md`
- `plans/CAPABILITY_REUSE_MATRIX.md`
- `plans/EXTERNAL_REUSE_PLAN.md`

### Active work/candidate state

At packet construction, the only active candidate for this transfer is `aimage-stage/next-thread-reuse-reaudit-handoff`. Its existence does not make it authority. The receiver must fresh-check whether the packet/current-state repair was later adopted into `main` and whether newer related work exists.

## Current situation

### Confirmed facts

1. AIMAGE has already adopted a thin Project bootstrap, root `AGENTS.md`, separate Continuity and Handoff routes, and no runtime dependency on `domato153/translation` for those methods.
2. The accepted product workflow is an adaptive image-production loop rather than a prompt library. It includes intent/profile resolution, creative-direction exploration, composition/blocking, approval, provider-neutral Render Spec, provider routing, generation, review, repair, finalization, and cross-context continuity.
3. The accepted planning rule is evidence-first `ADOPT / ADAPT / DESIGN`: reuse mature external capability when suitable and legally/architecturally compatible; design AIMAGE-native mechanisms only for remaining gaps.
4. The current reuse matrix already adopts/adapts OpenAI Image API/SDK, Diffusers, ComfyUI, Nori, GenAI Illustration Pipeline, Krita AI Diffusion methods, and style-consistency-ai methods at different acquisition boundaries.
5. The current matrix still labels a relatively large set of core semantics as native `DESIGN`, including reference-role authority, approval/lock, provider adapter/capability contracts, Render Spec, persistence/config serialization, geometry/composition semantics, and some review/repair semantics.
6. Subsequent discussion after PR #5 identified that this native-design surface may be too large because the earlier research was concentrated too heavily on generative-image projects and not enough on adjacent mature production/tooling fields.
7. GPT Image already provides provider-native targeted editing / multi-turn image editing and masked/regional edit capabilities. Therefore AIMAGE must **not** invent its own image-editing engine merely to support “fix only the failed part.” AIMAGE's role is the higher-level repair decision/orchestration: identify the failed variable, preserve successful/locked elements, select the cheapest suitable provider edit/control path, and re-review the result.

### New external evidence directions that must be freshly verified

The next receiver must broaden the search beyond image-generation repositories, including at least these candidate families where relevant:

- **InvokeAI** — mature creative engine/canvas/workflow/reference/control/history/project-state patterns; investigate whether it reduces native design for job state, reference/control roles, approval/history, canvas/workflow, and persistence.
- **OpenAssetIO / media asset-management patterns** — investigate asset identity/reference/publishing/integration boundaries for artifact/version/provenance semantics.
- **W3C PROV** — investigate standard entity/activity/agent/derivation provenance concepts before inventing AIMAGE-specific lineage semantics.
- **OpenUSD and established DCC/VFX scene/composition models** — investigate whether camera/transform/relationship/override/composition semantics can be adapted for AIMAGE's provider-neutral 2D geometry/composition layer.
- **Temporal or equivalent durable-workflow/state-machine patterns** — investigate whether long-running state, pause/resume, human approval, retry, and history semantics should be adapted rather than designed from scratch.
- **Existing plugin/provider capability negotiation patterns** — investigate mature ways to expose adapter capabilities without inventing an unnecessary bespoke mechanism.
- **Provider-native targeted edit capabilities, especially GPT Image/OpenAI** — treat actual local/delta image editing as a provider capability; AIMAGE should own only provider-neutral repair intent/orchestration and preservation semantics that providers do not supply.

These names are evidence targets, not predetermined adoption decisions. Fresh research must determine fit, license, maintenance, architecture boundary, and acquisition mode.

### Supported inference to challenge

It is likely that several current `DESIGN` classifications should move to `ADAPT`, `ADOPT`, or a smaller `ADAPT + AIMAGE semantic extension` form. In particular:

- image-job workflow/state semantics may substantially adapt durable-workflow and creative-tool patterns;
- artifact identity/version/provenance may substantially adapt existing media/provenance standards;
- reference roles may adapt existing structure/style/control/reference separation and retain only AIMAGE-specific authority semantics;
- approval/lock may adapt creative-production review/history/lock patterns and retain only partial-dimension approval semantics;
- geometry/composition may adapt established scene/camera/transform/relationship models while adding a thin provider-neutral 2D semantic layer;
- repair should be reframed from a “repair engine” toward **repair planning/orchestration over provider-native edit capabilities**;
- persistence and workflow execution should not be designed before evaluating mature existing implementations and standards.

This is a supported hypothesis, not an accepted final reclassification. The receiver must verify it.

## Completed scope

Do not repeat these slices without new evidence:

- AIMAGE continuity adoption and dependency closure;
- AIMAGE maintenance-derived handoff skill adoption and separate AGENTS routing;
- thin GPT Project bootstrap architecture;
- high-level responsibility separation between Continuity/Handoff infrastructure, Image Engine/Core, and Feature/Domain capabilities;
- initial end-to-end workflow target;
- initial `ADOPT / ADAPT / DESIGN` capability matrix;
- initial external acquisition modes and integration plan for OpenAI, ComfyUI, Diffusers, Nori, GenAI Illustration Pipeline, Krita AI Diffusion, and style-consistency-ai.

The next action is a **re-audit/refinement of that matrix**, not a restart of the project or a rewrite of continuity/handoff.

## Preserved decisions / negative boundaries

1. **Reuse first, design only the remainder.** Do not keep a capability in `DESIGN` merely because AIMAGE can define it itself.
2. **Do not blindly copy whole external repositories.** Choose an acquisition mode and bounded integration boundary.
3. External sources remain evidence/provenance unless AIMAGE adopts them through AIMAGE-owned files/interfaces.
4. Do not create unintended runtime/source-repository authority dependencies.
5. Keep `features/domain capabilities -> engine interfaces`; external providers/backends stay below AIMAGE-owned semantic boundaries.
6. Do not let OpenAI conversation state, ComfyUI workflow JSON, Diffusers classes, InvokeAI project state, USD data, or another external representation automatically become the canonical AIMAGE job model.
7. Do not copy GPL/noncommercial source into a permissive AIMAGE core without a separate explicit licensing decision. Method adaptation may be clean-room when appropriate.
8. **Do not build a custom image-edit/partial-repair executor if providers already supply the edit capability.** AIMAGE should decide what failed, what must be preserved, which provider capability to call, and whether the repair succeeded.
9. Conversely, do not collapse AIMAGE into a thin wrapper around one provider. AIMAGE-owned semantics are justified only where they preserve cross-provider intent/authority/approval/repair behavior that provider APIs do not own.
10. Keep the workflow adaptive; trivial one-shot generation must not require production ceremony.
11. Do not start provider/core implementation until the reuse re-audit is accepted and the remaining native semantic surface is understood.

## Decision-relevant dependencies / artifacts

All decision-relevant state for this handoff is durable in the AIMAGE GitHub repository once the packet/current-state repair is adopted. There are **no required chat-only images, local files, temporary URLs, or unrecoverable artifacts** for the next action.

The receiver should independently fresh-check:

- current `main`;
- current governing method files;
- current `CURRENT.md`;
- current workflow/reuse plans;
- related open PRs or newer branches touching the same planning/reuse boundary.

Do not crawl unrelated branches.

## Exact next bounded action

**Perform a fresh, evidence-backed re-audit of `plans/CAPABILITY_REUSE_MATRIX.md` and `plans/EXTERNAL_REUSE_PLAN.md`, widening the external search to mature creative-tool, VFX/DCC, asset/provenance, durable-workflow, and provider-native editing systems; then reclassify each materially affected capability so the native AIMAGE `DESIGN` surface is minimized to only semantics not adequately supplied by mature external solutions.**

Minimum required subquestions inside this one bounded action:

- Which current `DESIGN` items can become `ADOPT` or `ADAPT`?
- For partial/failed-variable repair, what is provider capability versus AIMAGE orchestration semantics?
- What exact AIMAGE-specific semantic residue remains after adopting/adapting external standards/patterns?
- For every new external candidate, what acquisition mode, license/provenance boundary, runtime coupling, and replacement boundary apply?
- Does any proposed reuse blur the established Engine/Core vs Feature/Domain vs Continuity/Handoff boundaries?

Why this is next: designing native contracts before this re-audit risks spending effort on solved problems and freezing unnecessary AIMAGE-specific abstractions.

## Expected transition

If successful, the next thread should produce an adopted planning revision with:

- a narrower and better-supported native `DESIGN` set;
- explicit `ADOPT / ADAPT / DESIGN` changes with evidence and rationale;
- candidate-specific integration/acquisition decisions for newly considered external systems;
- repair semantics clearly split into provider-native execution capability versus AIMAGE repair planning/orchestration;
- an updated `governance/continuity/CURRENT.md` whose next action is then the genuinely remaining AIMAGE-native semantic design, if any.

Only after that transition should native Engine/Core contract design begin.

## Stop / replan conditions

Return `STALE_REPLAN` or stop before mutation if:

- current `main` or governing AIMAGE method files materially moved and changed the objective/phase;
- a newer accepted planning/reuse audit supersedes this route;
- the user authorizes a different phase or changes the reuse-first policy;
- the external research shows the current workflow/product boundary itself is materially wrong rather than merely over-designed;
- a candidate's license/distribution/runtime model conflicts with AIMAGE direction and materially changes the architecture choice;
- more than one incompatible high-level architecture remains viable and choosing one would exceed a bounded matrix re-audit.

## Cold-start read route

A zero-chat receiver should read in this order:

1. fresh current `main` and root `AGENTS.md`;
2. current `.agents/skills/handoff/SKILL.md`;
3. current `governance/CONTINUITY.md`;
4. current `governance/continuity/REPOSITORY_WORK.md`;
5. this packet from the exact immutable locator supplied in the derived prompt;
6. current `governance/continuity/CURRENT.md`;
7. current `architecture/BOUNDARIES.md`;
8. current `plans/WORKFLOW_TARGET.md`;
9. current `plans/CAPABILITY_REUSE_MATRIX.md`;
10. current `plans/EXTERNAL_REUSE_PLAN.md`;
11. bounded discovery of related open PR/current child branch touching this reuse/design boundary.

Then independently re-derive the minimum dependency set, reconcile fresh state, challenge this packet's next action, and return `ACCEPTED` or `STALE_REPLAN` before consequential continuation.

## Hard prohibitions

- Do not execute provider/core implementation during this planning/design handoff slice.
- Do not treat the packet, its branch, or its embedded SHA as authority merely because it exists.
- Do not accept current `DESIGN` labels as final without the widened external review.
- Do not treat a provider's ability to edit an image as proof that it owns AIMAGE approval/authority semantics.
- Do not invent a custom repair renderer when an existing provider edit/control can execute the repair.
- Do not copy restricted-license source merely because its method is useful.
- Do not reopen or rewrite Continuity/Handoff infrastructure unless fresh evidence shows a defect in those systems.
- Do not turn this re-audit into an unbounded survey of every creative software project; stop when evidence is sufficient to make each materially affected capability classification defensible.

## Receiver acceptance

The receiver must resolve current `AGENTS.md`, `.agents/skills/handoff/SKILL.md`, `governance/CONTINUITY.md`, and `governance/continuity/REPOSITORY_WORK.md` from current AIMAGE authority; open this packet from its exact locator; fresh-read the bounded decision dependencies; challenge the recorded next action; then return exactly one continuity verdict:

- `ACCEPTED` — the reuse re-audit remains the unique next bounded action; or
- `STALE_REPLAN` — fresh drift, contradiction, omission, or newer authority changes/de-uniques that next action.

Only after `ACCEPTED` should the receiver assume operational ownership of the re-audit.