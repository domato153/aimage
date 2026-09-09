# AIMAGE External Reuse and Integration Plan

Status: planning/design. This document defines how externally existing capabilities may enter AIMAGE. It does not authorize implementation by itself.

## 1. Goal

AIMAGE should not redesign solved problems merely to keep the repository self-contained. It should also not become an uncontrolled collage of third-party repositories.

The integration objective is:

> reuse mature external capability at the narrowest stable boundary, preserve exact provenance and licensing, keep provider/domain semantics out of the core, and internalize only the AIMAGE semantics that must remain authoritative and replaceable.

## 2. Acquisition modes

Every external reuse decision must choose exactly one primary acquisition mode.

### A — Official package / SDK dependency

Use when a maintained library is the intended public integration surface.

Examples:

- OpenAI official SDK;
- Hugging Face Diffusers for optional local inference.

Rules:

- depend on a released package/version range appropriate to the implementation language;
- record package, version, upstream repository, license identifier, and local adapter owner;
- use only public documented APIs unless a specific exception is reviewed;
- isolate the dependency behind an AIMAGE interface so replacement does not rewrite core state semantics;
- tests must distinguish AIMAGE adapter behavior from upstream library correctness.

### B — External service / backend adapter

Use when the external system is better treated as a separately installed/running service.

Primary example: ComfyUI.

Rules:

- do not vendor or link external service source into AIMAGE core merely to simplify setup;
- communicate through its documented external interface;
- treat service availability/version/capabilities as provider state, not AIMAGE authority;
- make the dependency optional unless the architecture explicitly promotes it to required infrastructure;
- preserve a capability/fallback path when the backend is absent.

For GPL systems such as ComfyUI, this process boundary also avoids unnecessary source-copy coupling. It is not a substitute for legal review if distribution later bundles or modifies the external program.

### C — Selected permissive source import

Use only for small, clearly useful source units under a compatible permissive license where direct reuse is cheaper and safer than reimplementation.

Rules before import:

1. identify exact upstream repository and immutable commit/tag;
2. verify license at repository and selected-file level;
3. inspect transitive imports/dependencies for hidden coupling;
4. prove the selected code is generic enough for AIMAGE;
5. record original path and upstream identity;
6. preserve required license/copyright notices;
7. import only the bounded files/functions required;
8. adapt them behind an AIMAGE-owned interface;
9. add tests derived from AIMAGE requirements, not only upstream tests;
10. document how future upstream changes are evaluated rather than automatically mirrored.

Never copy a whole repository because one utility is useful.

### D — Interoperability artifact / schema snapshot

Use for externally defined workflow JSON, templates, schemas, or data formats when interoperability is the goal.

Rules:

- pin the upstream format version or commit;
- record whether the file is copied, generated, or only referenced;
- validate imported artifacts before use;
- keep the external format at the adapter edge;
- convert to/from AIMAGE-native contracts rather than making the external format canonical core state.

Primary example: selected MIT ComfyUI workflow templates/blueprints for the ComfyUI adapter.

### E — Clean-room method adaptation

Use when the useful asset is a method/pattern, or when source licensing is incompatible with direct reuse.

Rules:

- record the source as design evidence;
- extract only the high-level behavior/problem-solving principle;
- write an AIMAGE-native specification in AIMAGE terminology;
- do not copy source code or distinctive source text;
- validate the new implementation against AIMAGE-owned tests and requirements;
- do not pretend clean-room adaptation is an upstream implementation.

Primary examples:

- Krita AI Diffusion UX/control patterns under GPL-3.0;
- style-consistency-ai methods under PolyForm Noncommercial 1.0.0.

### F — Reference only

Use when a source supports a design decision but provides nothing that should be integrated.

Reference-only material stays in research/provenance and never becomes a runtime dependency.

## 3. Provenance record for external dependencies/imports

Before implementation, define an AIMAGE external-component registry. Each accepted external component should eventually record at least:

