# AIMAGE External Reuse and Integration Plan

Status: planning/design after capability-first cross-domain reuse re-audit. This document defines what external capability AIMAGE intends to use, how it enters the architecture, what stays optional/reference-only, and what must remain replaceable. It does not authorize implementation.

## 1. Goal

AIMAGE should neither redesign solved problems nor become an uncontrolled collage of third-party systems.

Integration rule:

> reuse mature external capability at the narrowest stable boundary; preserve exact provenance/licensing; keep provider/domain-specific state out of canonical core semantics; and retain only AIMAGE semantics whose absence would remove real user-visible or cross-provider control.

The accepted capability classifications live in `plans/CAPABILITY_REUSE_MATRIX.md`. Reuse/acquisition and final integration assurance follow `plans/REUSE_AND_INTEGRATION_ASSURANCE.md`.

## 2. Acquisition modes

Every external reuse decision selects one primary acquisition mode.

### A — Official package / SDK dependency

Use when a maintained public package is the intended integration surface.

Rules:

- pin an appropriate released version/range during implementation;
- record package/version/upstream/license/adapter owner;
- use documented public APIs;
- isolate behind an AIMAGE interface;
- test AIMAGE adapter behavior independently of upstream correctness.

Initial uses: OpenAI official SDK; optional Hugging Face Diffusers.

### B — External service / backend adapter

Use when the external system should remain separately installed/running.

Rules:

- do not vendor service source into AIMAGE merely for convenience;
- communicate through documented external interfaces;
- treat version/capability/availability as provider state;
- make optional unless architecture explicitly changes;
- preserve explicit absence/fallback behavior.

Initial use: ComfyUI.

### C — Selected permissive source import

Use only for a small exact source unit when direct reuse is demonstrably cheaper/safer than a normal dependency or small reimplementation.

Before import:

1. exact repository + immutable ref;
2. repository/file license check;
3. transitive import/dependency review;
4. generic-fit proof;
5. exact selected paths;
6. required notices/attribution;
7. bounded AIMAGE owner/interface;
8. AIMAGE-owned tests;
9. update/replacement policy.

**No source import is required by the initial architecture.** Nori/GenAI utility code remains reference/method evidence by default; reopen C only if implementation proves a measured gap.

### D — Interoperability artifact / schema snapshot

Use when compatibility with an external format is itself valuable.

Rules:

- pin external format/ref;
- validate on import;
- keep format at adapter/interoperability edge;
- convert to/from AIMAGE contracts;
- never make the external format canonical job state.

Possible uses: selected MIT ComfyUI workflows; future OpenUSD/OpenAssetIO interchange artifacts.

### E — Clean-room method/schema adaptation

Use when the useful asset is a mature method, architectural pattern, data-model principle or incompatible-license idea rather than runtime code.

Rules:

- cite external source as design evidence;
- extract behavior/principle, not distinctive code/text;
- specify result in AIMAGE terminology;
- validate against AIMAGE requirements;
- do not claim the result is the upstream implementation.

This is the dominant mode for the cross-domain standards/patterns below.

### F — Reference only

Use when a source justifies or challenges design but supplies nothing that should be integrated.

Reference-only material is neither runtime authority nor source dependency.

## 3. External component/provenance registry design

Before implementation installs/copies/bundles any concrete component, create a machine-readable AIMAGE external-component registry containing at least:

- `component_id`;
- `name`;
- `upstream_url`;
- `upstream_ref` or version;
- immutable commit/digest where applicable;
- acquisition mode;
- SPDX-style license/review label;
- selected paths/artifacts for copied material;
- AIMAGE adapter/owner;
- runtime required/optional/reference-only;
- transitive dependency note;
- currentness/security review date;
- update policy;
- replacement/fallback boundary;
- validation evidence identity.

Use SLSA resolved-dependency identity and SPDX component/license concepts as the external model references; do not invent a competing software-supply-chain ontology.

