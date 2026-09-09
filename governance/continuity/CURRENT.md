# AIMAGE Current Repository-Work Continuity

Status: current repository-work continuity locator for the active planning/design/research slice. This file records decision-relevant current state; it does not replace `governance/CONTINUITY.md`, `governance/continuity/REPOSITORY_WORK.md`, root `AGENTS.md`, or Image Engine specifications.

## 1. Authority snapshot

- Repository: `domato153/aimage`
- Authoritative branch: `main`
- Accepted `main` immediately before this successor-handoff update: `09edfa4a0b0760640c11280f721aaaa475a6fb52`
- Current governing entrypoint: `AGENTS.md`
- Continuity method: `governance/CONTINUITY.md`
- Repository-work profile: `governance/continuity/REPOSITORY_WORK.md`
- Handoff method: `.agents/skills/handoff/SKILL.md`
- **ACTIVE successor packet candidate:** `handoffs/2026-09-10_CROSS_DOMAIN_REUSE_REAUDIT_NEXT_THREAD.md`
- **Immutable successor packet construction locator:** repository `domato153/aimage`, commit `dbd514b5adfbf149177fcfcf42f548f9bc99b51a`, path `handoffs/2026-09-10_CROSS_DOMAIN_REUSE_REAUDIT_NEXT_THREAD.md`
- Handoff re-audit: `audits/NEXT_THREAD_HANDOFF_REAUDIT_2026-09-10.md`
- **SUPERSEDED predecessor after successor adoption:** `handoffs/2026-09-10_REUSE_MATRIX_REAUDIT_NEXT_THREAD.md` at prior accepted state `09edfa4a0b0760640c11280f721aaaa475a6fb52`

Fresh repository state always governs current factual state if these literals later move. The successor packet becomes operational continuity evidence only after current AIMAGE authority adopts the candidate and a receiver freshly reconciles it.

## 2. Current phase and scope

Phase: **planning / design / research only**.

The immediate work is **not native Engine/Core contract design yet**. The next slice must first perform a capability-first **cross-domain reuse re-audit** so AIMAGE does not redesign mature solutions that already exist outside image generation.

No Image Engine implementation, provider integration, package installation, external-code import, runtime dependency change, or production code adoption is authorized by this continuity state.

## 3. Completed foundation

The following foundation is accepted and should not be reopened without new evidence or an explicit scope change:

- thin GPT Project bootstrap -> current root `AGENTS.md`;
- separate Continuity and Handoff routes;
- AIMAGE-owned `governance/CONTINUITY.md` and `.agents/skills/handoff/SKILL.md` with no runtime dependency on `domato153/translation`;
- Continuity/Handoff separated from Image Engine/Core and Feature/Domain product semantics;
- intended product dependency direction `features/domain capabilities -> engine interfaces`;
- accepted `plans/WORKFLOW_TARGET.md`;
- accepted initial `plans/CAPABILITY_REUSE_MATRIX.md`;
- accepted initial `plans/EXTERNAL_REUSE_PLAN.md`;
- evidence-first `ADOPT / ADAPT / DESIGN` policy;
- decision that provider-native targeted/delta/masked/multi-turn editing should execute image repairs when suitable, while AIMAGE owns only repair planning/orchestration and preservation intent.

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

This workflow is still a target, not untouchable ceremony. The cross-domain re-audit may simplify a stage if evidence shows it can be collapsed, made optional, represented as state, or delegated without losing a real user decision boundary.

## 5. Why the prior next action is superseded

The earlier CURRENT moved from native Engine/Core design to a broader external-reuse re-audit. A second cold-reader audit found that even that handoff remained too candidate-driven: it named good systems such as InvokeAI/OpenUSD/Temporal but did not force the receiver to search the mature **non-image field corresponding to every remaining `DESIGN` problem**.

That creates a risk of checking a shortlist, finding no exact AIMAGE equivalent, and prematurely returning to bespoke design.

Therefore the prior reuse-re-audit packet is superseded by the cross-domain successor once adopted.

## 6. Governing research rule

For every materially `DESIGN` or partial-`DESIGN` capability:

1. translate the AIMAGE term into its **abstract problem**;
2. identify mature adjacent domains that solve that problem;
3. search standards/specifications, maintained implementations, established industry patterns, and relevant technical/academic literature as appropriate;
4. test direct `ADOPT`, `ADAPT`, method/schema reuse, interoperability, and **composition of multiple mature solutions**;
5. retain `DESIGN` only for the smallest irreducible AIMAGE-specific semantic residue.

A lack of software using AIMAGE's exact vocabulary is not evidence that the underlying problem is unsolved.

A retained `DESIGN` has a burden of proof: record the abstract problem, fields searched, strongest candidates, why external adoption/adaptation/composition is insufficient, and the exact semantic residue AIMAGE must own.

## 7. Cross-domain discovery families

The next slice should explicitly consider, where relevant:

- **creative tools / VFX / DCC / CAD / game engines** — project state, scene graphs, transforms, layers, non-destructive overrides, review/lock patterns;
- **UI layout and constraint solvers** — alignment, distance, relative placement, same-row/right-of/behind constraints;
- **compiler IR / build systems / query planners / job specifications** — provider-neutral Render Spec, validation, lowering, capability-dependent execution plans;
- **durable workflows / statecharts / BPMN / event sourcing** — long-running state, human gates, pause/resume, retry, history;
- **DAM/MAM / OpenAssetIO / version control / content-addressed storage / build and supply-chain provenance** — artifact identity, versions, resolution, derivation, immutable snapshots;
- **W3C PROV and C2PA where applicable** — internal derivation concepts versus optional exported-content provenance;
- **plugin / driver / protocol / hardware capability negotiation** — provider capability descriptors, compatibility, fallback, optional features;
- **policy / layered configuration / selective lock / creative-review systems** — visual-dimension authority, partial approval, overrides and lock/unlock behavior;
- **schema evolution / versioned serialization / configuration overlays** — persistence and contract evolution without bespoke infrastructure;
- **diagnosis/planning/executor and minimum-change/compensation patterns** — repair orchestration over existing provider execution;
- **provider-native image editing** — GPT Image/OpenAI, ComfyUI, Diffusers and other backends as actual edit executors.

