# AIMAGE Current Repository-Work Continuity

Status: current repository-work continuity locator for the active planning/design slice. This file records decision-relevant current state; it does not replace `governance/CONTINUITY.md`, `governance/continuity/REPOSITORY_WORK.md`, root `AGENTS.md`, or Image Engine specifications.

## 1. Authority snapshot

- Repository: `domato153/aimage`
- Authoritative branch: `main`
- Accepted `main` immediately before this continuity update: `ec72e423b9eaae9bbf759c3f642839feff46ab0c`
- Current governing entrypoint: `AGENTS.md`
- Continuity method: `governance/CONTINUITY.md`
- Repository-work profile: `governance/continuity/REPOSITORY_WORK.md`
- Handoff method: `.agents/skills/handoff/SKILL.md`
- Active next-thread handoff packet candidate: `handoffs/2026-09-10_REUSE_MATRIX_REAUDIT_NEXT_THREAD.md`

Fresh repository state always governs current factual state if these literals later move.

## 2. Current phase and scope

Phase: **planning / design / research only**.

The next work is **not** native Engine/Core contract design yet. The immediate planning task is to re-audit the current `ADOPT / ADAPT / DESIGN` matrix with a wider external evidence set so AIMAGE does not redesign mature solutions that already exist in adjacent creative-tool, VFX/DCC, asset/provenance, workflow, or provider ecosystems.

No Image Engine implementation, provider integration, package installation, external-code import, or runtime dependency change is authorized by this continuity state.

## 3. Completed foundation

The following foundation is accepted and should not be reopened without new evidence or an explicit scope change:

- a thin GPT Project bootstrap routes consequential work to current root `AGENTS.md` rather than duplicating project rules;
- root `AGENTS.md` separately routes Continuity and Handoff;
- `governance/CONTINUITY.md` is the AIMAGE-owned cross-context state/reconciliation contract;
- `.agents/skills/handoff/SKILL.md` is the AIMAGE-owned live-transfer construction/consumption method and delegates continuity semantics to the continuity contract/profile;
- runtime Continuity/Handoff interpretation has no dependency on `domato153/translation`; that repository is construction provenance/audit evidence only;
- Continuity/Handoff infrastructure remains separate from Image Engine Architecture/Core and AIMAGE Features/Domain Capabilities;
- the intended product dependency direction remains `features/domain capabilities -> engine interfaces`;
- `plans/WORKFLOW_TARGET.md`, `plans/CAPABILITY_REUSE_MATRIX.md`, and `plans/EXTERNAL_REUSE_PLAN.md` were adopted on `main` in the prior planning slice;
- external reuse decisions follow an evidence-first `ADOPT / ADAPT / DESIGN` policy rather than assuming every mechanism should be invented locally.

## 4. Current workflow baseline

The accepted product target remains an adaptive production loop rather than a prompt library:

1. intent/brief capture;
2. authority/profile/reference resolution;
3. creative-direction exploration;
4. composition/layout specification;
5. optional text/layout planning;
6. blocking/skeleton generation when structure matters;
7. composition approval and lock recording;
8. optional rough/staging refinement;
9. provider-neutral Render Spec lock;
10. provider capability resolution/routing;
11. generation/render;
12. explicit review;
13. failed-variable repair/escalation while preserving successful elements;
14. deterministic finalization/export;
15. continuity/handoff across context boundaries when required.

The workflow remains adaptive: low-risk one-shot requests do not need every stage.

## 5. Why the previous next action was superseded

The prior `CURRENT.md` said the next action was to design native AIMAGE Engine/Core contracts. Subsequent user discussion changed that planning decision before implementation began.

The new concern is that the current reuse research was too concentrated on generative-image projects and may have classified too many mature cross-industry concepts as AIMAGE-native `DESIGN`.

Therefore native contract design is **deferred until a widened reuse re-audit closes**.

## 6. New evidence directions to verify

The next planning slice must freshly investigate mature adjacent systems/patterns where relevant, including at least:

- **InvokeAI** for creative project/canvas/workflow/reference/control/history/state patterns;
- **OpenAssetIO or equivalent mature media asset-management interfaces** for artifact identity/reference/publishing/integration boundaries;
- **W3C PROV** for entity/activity/agent/derivation provenance concepts;
- **OpenUSD and established VFX/DCC scene/composition models** for camera/transform/relationship/override/composition semantics that may reduce custom geometry design;
- **Temporal or equivalent durable-workflow patterns** for long-running state, pause/resume, human approval, retry, and history semantics;
- mature plugin/provider capability-negotiation patterns;
- provider-native targeted editing, especially current GPT Image/OpenAI image edit capabilities.

These are research targets, not predetermined adoption decisions.

## 7. Repair semantics decision

A material clarification is now preserved:

**AIMAGE should not build a custom partial-image repair/editing engine when providers already expose suitable edit capabilities.**

Provider/backend capabilities may execute:

- targeted/delta image edits;
- masked/regional edits;
- multi-turn controlled edits;
- structural-control corrections;
- reference-conditioned edits.

