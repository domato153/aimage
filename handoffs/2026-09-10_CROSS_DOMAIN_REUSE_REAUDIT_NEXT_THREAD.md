# AIMAGE Next-Thread Handoff — Cross-Domain Reuse Re-audit

Packet status: **ACTIVE continuity evidence after fresh reconciliation and adoption**. This packet supersedes `handoffs/2026-09-10_REUSE_MATRIX_REAUDIT_NEXT_THREAD.md` once current AIMAGE authority adopts this successor.

## Identity / locator

- Repository: `domato153/aimage`
- Construction branch: `aimage-stage/cross-domain-reuse-handoff-reaudit`
- Path: `handoffs/2026-09-10_CROSS_DOMAIN_REUSE_REAUDIT_NEXT_THREAD.md`
- Construction base `main`: `09edfa4a0b0760640c11280f721aaaa475a6fb52`
- Handoff re-audit: `audits/NEXT_THREAD_HANDOFF_REAUDIT_2026-09-10.md`
- Governing handoff method: `.agents/skills/handoff/SKILL.md`
- Governing continuity method: `governance/CONTINUITY.md`
- Applicable profile: `governance/continuity/REPOSITORY_WORK.md`
- Canonical immutable commit locator: current continuity / the derived next-thread prompt must point to the exact commit that first contains this finalized packet. Fresh live AIMAGE authority controls whether this packet remains current.

## Immediate objective

Before AIMAGE designs any remaining Image Engine/Core capability, perform a **capability-first cross-domain reuse re-audit**.

For each capability currently classified as `DESIGN` or partly `DESIGN`, translate the AIMAGE term into the underlying abstract problem and search mature fields outside image generation for standards, libraries, architectures, and production methods that already solve that problem.

The goal is to reduce AIMAGE-native design to the smallest semantic residue that genuinely has to remain AIMAGE-owned.

## Current phase and authorized scope

- Phase: **planning / design / research only**.
- Authorized: fresh research, standards/architecture comparison, capability reclassification, planning-document repair, workflow simplification when evidence requires it, continuity update, bounded PR/adoption of the planning result.
- Stop boundary: **no Image Engine implementation, provider integration, package installation, external source import, runtime dependency change, or production code adoption** merely because a candidate is found.

## Fresh authority snapshot at construction

- Accepted `main`: `09edfa4a0b0760640c11280f721aaaa475a6fb52`
- Current root route: `AGENTS.md`
- Current state: `governance/continuity/CURRENT.md`
- Architecture boundary: `architecture/BOUNDARIES.md`
- Workflow target: `plans/WORKFLOW_TARGET.md`
- Capability matrix: `plans/CAPABILITY_REUSE_MATRIX.md`
- External reuse plan: `plans/EXTERNAL_REUSE_PLAN.md`
- Predecessor handoff: `handoffs/2026-09-10_REUSE_MATRIX_REAUDIT_NEXT_THREAD.md`

Fresh live state outranks these literals if it later moves.

## Current situation

### Confirmed

1. AIMAGE already has accepted Continuity/Handoff infrastructure, thin Project bootstrap, root AGENTS routing, high-level engine-vs-feature boundary, workflow target, initial reuse matrix, and external acquisition policy.
2. The accepted principle is reuse-first: `ADOPT` or `ADAPT` mature external capability when it closes the requirement; `DESIGN` only the genuine remainder.
3. Initial research focused too heavily on image-generation projects and likely overclassified several generic engineering/creative-production problems as AIMAGE-native design.
4. GPT Image/OpenAI and other backends already provide actual targeted/delta/masked/multi-turn editing capabilities. AIMAGE should not create a custom partial-image repair renderer. Its role is repair planning/orchestration, preservation intent, capability selection, execution through an adapter, and re-review.
5. The predecessor packet already widened research toward InvokeAI, OpenAssetIO, W3C PROV, OpenUSD, Temporal/equivalent workflows, capability negotiation, and provider-native editing.
6. A second audit found that naming good candidates is insufficient. The next thread must search **by abstract capability across non-image fields**, not merely inspect a predefined list.

### Supported hypothesis to challenge

