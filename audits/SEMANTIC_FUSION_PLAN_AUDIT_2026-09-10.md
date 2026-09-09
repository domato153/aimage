# AIMAGE Semantic Fusion Final-Plan Audit — 2026-09-10

Status: independent bounded planning/design audit of `plans/SEMANTIC_FUSION_PLAN.md` before adoption. No implementation, dependency installation, source import, provider integration, or runtime selection is authorized by this audit.

## 1. Verdict

**PASS** for planning adoption, subject to the normal final fresh-head/PR mergeability check.

The candidate meaningfully improves the accepted design by shrinking six separately described AIMAGE semantic residues into four coherent contract families while preserving existing provider, assurance, continuity/handoff, and feature/core boundaries.

## 2. Exact audit base and candidate

- Repository: `domato153/aimage`
- Fresh authoritative `main` at audit: `61ba94bc6279fa12091baa05c30a2ce1dd4fc5d8`
- Candidate branch: `aimage-stage/semantic-fusion-final-plan`
- Merge base: exact fresh `main`
- Candidate behind main at first compare: `0`

Initial candidate changes before this audit record:

- `plans/SEMANTIC_FUSION_PLAN.md` — new final semantic-fusion planning surface;
- `governance/continuity/CURRENT.md` — supersedes the stale six-separate-residue next action and routes the next bounded design action;
- `AGENTS.md` — adds the accepted-plan route so cold-start agents do not miss the new planning owner.

This audit file is the only additional file added by the audit itself.

## 3. External evidence audit

### RFC 9315

Confirmed as an **IRTF Informational RFC**, not an Internet Standards Track specification. It nevertheless provides mature consensus terminology for declarative intent, SSoT, fulfillment/translation/orchestration, assurance, monitoring and corrective behavior.

Audit decision: valid `E/F` method/reference evidence. The plan correctly avoids making it an executable or normative AIMAGE runtime specification.

Source:
- https://www.rfc-editor.org/info/rfc9315/

### OSGi Requirement-Capability / Resolver

Confirmed generic model:

- typed Requirements and Capabilities;
- domain semantics through namespaces;
- mandatory requirements must be satisfied;
- a resolver returns a consistent wiring result or explicit resolution failure.

Audit decision: strong method analogue for provider capability resolution. The plan correctly adopts the model, not OSGi runtime/framework coupling.

Sources:
- https://docs.osgi.org/specification/osgi.core/8.0.0/framework.resource.html
- https://docs.osgi.org/specification/osgi.core/8.0.0/service.resolver.html

### NIST configuration baseline

Confirmed definition: a reviewed/agreed configuration set that changes only through change-control procedures.

Audit decision: valid pattern for user-approved visual baselines without importing unrelated security-management ceremony.

Source:
- https://csrc.nist.gov/glossary/term/configuration_baseline

### Frame conditions / JML

Confirmed principle: the specification declares locations allowed to change; locations outside the frame are assumed unchanged.

Audit decision: valid semantic analogue for repair mutable/preserve dimensions. It is not treated as proof that visual edits can be mechanically verified like program memory and does not introduce JML syntax/runtime.

Source:
- https://www.openjml.org/tutorial/FrameConditions

### QSR/QSTR and OGC RCC8

Confirmed mature qualitative-spatial field covering symbolic topology/orientation/distance reasoning. OGC GeoSPARQL standardizes an RCC8 topological relation family.

Audit decision: strong basis for a compact spatial profile and explicit reference-frame handling. The plan correctly rejects creation of a universal AIMAGE spatial ontology and avoids mandatory RDF/GeoSPARQL runtime/storage.

Sources:
- https://www.ijcai.org/proceedings/2021/624
- https://docs.ogc.org/is/22-047r1/22-047r1.html

### W3C SHACL

Confirmed stable Recommendation semantics:

- shapes/constraints are separate from validated data;
- validation returns structured conformance/results;
- validation does not mutate the input graphs.

Audit decision: strong method/result-model analogue for AIMAGE validation profiles. The plan correctly keeps AIMAGE JSON-family and does not require RDF/SHACL runtime. SHACL 1.2 work is not relied on for a dependency decision.

Source:
- https://www.w3.org/TR/shacl/

### OPA

Confirmed general architecture separating policy decision from enforcement and accepting structured input to return decisions.

Audit decision: valid architecture pattern for keeping review/repair decisions separate from provider execution. No OPA runtime is required by the plan.

Source:
- https://www.openpolicyagent.org/docs

## 4. Architecture-boundary audit

Fresh `architecture/BOUNDARIES.md` requires:

- Continuity/Handoff stays outside image-production algorithms;
- Image Engine/Core owns reusable mechanics/interfaces;
- domain features depend on engine interfaces;
- adapters must not become canonical job authority.

Candidate compatibility:

- `VisualIntentState` is engine semantic authority, not Continuity/Handoff state ownership;
- Continuity/Handoff may transport identities/accepted state but does not define image semantics;
- Family D allows domain profiles to supply domain rules through engine interfaces without importing domain implementations into core;
- provider-native prompts/IDs/graphs and `ExecutionPlan` are explicitly non-authoritative;
- `RenderSpec` is a derived compiled view, preventing adapter/provider representation from becoming canonical authority.

Result: **PASS**.

No update to `architecture/BOUNDARIES.md` is required by this plan because it refines the contents of the already-reserved Engine/Core responsibility rather than moving responsibility between the three zones.

## 5. Existing-plan compatibility audit

### Capability reuse matrix

The candidate does not invalidate the accepted `ADOPT / ADAPT / DESIGN` classification. It refines the exact small AIMAGE extension/residue by showing that the generic mechanism under several residue descriptions can be composed from stronger cross-domain primitives.

The remaining AIMAGE-owned content becomes primarily image ontology/profile vocabulary rather than six independent mechanisms.

Result: **PASS**.

### External reuse plan

Concrete provider decisions remain unchanged:

- OpenAI official SDK/API;
- optional Diffusers;
- optional external ComfyUI;
- no initial source copying;
- optional OpenAssetIO/OpenUSD/C2PA interoperability only when justified.

New external sources are method/reference inputs and introduce no new mandatory runtime dependency.

Result: **PASS**.

### Reuse/integration assurance

Existing Gate A/B/C/D remains applicable. The fusion plan adds semantic invariants and design-level tabletop simulation requirements rather than inventing a competing V&V process.

Result: **PASS**.

### Workflow target

No workflow stage is added or deleted. The fusion plan assigns existing W0-W14 logical functions to clearer semantic owners.

Result: **PASS**.

## 6. Semantic ownership audit

Checked for duplicate or circular ownership.

### Family A — Visual Intent & Authority

Owns desired-state authority, dimension authority, baseline/change-control and preserve/mutable semantics.

Does not own provider execution or validation judgment implementation.

### Family B — Requirement, Capability & Lowering

Owns requirement/capability matching and provider-specific lowering.

Does not own user intent or silently rewrite mandatory semantics.

### Family C — Spatial & Composition Profile

Owns spatial vocabulary/profile content used by intent, compilation and review.

Does not become a general geometry engine or provider representation.

### Family D — Validation & Domain Profile

Owns rule/profile evaluation semantics and structured results.

Does not mutate canonical state or directly execute provider repair.

No blocking ownership cycle was found. Family C/D are semantic profiles consumed by A/B; they do not become alternative authorities.

Result: **PASS**.

## 7. Critical invariant audit

The candidate explicitly requires:

- single canonical semantic authority;
- no silent loss during lowering;
- controlled baseline mutation;
- bounded repair frame;
- explicit viewpoint/reference frame for ambiguous direction;
- provider replaceability;
- validation/enforcement separation;
- validation purity;
- domain -> engine dependency direction;
- derived-view provenance;
- explicit unsatisfied mandatory requirement behavior;
- one-shot simplicity.

These invariants are sufficient to drive the next contract-design/tabletop slice and map cleanly into existing Assurance Gate C/D scenarios.

Result: **PASS**.

## 8. Risks deliberately deferred to the next slice

These are not planning-adoption blockers because the fusion plan explicitly makes them next-step acceptance obligations:

- exact field/schema design for each four-family contract;
- exact representation of precedence/conflict rules;
- exact spatial predicate subset and defaults;
- exact distinction between mandatory versus preference-level intent;
- exact normalized ValidationReport structure;
- exact JSON Schema layout/versioning;
- whether a concrete spatial solver or validation/rule library is required at all;
- implementation language/runtime and package choices.

These must not be silently decided during implementation. They belong to contract-schema design or later Gate B acquisition.

## 9. Final audit conclusion

The semantic-fusion plan reduces custom architecture rather than increasing it, keeps external systems as method evidence or replaceable provider edges, preserves current authority boundaries, and creates a testable route from user visual intent to provider execution and back to assurance/repair.

**Planning adoption verdict: PASS.**

After adoption, the next bounded action should be exactly the one recorded in `governance/continuity/CURRENT.md`: define the minimum provider-neutral four-family contracts and immediately tabletop-simulate the canonical assurance scenarios before any implementation planning.