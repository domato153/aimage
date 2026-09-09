# AIMAGE Capability Reuse Matrix

Status: planning/design classification after capability-first cross-domain reuse re-audit. This matrix decides where AIMAGE should adopt, adapt, compose, or retain native semantics before implementation begins.

The matrix is evidence-first and may be revised when a candidate fails technical, licensing, maintenance, integration, or architecture-fit review. Implementation is not authorized by this file.

## 1. Classification vocabulary

- `ADOPT` — use an external implementation/service/standard substantially as-is behind an AIMAGE-owned boundary.
- `ADAPT` — reuse an external implementation, workflow pattern, method, schema, protocol idea, or selected code while changing/wrapping/internalizing it for AIMAGE requirements.
- `ADAPT + small AIMAGE extension` — mature external primitives solve the generic problem; AIMAGE owns only a narrow visual/domain semantic that would otherwise be lost to the user or across providers.
- `DESIGN` — define an AIMAGE-native semantic because direct adoption, adaptation, interoperability, and composition of mature external solutions do not close the actual product requirement.

Modifiers:

- `runtime dependency` — the external package/service remains present at runtime.
- `optional backend` — runtime dependency exists only when that provider/backend is enabled.
- `selective source import` — permissively licensed source may be copied only after file-level audit and attribution.
- `method-only` — ideas/methods may inform AIMAGE, but source/code/text should not be copied.
- `provider capability` — capability lives behind a provider adapter and does not become core semantics.
- `reference/interoperability` — external format/spec remains at an edge or is design evidence, not canonical AIMAGE state.
- `deferred implementation check` — semantic/acquisition boundary is settled but exact language-specific package/version is intentionally chosen only after implementation language/runtime exists.

## 2. Cross-domain evidence set

Evidence checked for this re-audit includes the prior image-production sources plus mature non-image domains. Currentness was checked on 2026-09-10 against official specifications/docs where available.

### Workflow, state and human gates

- W3C SCXML 1.0 — generic event/state/transition/history execution semantics.
  - https://www.w3.org/TR/scxml/
- OMG BPMN 2.0.2 — established process/gateway/human-task vocabulary.
  - https://www.omg.org/spec/BPMN/
- Temporal approval/durable-workflow patterns — human approval, signals, timeouts, idempotency and durable execution as implementation evidence; not selected as mandatory AIMAGE runtime.
  - https://docs.temporal.io/

### Asset identity, lineage and provenance

- W3C PROV — entity/activity/agent and derivation provenance model.
  - https://www.w3.org/groups/wg/prov/publications/
- OpenAssetIO — abstract host/asset-manager boundary, opaque entity references, traits, capability/policy queries, resolution/publishing; Apache-2.0.
  - https://docs.openassetio.org/OpenAssetIO/
- SLSA provenance — resolved-dependency identity/provenance principles.
  - https://slsa.dev/spec/v1.2/
- C2PA — optional externally verifiable content provenance for exported media; not an internal job-state model.
  - https://c2pa.org/

### Spatial composition and constraints

- OpenUSD — scene graph, transforms, references, layering, composition arcs and non-destructive overrides.
  - https://openusd.org/
- Cassowary — mature incremental linear constraint-solving method for relations such as left/right/alignment/containment.
  - https://constraints.cs.washington.edu/solvers/cassowary-tr.html
- CSS Grid — mature 2D alignment/placement vocabulary useful as layout evidence.
  - https://www.w3.org/TR/css-grid-1/

### Intermediate representations and lowering

- LLVM IR — stable common intermediate representation across compilation stages.
  - https://llvm.org/docs/LangRef.html
- MLIR dialect conversion — explicit conversion targets, legality, rewrite/lowering and partial conversion patterns.
  - https://mlir.llvm.org/docs/DialectConversion/
- JSON Schema 2020-12 — versioned schema/validation standard suitable for AIMAGE-owned serialized contracts.
  - https://json-schema.org/specification

### Capability negotiation and adapters

- Language Server Protocol — standardized client/server protocol intended to make language servers reusable across many tools; capability negotiation is part of the protocol family.
  - https://microsoft.github.io/language-server-protocol/
