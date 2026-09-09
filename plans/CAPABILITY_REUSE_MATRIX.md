# AIMAGE Capability Reuse Matrix

Status: planning/design classification. This matrix decides where AIMAGE should adopt, adapt, or design capabilities before implementation begins.

The matrix is evidence-first and may be revised when a candidate fails technical, licensing, maintenance, or architecture-fit review.

## 1. Classification vocabulary

- `ADOPT` — use an external implementation/service substantially as-is behind an AIMAGE-owned interface.
- `ADAPT` — reuse an external implementation, workflow pattern, method, schema idea, or selected code while changing/wrapping/internalizing it for AIMAGE requirements.
- `DESIGN` — define an AIMAGE-native mechanism because no suitable external solution closes the requirement.

Modifiers:

- `runtime dependency` — the external package/service remains present at runtime.
- `optional backend` — runtime dependency exists only when that provider/backend is enabled.
- `selective source import` — permissively licensed source may be copied only after file-level audit and attribution.
- `method-only` — ideas/methods may inform AIMAGE, but source/code/text should not be copied.
- `provider capability` — the capability lives behind a provider adapter and does not become core semantics.
- `deferred` — classification is recorded now, but implementation/evaluation is intentionally postponed until the core workflow proves the need.

## 2. External evidence set used for this classification

Current evidence includes:

1. OpenAI Image Generation API documentation — generation, edits, image references, multi-turn editing, masks, high-fidelity image inputs, Responses API.
   - https://developers.openai.com/api/docs/guides/image-generation
2. OpenAI official SDKs — official API clients, Apache-2.0 for Python/Node SDKs.
   - https://github.com/openai/openai-python
   - https://github.com/openai/openai-node
3. ComfyUI workflow templates — official MIT-licensed workflow templates/subgraph blueprints with JSON/schema validation.
   - https://github.com/Comfy-Org/workflow_templates
4. ComfyUI core — graph/node image-generation backend, GPL-3.0.
   - https://github.com/Comfy-Org/ComfyUI
5. Hugging Face Diffusers — Apache-2.0 diffusion framework; ControlNet and IP-Adapter support structural and image-reference conditioning.
   - https://github.com/huggingface/diffusers
   - https://huggingface.co/docs/diffusers/using-diffusers/ip_adapter
6. Nori — MIT persistent creative-agent architecture with projects, style/character bibles, plan/explore/critique/refine/finish loop, history and thin model adapters.
   - https://github.com/aditya-ramesh/nori
7. GenAI Illustration Pipeline — MIT production pipeline reporting ~1,523 delivered still assets, with shot lists, model routing, reference stacks, agent QA, human review, deterministic finishing, fixtures, and revision handling.
   - https://github.com/Kanishk688/genai-illustration-pipeline
8. Krita AI Diffusion — GPL-3.0 image workflow demonstrating regions, history, inpainting, ControlNet, IP-Adapter and optional ComfyUI backend.
   - https://github.com/Acly/krita-ai-diffusion
9. style-consistency-ai — PolyForm Noncommercial method set for smallest-edit-first, reference atlases, closest-reference selection, escalation, model routing, and drift verification.
   - https://github.com/GenielabsOpenSource/style-consistency-ai

External evidence informs design but does not become AIMAGE authority.

## 3. Engine/Core capability classification