Several remaining `DESIGN` areas may shrink to `ADAPT`, `ADOPT`, or `ADAPT + small AIMAGE extension`. Even apparently AIMAGE-specific concepts should survive only if they provide real cross-provider/user-control value not already obtainable by composing mature external primitives.

## Mandatory research method

For **every materially retained `DESIGN` or partial-`DESIGN` capability**:

1. state the AIMAGE capability in abstract problem terms;
2. identify mature adjacent fields that solve the same class of problem;
3. search official standards/specifications, mature implementations, established industry patterns, and relevant technical/academic literature as appropriate;
4. identify the strongest external candidates;
5. test `ADOPT`, `ADAPT`, method/schema reuse, interoperability, and composition of multiple mature solutions;
6. only then retain native `DESIGN`;
7. if `DESIGN` remains, record the smallest AIMAGE-specific semantic residue and why external composition is insufficient.

**Lack of a project using AIMAGE's exact vocabulary is not evidence that the problem is unsolved.**

A `DESIGN` classification has a burden of proof. It should record:

- abstract problem;
- searched fields;
- best external candidates;
- why direct adoption/adaptation/composition does not close the requirement;
- exact semantic residue AIMAGE must own.

## Cross-domain discovery surface

The receiver is not limited to these examples, but should explicitly consider them where relevant.

### 1. Workflow/state/history/human gates

Search beyond image tools:

- durable workflow engines;
- statecharts/state machines;
- BPMN/user-task patterns;
- event sourcing and append-only history;
- saga/compensation patterns where relevant.

Questions:

- Does AIMAGE need its own lifecycle semantics, or only a thin domain profile over mature workflow primitives?
- Are approval/pause/resume/retry/history already standard machinery?

### 2. Artifact identity/version/provenance

Search:

- DAM/MAM systems;
- OpenAssetIO and similar media asset boundaries;
- W3C PROV;
- version-control/content-addressed-storage/build provenance;
- supply-chain provenance patterns;
- C2PA where exported media provenance is relevant.

Questions:

- Which identity/lineage semantics are generic and should be reused?
- What, if anything, must AIMAGE add for accepted/rejected/derived image-job state?

### 3. Geometry/composition/spatial constraints

Search:

- OpenUSD and VFX/DCC scene graphs;
- CAD scene/constraint models;
- game-engine transforms/scene graphs;
- UI constraint solvers/layout engines such as relative alignment/distance systems;
- 2D spatial-relation representations.

Questions:

- Can camera, transform, relation, distance, alignment, layer, override, and constraint primitives be adapted rather than invented?
- What thin semantic layer is needed for language such as `same row`, `right of`, `slightly behind`, `distance`, `gaze`, and reading order?

### 4. RenderSpec / provider lowering

Search:

- compiler intermediate representations;
- build systems and execution plans;
- query planners;
- job specifications;
- validation/lowering/normalization architectures.

Questions:

- Is `RenderSpec` best understood as a small AIMAGE IR that compiles into provider-specific requests?
- Which IR/versioning/validation patterns can be adopted rather than designed ad hoc?

### 5. Provider adapters and capability negotiation

Search:

- plugin architectures;
- ports/adapters/hexagonal systems;
- driver models;
- protocol feature negotiation;
- hardware/API capability descriptors and compatibility negotiation.

Questions:

- Can mature capability-set/feature-negotiation patterns replace bespoke provider machinery?
- What AIMAGE-specific vocabulary is actually necessary?

### 6. Reference authority / partial approval / locks / overrides

Search:

- DCC/CAD layer locking and non-destructive overrides;
- policy/constraint systems;
- layered configuration/override semantics;
- creative review/approval workflows;
- selective staging/approval/version-review patterns.

Questions:

- Which pieces of identity/style/structure/reference separation are already represented elsewhere?
- Is the genuinely new part only a thin user-intent authority mapping across visual dimensions?
- Can partial-dimension approval reuse established lock/override/review primitives?

### 7. Persistence/schema/configuration

Search:

- schema evolution;
- versioned serialization;
- configuration overlays;
- project-state persistence patterns;
- content-addressable artifacts and immutable snapshots.

Do not choose a database before the semantic boundary is understood.

### 8. Repair planning/orchestration

Treat actual image editing as provider capability when available.

Search analogues in:

- diagnosis/planning/executor separation;
- minimum-change repair;
- transaction compensation;
- planner/tool orchestration;
- fault localization followed by bounded action.

AIMAGE should own only the repair decision semantics needed to:

1. identify failed variable(s);
2. preserve successful/locked elements;
3. choose the cheapest suitable provider/tool capability;
4. express the intended delta;
5. execute through an adapter;
6. verify the repair did not regress protected dimensions.

Do not reinvent the renderer/editor.

## Existing named candidates that still require fresh verification

Candidate names remain useful evidence targets, not predetermined answers:

- InvokeAI;
- OpenAssetIO;
- W3C PROV;
- OpenUSD;
- Temporal or equivalent durable-workflow systems;
- OpenAI/GPT Image targeted editing;
- ComfyUI;
- Diffusers;
- Nori;
- GenAI Illustration Pipeline;
- Krita AI Diffusion patterns;
- style-consistency-ai patterns.

For new candidates, determine acquisition mode, license/provenance, runtime/source coupling, maintenance/currentness, AIMAGE boundary, and replacement/fallback behavior.

## AIMAGE-specific value test

Do not retain a native semantic merely because it is provider-neutral.

For every proposed AIMAGE-owned concept ask:

> What user-visible or cross-provider control would be lost if AIMAGE did not own this semantic and instead used mature external primitives directly?

If the answer is only renaming, wrapper convenience, storage preference, or duplication, do not keep it as native core design.

Possible legitimate residues — still to be challenged — include:

- user-intent authority across visual dimensions;
- partial-dimension approval/lock meaning;
- provider-neutral preservation intent;
- cross-provider capability-aware orchestration.

These are hypotheses, not exemptions from the reuse audit.

## Composition is allowed

Do not require one external project to solve a whole AIMAGE capability.

A valid result may combine:

- a standard data model;
- an established workflow/state pattern;
- an existing provider capability;
- a small AIMAGE semantic adapter.

Only the irreducible glue/semantic residue should remain native.

## Workflow simplification check

`plans/WORKFLOW_TARGET.md` remains the current accepted product target, but the re-audit should test whether any stages exist only because prior planning assumed missing infrastructure.

A stage may be:

- collapsed;
- made optional;
- represented as state instead of a separate phase;
- delegated to a provider/tool;
- preserved if it still reflects a real user decision boundary.

Do not rewrite the workflow without evidence, but do not preserve ceremony merely because it was previously written down.

## Preserved decisions / negative boundaries

- Reuse mature capability first; design only the remainder.
- Search by abstract problem, not exact AIMAGE terminology.
- Do not blindly copy whole external repositories.
- Reuse can be package dependency, service adapter, selected permissive source import, interoperability snapshot, clean-room method adaptation, reference-only evidence, or composition of multiple mature pieces.
- External systems never become AIMAGE authority merely by informing design.
- Do not make OpenAI conversation state, ComfyUI workflow JSON, Diffusers classes, InvokeAI project state, USD data, or another external representation the canonical AIMAGE job model merely for convenience.
- Do not copy GPL/noncommercial source into a permissive AIMAGE core without an explicit licensing decision.
- Do not infer model/checkpoint/content licenses from library licenses.
- Do not build a custom image-edit/repair executor where provider capability already performs the edit.
- Do not collapse AIMAGE into a thin wrapper around one provider.
- Keep Continuity/Handoff separate from Image Engine product semantics.
- Keep `features/domain capabilities -> engine interfaces` unless an explicitly accepted architecture revision changes it.
- Keep one-shot generation simple; do not add workflow ceremony without decision value.
- Do not implement providers/core during this planning slice.

## Completed scope

Do not restart without new evidence:

- Continuity adoption;
- Handoff adoption;
- thin GPT Project bootstrap;
- root AGENTS routing;
- initial architecture boundary;
- initial workflow target;
- initial reuse matrix;
- initial external acquisition plan;
- prior conclusion that partial-image edit execution belongs to providers when available.

The current task is a **cross-domain re-audit of the remaining native-design surface**.

## Decision-relevant dependencies / artifacts

All required state is durable in `domato153/aimage`. No chat-only/local image or temporary artifact is needed for this next action.