- Vulkan feature structures/extensions — explicit queryable feature support and extension capability model.
  - https://registry.khronos.org/vulkan/
- OpenAssetIO ManagerInterface capability/policy model — optional functionality exposed without making one backend canonical.
  - https://docs.openassetio.org/OpenAssetIO/classopenassetio_1_1v1_1_1manager_api_1_1_manager_interface.html

### Serialization/evolution and deterministic graphic layout

- JSON Schema — contract validation.
  - https://json-schema.org/specification
- Apache Avro schema resolution — writer/reader schema evolution pattern used as method evidence, not selected as AIMAGE's required wire format.
  - https://avro.apache.org/docs/1.11.2/specification/
- SVG 2 text/layout — deterministic text placement, transforms, wrapping and graphic composition.
  - https://www.w3.org/TR/SVG2/text.html
- CSS Grid — deterministic 2D designed-layout primitives.
  - https://www.w3.org/TR/css-grid-1/

### Repair planning and verification method

- IBM autonomic MAPE/MAPE-K family — monitor/analyze/plan/execute separation as generic repair-orchestration evidence.
- Existing provider-native editing — actual image delta/masked/multi-turn/structural edits remain provider/tool execution capabilities.

### Prior image-production evidence retained

- OpenAI image generation/edit APIs and official SDKs.
- ComfyUI and official workflow templates.
- Hugging Face Diffusers.
- Nori.
- GenAI Illustration Pipeline.
- Krita AI Diffusion.
- style-consistency-ai.

External evidence informs design but does not become AIMAGE authority.

## 3. Cross-domain re-audit of material native-design claims

The following records carry the burden-of-proof result for every materially `DESIGN` or partial-`DESIGN` row plus generic rows whose decisions still claimed substantial AIMAGE-owned mechanics.

