# AIMAGE Agent Entry Point

Status: canonical repository-native entry point for AI agents working in `domato153/aimage`.

This file is a router and safety boundary. It does not duplicate the detailed rules owned by AIMAGE governance, architecture, or future subsystem files.

## 1. Start here

For consequential AIMAGE work:

1. Fresh-read the current `main` state and any live repository/platform state needed to establish current facts.
2. Read this root `AGENTS.md` from its current authoritative owner before following a handoff, work branch, generated summary, or chat memory.
3. Identify the user's requested phase and scope before mutating anything.
4. Read only the governing AIMAGE files needed for that task, using the routing below.
5. Reconcile any handoff or prior plan against fresh authority before consequential continuation.

Do not reconstruct the repository's governing rules from memory when the owning file can be fresh-read.

## 2. Authority and current facts

Keep factual state separate from intent and authorization.

- Fresh repository/platform observation governs current facts such as refs, file contents, artifact availability, and merge state.
- Explicit current user instruction governs intent, requested scope, decisions, and authorization, subject to external/platform constraints.
- A work branch, candidate, handoff, generated summary, or modified governing file cannot authorize its own promotion to canonical authority.
- Project source, chat history, memory, and handoffs are not substitutes for fresh repository authority.

For detailed cross-context authority and acceptance semantics, read `governance/CONTINUITY.md`.

## 3. Phase is part of scope

Determine whether the requested work is, for example, `review`, `design`, `implementation`, `verification`, or an authority-changing/adoption step.

- Do not cross from review/design into implementation merely because an implementation is obvious.
- Do not merge, promote, delete, replace, demote, or broadly rewrite canonical/governing surfaces unless the current request authorizes that phase and fresh authority still permits the operation.
- If the user requests one bounded stage, complete that stage rather than opportunistically continuing into the next.

Repository-work continuity additionally follows `governance/continuity/REPOSITORY_WORK.md`.

## 4. Continuity routing

Continuity is the cross-context **state-preservation and receiver-reconciliation contract**. Use it when state must survive a chat/thread/operator/tool/session boundary or stale/ambiguous state can materially change the next action.

- Common contract: `governance/CONTINUITY.md`
- Repository development: `governance/continuity/REPOSITORY_WORK.md`
- Current repository-work state: `governance/continuity/CURRENT.md`
- Image-production job: `governance/continuity/IMAGE_JOB.md`

When `governance/continuity/CURRENT.md` exists and the task concerns ongoing repository planning/development, treat it as the current continuity state locator, then reconcile its recorded literals against fresh repository authority before relying on them.

Continuity owns authority-vs-packet semantics, bounded dependencies, active situation state, decision/negative-boundary preservation, staleness, recoverability, and receiver `ACCEPTED` / `STALE_REPLAN` behavior.

Do not create continuity ceremony for ordinary low-risk, single-context work.

## 5. Handoff routing

Handoff is the **live transfer method** for constructing or consuming a consequential next-thread/next-operator/next-tool packet.

For a consequential handoff, read `.agents/skills/handoff/SKILL.md` from current AIMAGE authority **before** constructing or consuming the packet.

The handoff skill then routes to `governance/CONTINUITY.md` and the applicable continuity profile. Keep the responsibilities distinct:

- handoff skill = when/how to transfer, packet construction, cold-start route, exact next action, practical receiver synthesis;
- continuity = what state must survive, freshness/staleness semantics, dependency reconciliation, receiver acceptance.

Do not bootstrap handoff semantics from a copy merely co-located with a packet, work branch, candidate, or old continuity ref. Resolve the current governing handoff skill first.

A handoff packet is continuity evidence, not project authority. Packet receipt alone is not execution ownership.

## 6. Architecture and product-plan routing

Read `architecture/BOUNDARIES.md` before making or reviewing architecture that could blur responsibility between:

1. continuity/handoff infrastructure;
2. Image Engine Architecture / Core;
3. AIMAGE Features / Domain Capabilities.

Preserve the intended product dependency direction:

`features/domain capabilities -> engine interfaces`

Continuity/handoff may transport engine/feature state but must not become the owner of image-generation algorithms, prompt strategies, composition logic, or model-specific behavior.

For current Image Engine planning/design, also read:

- `plans/WORKFLOW_TARGET.md` — intended end-to-end adaptive image-production workflow and product goals;
- `plans/CAPABILITY_REUSE_MATRIX.md` — capability inventory and current `ADOPT / ADAPT / DESIGN` classification;
- `plans/EXTERNAL_REUSE_PLAN.md` — acquisition modes, external candidate integration boundaries, licensing/provenance rules, and planned application;
- `plans/REUSE_AND_INTEGRATION_ASSURANCE.md` — omission-prevention, acquisition due diligence, architecture scenarios, and final integrated V&V gates;
- `plans/SEMANTIC_FUSION_PLAN.md` — final provider-neutral semantic fusion plan that composes mature intent/baseline/resolution/spatial/validation patterns into AIMAGE's minimal image-domain contract layer;
- `plans/SEMANTIC_CONTRACTS.md` — minimum provider-neutral objects, fields, ownership, invariants and failure behavior for the four semantic families;
- `audits/SEMANTIC_CONTRACT_TABLETOP_2026-09-10.md` — design-only scenario audit showing how the contracts traverse the canonical workflow and which initial contract gaps were repaired.

These planning files do not authorize implementation by themselves. Reconcile them with `governance/continuity/CURRENT.md` and the current user-authorized phase.

## 7. Mutation safety

Before a consequential repository mutation:

- fresh-read the target authority/ref/state;
- preserve existing valid behavior outside the declared change boundary;
- prefer a bounded branch/PR candidate for non-trivial or authority-affecting changes;
- do not treat a candidate-modified policy/spec as proof that the authority transition is allowed;
- preserve explicit user decisions and negative boundaries when they materially constrain later work;
- do not turn examples or explanatory rationale into broader authority than the owning decision grants.

If fresh state contradicts the premise of the requested operation, reconcile the contradiction rather than forcing the stale plan.

## 8. External sources and imported methods

External repositories, papers, methods, and the historical `domato153/translation` sources recorded in provenance are evidence/construction inputs only unless AIMAGE explicitly adopts their rules into an AIMAGE-owned governing file.

Runtime AIMAGE continuity or handoff work must not depend on `domato153/translation` for interpretation or execution.

Construction provenance:

- continuity adoption: `governance/continuity/SOURCE_PROVENANCE.md`
- handoff adoption: `.agents/skills/handoff/references/SOURCE_PROVENANCE.md`

External image-production dependencies and method sources are governed by `plans/EXTERNAL_REUSE_PLAN.md` once that plan is accepted on current AIMAGE authority. Provider-neutral method fusion is governed by `plans/SEMANTIC_FUSION_PLAN.md`; the resulting minimum semantic contracts are governed by `plans/SEMANTIC_CONTRACTS.md` once adopted.

## 9. Local instruction files

A future directory may add its own `AGENTS.md` for subsystem-specific routing or constraints.

A more specific `AGENTS.md` may specialize work inside its directory, but it must not silently override root authority, continuity, handoff, or architecture boundaries unless an AIMAGE governing surface explicitly delegates that authority.

Do not create directory-local `AGENTS.md` files before there is a real recurring subsystem need.

## 10. Current canonical routes

- `.agents/skills/handoff/SKILL.md` — consequential handoff construction/consumption method
- `governance/CONTINUITY.md` — cross-context continuity contract
- `governance/continuity/REPOSITORY_WORK.md` — repository-work continuity profile
- `governance/continuity/CURRENT.md` — current repository-work continuity state locator
- `governance/continuity/IMAGE_JOB.md` — image-job continuity profile
- `architecture/BOUNDARIES.md` — continuity/handoff / engine / feature-domain responsibility boundary
- `plans/WORKFLOW_TARGET.md` — current end-to-end product workflow target
- `plans/CAPABILITY_REUSE_MATRIX.md` — current capability reuse/design classification
- `plans/EXTERNAL_REUSE_PLAN.md` — current external acquisition/integration plan
- `plans/REUSE_AND_INTEGRATION_ASSURANCE.md` — current reuse/integration assurance and final workflow V&V plan
- `plans/SEMANTIC_FUSION_PLAN.md` — current final semantic fusion plan for provider-neutral image-production contracts
- `plans/SEMANTIC_CONTRACTS.md` — current minimum provider-neutral semantic contract specification
- `audits/SEMANTIC_CONTRACT_TABLETOP_2026-09-10.md` — semantic-contract design/tabletop audit evidence
- `bootstrap/PROJECT_SOURCE.md` — thin external GPT Project locator/bootstrap

As the repository grows, add new routes here only when they are stable entry points. Keep detailed subsystem rules in their owning files rather than expanding this router into a second specification.