Sources:
- https://slsa.dev/spec/v1.2/
- https://spdx.github.io/spdx-spec/

Material OSS dependencies should also be reviewed proportionally under NIST SSDF/C-SCRM guidance and may use OpenSSF Scorecard as one security/maintenance signal.

Sources:
- https://csrc.nist.gov/pubs/sp/800/218/final
- https://csrc.nist.gov/Projects/cyber-supply-chain-risk-management/publications
- https://openssf.org/projects/scorecard/

## 4. Concrete provider/tool acquisition decisions

### 4.1 OpenAI image provider

Classification: **ADOPT as provider integration**.

Acquisition: mode A, official SDK/API.

Current official model/API documentation confirms image generation/edit endpoints and image-input/editing capability; exact model choice remains a routing/configuration decision rather than a core semantic.

Sources:
- https://developers.openai.com/api/docs/guides/image-generation
- https://developers.openai.com/api/docs/models/gpt-image-2
- https://github.com/openai/openai-python
- https://github.com/openai/openai-node

Planned boundary:

`AIMAGE RenderSpec IR -> OpenAIProviderAdapter -> official SDK/API -> provider result -> AIMAGE Artifact/Run records`

Adapter owns:

- request construction/lowering;
- generate/edit mode;
- role-bound image input mapping;
- provider conversation/image/mask identifiers;
- output settings;
- raw error + normalized error;
- usage/cost metadata;
- capability report.

Adapter does not own:

- approval/lock semantics;
- reference-role authority;
- job state transitions;
- geometry semantics;
- repair policy.

Replacement boundary: another provider adapter must be able to consume the same supported AIMAGE intent subset without changing canonical authority semantics.

### 4.2 ComfyUI

Classification: **ADAPT as optional external backend**.

Acquisition: mode B; mode D only for selected pinned MIT workflow-template artifacts.

Sources:
- https://github.com/Comfy-Org/ComfyUI
- https://github.com/Comfy-Org/workflow_templates

Planned boundary:

`AIMAGE ExecutionPlan -> ComfyUIAdapter -> external ComfyUI service -> output artifacts`

Adapter responsibilities:

- server/version/node/capability discovery;
- select compatible adapter-owned workflow template;
- inject provider-specific prompt/reference/control values;
- submit/observe execution;
- normalize outputs/errors;
- never expose arbitrary node names as core semantics.

GPL core source is not copied into AIMAGE. If distribution later bundles/modifies ComfyUI, perform a separate licensing decision.

Replacement boundary: absence of ComfyUI must produce capability fallback/unsatisfied-plan behavior, not invalid AIMAGE state.

### 4.3 Hugging Face Diffusers

Classification: **ADOPT as optional local provider library**.

Acquisition: mode A.

Sources:
- https://github.com/huggingface/diffusers
- https://huggingface.co/docs/diffusers/using-diffusers/ip_adapter

Planned boundary:

`AIMAGE ExecutionPlan -> DiffusersProviderAdapter -> selected local pipeline -> output artifacts`

Adapter reports only actually available operations such as text/image generation, inpainting, reference conditioning and structural controls. Model/checkpoint/control-weight licenses are recorded separately from the Diffusers library license.

Replacement boundary: direct local execution is optional; ComfyUI or hosted providers can satisfy overlapping capabilities without changing job semantics.

## 5. Cross-domain reuse decisions that shape AIMAGE without mandatory runtime dependencies

### 5.1 Workflow/state/history/human approval

Classification: **ADAPT + small AIMAGE extension**.

Strongest sources:

- W3C SCXML — state/transition/event/history semantics;
- OMG BPMN — mature process/gate/user-task vocabulary;
- Temporal — durable workflow/human approval/signal/timeout/idempotency implementation pattern.

Sources:
- https://www.w3.org/TR/scxml/
- https://www.omg.org/spec/BPMN/
- https://docs.temporal.io/

Acquisition: E/F initially. Do **not** make Temporal or a BPMN engine mandatory infrastructure.

Apply as:

- AIMAGE lifecycle is expressed as explicit state + events/transitions, not a hand-coded pile of stage flags;
- user approval is a state transition carrying decision metadata;
- pause/resume/history and duplicate/late event behavior are explicit;
- retries belong to execution failures, not subjective image failures;
- future multi-user/server deployments may plug a durable workflow engine behind this boundary if measured needs justify it.

AIMAGE residue: only image-job event/state payload semantics and visual decision boundaries.

### 5.2 Artifact identity/version/lineage

Classification: **ADAPT + small AIMAGE extension**.

Strongest sources:

- W3C PROV for derivation concepts;
- OpenAssetIO for host↔asset-manager resolution/publishing boundary, opaque entity references and traits;
- content-addressed/digest identity and SLSA dependency/provenance principles;
- C2PA only for optional exported-content provenance.

Sources:
- https://www.w3.org/groups/wg/prov/publications/
- https://docs.openassetio.org/OpenAssetIO/
- https://slsa.dev/spec/v1.2/
- https://c2pa.org/

Acquisition:

- W3C PROV/SLSA: E/F;
- OpenAssetIO: optional A/D interoperability if a real DAM/MAM system is used;
- C2PA: optional export interoperability, never internal authority.

Apply as:

- artifact content has stable identity/digest + media metadata;
- derivation links identify source artifacts and generating activity/run;
- asset-manager references remain optional external handles;
- AIMAGE stores accepted/rejected/superseded/locked visual-role relationships as its small extension;
- loss of an external manager must not destroy AIMAGE's local artifact identity/lineage.

### 5.3 Reference-role authority and partial locks

Classification: **ADAPT + small AIMAGE extension**.

External primitives:

- OpenAssetIO trait/relationship patterns;
- OpenUSD references/layers/non-destructive composition/override patterns;
- workflow approval patterns from Temporal/BPMN.

Sources:
- https://docs.openassetio.org/OpenAssetIO/entities_traits_and_specifications.html
- https://openusd.org/dev/glossary.html
- https://docs.temporal.io/

Acquisition: E/F; no OpenUSD/OpenAssetIO runtime requirement in core.

Apply as:

- use typed role/relationship concepts rather than ad-hoc prompt labels;
- approval records a state transition and dimension coverage;
- override/reopen is explicit and non-destructive;
- later execution receives preservation obligations rather than relying on wording such as "keep everything else".

AIMAGE residue:

- visual authority dimensions/roles;
- precedence/conflict rules;
- dimension-scoped lock and preservation meaning across provider changes.

### 5.4 Provider adapter/capability negotiation

Classification: **ADAPT + small AIMAGE extension**.

Strongest patterns:

- LSP multi-tool/server protocol separation;
- Vulkan explicit feature/extension support structures;
- OpenAssetIO host/manager capabilities and policy queries.

Sources:
- https://microsoft.github.io/language-server-protocol/
- https://registry.khronos.org/vulkan/
- https://docs.openassetio.org/OpenAssetIO/classopenassetio_1_1v1_1_1manager_api_1_1_manager_interface.html

Acquisition: E/F.

Apply as:

- provider descriptor reports version + supported operation/features + limits/constraints;
- execution planner asks for capabilities; it does not inspect provider type names throughout core;
- optional capabilities are explicit;
- unsupported requirements produce fallback/alternate plan/unsatisfied result;
- capability reports are version-sensitive observations, not permanent truth.

AIMAGE residue: only image-domain capability names and compatibility predicates.

### 5.5 RenderSpec as a small intermediate representation

Classification: **ADAPT + small AIMAGE extension**.

Strongest patterns:

- LLVM IR — common representation separated from target code;
- MLIR — dialect conversion/lowering, target legality and partial conversion;
- JSON Schema — contract validation/versioning.

Sources:
- https://llvm.org/docs/LangRef.html
- https://mlir.llvm.org/docs/DialectConversion/
- https://json-schema.org/specification