| ID | Old classification | Abstract problem / fields searched | Strongest external candidates | New classification | Acquisition / coupling / fallback | Exact AIMAGE semantic residue |
|---|---|---|---|---|---|---|
| C01 | `ADAPT` | Long-running state, event transitions, history, human gates; statecharts/BPMN/durable workflows | SCXML, BPMN, Temporal approval/durable patterns | `ADAPT + small AIMAGE extension` | Method/reference first; no mandatory workflow-engine runtime. Optional durable engine may be added behind engine interfaces if real deployment needs it. | Image-job state names/payloads and which visual decisions trigger transitions; not generic state-machine mechanics. |
| C02 | `ADAPT` | Artifact identity/version/derivation/resolve/publish; DAM/MAM, provenance, CAS/build provenance | W3C PROV, OpenAssetIO, SLSA/CAS principles, optional C2PA export | `ADAPT + small AIMAGE extension` | PROV/schema concepts adapted internally; OpenAssetIO optional interoperability edge; C2PA export-only. Local identity must survive all external-system loss. | Visual artifact roles plus accepted/rejected/superseded/locked authority relationships inside an image job. |
| C03 | `DESIGN` | Typed relationship/role binding and authority; asset traits, scene relationships, layered references | OpenAssetIO traits/entity relationships, OpenUSD references/layers | `ADAPT + small AIMAGE extension` | Method/schema adaptation; no OpenAssetIO/USD canonical job dependency. | Visual authority role vocabulary (`identity`, `style`, `composition`, `blocking`, etc.), dimension coverage and precedence/conflict rules. |
| C04 | `DESIGN` | Human decision gate, selective lock, override/reopen; workflow approval + layered/non-destructive override systems | Temporal approval pattern, BPMN user tasks/gates, OpenUSD layer/override semantics | `ADAPT + small AIMAGE extension` | Method adaptation only by default; no mandatory Temporal/USD runtime. | Dimension-scoped visual approval/lock meaning and preservation obligations across later edits/provider changes. |
| C05 | `DESIGN` | Stable host/backend boundary and replaceable adapters | LSP protocol separation, OpenAssetIO Host/Manager interfaces, ports/adapters industry pattern | `ADAPT + small AIMAGE extension` | AIMAGE interface uses generic adapter principles; provider SDK/service remains outside. | Small image-provider operation surface and mapping between AIMAGE visual intent and provider requests/results. |
| C09 | `DESIGN` + `ADAPT` | Feature discovery, optional feature sets, compatibility/fallback negotiation | LSP capabilities, Vulkan feature structures/extensions, OpenAssetIO capability/policy queries | `ADAPT + small AIMAGE extension` | Pattern/schema adaptation; provider adapters report capabilities. No dependency on LSP/Vulkan/OpenAssetIO. | AIMAGE image-capability taxonomy and predicates such as `masked_edit`, `multi_reference`, `structural_conditioning`, fidelity/cost/privacy constraints. |
| C12 | `DESIGN` | Provider-neutral intent represented, validated and lowered to target-specific execution | LLVM IR, MLIR conversion/lowering, JSON Schema | `ADAPT + small AIMAGE extension` | IR/lowering method adaptation + JSON Schema contract validation; no LLVM/MLIR runtime. | The visual-intent vocabulary and invariants that must survive provider lowering. `RenderSpec` is an AIMAGE IR profile, not an invented compiler framework. |
| C16 | `DESIGN` | Durable storage boundary for metadata plus immutable/binary artifacts | repository/blob-store separation, content-addressed identity, OpenAssetIO asset boundary patterns | `ADAPT` | Define generic metadata-store/blob-store interfaces; actual DB/blob implementation deferred to runtime needs. | No independent persistence semantic. Stores AIMAGE schemas/artifact identities without redefining them. |
| C17 | `DESIGN` | Versioned serialization, validation, forward/backward evolution | JSON Schema 2020-12, Avro writer/reader schema-resolution principles | `ADAPT` | Use JSON-family serialization + versioned JSON Schema as planning default; implementation library chosen with language. | AIMAGE owns schema contents, not a custom serializer/evolution framework. |
| F03 | `ADAPT` + `DESIGN` | Generate materially distinct options rather than cosmetically repeated priors; design-of-experiments/combinatorial coverage + creative exploration | NIST combinatorial/DOE principles, Nori direction exploration | `ADAPT + small AIMAGE extension` | Method-only; no ACTS runtime required. | Image-specific diversity axes, anti-prior heuristics and creative quality judgment. |
| F04 | `DESIGN` | Represent 2D/2.5D spatial relations, transforms, alignment, distance and constraints independently of provider syntax | OpenUSD transforms/relationships/layers, Cassowary constraints, CSS Grid alignment concepts | `ADAPT + small AIMAGE extension` | Adapt scene/constraint vocabulary; solver implementation deferred to language/runtime. USD remains optional interoperability, not canonical job state. | Compact visual-semantic predicates such as camera relation, same-row/right-of/front-behind, gaze, reading order and importance hierarchy, plus mapping to solver/provider controls. |
| F05 | `ADAPT` + `DESIGN` | Low-cost structural intermediate artifact plus human acceptance before expensive rendering | DCC/VFX blocking/previsualization pattern, provider structural controls, generic approval/artifact semantics | `ADAPT + small AIMAGE extension` | Provider/tool creates blocking artifact; AIMAGE stores its role/approval using C02/C04 semantics. | `blocking` as a visual authority role and rules for what approval freezes versus leaves creative. No custom blocking renderer required. |
| F20 | `DESIGN` initially | Separate exact text content from deterministic spatial/typographic layout | SVG 2 text, CSS Grid/layout systems | `ADAPT + small AIMAGE extension` | Prefer deterministic SVG/CSS-like layout/finalization when exact text is required; provider rendering remains optional capability. | Provider-neutral declaration of text content, intended graphic region, editability and whether text is generated-in-image or deterministically composed. |
| F21 | `DESIGN` on generic review | Domain-specific acceptance criteria and defect semantics | generic rule/check systems, external domain QA examples | `DESIGN` — domain layer only | Generic review transport/result machinery is reused; checks live in replaceable domain plugins. | The actual domain rubric/threshold/defect meaning (for example character identity or product-specific acceptance) because generic frameworks cannot supply product-specific correctness. |
| F23 | `DESIGN` | Domain-specific behavior loaded through an extension boundary | mature plugin/adapter patterns solve extension mechanics, not domain meaning | `DESIGN` — domain semantics only | Extension/plugin mechanics must be adapted from generic patterns; individual domain modules depend on engine interfaces. | New domain behavior itself. No native plugin framework should be invented beyond the minimum extension contract. |

