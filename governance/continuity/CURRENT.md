# AIMAGE Current Repository-Work Continuity

Status: current repository-work continuity locator for the active planning/design slice. This file records decision-relevant current state; it does not replace `governance/CONTINUITY.md`, `governance/continuity/REPOSITORY_WORK.md`, root `AGENTS.md`, or Image Engine specifications.

## 1. Authority snapshot

- Repository: `domato153/aimage`
- Authoritative branch: `main`
- Accepted/base commit at the start of this planning slice: `3ed8f40509a65fecd831149f32acc71c56c2ffa3`
- Current governing entrypoint: `AGENTS.md`
- Continuity method: `governance/CONTINUITY.md`
- Repository-work profile: `governance/continuity/REPOSITORY_WORK.md`
- Handoff method: `.agents/skills/handoff/SKILL.md`

Fresh repository state always governs current factual state if these literals later move.

## 2. Current phase and scope

Phase: **planning / design only**.

Current work is defining the AIMAGE image-production workflow, classifying capabilities by external reuse potential, and fixing the integration boundary for reusable external systems before native Image Engine architecture is designed.

No Image Engine implementation, external-code adoption, package installation, provider integration, or runtime dependency change is authorized merely by these plans.

## 3. Completed foundation

The following foundation is accepted and should not be reopened without new evidence or an explicit scope change:

- a thin GPT Project bootstrap routes consequential work to current root `AGENTS.md` rather than duplicating project rules;
- root `AGENTS.md` separately routes Continuity and Handoff;
- `governance/CONTINUITY.md` is the AIMAGE-owned cross-context state/reconciliation contract;
- `.agents/skills/handoff/SKILL.md` is the AIMAGE-owned live-transfer construction/consumption method and delegates continuity semantics to the continuity contract/profile;
- runtime Continuity/Handoff interpretation has no dependency on `domato153/translation`; that repository is construction provenance/audit evidence only;
- Continuity/Handoff infrastructure remains separate from Image Engine Architecture/Core and AIMAGE Features/Domain Capabilities;
- the intended product dependency direction remains `features/domain capabilities -> engine interfaces`;
- external reuse decisions follow an evidence-first `ADOPT / ADAPT / DESIGN` policy rather than assuming every mechanism should be invented locally.

## 4. Current planning outputs

When the following files are present on authoritative `main`, they form the current accepted planning baseline for the next architecture slice:

- `plans/WORKFLOW_TARGET.md` — full adaptive workflow target;
- `plans/CAPABILITY_REUSE_MATRIX.md` — engine/feature capability inventory and reuse classification;
- `plans/EXTERNAL_REUSE_PLAN.md` — acquisition modes and candidate-specific integration plan.

A work-branch copy of these files remains a proposal until it is adopted by current AIMAGE authority.

## 5. Workflow target now defined

The planned product workflow is an adaptive production loop rather than a prompt library:

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

The workflow is adaptive: low-risk one-shot requests do not need every stage.

## 6. External reuse decisions

Current planning conclusions:

### Direct adoption / optional runtime integration

- **OpenAI official SDK/API** — `ADOPT` as the first cloud image-provider adapter. Provider-native multi-reference, editing, multi-turn state, masks and image IDs stay behind the adapter.
- **Hugging Face Diffusers** — `ADOPT` as an optional local-provider library. Model/checkpoint licenses remain separately tracked.
- **ComfyUI** — `ADAPT` as an optional separately installed backend accessed through an AIMAGE adapter. Do not copy GPL core into AIMAGE core.

### Permissive selective reuse candidates

- **Nori (MIT)** — adapt project/bible/history/thin-adapter architecture; copy only bounded dependency-light modules after exact source audit.
- **GenAI Illustration Pipeline (MIT)** — adapt model-routing, QA/revision, fixtures and deterministic-finishing patterns; selectively import small generic utilities only after file-level audit.
- **ComfyUI workflow templates/blueprints (MIT)** — selected workflow artifacts may be snapshotted for the ComfyUI adapter with exact upstream provenance and validation; do not import the entire template repository.

### Method-only / clean-room sources