Acquisition: E/F for compiler patterns; JSON Schema as the validation standard with a language-appropriate library later.

Apply as:

1. compile current approved authority into a typed/versioned `RenderSpec` IR;
2. validate required invariants before provider selection;
3. choose a provider capability target;
4. lower only supported semantics into an `ExecutionPlan`/provider request;
5. if required semantics cannot be legally lowered, reroute or report an unsatisfied plan rather than silently dropping them;
6. preserve the original RenderSpec identity alongside the lowered request/run.

Do not import LLVM/MLIR libraries. Do not make OpenAI/ComfyUI/Diffusers request formats the canonical IR.

AIMAGE residue: the compact visual execution-intent vocabulary/invariants.

### 5.6 Geometry/composition constraints

Classification: **ADAPT + small AIMAGE extension**.

Strongest sources:

- OpenUSD transforms/scene relationships/layering;
- Cassowary constraint-solving method;
- CSS Grid alignment/placement concepts.

Sources:
- https://openusd.org/
- https://constraints.cs.washington.edu/solvers/cassowary-tr.html
- https://www.w3.org/TR/css-grid-1/

Acquisition:

- OpenUSD: E/F initially, optional D/A interoperability later;
- Cassowary: E now; exact mature solver package is a `DEFERRED_IMPLEMENTATION_CHECK` tied to implementation language;
- CSS: E/F.

Apply as:

- normalize spatial intent into entities, coordinate spaces, transforms and relative constraints;
- prefer solver-friendly relations for deterministic/algebraic facts;
- keep qualitative visual semantics such as gaze, reading order and foreground ownership as explicit AIMAGE predicates layered above generic constraints;
- adapters lower constraints into prompt language, structural-control artifacts, masks/poses/depth or other provider mechanisms;
- an approved blocking artifact may override/instantiate the same spatial intent without making its provider format canonical.

### 5.7 Persistence and schema evolution

Classification: **ADAPT**.

Strongest sources:

- JSON Schema 2020-12;
- Avro writer/reader schema-resolution ideas;
- generic metadata-store + blob/artifact-store separation.

Sources:
- https://json-schema.org/specification
- https://avro.apache.org/docs/1.11.2/specification/

Acquisition: standard/method adaptation; actual database/blob implementation deferred to runtime requirements.

Apply as:

- JSON-family versioned contracts + JSON Schema validation are the planning default;
- every persisted object carries schema/version identity;
- evolution rules distinguish compatible read, explicit migration and unsupported version;
- binary/image artifacts live behind artifact/blob storage, not embedded as persistence semantics;
- no custom serializer/database is part of AIMAGE's semantic center.

### 5.8 Text/graphic layout

Classification: **ADAPT + small AIMAGE extension**.

Strongest sources:

- SVG 2 deterministic text/graphics layout;
- CSS Grid 2D placement/alignment.

Sources:
- https://www.w3.org/TR/SVG2/text.html
- https://www.w3.org/TR/css-grid-1/

Acquisition: E initially; language/browser/render-library choice later.

Apply as:

- separate exact text content from its graphic region/layout;
- when exact text correctness matters, prefer deterministic layout/composition over repeated whole-image generation;
- provider-native text rendering is an optional capability when aesthetic integration is preferred and review permits it;
- AIMAGE keeps only the intent that text exists, its content/region/role/editability, and chosen execution mode.

### 5.9 Repair orchestration

Classification: **ADAPT** for orchestration pattern + provider capabilities for editing.

Generic method basis: diagnosis/analyze → plan → execute → verify, consistent with mature autonomic/control-loop patterns.

Provider execution may supply:

- targeted/delta edit;
- masked/regional edit;
- multi-turn edit;
- structural correction;
- reference-conditioned edit.

AIMAGE flow:

1. diagnose failed variable(s);
2. identify successful/locked dimensions;
3. form preservation/delta intent;
4. choose cheapest capability that can satisfy it;
5. execute through adapter;
6. review requested change and regression;
7. escalate/reroute only when needed.