### Retained DESIGN burden of proof

Only `F21` and the semantic content portion of `F23` remain materially `DESIGN` in this matrix.

They survive because external frameworks can provide plugin/check machinery but cannot know the user's domain-specific definition of a correct character illustration, product image, storyboard, spatial design, or future domain. Removing AIMAGE ownership here would remove actual product behavior rather than merely naming or storage convenience.

Everything else previously listed as a major native-core gap has been reduced to adaptation plus a small image-specific vocabulary or to generic reuse.

## 4. Engine/Core capability classification after re-audit

| ID | Capability | Classification | External basis | Decision |
|---|---|---|---|---|
| C01 | Image-job lifecycle / state machine | `ADAPT + small AIMAGE extension` | SCXML; BPMN; Temporal patterns | Reuse generic state/event/history/human-gate semantics. Do not build a bespoke workflow engine. |
| C02 | Artifact identity, versioning, lineage | `ADAPT + small AIMAGE extension` | W3C PROV; OpenAssetIO; SLSA/CAS; optional C2PA | Reuse identity/derivation/resolution concepts; add only visual authority lifecycle relationships. |
| C03 | Reference-role binding contract | `ADAPT + small AIMAGE extension` | OpenAssetIO traits/relationships; OpenUSD references/layers | Use typed relationship/trait patterns; retain small visual-role vocabulary/precedence. |
| C04 | Approval and lock semantics | `ADAPT + small AIMAGE extension` | Temporal/BPMN approval; layered override patterns | Approval is a state transition; lock meaning is dimension-scoped visual preservation intent. |
| C05 | Provider adapter interface | `ADAPT + small AIMAGE extension` | LSP/OpenAssetIO/ports-adapters patterns | Reuse stable host/backend separation; define only image operation contract. |
| C06 | OpenAI image provider | `ADOPT` — runtime dependency | OpenAI official SDK/API | Official SDK behind provider adapter; no reimplementation of API transport. |
| C07 | ComfyUI provider/backend | `ADAPT` — optional backend | ComfyUI service + official workflow templates | Separate optional service; selected pinned MIT workflow artifacts only when required. |
| C08 | Diffusers local provider/backend | `ADOPT` — optional backend | Hugging Face Diffusers | Optional normal package dependency; model/checkpoint license separate. |
| C09 | Provider capability discovery | `ADAPT + small AIMAGE extension` | LSP capabilities; Vulkan features/extensions; OpenAssetIO capabilities | Reuse capability-negotiation model; keep only image capability taxonomy. |
| C10 | Model/provider routing policy | `ADAPT` | GenAI Illustration Pipeline, Nori, style-consistency-ai | Reuse task/capability routing and escalation; domain policy remains above engine. |
| C11 | Provider workflow graph interoperability | `ADAPT` | ComfyUI workflow JSON/blueprints | Adapter-edge import/export/validation only; never canonical job state. |
| C12 | Render specification / provider-neutral execution intent | `ADAPT + small AIMAGE extension` | LLVM/MLIR IR/lowering; JSON Schema | Treat RenderSpec as a small typed/versioned AIMAGE IR lowered by adapters. Do not invent IR infrastructure. |
| C13 | Run/provenance record | `ADAPT` | W3C PROV/SLSA concepts; GenAI/Nori history | Record exact inputs, provider/model/capability, output identity, cost and derivation without duplicating external provenance systems. |
| C14 | Error classification / retry policy | `ADAPT` | provider error contracts; workflow retry patterns | Normalize errors while retaining raw provider identity; retry only retryable execution failures. |
| C15 | Cost/latency telemetry | `ADAPT` | provider usage/cost data; production-pipeline reporting | Generic telemetry interface with provider collectors. |
| C16 | Persistence store interface | `ADAPT` | generic metadata/blob-store and content-addressed patterns | No bespoke persistence semantics; implementation choice deferred until runtime needs are known. |
| C17 | Configuration/profile serialization | `ADAPT` | JSON Schema; schema-evolution patterns | Standard serialization/validation/evolution machinery; AIMAGE only owns the schemas. |
| C18 | Handoff/continuity integration | `ADOPT` — existing internal | Existing AIMAGE Continuity/Handoff | Engine exposes required state; continuity remains outside image-production semantics. |