- **Krita AI Diffusion (GPL-3.0)** — design evidence for control layers, region edits, history/job UX and external-backend separation; no source copying under the current permissive-core direction.
- **style-consistency-ai (PolyForm Noncommercial 1.0.0)** — conceptual evidence for smallest-edit-first, atlas/closest-reference selection, corrective guidelines and escalation; independently reimplement concepts unless licensing changes.

## 7. External acquisition policy

External reuse must use an explicit acquisition mode:

- official package/SDK dependency;
- external service/backend adapter;
- selected permissive source import;
- interoperability artifact/schema snapshot;
- clean-room method adaptation;
- reference only.

Before code-level `ADOPT`/`ADAPT`, record exact source/version, immutable identity where applicable, license, selected paths, runtime/optional status, AIMAGE owner/adapter, transitive dependency implications, update policy, replacement boundary and AIMAGE-owned validation.

Do not use floating upstream `main` as sufficient provenance for copied or decision-critical material.

## 8. Native AIMAGE design gaps that remain

External research did **not** provide a complete reusable solution for the following core semantics, so these remain native design work:

1. provider-neutral image-job state model;
2. explicit reference-role authority contract;
3. approval and lock semantics;
4. provider-neutral Render Spec;
5. provider capability descriptor and adapter contract;
6. provider-neutral geometry/composition semantic contract;
7. artifact identity/version/provenance model;
8. generic review/repair schemas;
9. persistence boundary;
10. exact interface separation between engine and feature/domain strategies.

External sources may inform these designs but do not own them.

## 9. Preserved decisions and negative boundaries

Preserve these boundaries:

- Do not blindly copy an external repository or mechanically mirror its architecture.
- Do not create a runtime dependency on a construction/reference source repository unless explicitly selected.
- Do not let an external provider, workflow graph, or source repository become AIMAGE authority.
- Do not make ComfyUI workflow JSON, OpenAI conversation state, Diffusers pipeline classes, or another provider representation the canonical AIMAGE job model.
- Do not copy GPL or noncommercial source into a permissive AIMAGE core under the current plan without a separate licensing decision.
- Do not infer that the library license covers model/checkpoint/content licenses.
- Do not import book/manuscript/print-specific machinery into generic AIMAGE core merely because it comes from a useful production pipeline.
- Do not start implementation before the native core contracts and reuse boundaries are reviewed/accepted.
- Keep Continuity/Handoff infrastructure outside Image Engine product semantics.
- Keep Image Engine Architecture/Core separate from concrete Feature/Domain implementations.

## 10. Current uncertainty

The major external capability categories and acquisition paths are now classified, but code-level source audits have **not** yet been performed for selective MIT imports, and the native AIMAGE core contracts are not yet designed.

Unresolved items include:

- exact implementation language/runtime for the first engine slice;
- exact Nori modules, if any, worth source-level import rather than conceptual adaptation;
- exact GenAI pipeline utility files worth source-level import;
- exact ComfyUI workflow templates needed for first supported local workflows;
- storage technology, which should follow the native persistence contract rather than be selected first;
- the final provider capability vocabulary and Render Spec schema.

## 11. Exactly one next bounded action

**Design the native AIMAGE Engine/Core contracts that external providers and adapted feature strategies must plug into, beginning with the job state model, artifact/reference/approval semantics, Render Spec, provider capability/adapter boundary, and generic review/repair records; use the accepted external-reuse plan as a constraint and do not implement providers yet.**

If the workflow/reuse planning files have not yet been adopted on current `main`, the immediate action is instead to review/adopt that planning candidate before beginning native contract design.

## 12. Expected transition

After the next bounded action, AIMAGE should have a provider-neutral architecture contract capable of accepting the already-classified external integrations without letting any provider define core semantics.

Only after that architecture survives review should implementation planning begin.

## 13. Stop / replan conditions

Stop and replan if:

- fresh AIMAGE authority materially changes the phase or product boundaries;
- external evidence invalidates an adopted integration assumption;
- a proposed native contract merely renames one provider's API instead of remaining provider-neutral;
- licensing or distribution direction changes materially;
- more than one incompatible core architecture remains viable and the choice affects downstream implementation;
- the user changes the acquire/adapt/design policy.