No custom AIMAGE image editor/repair renderer is planned.

## 6. Prior image-production projects: final acquisition stance

### Nori

Use: E/F architecture evidence for persistent projects, style/character bibles, explore/refine/history, thin adapters.

Initial source import: **none**.

Reason: its useful architectural ideas are already captured in AIMAGE contracts; copying application/runtime modules would add stack coupling without a proven gap.

### GenAI Illustration Pipeline

Use: E/F evidence for work-item records, routing, QA/human review, minimal-change revisions, deterministic finishing and fixtures.

Initial source import: **none**.

Small deterministic utilities may later be reconsidered under mode C only if implementation shows reuse is cheaper than standard libraries/small native utilities.

### Krita AI Diffusion

Use: E/F only under current permissive-core direction due GPL-3.0; evidence for regions, history, structural controls, edit UX and separate backend architecture.

### style-consistency-ai

Use: E/F method-only under PolyForm Noncommercial constraints; independent implementation of generic ideas only.

## 7. Integrated architecture implied by reuse

```text
Feature/domain strategies
(character/style/composition/review/repair/domain QA)
                    |
                    v
Thin AIMAGE semantic center
- visual authority roles
- dimension locks/preservation intent
- RenderSpec visual IR vocabulary
- image capability taxonomy
- visual spatial predicates
                    |
        +-----------+------------+
        |                        |
Generic reused mechanics     Optional interoperability
state/events/history         OpenAssetIO / OpenUSD / C2PA
provenance/identity
schema/evolution
constraints/layout
IR validation/lowering pattern
        |
        v
Provider capability / adapter boundary
        |
  +-----+---------+---------+
  |               |         |
OpenAI          ComfyUI   Diffusers
SDK/API         service   optional pkg
```

Generic mechanics must not become a second AIMAGE-specific framework merely because AIMAGE wraps them.

## 8. Implementation-ready meaning

A design-level reuse decision is considered **architecture-resolved** when:

- capability classification and semantic residue are fixed;
- acquisition mode is fixed;
- runtime/source coupling is fixed;
- canonical-state owner is fixed;
- replacement/fallback boundary is fixed;
- licensing model is known at the required granularity;
- implementation-language-dependent package selection is the only remaining deferred choice where applicable.

A concrete component is **implementation-ready** only after Gate B in `plans/REUSE_AND_INTEGRATION_ASSURANCE.md` additionally closes exact version/ref, transitive/security/currentness checks and AIMAGE contract tests.

This distinction prevents premature package pinning before the runtime exists without leaving architecture unresolved.

## 9. Planned implementation sequence after native semantic design is approved

Implementation remains unauthorized in this slice. When authorized, the expected sequence is:

1. define the narrowed AIMAGE semantic contracts from `CAPABILITY_REUSE_MATRIX.md` using JSON Schema/versioning and the accepted generic patterns;
2. implement generic state/artifact/IR/capability interfaces without a workflow-engine/database/provider dependency becoming canonical;
3. implement one thin OpenAI vertical slice with provider-native generation/editing;
4. run the minimal end-to-end scenarios and contract fixtures;
5. add optional Diffusers and/or ComfyUI adapters and prove provider replacement/fallback without semantic changes;
6. add deterministic text/layout and finishing utilities only where scenarios require them;
7. add optional OpenAssetIO/OpenUSD/C2PA interoperability only for concrete use cases;
8. reopen source-import candidates only for measured gaps;
9. execute the full Gate C/D architecture + workflow audit before declaring the system complete.

## 10. Assurance gate

All external adoption/application decisions in this file are subject to `plans/REUSE_AND_INTEGRATION_ASSURANCE.md`:

- Gate A closes capability coverage and native-design burden of proof;
- Gate B prevents incomplete/unsafe external acquisition;
- Gate C performs scenario-based architecture tradeoff review;
- Gate D performs full integrated workflow simulation, transition coverage, combinatorial interaction coverage and fault/regression injection.