## 5. Feature/Domain capability classification after re-audit

| ID | Capability | Classification | External basis | Decision |
|---|---|---|---|---|
| F01 | Intent / brief extraction | `ADAPT` | Nori intent stage; GenAI shot/work-item extraction | Reuse brief→structured-work-item pattern; keep generic. |
| F02 | Creative direction generation | `ADAPT` | Nori exploration pattern | Reuse multiple-direction exploration; exact creative strategy remains feature logic. |
| F03 | Composition diversity / anti-collapse strategy | `ADAPT + small AIMAGE extension` | Nori + NIST combinatorial/DOE method | Reuse coverage/diversity method; retain visual diversity axes/anti-prior heuristics. |
| F04 | Geometry / composition specification | `ADAPT + small AIMAGE extension` | OpenUSD; Cassowary; CSS Grid | Adapt mature spatial/constraint primitives; retain compact visual semantic vocabulary. |
| F05 | Blocking / skeleton artifact workflow | `ADAPT + small AIMAGE extension` | DCC/VFX blocking; provider structural controls | Provider/tool creates structure; AIMAGE owns only role/approval meaning. |
| F06 | Character/subject bible | `ADAPT` | Nori Character Bible; consistency atlas method | AIMAGE profile schema informed by proven patterns. |
| F07 | Style bible/profile | `ADAPT` | Nori Style Bible; production reference anchors | Style remains independent authority dimension. |
| F08 | Reference atlas | `ADAPT` — method-only where restricted | style-consistency-ai; Nori | Independently implement atlas/coverage concept; no restricted-source copy. |
| F09 | Closest-reference selection | `ADAPT` — method-only | style-consistency-ai | Independently implement measurable similarity/routing strategy. |
| F10 | Corrective-guideline accumulation | `ADAPT` — method-only | style-consistency-ai | Record observed recurring corrections only. |
| F11 | Structural conditioning | `ADOPT` — provider capability | Diffusers ControlNet; ComfyUI workflows | Adapter exposes when available; never required by core. |
| F12 | Image-reference conditioning / identity guidance | `ADOPT` — provider capability | OpenAI image input; Diffusers IP-Adapter; ComfyUI | Map role-bound references to provider-native controls. |
| F13 | Masked / regional editing | `ADOPT` — provider capability | OpenAI image edits/masks; ComfyUI/Diffusers inpainting | Provider executes edit; AIMAGE owns delta/preservation intent. |
| F14 | Multi-turn controlled editing | `ADOPT` + `ADAPT` | provider multi-turn edit state; Nori controlled refine | Provider state is acceleration/cache, never canonical AIMAGE authority. |
| F15 | Minimal-delta repair strategy | `ADAPT` | MAPE-style analyze/plan/execute separation; Nori/style-consistency/GenAI | Diagnose, plan, select capability, execute through provider, verify regression. No AIMAGE renderer. |
| F16 | Automated visual review rubric | `ADAPT` | Nori critique; GenAI agent QA | Generic review schema with modular domain rubrics. |
| F17 | Human review / approval | `ADAPT` | Temporal/BPMN approval; GenAI/Nori review | Human subjective approval integrates with C04 state/lock semantics. |
| F18 | Contact sheets / comparison boards | `ADAPT` | common art workflow; GenAI utility evidence | Prefer small deterministic AIMAGE utility; source import is not required initially. |
| F19 | Deterministic finishing utilities | `ADAPT` | common image utilities; GenAI scripts as evidence | Implement/use small standard libraries per language; source-copy decision only if clearly cheaper after audit. |
| F20 | Output-text / graphic-layout planning | `ADAPT + small AIMAGE extension` | SVG 2; CSS Grid/layout | Deterministic layout primitives first for exact text; provider-native text only when suitable. |
| F21 | Domain-specific QA | `DESIGN` — domain layer only | generic review/check machinery | Only domain correctness semantics are native; execution framework is reused. |
| F22 | Character consistency escalation to datasets/training | `ADAPT` — optional/future | consistency ladder; diffusion training ecosystem | Keep escalation concept, defer training until lighter methods fail. |
| F23 | Domain extensions | `DESIGN` — domain semantics only | generic plugin patterns for mechanics | Native domain behavior only; extension machinery must remain thin/reused. |
| F24 | Canvas/editor UI | `ADAPT` — deferred | Krita AI Diffusion, Nori and mature DCC interaction models | Reuse interaction patterns when UI is justified; no UI dependency now. |