- `component_id`;
- `name`;
- `upstream_url`;
- `upstream_ref` / version;
- immutable commit/digest when applicable;
- acquisition mode;
- SPDX-style license identifier or reviewed license label;
- selected paths/artifacts if vendored;
- AIMAGE owner/adapter;
- runtime required vs optional;
- transitive dependency note;
- update policy;
- replacement/fallback boundary;
- validation status.

This follows the useful supply-chain principle behind SLSA `resolvedDependencies`: do not record only a floating repository name when the exact source identity can affect reproducibility or trust.

Reference:
- https://slsa.dev/spec/v1.2/

For material open-source dependencies, OpenSSF Scorecard may be used as one input to maintenance/security review. A score is evidence, not automatic acceptance/rejection authority.

Reference:
- https://openssf.org/projects/scorecard/

## 4. Candidate-specific acquisition decisions

### 4.1 OpenAI image generation and official SDK

Classification: **ADOPT as provider integration**.

Evidence:

- OpenAI's image API supports generation and edits.
- The Responses API supports conversational/multi-step image generation and high-fidelity multi-turn editing.
- Image-reference workflows can accept one or more input images.
- Masked editing exists, while mask adherence is guidance rather than exact geometric guarantee.
- Current GPT Image workflows support provider-side high-fidelity input handling.
- Official Python and Node SDKs are Apache-2.0.

Sources:
- https://developers.openai.com/api/docs/guides/image-generation
- https://github.com/openai/openai-python
- https://github.com/openai/openai-node

#### How to bring it in

Do not copy OpenAI SDK code. Add the official SDK as a normal dependency when the implementation language is selected.

Create an AIMAGE adapter conceptually like:

`AIMAGE RenderSpec -> OpenAIProviderAdapter -> OpenAI SDK/API -> provider result -> AIMAGE ArtifactRecord/RunRecord`

The adapter should own:

- request construction;
- mapping AIMAGE role-bound image references to provider image inputs;
- generate vs edit mode;
- provider conversation/image IDs;
- mask input when supported;
- provider output settings;
- raw error preservation and normalization;
- usage/cost metadata extraction;
- capability reporting.

The adapter must **not** own:

- AIMAGE approval semantics;
- reference authority meaning;
- job state transitions;
- geometry locks;
- repair-policy decisions.

#### Planned application

OpenAI should be the first cloud provider path because it directly supports the project's important reference/edit loop. Multi-turn provider state may accelerate repairs, but AIMAGE must also persist enough of its own state to reconstruct intent without trusting an opaque provider conversation as canonical authority.

### 4.2 ComfyUI core/backend

Classification: **ADAPT as optional external backend**.

Evidence:

- ComfyUI is a mature graph/node image-generation backend and API ecosystem.
- ComfyUI core is GPL-3.0.
- Official workflow templates/subgraph blueprints are maintained separately under MIT and include validation/schema tooling.

Sources:
- https://github.com/Comfy-Org/ComfyUI
- https://github.com/Comfy-Org/workflow_templates

#### How to bring it in

Do not copy ComfyUI core into AIMAGE.

Support it as an optional separately installed backend:

`AIMAGE ExecutionPlan -> ComfyUIAdapter -> external ComfyUI API/server -> output artifacts`

The adapter should:

- discover server/version/node capability;
- select a compatible workflow template/blueprint;
- inject prompt/reference/control inputs;
- submit workflow;
- observe execution/output identity;
- convert output back to AIMAGE artifacts;
- expose backend failures without turning node names into core semantics.

#### Workflow-template handling

For a specific supported capability, AIMAGE may copy selected MIT workflow JSON/blueprints from `Comfy-Org/workflow_templates` using acquisition mode D.

Each copied workflow must be pinned to an upstream commit, normalized into an AIMAGE-owned adapter directory, validated against the expected external schema, and accompanied by provenance/license metadata.

Do not import the whole template repository.

#### Planned application

ComfyUI is the preferred optional graph backend for advanced/local composition controls where node ecosystems already solve model-specific wiring. It should not define AIMAGE's workflow graph or job-state schema.