Named systems such as InvokeAI, OpenAssetIO, W3C PROV, OpenUSD, Temporal, OpenAI/GPT Image, ComfyUI, Diffusers, Nori, GenAI Illustration Pipeline, Krita AI Diffusion, and style-consistency-ai remain evidence targets, not predetermined adoption decisions.

## 8. Repair semantics decision

AIMAGE should not build a custom partial-image repair/editing engine when providers/tools already expose suitable edit capabilities.

Provider/backend capability may execute:

- targeted/delta edit;
- masked/regional edit;
- multi-turn controlled edit;
- structural-control correction;
- reference-conditioned edit.

AIMAGE's provider-neutral responsibility is higher-level **repair planning/orchestration**:

1. identify failed variable(s);
2. identify successful/locked elements that must be preserved;
3. choose the cheapest suitable repair path/provider capability;
4. express delta and preservation intent;
5. execute through the selected adapter;
6. re-review for repair success and regression.

Even these orchestration semantics should reuse mature diagnosis/planning patterns where suitable rather than being designed ad hoc.

## 9. AIMAGE-specific value test

Do not keep a native semantic merely because it is provider-neutral.

For every proposed AIMAGE-owned concept ask:

> What user-visible or cross-provider control would be lost if AIMAGE used mature external primitives directly instead?

If the answer is only naming, wrapper convenience, storage preference, or duplication, it should not survive as native core design.

Possible genuine residues — still hypotheses to challenge — include cross-provider user-intent authority, partial-dimension approval/lock meaning, provider-neutral preservation intent, and capability-aware orchestration.

## 10. Preserved decisions and negative boundaries

- Reuse mature external capability when it closes the requirement; design only the remainder.
- Search by abstract problem, not exact AIMAGE terminology or only image-generation products.
- Do not blindly copy whole external repositories.
- Reuse may be package dependency, service/backend adapter, selected permissive source import, interoperability snapshot, clean-room method adaptation, reference-only evidence, or composition of multiple mature pieces.
- External providers/standards/tools remain evidence or dependencies behind AIMAGE boundaries, not AIMAGE authority.
- Do not make OpenAI conversation state, ComfyUI workflow JSON, Diffusers classes, InvokeAI project state, USD data, or another external representation canonical AIMAGE job state merely for convenience.
- Do not copy GPL/noncommercial source into a permissive AIMAGE core without a separate explicit licensing decision.
- Do not infer model/checkpoint/content licenses from library licenses.
- Do not build a custom image-edit/repair executor where provider capability already performs the edit.
- Conversely, do not collapse AIMAGE into a thin wrapper around one provider.
- Keep Continuity/Handoff outside Image Engine product semantics.
- Keep Image Engine/Core separate from concrete Feature/Domain implementations unless an accepted architecture revision changes that boundary.
- Keep trivial one-shot generation simple.
- Do not start implementation before the cross-domain reuse re-audit is accepted.

## 11. Current uncertainty

Unresolved:

- which existing `DESIGN` rows should become `ADOPT`, `ADAPT`, `ADAPT + small AIMAGE extension`, or remain `DESIGN`;
- what non-image standards/patterns best close workflow, artifact, geometry, approval, adapter, RenderSpec, persistence, and repair semantics;
- whether the workflow target can be materially simplified after reuse;
- exact AIMAGE semantic residue that remains after external composition;
- acquisition mode, license/provenance, runtime coupling, maintenance/currentness, replacement/fallback for newly accepted candidates;
- eventual implementation language/runtime, intentionally deferred until the semantic/reuse boundary is clearer.

## 12. Exactly one next bounded action

**Re-audit every materially `DESIGN` or partial-`DESIGN` capability in `plans/CAPABILITY_REUSE_MATRIX.md` using capability-first cross-domain research outside image generation; update `plans/CAPABILITY_REUSE_MATRIX.md` and `plans/EXTERNAL_REUSE_PLAN.md` with evidence-backed reclassifications and acquisition boundaries, simplify `plans/WORKFLOW_TARGET.md` only where the same evidence proves a stage redundant, and update this CURRENT so only the irreducible AIMAGE-native semantic residue remains for the following design slice.**

This is one bounded planning action and does **not** authorize provider/core implementation.

## 13. Expected transition

After a successful re-audit, AIMAGE should have:

- a materially narrower and defensible native `DESIGN` set;
- explicit negative evidence for every retained `DESIGN`;
- accepted cross-domain standards/tools/patterns and acquisition boundaries;
- provider-native image editing cleanly separated from AIMAGE repair orchestration;
- any evidence-backed workflow simplification;
- exactly one next action aimed only at the genuinely remaining AIMAGE-specific semantic layer, unless the audit shows a different architecture direction is warranted.

## 14. Stop / replan conditions

Stop and replan if:

- fresh AIMAGE authority materially changes the phase/product boundaries;
- a newer accepted handoff/reuse audit supersedes this action;
- the user changes the reuse-first policy or authorizes a different phase;
- research shows the current product/workflow boundary itself is materially wrong rather than merely over-designed;
- license/runtime/distribution constraints force a materially different high-level architecture;
- multiple incompatible architectures remain and choosing among them exceeds this bounded cross-domain audit.