| ID | Capability | Classification | External basis | Decision |
|---|---|---|---|---|
| C01 | Image-job lifecycle / state machine | `ADAPT` | Nori generation loop; production pipeline stage structure | Reuse proven stage patterns, but define AIMAGE-native state/gate semantics because approval, locks, repair and continuity boundaries are project-specific. |
| C02 | Artifact identity, versioning, lineage | `ADAPT` | Nori project/history model; pipeline provenance patterns | Reuse version-graph/provenance concepts. AIMAGE must own artifact identity and accepted/rejected/derived relationships. |
| C03 | Reference-role binding contract | `DESIGN` | OpenAI supports multiple references; diffusion stacks separate structural/image controls | No external standard found that gives AIMAGE's required explicit identity/style/composition/blocking authority semantics. Design core contract. |
| C04 | Approval and lock semantics | `DESIGN` | Human-review gates exist in external pipelines | External workflows prove the gate pattern, but AIMAGE must define what approval locks and how later edits preserve/reopen it. |
| C05 | Provider adapter interface | `DESIGN` | Nori thin model adapters; multi-provider illustration pipeline | External architectures support adapter separation, but AIMAGE needs its own provider-neutral contract and capability vocabulary. |
| C06 | OpenAI image provider | `ADOPT` — runtime dependency | OpenAI official SDK/API | Use official SDK behind AIMAGE provider adapter; do not reimplement HTTP surface unless required. |
| C07 | ComfyUI provider/backend | `ADAPT` — optional backend | ComfyUI API/backend + official workflow templates | Treat ComfyUI as separately installed optional service; use AIMAGE adapter and selected normalized workflows. Do not copy GPL core into AIMAGE core. |
| C08 | Diffusers local provider/backend | `ADOPT` — optional backend | Hugging Face Diffusers Apache-2.0 | Use Diffusers as optional package/backend where direct local pipelines are useful. Keep model/checkpoint licenses separately tracked. |
| C09 | Provider capability discovery | `DESIGN` + `ADAPT` | OpenAI API features; Diffusers/ComfyUI controls; Nori routing | Define AIMAGE capability descriptors, populated by provider-specific adapters. |
| C10 | Model/provider routing policy | `ADAPT` | GenAI Illustration Pipeline, Nori, style-consistency-ai | Reuse task-based routing and escalation principles. Keep actual routing policy in feature/domain layer where possible. |
| C11 | Provider workflow graph interoperability | `ADAPT` | ComfyUI workflow JSON / blueprints | Support import/export/validation for ComfyUI adapter; do not make ComfyUI JSON the canonical AIMAGE job schema. |
| C12 | Render specification | `DESIGN` | No exact cross-provider equivalent | Build provider-neutral AIMAGE Render Spec compiled by adapters into provider controls. |
| C13 | Run/provenance record | `ADAPT` | GenAI pipeline metrics/provenance; Nori history | Define AIMAGE record, borrowing practical fields such as model, refs, cost, inputs, output lineage, review result. |
| C14 | Error classification / retry policy | `ADAPT` | Provider error contracts, including OpenAI stable error codes | Normalize provider errors to AIMAGE categories but retain raw provider error identity. Never blind-retry user-correctable image failures. |
| C15 | Cost/latency telemetry | `ADAPT` | Provider usage/cost data; GenAI pipeline cost reporting | AIMAGE-owned telemetry interface, provider-specific collectors. |
| C16 | Persistence store interface | `DESIGN` | Nori Postgres/Redis implementation | Do not inherit Nori's infrastructure by default. Define storage boundary first; choose implementation only after scale/usage needs exist. |
| C17 | Configuration/profile serialization | `DESIGN` | General JSON/YAML patterns | AIMAGE-specific semantic contracts require native schemas; generic serializers can be dependencies later. |
| C18 | Handoff/continuity integration | `ADOPT` — existing internal | Existing AIMAGE Continuity/Handoff | Already implemented as AIMAGE-owned infrastructure; engine only exposes state needed by these contracts. |

## 4. Feature/Domain capability classification

| ID | Capability | Classification | External basis | Decision |
|---|---|---|---|---|
| F01 | Intent / brief extraction | `ADAPT` | Nori intent stage; GenAI shot-list/brief extraction | Reuse brief→structured-work-item concepts. AIMAGE brief remains generic, not manuscript-specific. |
| F02 | Creative direction generation | `ADAPT` | Nori proposes multiple directions and exploration boards | Reuse multi-direction exploration pattern; AIMAGE adds explicit diversity axes and anti-prior checks. |
| F03 | Composition diversity / anti-collapse strategy | `ADAPT` + `DESIGN` | Nori composition reasoning, external visual-control workflows | Reuse direction-board principle, but design AIMAGE-specific geometry/diversity gates because the exact failure class is central and no complete external solution was found. |
| F04 | Geometry / composition specification | `DESIGN` | Structural controls exist but not a cross-provider semantic format | Define AIMAGE semantic geometry contract independent of ControlNet/masks/provider prompt syntax. |
| F05 | Blocking / skeleton artifact workflow | `ADAPT` + `DESIGN` | OpenAI sketch/reference editing; Krita/ControlNet structural workflows | Reuse sketch/structure-as-control concept. Design provider-neutral artifact role, approval and fallback behavior. |
| F06 | Character/subject bible | `ADAPT` | Nori Character Bible; style-consistency atlas/dataset method | Define AIMAGE profile schema based on these proven patterns; do not copy noncommercial skill text. |
| F07 | Style bible/profile | `ADAPT` | Nori Style Bible; production pipeline style/reference anchors | Define AIMAGE profile schema; preserve style as independent authority from composition/identity. |
| F08 | Reference atlas | `ADAPT` — method-only where source restricted | style-consistency-ai; Nori multi-angle bible | Implement AIMAGE-owned atlas/coverage concepts; no direct copying from PolyForm Noncommercial material. |
| F09 | Closest-reference selection | `ADAPT` — method-only | style-consistency-ai | Implement AIMAGE-owned reference selection strategy after defining measurable pose/angle/context similarity. |
| F10 | Corrective-guideline accumulation | `ADAPT` — method-only | style-consistency-ai | Keep only observed, recurring correction rules rather than giant descriptive prompts. Reimplement independently. |
| F11 | Structural conditioning | `ADOPT` — provider capability | Diffusers ControlNet; ComfyUI control workflows | Expose when backend supports pose/depth/edge/segmentation/etc. Core must not require it. |
| F12 | Image-reference conditioning / identity guidance | `ADOPT` — provider capability | OpenAI image references/high fidelity; Diffusers IP-Adapter; ComfyUI | Map AIMAGE role-bound references into backend-specific mechanisms. |
| F13 | Masked / regional editing | `ADOPT` — provider capability | OpenAI masks; Krita/ComfyUI inpainting patterns | Provider adapter capability. AIMAGE owns requested region/delta semantics. |
| F14 | Multi-turn controlled editing | `ADOPT` + `ADAPT` | OpenAI Responses API multi-turn editing; Nori controlled refine | Use provider-native edit state where available while persisting AIMAGE-owned edit intent and artifact lineage. |
| F15 | Minimal-delta repair strategy | `ADAPT` | Nori controlled edits; style-consistency smallest-edit principle; GenAI revision handling | AIMAGE repair policy should preserve successful parts and escalate only after evidence of failure. |
| F16 | Automated visual review rubric | `ADAPT` | Nori critique dimensions; GenAI agent QA | Build AIMAGE review schema and modular rubrics; do not hard-code book-print QA into generic engine. |
| F17 | Human review / approval | `ADAPT` | GenAI human art-direction gate; Nori accept/reject/edit loop | Keep human approval as authoritative subjective decision; integrate into AIMAGE approval state. |
| F18 | Contact sheets / comparison boards | `ADAPT` — selective source import candidate | GenAI contact-sheet script; common art workflow | Likely reuse or reimplement small deterministic tooling after source audit. |
| F19 | Deterministic finishing utilities | `ADAPT` — selective source import candidate | GenAI scripts for crop/pad, alpha, DPI, WebP, finishing QA | Import only generic useful MIT modules after file-level audit; otherwise implement equivalent small utilities. |
| F20 | Output-text / graphic-layout planning | `DESIGN` initially | Image APIs support text but no complete AIMAGE layout contract identified | Define semantic text/layout layer; later evaluate specialized layout libraries separately. |
| F21 | Domain-specific QA | `DESIGN` on top of generic review contract | External pipelines show domain QA patterns | Each domain owns its checks; do not put character/book/product-specific checks in core. |
| F22 | Character consistency escalation to datasets/training | `ADAPT` — optional/future | style-consistency ladder; diffusion training ecosystem | Preserve escalation concept but do not make training a default dependency. Evaluate only after lighter controls demonstrably fail. |
| F23 | Domain extensions | `DESIGN` | No single external system covers AIMAGE's planned domains | Implement later as plugins/profiles against engine interfaces. |
| F24 | Canvas/editor UI | `ADAPT` — deferred | Krita AI Diffusion and Nori show useful interaction models | Reuse interaction concepts when UI work becomes necessary, but postpone UI-specific source/tool evaluation until the core workflow proves the need. |