AIMAGE's provider-neutral responsibility is the higher-level **repair planning/orchestration**:

1. identify the failed variable(s);
2. identify successful/locked elements that must be preserved;
3. choose the cheapest suitable repair path/provider capability;
4. express the requested delta/preservation intent;
5. execute through the selected adapter;
6. re-review whether the repair succeeded without unacceptable regression.

This means current repair-related `DESIGN`/`ADAPT` labels must be reassessed so provider execution capability is not reimplemented inside AIMAGE.

## 8. Current reuse hypothesis to challenge

The working hypothesis is that several current native-design areas can shrink substantially after broader research:

- job/workflow state -> mature durable-workflow and creative-tool patterns;
- artifact identity/version/provenance -> media asset/provenance standards and patterns;
- reference roles -> existing structure/style/control/reference separation plus only a thin AIMAGE authority extension;
- approval/lock -> established review/history/lock patterns plus only AIMAGE-specific partial-dimension approval semantics;
- provider adapter/capability model -> mature plugin/adapter/capability patterns;
- geometry/composition -> established camera/scene/transform/relationship models plus a thin provider-neutral 2D semantic layer;
- persistence -> mature existing storage/project-state mechanisms selected only after semantic boundaries are known;
- repair -> provider-native edit execution plus AIMAGE orchestration/preservation semantics.

This is a supported inference only. The re-audit must verify each reclassification rather than assuming it.

## 9. Preserved decisions and negative boundaries

Preserve these boundaries during the re-audit:

- Reuse mature external capability when it closes the requirement; design only the remainder.
- Do not blindly copy an external repository or mechanically mirror its architecture.
- Do not create a runtime dependency on a construction/reference source repository unless explicitly selected.
- Do not let external methods/providers become AIMAGE authority merely because they informed the design.
- Do not make OpenAI conversation state, ComfyUI workflow JSON, Diffusers classes, InvokeAI project state, USD data, or another external representation the canonical AIMAGE job model merely for convenience.
- Do not copy GPL/noncommercial source into a permissive AIMAGE core without a separate explicit licensing decision.
- Do not infer that a library license covers model/checkpoint/content licenses.
- Do not import domain-specific machinery into generic AIMAGE core merely because it coexists with a useful concept.
- Do not build a custom image-edit/repair executor when a provider capability already performs the actual edit.
- Conversely, do not collapse AIMAGE into one provider wrapper; keep only cross-provider semantics that materially preserve user intent, authority, approval, and repair decisions.
- Keep Continuity/Handoff infrastructure outside Image Engine product semantics.
- Keep Image Engine Architecture/Core separate from concrete Feature/Domain implementations.
- Do not start implementation before the widened reuse re-audit is reviewed/accepted.

## 10. Current uncertainty

Unresolved items now include:

- which current `DESIGN` classifications should become `ADOPT`, `ADAPT`, or `ADAPT + small AIMAGE extension`;
- whether existing standards/patterns can materially reduce custom artifact, workflow, geometry, persistence, approval, and adapter semantics;
- what exact semantic residue is genuinely unique to AIMAGE after external reuse is maximized;
- exact acquisition mode, license/provenance, runtime coupling, and replacement boundary for newly considered candidates;
- whether any external system is useful only as design evidence versus suitable code/service dependency;
- the eventual implementation language/runtime, which remains intentionally unresolved until the semantic/reuse boundary is clearer.

## 11. Exactly one next bounded action

**Perform a fresh evidence-backed re-audit of `plans/CAPABILITY_REUSE_MATRIX.md` and `plans/EXTERNAL_REUSE_PLAN.md`, widening the search to mature creative-tool, VFX/DCC, asset/provenance, durable-workflow, plugin/capability, and provider-native editing systems; reclassify each materially affected capability so native AIMAGE `DESIGN` is minimized to only semantics not adequately supplied by mature external solutions.**

This one action includes updating the planning documents and this continuity state to reflect the accepted result. It does **not** authorize provider/core implementation.

## 12. Expected transition

If the re-audit succeeds, AIMAGE should have:

- a narrower, evidence-backed native `DESIGN` set;
- explicit `ADOPT / ADAPT / DESIGN` changes and rationale;
- acquisition/integration decisions for newly accepted external candidates;
- a clean split between provider-native edit execution and AIMAGE repair planning/orchestration;
- enough certainty to identify the genuinely remaining AIMAGE-native semantic contracts.

Only then should the next continuity state advance to native Engine/Core semantic design, if any remains.

## 13. Stop / replan conditions

Stop and replan if:

- fresh AIMAGE authority materially changes the phase or product boundaries;
- a newer accepted reuse audit supersedes this action;
- external evidence invalidates the current workflow/product boundary itself rather than merely shrinking native design;
- licensing/distribution direction changes materially;
- more than one incompatible high-level architecture remains viable and selecting one exceeds a bounded reuse re-audit;
- the user changes the reuse-first policy or authorizes implementation instead.