## 6. Resulting AIMAGE-owned semantic residue

After external composition, the core/domain boundary should not treat generic state machines, provenance graphs, serializers, constraint solvers, plugin systems, or compiler-lowering mechanics as inventions of AIMAGE.

The remaining AIMAGE-owned semantic center is intentionally small:

1. **visual authority vocabulary** — which dimension a profile/reference/artifact governs and precedence/conflict meaning;
2. **dimension-scoped approval/lock/preservation intent** — what the user approved and what later execution must preserve or explicitly reopen;
3. **visual execution intent vocabulary** — the small provider-neutral fields/invariants in the RenderSpec IR that adapters must lower without semantic loss;
4. **image capability taxonomy/compatibility predicates** — the visual operations and constraints routing reasons about;
5. **visual spatial predicates and reading hierarchy** — the domain vocabulary layered on mature transform/constraint primitives;
6. **domain-specific review/extension semantics** — actual correctness/behavior for character, product, storyboard and future domains.

These are not exemptions from future review. If a mature standard later closes one of them without losing user-visible control, reclassify it.

## 7. What is actually brought into the initial implementation versus only reused as method

### Initial concrete runtime/provider integrations

- OpenAI official SDK/API — normal dependency behind `OpenAIProviderAdapter`.
- Hugging Face Diffusers — optional local-provider package when the selected implementation runtime supports it.
- ComfyUI — optional separately installed service/backend; no GPL core source copied into AIMAGE.

### Standards/methods used to shape AIMAGE contracts without runtime coupling

- SCXML/BPMN/Temporal patterns for workflow/gates;
- W3C PROV and SLSA concepts for lineage/provenance;
- LLVM/MLIR IR/lowering patterns;
- LSP/Vulkan/OpenAssetIO capability/adapter patterns;
- OpenUSD/Cassowary/CSS layout patterns for spatial constraints;
- Avro schema-evolution principles;
- SVG/CSS for deterministic text/graphic layout;
- MAPE-style diagnose/plan/execute/verify separation for repair.

### Optional interoperability only

- OpenAssetIO integration when a real DAM/MAM manager is used;
- OpenUSD import/export or geometry bridge if a concrete DCC/VFX use case justifies it;
- C2PA packaging for exported-content provenance;
- selected ComfyUI workflow templates pinned at the adapter edge.

### No initial source copying

Nori, GenAI Illustration Pipeline, Krita AI Diffusion and style-consistency-ai remain architecture/method/UX evidence by default. Small permissive utilities may be reconsidered only after implementation shows a measured gap and the acquisition gate in `plans/REUSE_AND_INTEGRATION_ASSURANCE.md` passes. This removes unnecessary pre-commitment to source imports.

## 8. Reclassification and assurance rule

A candidate may move from `ADOPT`/`ADAPT` toward more native work only when evidence shows a material problem such as incompatible license/distribution, unacceptable runtime coupling, semantic leakage, maintenance failure, untestable behavior, or integration complexity exceeding a bounded AIMAGE implementation.

Conversely, any remaining AIMAGE semantic must shrink when a mature compatible external primitive is found.

Before implementation, each concrete external component must pass `plans/REUSE_AND_INTEGRATION_ASSURANCE.md` Gate B. Before the architecture/workflow is treated as complete, the integrated system must pass Gates C and D.