### 4.3 Hugging Face Diffusers

Classification: **ADOPT as optional local provider library**.

Evidence:

- Diffusers is Apache-2.0.
- It exposes many diffusion pipelines and adapters.
- Official documentation supports IP-Adapter image guidance and combinations with ControlNet for structural control.

Sources:
- https://github.com/huggingface/diffusers
- https://huggingface.co/docs/diffusers/using-diffusers/ip_adapter

#### How to bring it in

Use a normal package dependency behind `DiffusersProviderAdapter`; do not vendor Diffusers source.

The adapter should keep model/checkpoint selection separate from engine semantics and report capabilities such as:

- text-to-image;
- image-to-image;
- inpaint;
- IP-Adapter/reference conditioning;
- ControlNet depth/edge/pose/etc.;
- locally available device/precision constraints.

Model weights and adapters must have separate license/provenance records; the Diffusers library license does not license every checkpoint loaded through it.

#### Planned application

Diffusers is useful for direct local execution, research, deterministic provider experiments, and structural-control paths without requiring ComfyUI. It remains optional because the main AIMAGE engine must also work with hosted providers.

### 4.4 Nori

Classification: **ADAPT; permissive source candidate, no wholesale runtime dependency**.

Evidence:

Nori is MIT and presents a close architectural analogue: persistent art projects, style/character bibles, plan→explore→critique→refine→finish, version history, and thin model adapters.

Source:
- https://github.com/aditya-ramesh/nori

#### What to reuse

Strong candidates for adaptation:

- separation between art-project state and model wrappers;
- Style Bible / Character Bible decomposition;
- explicit exploration and refine loops;
- version/history concepts;
- thin provider adapter principle;
- evaluation-oriented architecture.

#### What not to adopt by default

- Nori's whole application/runtime stack;
- Postgres/pgvector/Redis as assumed AIMAGE infrastructure;
- Sora/video scope before still-image workflow is proven;
- Nori-specific taste-model/product positioning;
- any source module whose dependencies make it more expensive than an AIMAGE-native equivalent.

#### How to bring it in

Before implementation, perform a bounded source audit on the exact modules corresponding to project state, bibles, history, model adapters, and eval contracts.

For each useful slice choose either:

1. **selected MIT source import** with attribution if the implementation is generic and dependency-light; or
2. **AIMAGE-native adaptation** if semantics are intertwined with Nori's stack.

Default preference: adapt architecture and data-shape lessons first; copy code only where the file-level audit proves it is cleaner.

### 4.5 GenAI Illustration Pipeline

Classification: **ADAPT; selective MIT source import candidate**.

Evidence:

The project reports a production-proven still-image pipeline at ~1,523 delivered assets across three books, with brief extraction, art-direction audit, model routing, locked references, agent QA, human review, revisions, deterministic finishing and synthetic fixtures. The repository is MIT.

Source:
- https://github.com/Kanishk688/genai-illustration-pipeline

#### What to reuse

High-value generic candidates:

- explicit shot/work-item records;
- task-based model routing pattern;
- style/hero reference stack concept;
- agent QA before human review;
- "change one thing, preserve the rest" revision discipline;
- contact-sheet generation;
- synthetic defective fixtures;
- deterministic finishing utilities;
- cost/first-pass-yield reporting.

#### What not to import as generic AIMAGE core

- manuscript/DOCX-specific extraction semantics;
- book-layout assumptions;
- print-only constraints such as fixed 300-DPI ownership in the core;
- provider choices presented as universal ranking;
- client/publishing workflow conventions.

#### How to bring it in

Perform file-level audit of small deterministic scripts first. Good candidates may be selectively imported or rewritten under AIMAGE-owned interfaces.

Probable first audit targets:

- contact-sheet utility;
- aspect pad/crop utility;
- format/WebP utility;
- alpha/background helpers if a domain requires them;
- QA fixture architecture;
- cost report data model.