Fresh-check only the bounded surfaces relevant to this planning boundary, including related open PRs/active work. Do not crawl unrelated branches.

## Exact next bounded action

**Re-audit every materially `DESIGN` or partial-`DESIGN` capability in `plans/CAPABILITY_REUSE_MATRIX.md` using capability-first cross-domain research outside image generation, update `plans/CAPABILITY_REUSE_MATRIX.md` and `plans/EXTERNAL_REUSE_PLAN.md` with evidence-backed reclassifications and acquisition boundaries, simplify `plans/WORKFLOW_TARGET.md` only where the same evidence proves a stage redundant, and update `governance/continuity/CURRENT.md` so only the irreducible AIMAGE-native semantic residue remains for the following design slice.**

This is one bounded planning action. It does not authorize implementation.

## Required result for each materially affected capability

Record, as applicable:

- old classification;
- abstract problem statement;
- external fields searched;
- strongest standard/tool/method candidates;
- evidence/currentness;
- new classification (`ADOPT`, `ADAPT`, `ADAPT + small AIMAGE extension`, `DESIGN`);
- acquisition mode;
- license/provenance/runtime coupling;
- replacement/fallback boundary;
- exact AIMAGE-owned semantic residue;
- reason a retained `DESIGN` could not be closed by external composition.

## Expected transition

A successful next thread leaves:

- a materially narrower and defensible native `DESIGN` set;
- explicit evidence for every retained native semantic;
- newly accepted cross-domain reuse candidates and integration boundaries;
- provider-native editing clearly separated from AIMAGE repair orchestration;
- any evidence-backed workflow simplifications;
- an updated CURRENT with exactly one next action: design only the genuinely remaining AIMAGE semantic layer, or a different action if the re-audit shows even that framing is wrong.

## Stop / replan conditions

Return `STALE_REPLAN` or stop before mutation if:

- current AIMAGE authority materially moved or a newer accepted handoff/audit supersedes this route;
- the user changes phase or reuse-first policy;
- research invalidates the product/workflow boundary itself rather than merely shrinking native design;
- a license/runtime/distribution choice forces a materially different architecture;
- multiple incompatible high-level architectures remain and choosing among them exceeds this bounded re-audit.

## Cold-start read route

A zero-chat receiver should read in order:

1. fresh current `main` and `AGENTS.md`;
2. current `.agents/skills/handoff/SKILL.md`;
3. current `governance/CONTINUITY.md`;
4. current `governance/continuity/REPOSITORY_WORK.md`;
5. this successor packet from the exact immutable commit locator supplied by current continuity/derived prompt;
6. `audits/NEXT_THREAD_HANDOFF_REAUDIT_2026-09-10.md`;
7. current `governance/continuity/CURRENT.md`;
8. current `architecture/BOUNDARIES.md`;
9. current `plans/WORKFLOW_TARGET.md`;
10. current `plans/CAPABILITY_REUSE_MATRIX.md`;
11. current `plans/EXTERNAL_REUSE_PLAN.md`;
12. bounded discovery for newer work touching this same reuse/design boundary.

Then independently re-derive dependencies, challenge the next action, and return exactly `ACCEPTED` or `STALE_REPLAN` before consequential continuation.

## Hard prohibitions

- Do not begin provider/core implementation.
- Do not search only image-generation projects.
- Do not search only the named candidate list.
- Do not leave `DESIGN` because no project uses the same terminology.
- Do not require a single upstream system to satisfy an entire capability before crediting reuse.
- Do not treat provider edit capability as AIMAGE repair-authority semantics.
- Do not invent a custom repair renderer when existing provider/tool execution suffices.
- Do not copy restricted-license source without an explicit compatible licensing decision.
- Do not reopen Continuity/Handoff without fresh evidence of a defect.

## Receiver acceptance

The receiver must resolve current AIMAGE governing files, open this packet from its exact immutable locator, fresh-read the bounded decision dependencies, challenge the next action, and return:

- `ACCEPTED` — this cross-domain reuse re-audit remains the unique next bounded action; or
- `STALE_REPLAN` — fresh drift, contradiction, supersession, or ambiguity changes/de-uniques it.

Only after `ACCEPTED` should the receiver assume operational ownership of the planning re-audit.