## 5. What can be brought in now at planning level

The following reuse decisions are strong enough to shape architecture now even though implementation is not authorized:

### Direct/optional implementation dependencies

- OpenAI official SDK/API for the OpenAI provider adapter.
- Hugging Face Diffusers as an optional local-provider dependency.
- ComfyUI as an optional separately installed backend accessed through an adapter, not copied into AIMAGE core.

### Permissively licensed source candidates requiring file-level audit before copying

- selected generic utilities/patterns from `genai-illustration-pipeline` (MIT);
- selected generic abstractions/patterns from Nori (MIT);
- selected official ComfyUI workflow-template/blueprint JSON files (MIT), only if a specific supported backend path benefits from them.

No wholesale repository import is approved.

### Method-only sources

- Krita AI Diffusion (GPL-3.0): use as design evidence for control layers, regions, history, edit UX and external-backend separation; do not copy source into AIMAGE unless the project deliberately accepts compatible GPL obligations.
- style-consistency-ai (PolyForm Noncommercial): use only as conceptual evidence unless the licensing situation changes or explicit permission is obtained. Reimplement concepts independently.

## 6. Capabilities that still require native AIMAGE design

The most important native design gaps are:

1. provider-neutral image-job state model;
2. explicit reference-role authority contract;
3. approval/lock semantics;
4. AIMAGE Render Spec;
5. provider capability descriptor and routing boundary;
6. provider-neutral geometry/composition semantic contract;
7. artifact identity/version/provenance model;
8. generic review/repair schemas;
9. persistence boundary;
10. exact separation between engine interfaces and feature/domain strategies.

These gaps should be designed only after the external-reuse integration boundaries in `plans/EXTERNAL_REUSE_PLAN.md` are accepted.

## 7. Reclassification rule

A candidate moves from `ADOPT`/`ADAPT` to `DESIGN` if any of the following becomes material:

- license or redistribution requirements conflict with the intended AIMAGE distribution;
- runtime coupling would make the source project an unintended authority;
- the candidate's data model leaks provider/domain semantics into core;
- the candidate is insufficiently maintained or validated for the required role;
- the integration surface is more complex than a small AIMAGE-native implementation;
- a source's advertised behavior is not reproduced under AIMAGE's actual use case.

Conversely, a `DESIGN` capability may become `ADOPT`/`ADAPT` if later evidence finds a mature compatible solution.
