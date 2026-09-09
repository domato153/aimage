# AIMAGE Current Repository-Work Continuity

Status: current repository-work continuity locator for the active planning/design slice. This file records decision-relevant current state; it does not replace `governance/CONTINUITY.md`, `governance/continuity/REPOSITORY_WORK.md`, root `AGENTS.md`, or any future Image Engine specification.

## 1. Authority snapshot

- Repository: `domato153/aimage`
- Authoritative branch: `main`
- Accepted/base commit at this continuity capture: `db5adaac8ebfc1a577a3b8f3ac4e334e00b3e6b7`
- Current governing entrypoint: `AGENTS.md`
- Continuity method: `governance/CONTINUITY.md`
- Repository-work profile: `governance/continuity/REPOSITORY_WORK.md`
- Handoff method: `.agents/skills/handoff/SKILL.md`

Fresh repository state always governs current factual state if these literals later move.

## 2. Current phase and scope

Phase: **planning / design only**.

Current work is to revise the AIMAGE Image Engine plan and capability decomposition. No Image Engine implementation has started, and this continuity state does not authorize implementation, adoption of external code, or a later merge merely because a design becomes obvious.

## 3. Completed foundation

The following foundation is accepted and should not be reopened without new evidence or an explicit scope change:

- a thin GPT Project bootstrap routes consequential work to current root `AGENTS.md` rather than duplicating project rules;
- root `AGENTS.md` separately routes Continuity and Handoff;
- `governance/CONTINUITY.md` is the AIMAGE-owned cross-context state/reconciliation contract;
- `.agents/skills/handoff/SKILL.md` is the AIMAGE-owned live-transfer construction/consumption method and delegates continuity semantics to the continuity contract/profile;
- runtime Continuity/Handoff interpretation has no dependency on `domato153/translation`; that repository is construction provenance/audit evidence only;
- Continuity/Handoff infrastructure remains separate from Image Engine Architecture/Core and AIMAGE Features/Domain Capabilities;
- the intended product dependency direction remains `features/domain capabilities -> engine interfaces`.

## 4. Current objective

Revise the AIMAGE plan so capability design follows an **evidence-first acquire/adapt/design decision rule** rather than assuming every mechanism should be invented inside AIMAGE.

For each planned capability, first determine whether a suitable external method, component, workflow pattern, specification, or reusable implementation already exists.

- If a suitable external solution exists and is validated, reusable, legally compatible, and architecturally compatible, prefer adopting or adapting it rather than re-designing the same mechanism from scratch.
- Internalize the semantics AIMAGE needs, record provenance, close unintended source-repository/runtime dependencies, and keep AIMAGE authority explicit.
- If no suitable external solution exists, or available solutions fail AIMAGE requirements, design an AIMAGE-native mechanism.

This is a planning principle, not blanket authorization to copy code or add dependencies.

## 5. Decision criteria for external reuse

External material is a reuse candidate only after bounded evidence review appropriate to the capability. Material criteria include, when relevant:

- functional fit to the AIMAGE requirement;
- demonstrated/credible use or validation rather than name recognition alone;
- license and redistribution/derivative compatibility;
- maintenance and provenance quality;
- architectural fit with AIMAGE boundaries;
- ability to avoid or explicitly justify runtime/source-repository coupling;
- ability to preserve AIMAGE authority, replaceability, and model/provider independence where required;
- cost/complexity compared with a native design.

Classification vocabulary for the upcoming plan review:

- `ADOPT` — use an external solution substantially as-is behind an AIMAGE-owned boundary where appropriate;
- `ADAPT` — reuse a validated method/component/idea but modify, wrap, reimplement, or internalize it to fit AIMAGE requirements and dependency/licensing constraints;
- `DESIGN` — create an AIMAGE-native mechanism because no suitable reusable solution closes the requirement.

A classification is not final merely because a candidate was found; it must survive the relevant evidence and boundary review.

## 6. Preserved decisions and negative boundaries

Preserve these boundaries during plan revision:

- Do not blindly copy an external repository or mechanically mirror its architecture.
- Do not create a runtime dependency on a construction/reference source repository unless that dependency is explicitly selected as part of the AIMAGE architecture.
- Do not let external methods or repositories become AIMAGE authority merely because they informed the design.
- Do not ignore license, provenance, security/maintenance, or replacement implications when reuse involves code/assets rather than ideas alone.
- Do not import domain-specific machinery that is irrelevant to AIMAGE merely because it coexists with a useful concept in the source project.
- Do not force `ADOPT` when adaptation is needed to close authority/dependency boundaries.
- Do not force `DESIGN` merely to make AIMAGE appear self-contained when a mature compatible solution already closes the requirement better.
- Do not start Image Engine implementation before the revised capability plan is reviewed/accepted.
- Keep Continuity/Handoff infrastructure outside Image Engine product semantics.
- Keep Image Engine Architecture/Core separate from concrete Feature/Domain implementations.

## 7. Current uncertainty

The capability inventory has not yet been reclassified under `ADOPT / ADAPT / DESIGN`.

Therefore it is currently unresolved:

- which planned AIMAGE mechanisms already have suitable reusable external solutions;
- which candidates are method-only references versus code/components worth integrating;
- where licensing or runtime dependency constraints force reimplementation/internalization;
- which capabilities genuinely require AIMAGE-native design.

No capability should be presumed `ADOPT`, `ADAPT`, or `DESIGN` until that bounded review is performed.

## 8. Exactly one next bounded action

**Inventory the planned Image Engine/Core and Feature/Domain capabilities, then for each capability perform a bounded external-evidence search and classify it as `ADOPT`, `ADAPT`, or `DESIGN`, recording rationale, candidate provenance, dependency/licensing implications, and unresolved gaps.**

This action is planning/research only. It does not authorize implementation.

## 9. Expected transition

If the next action succeeds, AIMAGE should have a revised capability plan that distinguishes:

- mature external capabilities/methods that should be reused;
- external ideas/components that should be adapted or internalized;
- genuine design gaps requiring AIMAGE-native architecture;
- interfaces/boundaries needed to keep adopted/adapted components replaceable and subordinate to AIMAGE authority.

That revised plan becomes the basis for the later Image Engine Architecture design/audit.

## 10. Stop / replan conditions

Stop and replan before implementation if:

- fresh AIMAGE authority materially changes these boundaries or the current phase;
- an external candidate would require a license/runtime dependency incompatible with the intended project;
- external evidence materially contradicts an assumed capability decomposition;
- reuse would blur Continuity/Handoff, Engine Core, and Feature/Domain ownership;
- more than one materially different architecture remains viable and the choice affects downstream boundaries;
- the user changes the reuse-vs-native-design policy.