The orchestration and QA ideas should be adapted into AIMAGE contracts rather than copying a book-specific orchestrator.

### 4.6 Krita AI Diffusion

Classification: **ADAPT method-only / reference-only for most of core**.

Evidence:

Krita AI Diffusion demonstrates mature editing UX around regions, generation history, inpainting/outpainting, ControlNet, IP-Adapter and a separately running ComfyUI backend. It is GPL-3.0.

Source:
- https://github.com/Acly/krita-ai-diffusion

#### How to use it

Do not copy source into a permissive AIMAGE core under the current plan.

Use it as design evidence for:

- control-layer abstraction;
- region-scoped prompting/editing;
- history and job queue UX;
- sketch/pose/depth/segmentation control selection;
- keeping the editing UI separate from the generation backend.

If AIMAGE later intentionally becomes GPL-compatible, code-level reuse can be reconsidered separately.

### 4.7 style-consistency-ai

Classification: **ADAPT method-only**.

Evidence:

The repository provides a useful consistency ladder: smallest edit first, corrective guidelines, reference atlas, closest reference, datasets, model routing, then training only when lighter methods fail. Its license is PolyForm Noncommercial 1.0.0.

Source:
- https://github.com/GenielabsOpenSource/style-consistency-ai

#### How to use it

Treat it as conceptual evidence only under the current general-purpose project plan.

AIMAGE may independently implement the following generic ideas:

- prefer delta edits over full rerolls;
- use representative atlases;
- select the closest reference to the requested pose/context;
- add corrective rules only for observed recurring failures;
- route by task/capability;
- escalate to datasets/training only after cheaper controls fail.

Do not copy its skill text, reference files, or source implementation unless the license situation is explicitly accepted.

## 5. Integration architecture implied by external reuse

External reuse should converge on the following shape:

```text
AIMAGE-owned Job / RenderSpec / Artifact / Approval / Review semantics
                            |
                  Provider Capability Boundary
                            |
      +---------------------+----------------------+
      |                     |                      |
 OpenAI Adapter       ComfyUI Adapter      Diffusers Adapter
 official SDK         external service      optional package
      |                     |                      |
 provider-native       workflow JSON         model pipelines
 refs/edits/masks      nodes/controls         ControlNet/IP-Adapter
```

Feature strategies sit above the capability boundary:

```text
Character/Style/Composition/Repair/QA strategies
                    |
                    v
          AIMAGE Engine interfaces
                    |
                    v
           provider adapters
```

This ensures external provider innovations can be adopted without redefining the AIMAGE workflow.

## 6. External-source acceptance gate before implementation

An `ADOPT` or code-level `ADAPT` candidate is implementation-ready only after all applicable items below are closed:

1. exact source/version identified;
2. license identified and compatible with selected acquisition mode;
3. upstream maintenance/activity reviewed proportionally;
4. functional fit reproduced or independently supported;
5. selected dependency/import boundary documented;
6. transitive dependencies understood sufficiently for the integration risk;
7. no source repository becomes accidental AIMAGE authority;
8. no provider-specific state leaks into generic core contracts;
9. fallback/replacement behavior defined where material;
10. AIMAGE-owned tests identified;
11. provenance/update policy recorded.

For higher-impact dependencies, use OpenSSF Scorecard or equivalent supply-chain evidence as an input rather than inventing trust from popularity alone.

## 7. Planned implementation order after design approval

Implementation is not authorized by this document, but the expected order is:

1. design the native AIMAGE contracts that external components must plug into;
2. implement one thin OpenAI adapter as the first vertical slice;
3. validate the complete minimal workflow on that adapter;
4. add optional ComfyUI and/or Diffusers adapters without changing core semantics;
5. selectively import/adapt deterministic MIT utilities that close measured gaps;
6. implement method-only consistency/repair strategies independently;
7. add heavier dataset/training support only when evidence shows it is needed.

This order uses external capability to accelerate proof of the workflow while keeping AIMAGE's semantic center provider-neutral.
