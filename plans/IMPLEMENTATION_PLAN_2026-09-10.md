# AIMAGE Concrete Implementation Plan — 2026-09-10

Status: planning/design artifact only. This plan does **not** authorize production implementation, dependency installation, lockfile mutation, source import, provider integration, or final Gate-D/system PASS.

Fresh planning base at branch creation: `main = a7f6343cd1315cedf81fc68d77862125f17468be`.

Governing semantic authority remains `plans/SEMANTIC_CONTRACTS.md`. This document selects a concrete implementation shape under that authority; it does not replace or reopen the accepted semantic contracts.

## 1. Decision summary

The first implementation slice SHALL use:

- runtime: **CPython 3.13** as the initial supported baseline;
- validation/schema library: **Pydantic 2.13.5**;
- metadata persistence: **SQLite via SQLAlchemy 2.0.52 Core**, using explicit non-legacy transaction control;
- relational migration tool: **Alembic 1.19.2**, with human-reviewed explicit migrations;
- artifact/blob storage: AIMAGE-owned `ArtifactStore` interface with a first **local content-addressed filesystem** implementation using Python stdlib only;
- hosted image provider adapter: **OpenAI Python SDK 3.11.0**;
- first provider capability target: **`gpt-image-2.5-sunburst-2026-09-08`**, recorded only as provider capability/configuration evidence, never semantic authority;
- test runner: **pytest 9.1.1**;
- async test support: **pytest-asyncio 1.4.0**;
- solver: **none in the first slice**; add a constraint solver only after a measured requirement demonstrates that direct qualitative/structural predicates are insufficient;
- Diffusers: optional future local-provider integration, **not** a first-slice dependency;
- ComfyUI: optional future external-backend integration, **not** a first-slice dependency.

All exact versions above are the **planning baseline**, not permission to install. At the start of a separately authorized implementation slice, fresh-read releases/security/provider capability state. If a newer version is proposed, rerun the affected Gate-B row before changing the selected version. The future lock must bind exact resolved artifacts/hashes; no lockfile is created in this planning slice.

## 2. Runtime/language selection

### 2.1 Compared candidates

| Criterion | CPython 3.13 | Node.js + TypeScript | Decision consequence |
|---|---|---|---|
| Accepted semantic-contract expression | Strong: dataclasses/typing plus Pydantic models and discriminated unions | Strong: TypeScript types plus a runtime schema library would still be needed | Both viable |
| OpenAI official SDK/API | Official typed sync/async Python SDK | Official TypeScript SDK | Tie on provider viability |
| JSON Schema ergonomics | Pydantic directly emits Draft 2020-12 schema | Would need an additional runtime schema choice and type/schema synchronization policy | Python advantage |
| Async/provider orchestration | `asyncio` + `AsyncOpenAI` | Native Promise/event-loop model | Both viable |
| Persistence/migrations | SQLAlchemy/Alembic mature SQLite path | Several viable choices, but would add a separate ORM/schema-selection decision | Python advantage for this plan |
| Optional Diffusers boundary | Native ecosystem if/when a local provider is authorized | Requires an external Python/service boundary | Python advantage, while still keeping Diffusers optional |
| ComfyUI boundary | HTTP/service adapter | HTTP/service adapter | Tie |
| Testing | pytest ecosystem | Vitest/Jest/node:test alternatives | Tie for first slice |
| Packaging/distribution | Standard `pyproject.toml`, wheel/app packaging | npm package/application packaging | Tie |
| Provider/dependency replacement | Explicit Protocol/adapter boundaries available | Interfaces/adapters available | Tie |
| Current complexity | One runtime covers core contracts, OpenAI adapter, DB, tests, and future optional local provider | Core/provider is viable but local Diffusers would necessarily become cross-runtime | Python advantage |

### 2.2 Selection

Select **CPython 3.13**.

Reasoning:

1. it directly supports the accepted JSON-family semantic-contract design through Pydantic without creating a second schema/type authority;
2. the official OpenAI Python SDK is typed and provides equivalent sync/async APIs;
3. SQLAlchemy/Alembic provides a replaceable metadata-store boundary without making persistence semantics the domain model;
4. a future Diffusers adapter can be Python-native or isolated in a separate provider environment, while ComfyUI remains an external service either way;
5. Python does not force provider-native representations into the core and does not change `features/domain capabilities -> engine interfaces`.

CPython 3.14 SHOULD be a CI compatibility target once implementation begins, but 3.13 is the initial baseline so the first slice does not depend on the newest interpreter as its only runtime. The core API SHALL avoid 3.13-only semantics where doing so materially eases 3.14 compatibility and future replacement.

## 3. Concrete external dependency Gate B

Evidence state meanings follow `plans/REUSE_AND_INTEGRATION_ASSURANCE.md`.

### 3.1 `openai==3.11.0` — PASS

- Identity: official `openai` Python package, version `3.11.0`.
- Distribution/source: PyPI official project and `openai/openai-python`.
- Currentness: PyPI lists 3.11.0 as latest, released 2026-09-09.
- Provenance: PyPI Trusted Publishing + attestation; published wheel SHA-256 `2fc169442feafd535f4959605b42d47bc922216385a6d2473b0d47956691d9fd`; attested source commit `41f0a2317759e8796ccfbde75536bd42e4aca7a2`.
- License: Apache-2.0.
- Runtime fit: Python >=3.10; typed request/response surface; `AsyncOpenAI` available.
- Functional fit: official SDK transport for the OpenAI image adapter.
- Important runtime behavior: SDK automatically retries some connection/408/409/429/5xx failures twice by default and has a long default timeout. AIMAGE SHALL construct its provider client with `max_retries=0` and an explicit finite timeout so attempt count, cost, retry eligibility, and stop policy remain AIMAGE-owned and auditable.
- Failure evidence: normalized adapter error plus raw SDK status/error/request-id evidence in `RunRecord`; provider error objects are execution evidence only.
- Security/maintenance: active official SDK with a published vulnerability-reporting policy. Fresh vulnerability/dependency scan of the future exact lock remains an implementation-entry check.
- Coupling: all imports live under `providers/openai/`; core semantic packages SHALL NOT import the SDK.
- Replacement: another adapter consumes the same `RenderSpec`/`RequirementSet` subset and emits its own capability descriptor/lowering.
- AIMAGE-owned tests: request-lowering fixture tests, error normalization, zero-hidden-retry configuration assertion, request-id preservation, capability descriptor exactness, stale descriptor rejection, synthetic replacement adapter contract suite, and credentialed smoke test when implementation is separately authorized.

Evidence:

- https://pypi.org/project/openai/3.11.0/
- https://github.com/openai/openai-python
- https://github.com/openai/openai-python/blob/main/SECURITY.md

No blocking `UNRESOLVED` item.

### 3.2 OpenAI image-provider capability target — PASS with declared-evidence boundary

- Provider: OpenAI Image API / official SDK.
- First target: `gpt-image-2.5-sunburst-2026-09-08`.
- Current official claim: GPT-Image-2.5 Sunburst supports image generation and editing from text/image inputs; official docs expose the dated snapshot.
- Evidence class at planning close: **declared official documentation**, not reproduced live capability evidence. No credentialed provider probe was required to choose the architecture.
- Capability descriptor SHALL include: provider, SDK version, API surface, exact model snapshot, supported operation/input classes used by the slice, applicability limits relied upon, evidence kind, evidence URI, observed-at time, and descriptor digest.
- The undated alias MAY be used for discovery/user configuration, but a reproducible capability record and contract-test fixture SHALL identify the dated snapshot actually relied upon.
- Provider capability cannot alter `VisualIntentState`; lack/drift yields `stale_capabilities`, re-resolution, or explicit `unsatisfied`.
- Security/credentials: secrets remain runtime configuration and never semantic/persisted provider authority.
- Replacement: OpenAI is the first hosted adapter, not the canonical job representation.
- AIMAGE-owned implementation-entry check: one credentialed generate smoke and one image-edit smoke against the selected target, capturing actual model/provider response identity and descriptor evidence. Failure blocks production integration but does not retroactively mutate semantic architecture.

Evidence:

- https://developers.openai.com/api/docs/models/gpt-image-2.5-sunburst
- https://developers.openai.com/api/docs/guides/image-generation

No blocking `UNRESOLVED` item. Live behavior remains an explicit implementation-time empirical check, correctly classified as not-yet-reproduced evidence.

### 3.3 `pydantic==2.13.5` — PASS

- Identity/currentness: PyPI latest 2.13.5, released 2026-08-28.
- Distribution/source: PyPI and `pydantic/pydantic`.
- Provenance: Trusted Publishing with provenance bound to source commit `001dea020e0809844e5b17666432c9135a976f46`.
- License: MIT.
- Functional fit: typed validation/serialization and JSON Schema generation; official documentation states generated schemas are JSON Schema Draft 2020-12 compliant.
- Exclusion: Pydantic validation models are **representations of AIMAGE-owned contracts**, not semantic authority and not the migration engine.
- Evolution: every durable AIMAGE object keeps explicit `schema_version`; AIMAGE-owned deterministic migration functions own version-to-version meaning preservation.
- Failure: unknown mandatory semantic fields/versions fail safe rather than being dropped through permissive parsing.
- Coupling/replacement: contract codecs are isolated under `contracts/codec/`; a future validator may replace Pydantic if it can pass generated-schema and semantic round-trip tests.
- AIMAGE-owned tests: strict parsing, JSON schema snapshot/compatibility, version migration, unknown mandatory extension rejection, round-trip preservation, frozen derived-object behavior.

Evidence:

- https://pypi.org/project/pydantic/2.13.5/
- https://docs.pydantic.dev/latest/concepts/json_schema/

No blocking `UNRESOLVED` item.

### 3.4 `SQLAlchemy==2.0.52` — PASS WITH CONTROLS

- Identity/currentness: official SQLAlchemy 2.0.52, latest on PyPI at review, released 2026-08-11.
- License: MIT.
- Distribution: official PyPI / SQLAlchemy source. The reviewed CPython 3.13 Windows wheel is **not** marked Trusted Publishing on PyPI; future installation therefore requires exact artifact/hash binding from official PyPI plus future-lock verification rather than assuming publisher attestation.
- Functional fit: SQL metadata persistence over SQLite while keeping semantic contract objects as AIMAGE-owned documents/records.
- Acquisition mode: required runtime library for first metadata-store implementation, hidden behind repository interfaces.
- Exclusion: no SQLAlchemy ORM object becomes canonical semantic truth. Core contracts do not import persistence models.
- SQLite control: do not rely on Python sqlite3 legacy transaction defaults. The connection configuration SHALL use explicit modern transaction control and transaction-bound compare/currentness operations. Schema/state tests must prove rollback/atomicity.
- Concurrency/currentness: updates that can make an artifact/decision current SHALL compare the expected `semantic_revision`/intent digest inside the same database transaction; late results may be recorded historically but cannot advance current state after the compare fails.
- Replacement: repository interfaces permit later PostgreSQL/another metadata store without changing semantic objects.
- AIMAGE-owned tests: transaction rollback, concurrent/stale currentness compare, foreign-key enforcement, repository round-trip, provider payload non-leakage, replacement repository contract suite.

Evidence:

- https://pypi.org/project/SQLAlchemy/2.0.52/
- https://docs.sqlalchemy.org/en/20/dialects/sqlite.html

No blocking `UNRESOLVED` item. Lack of Trusted Publishing is recorded supply-chain evidence, not hidden.

### 3.5 `alembic==1.19.2` — PASS WITH CONTROLS

- Identity/currentness: official Alembic 1.19.2, released 2026-09-04.
- License: MIT.
- Distribution: official PyPI / SQLAlchemy project.
- Supply-chain note: reviewed PyPI files are not marked Trusted Publishing; bind future artifacts by official hash/lock and repeat security check before install.
- Functional fit: relational metadata-schema migrations for SQLAlchemy/SQLite.
- Exclusion: Alembic is not the semantic-contract migration authority. Pydantic/document `schema_version` migration remains explicit AIMAGE code.
- Autogenerate is advisory only; every migration revision is reviewed and checked in. SQLite batch/reflection edge cases mean autogenerated output SHALL NOT be accepted as correctness proof.
- Replacement: migration history is confined to persistence implementation; semantic contracts remain portable.
- AIMAGE-owned tests: empty->head migration, prior fixture->head migration, downgrade only where explicitly supported, idempotent startup/version check, SQLite constraints after migration, semantic-document compatibility after DB migration.

Evidence:

- https://pypi.org/project/alembic/1.19.2/
- https://alembic.sqlalchemy.org/

No blocking `UNRESOLVED` item.

### 3.6 `pytest==9.1.1` — DEV PASS WITH WATCH

- Identity/currentness: official pytest 9.1.1, latest on PyPI at review, released 2026-06-19.
- License: MIT.
- Provenance: PyPI Trusted Publishing for the reviewed wheel.
- Functional fit: test runner only; not production runtime.
- Known exclusion/risk: current upstream issue reports include collection/performance regressions for some large/plugin-heavy suites. The initial AIMAGE suite is small and does not rely on that shape, so this is nonblocking but becomes a pin/review trigger if observed.
- Replacement: tests SHOULD use normal assertions/fixtures and minimize pytest-only custom plugin coupling.
- AIMAGE-owned tests: this is the runner for the inventory below; package itself is not trusted as proof of application correctness.

Evidence:

- https://pypi.org/project/pytest/9.1.1/
- https://github.com/pytest-dev/pytest

No blocking `UNRESOLVED` item.

### 3.7 `pytest-asyncio==1.4.0` — DEV PASS WITH WATCH

- Identity/currentness: official pytest-asyncio 1.4.0, released 2026-05-26.
- License: Apache-2.0.
- Provenance: PyPI Trusted Publishing.
- Functional fit: deterministic asyncio tests for provider/orchestrator boundaries.
- Exclusion: first slice uses the normal asyncio loop; it does not depend on custom loop-factory behavior where current upstream issues exist.
- Replacement: async core code remains ordinary `asyncio`; tests can move to another runner/plugin if required.

Evidence:

- https://pypi.org/project/pytest-asyncio/1.4.0/
- https://github.com/pytest-dev/pytest-asyncio

No blocking `UNRESOLVED` item.

### 3.8 Not selected as first-slice dependencies

- **Diffusers**: remains optional. Current Hugging Face installation guidance and underlying PyTorch platform/interpreter support have enough platform-specific coupling that its exact version/environment deserves a separate Gate-B pass when local execution becomes a real requirement. It MUST NOT constrain the core CPython environment now; a later Diffusers provider may use an isolated environment/service if needed.
- **ComfyUI**: remains optional external service; no package/source vendoring or runtime dependency now.
- **constraint solver/Cassowary implementation**: no measured need in the first slice; qualitative spatial relations and explicit frames are represented directly. Reopen only with a failing deterministic constraint case.
- **Pillow/fsspec/object-store SDK**: no first-slice requirement. Artifact bytes can be content-addressed/stored with stdlib; add media/object-store libraries only when an actual decoding/cloud-store requirement appears.
- **OSGi/SHACL/OPA/JML/LLVM/MLIR/GeoSPARQL/Temporal/BPMN runtimes**: remain method/reference evidence only.

## 4. Proposed repository/module layout

Implementation is not created in this slice. The authorized implementation slice should create the following shape unless fresh evidence forces a bounded replan:

```text
src/aimage/
  contracts/
    common.py
    visual_intent.py
    spatial.py
    validation.py
    render.py
    requirements.py
    resolution.py
    execution.py
    codec/
      json_codec.py
      migrations.py
  engine/
    compile.py
    capabilities.py
    resolve.py
    lower.py
    lifecycle.py
    repair.py
    validation_service.py
    currentness.py
    interfaces/
      provider.py
      artifact_store.py
      metadata_repository.py
      validator.py
  persistence/
    sqlite/
      schema.py
      repository.py
      transactions.py
    artifact_fs.py
  providers/
    openai/
      adapter.py
      capability.py
      lowering.py
      errors.py
  features/
    composition/
      profile.py
      validation.py
  app/
    use_cases.py

migrations/
  versions/

tests/
  contract/
  unit/
  integration/
  provider_contract/
  migration/
  fixtures/
```

Boundary rules:

1. `contracts/visual_intent.py` owns the typed representation of `VisualIntentState`, but the runtime instance/revision remains the sole semantic SSoT; storage/provider objects never replace it.
2. `contracts/render.py`, `requirements.py`, `resolution.py`, `execution.py` and `validation.py` represent immutable derived/evidence records.
3. `engine/*` may depend on contract interfaces; `providers/*`, `persistence/*`, and `features/*` depend on engine interfaces.
4. `engine/*` SHALL NOT import OpenAI/SQLAlchemy/Alembic/feature implementation modules.
5. provider request JSON, provider image IDs, request IDs and raw responses live only behind provider/run evidence surfaces.
6. human waits and durable resume are lifecycle/orchestration concerns. `ExecutionPlan` itself remains bounded, acyclic, attempt-local data.
7. Continuity/Handoff imports no provider implementation and owns no engine semantic type definitions.

## 5. Concrete type/schema mapping

All durable semantic/derived documents use the common identity envelope already accepted in `plans/SEMANTIC_CONTRACTS.md`.

### 5.1 Canonical semantic state

`VisualIntentStateModel`

- immutable persisted revision document;
- `job_id`, `semantic_revision`, `schema_version`, intent/authority/reference/baseline/disposition bindings, spatial/domain references;
- only explicit semantic decisions can create the next revision;
- persistence supplies atomic storage/current pointer, not semantic precedence.

### 5.2 Derived execution/evidence types

- `RenderSpecModel` — frozen compiled semantic view; exact source revision + intent digest;
- `RequirementSetModel` — frozen execution requirements;
- `ProviderCapabilityDescriptorModel` — frozen, time/version/evidence-sensitive observation;
- `ResolutionResultModel` — frozen legal strategy or explicit unsatisfied/stale result;
- `ExecutionPlanModel` — frozen bounded DAG, one attempt only;
- `MutationFrameModel` — frozen allowed/preserved paths for an attempt;
- `ValidationReportModel` — frozen artifact/revision/evaluator-bound evidence;
- `ArtifactRecordModel` / `RunRecordModel` — artifact lineage and actual execution evidence;
- `DecisionRecordModel`, `BaselineRecordModel`, `ArtifactDispositionRecordModel` — revision-bound controlled decision records.

Pydantic configuration SHALL reject unexpected fields for core contract versions by default unless an explicitly versioned extension namespace permits them. Unknown mandatory semantics never disappear through permissive deserialization.

## 6. Persistence layout

### 6.1 Metadata SQLite

Use relational headers for identity/currentness and validated JSON documents for contract payloads so persistence does not create a duplicate object model.

Minimum tables:

```text
jobs
  job_id PK
  current_semantic_revision
  current_intent_digest
  lifecycle_state
  accepted_artifact_id?
  updated_at

semantic_documents
  object_id PK
  job_id
  semantic_revision
  schema_version
  intent_digest
  payload_json
  created_at
  UNIQUE(job_id, semantic_revision)

derived_documents
  object_id PK
  contract_type
  job_id
  source_semantic_revision
  source_intent_digest
  schema_version
  payload_json
  created_at

capability_descriptors
  descriptor_id PK
  descriptor_digest UNIQUE
  target_id
  adapter_id
  adapter_version
  target_model_version
  evidence_kind
  evidence_uri
  observed_at
  payload_json

decisions
  decision_id PK
  job_id
  base_semantic_revision
  kind
  subject_ref
  resulting_semantic_revision?
  payload_json

baselines
  baseline_id PK
  job_id
  approved_at_revision
  approval_decision_id UNIQUE
  status
  payload_json

artifact_dispositions
  artifact_ref
  semantic_revision
  status
  basis_decision_id?
  payload_json
  PRIMARY KEY(artifact_ref, semantic_revision, status)

runs
  run_id PK
  job_id
  source_semantic_revision
  source_intent_digest
  execution_plan_ref
  capability_descriptor_ref
  target_model_version
  provider_request_id?
  status
  attempt_index
  normalized_error_class?
  raw_provider_evidence_json?
  usage_cost_latency_json?
  started_at
  finished_at?

artifacts
  artifact_id PK
  content_digest UNIQUE
  producing_run_ref
  source_semantic_revision
  blob_key
  media_metadata_json
  created_at

validation_reports
  report_id PK
  artifact_ref
  semantic_revision
  render_spec_ref
  execution_plan_ref
  overall_outcome
  evaluator_identity
  evaluator_version?
  evidence_class
  evaluator_provenance_json
  calibration_ref?
  correlation_note?
  payload_json
  created_at
```

`derived_documents` may contain only accepted immutable contract types. Provider-native payloads SHALL NOT be placed there merely for convenience; those stay under `runs.raw_provider_evidence_json` or external evidence blobs.

### 6.2 Currentness transaction

Any transition that could change the current/accepted artifact or apply a decision SHALL execute a compare-and-advance transaction conceptually equivalent to:

```text
expected revision/digest == jobs.current_semantic_revision/current_intent_digest
AND decision.base_semantic_revision == expected revision
AND artifact/report.source_semantic_revision == expected revision
```

If the comparison fails:

- preserve the late run/artifact/report as immutable historical evidence;
- do not update `jobs.accepted_artifact_id`, baseline, current semantic revision, or disposition to accepted;
- return an explicit stale/currentness failure to orchestration.

This is the implementation currentness fence; wall-clock completion order is never authority.

### 6.3 Artifact store

Initial `LocalArtifactStore` uses stdlib only:

- compute SHA-256 while writing;
- write to a temporary path;
- flush/close and atomically rename into a content-addressed key such as `sha256/<prefix>/<digest>`;
- treat digest as immutable content identity;
- store only blob key/digest/media metadata in SQLite;
- provider IDs are never blob identity.

`ArtifactStore` protocol exposes put/open/exists/metadata-delete-policy operations needed by engine use cases. Future S3/object storage implements the same protocol; no `fsspec` dependency is justified yet.

## 7. Compiler/resolver/lowering behavior

### 7.1 Fail-closed compilation

`compile_render_spec()` returns an explicit success/error result. It SHALL NOT produce an executable `RenderSpec` when any of the following is unresolved:

- contradictory equal-precedence mandatory intent;
- mandatory spatial relation missing its required explicit/inherited frame;
- invalid baseline scope/reference;
- unknown mandatory schema/extension semantic;
- preservation obligations that cannot be represented in the compiled contract.

Preferred/advisory conflicts may produce recorded diagnostics but cannot erase mandatory semantics.

### 7.2 Requirement derivation

`derive_requirements()` maps each effective mandatory semantic/preservation obligation to one or more `CapabilityRequirement`s with source semantic paths. Every mandatory path has traceability into resolution/lowering or the result is illegal.

### 7.3 Capability matching

Resolver matching key includes, when material:

- exact adapter/provider;
- exact model/target version;
- operation;
- accepted input types/count/role applicability;
- image/output constraints actually relied on;
- evidence kind/currentness;
- known limits;
- compatibility with preservation obligations.

A capability-name string match alone is never sufficient.

### 7.4 Resolution

- returns `resolved`, `unsatisfied`, or `stale_capabilities`;
- every mandatory requirement must be wired to compatible capability evidence;
- legal composite strategies are permitted but remain small and bounded;
- first OpenAI slice uses a single provider target for generation/editing;
- synthetic contract tests still cover bounded composite strategy so the architecture does not regress to single-provider-only semantics.

### 7.5 ExecutionPlan bound

`ExecutionPlan` is a finite DAG generated for **one execution attempt**.

The implementation SHALL impose structural bounds (acyclic graph validation and an explicit maximum-step policy/configuration). It does not contain:

- human approval waits;
- durable resume;
- retry loops;
- repair loops;
- open-ended dynamic branching.

Those live in `engine/lifecycle.py` / `engine/repair.py`, where every new retry/repair creates a new attempt-local plan.

### 7.6 Lowering trace

Every mandatory semantic path records:

`semantic path -> requirement -> execution step -> representation -> fidelity`.

`not_representable` on mandatory semantics fails lowering. `within_declared_tolerance` is permitted only if the source semantic explicitly grants that tolerance.

## 8. First thin OpenAI vertical slice

The first implementation target is intentionally small but genuinely end-to-end.

### V0 — OneShot generate

1. create `VisualIntentState(rev1)` from a simple generation request;
2. compile immutable `RenderSpec(rev1)`;
3. derive `RequirementSet(generate_image=mandatory)`;
4. resolve against the exact fresh OpenAI capability descriptor;
5. pre-execution descriptor freshness/compatibility check;
6. lower to one OpenAI generation step;
7. record `RunRecord(started)`;
8. call the provider with SDK retries disabled and explicit timeout;
9. store returned bytes through `ArtifactStore`, create `ArtifactRecord`, finish `RunRecord` with actual request/model/provider evidence;
10. create a lightweight `ValidationReport` covering deterministic contract/currentness/provenance checks;
11. keep one-shot user experience free of composition/approval ceremony unless the intent actually requests it.

### V1 — composition-sensitive baseline

1. `VisualIntentState` includes composition/camera/spatial obligations;
2. include an explicit `SpatialProfile` containing a viewer entity plus a `viewer_deictic` relation;
3. compile and render a composition candidate;
4. user approves composition only; persist revision-bound `DecisionRecord` and `BaselineRecord` limited to composition/camera/spatial paths;
5. identity/style/lighting/expression remain free unless separately locked.

Human approval is a lifecycle transition, **not** an `ExecutionPlan` step.

### V2 — viewer-relative distinction

Contract tests and the slice use at least these semantically different facts:

```text
right_of(subject, viewer, frame=viewer_deictic)
```

versus a literal output placement such as a `screen_image` right-region relation.

Compiler/validator SHALL preserve frame identity. Adapter prompt/request text may choose a provider-appropriate representation, but it cannot rewrite `viewer_deictic` into `screen_image`, or infer `front-right` from `right_of(viewer)`.

### V3 — minimal-delta edit/repair

1. validation identifies one failing target path while approved composition paths remain good;
2. build `MutationFrame(mutable=[failed target], preserve=[approved baseline paths])`;
3. derive edit/preservation requirements;
4. resolve against a fresh exact OpenAI edit capability descriptor;
5. lower baseline/reference image and edit instruction into provider-native input;
6. execute as a new attempt and produce a new artifact/run;
7. validate the **final externally visible artifact** for both the target correction and all preserved dimensions;
8. only an explicit valid decision can accept/supersede artifacts.

The OpenAI request/image IDs are execution evidence. They never become the source of the baseline or mutation frame.

### V4 — provider failure/reroute/unsatisfied

Classify provider failures at the adapter boundary:

- retry-eligible transient transport/timeout/rate/service class;
- authentication/permission/quota/configuration class;
- invalid/user-correctable request class;
- target/capability drift class;
- unknown provider failure.

Rules:

- SDK performs no hidden retries;
- lifecycle retry only when policy permits and budget remains;
- target/capability drift refreshes descriptor and re-resolves;
- unchanged invalid requests are not blindly retried;
- no fallback may silently weaken mandatory intent;
- if no legal strategy remains, return explicit `unsatisfied`/bounded failure.

The first production candidate need not implement another provider merely to prove rerouting; resolver/provider-contract fixtures use a fake alternate adapter, and a real provider replacement is later validated by S14/Gate D.

## 9. Bounded repair policy

Repair remains orchestration policy, not semantic authority.

Each repair attempt stores:

- source semantic revision/digest;
- source artifact + validation report;
- `MutationFrame`;
- attempt index;
- execution plan;
- resulting artifact/report;
- observed mandatory failures/regressions;
- usage/cost/latency evidence.

Required controls:

1. configurable hard attempt and/or spend boundary; no infinite automatic repair;
2. preserve best-known non-regressed artifact rather than newest artifact;
3. detect non-improvement/oscillation using repeated failure-dimension/signature + no strict evidence improvement across attempts;
4. do not invent a total aesthetic score. Prefer a partial order: an artifact is strictly better only when it removes at least one material failure without adding a mandatory/preserved regression; incomparable candidates do not silently displace the current best;
5. when budget expires, oscillation appears, or candidates are incomparable after the bounded policy, escalate to user/reopen/rerender rather than widening the mutation frame automatically.

## 10. Validation-oracle policy

Every material validation result records:

- evaluator identity;
- evaluator version/configuration when applicable;
- evidence class (`deterministic`, `human`, `model_assisted`, `provider_feedback`, etc.);
- evidence references/provenance;
- known evaluator correlation with generator/provider where material;
- calibration reference or explicit `not_calibrated` state when quantitative claims would otherwise be implied.

First slice strategy:

- deterministic checks cover schema/currentness/traceability/digest/linkage;
- the composition baseline is established by explicit human approval;
- visual preservation/failure checks may be human/manual fixtures initially;
- provider/generator self-report is **not** treated as independent evidence for mandatory visual correctness;
- a future automated visual evaluator requires its own Gate-B/validation evidence before it can auto-accept a mandatory rule.

Mandatory unevaluable checks yield `indeterminate`, never pass by omission.

## 11. Capability freshness/drift fence

Resolution records descriptor identity/digest. Immediately before provider execution:

1. compare the plan's descriptor identity to adapter/provider configuration and freshness policy;
2. if a material capability/model/configuration changed, do not execute the stale plan;
3. refresh capability evidence;
4. re-run requirement resolution;
5. execute only a newly legal plan or terminate with explicit bounded failure.

Runtime provider failure indicating capability drift triggers the same path; it never mutates intent.

## 12. Test inventory and traceability

Minimum implementation test IDs:

| Test | Obligation/failure class | Prior evidence |
|---|---|---|
| `T01_revision_traceability` | every derived object carries exact source revision/digest | semantic invariant; S03/S05/S08 |
| `T02_decision_idempotent` | duplicate DecisionRecord is idempotent | tabletop repair; S13 |
| `T03_stale_late_decision_rejected` | stale/late approval cannot overwrite current | tabletop repair; S13; red-team currentness |
| `T04_baseline_reopen_required` | approved paths change only through reopen/supersede | S01 |
| `T05_rejected_artifact_non_resurrection` | rejected/newer artifact cannot become current by recency/resume | tabletop repair; S12 |
| `T06_reference_role_separation` | replacing identity ref leaves style/composition bindings untouched | S05 |
| `T07_viewer_deictic_not_screen_image` | explicit reference-frame distinction survives compile/lowering | S15 |
| `T08_contradictory_mandatory_fail_closed` | no executable RenderSpec from unresolved mandatory conflict | red-team obligation 1 |
| `T09_unknown_mandatory_schema_fail_safe` | unknown mandatory semantic/version not discarded | S09; RT schema attack |
| `T10_mandatory_capability_unsatisfied` | no silent weakening if mandatory capability absent | S06 |
| `T11_composite_strategy_bounded` | resolver permits legal small DAG; plan rejects cycles/oversize | S07; obligation 6 |
| `T12_lowering_semantic_loss_rejected` | mandatory `not_representable` fails lowering | S06/S07 |
| `T13_validation_tri_state` | mandatory unevaluable -> indeterminate, not pass | tabletop repair |
| `T14_mutation_frame_enforced` | only mutable paths may change | S04 |
| `T15_repair_preservation_regression` | final repaired artifact rechecks preserved dimensions | S04; obligation 7 |
| `T16_old_inflight_result_currentness_fence` | rev N late result cannot advance rev N+1 job | obligation 2; R6 |
| `T17_capability_applicability` | target/model/version/input/limits/evidence all participate in matching | obligation 3 |
| `T18_capability_drift_before_execute` | stale descriptor causes refresh/re-resolution/failure | obligation 8 |
| `T19_validation_false_pass_defense` | provider self-report/correlated uncalibrated evidence cannot satisfy independent mandatory policy | obligation 4 |
| `T20_repair_termination` | non-improvement/oscillation/budget terminates and preserves best-known artifact | obligation 5 |
| `T21_sqlite_atomic_currentness` | state advance is conditional/transactional; rollback leaves no partial acceptance | obligation 2 |
| `T22_artifact_blob_digest_identity` | provider ID cannot replace content digest/artifact ID | S11/provider-independence |
| `T23_provider_adapter_replacement_contract` | fake adapter swap preserves same core intent/contracts | S03/S14 |
| `T24_dependency_repository_replacement` | in-memory repository and SQLite repository satisfy same contract | S14 |
| `T25_schema_migration_roundtrip` | old supported representation migrates without semantic change | S09 |
| `T26_provider_failure_no_intent_mutation` | retry/reroute/unsatisfied leaves VisualIntentState unchanged | S03/S06/S10 |
| `T27_openai_hidden_retry_disabled` | adapter client configuration proves SDK retry count is zero | bounded-repair/cost policy |
| `T28_final_composite_artifact_regression` | final externally-visible artifact is checked after all steps | obligation 7 |
| `T29_one_shot_no_ceremony` | S00 path does not require baseline/red-team/repair stages | S00 |
| `T30_live_openai_generate_smoke` | separately authorized credentialed provider reproduction | Gate B provider empirical check |
| `T31_live_openai_edit_smoke` | separately authorized credentialed edit reproduction | S04 / provider Gate B |

Scenario coverage summary:

- S00 -> T29 + V0;
- S01/S02 -> T04/T14 + V1;
- S03/S10/S14 -> T23/T26;
- S04 -> T14/T15/T20/T31;
- S05 -> T06;
- S06 -> T10/T12/T26;
- S07 -> T11/T28;
- S08 -> T01/T05/T16;
- S09 -> T09/T25;
- S11 -> T22;
- S12 -> T05;
- S13 -> T02/T03;
- S15 viewer-relative tabletop -> T07;
- eight retained adversarial obligations -> T08, T16, T17, T19, T20, T11, T15/T28, T18.

## 13. Stop/go, rollback/fallback and replacement

### Go from planning to a separately authorized implementation slice only if

- this plan and its audit are accepted on fresh authority;
- every selected dependency/provider row remains Gate-B nonblocking;
- implementation user authorization is explicit.

### Stop/replan during implementation entry if

- package/provider identity/currentness materially moved and new Gate-B evidence is blocking;
- Python/runtime choice creates a real contract/leakage problem;
- the selected OpenAI model/API no longer exposes the mandatory generation/edit capability used by the slice;
- a dependency license/security/supply-chain fact becomes blocking;
- a new concurrent implementation effort changes ownership/order.

### Rollback/fallback

- provider failure rolls back only execution attempt state; semantic intent remains intact;
- DB transaction failure leaves no partially accepted/current artifact;
- blob write is content-addressed and only linked after successful metadata commit/reconciliation policy;
- provider fallback requires legal re-resolution against the same RequirementSet;
- no legal target -> explicit unsatisfied, never intent weakening;
- metadata store can fall back to a test/in-memory repository for tests, not as hidden production authority;
- optional Diffusers/ComfyUI absence cannot block the first core path.

### Replacement boundaries

- OpenAI SDK/provider -> `ProviderAdapter` + `ProviderCapabilityDescriptor` contract;
- Pydantic -> contract codec/validation boundary + JSON-schema/round-trip tests;
- SQLAlchemy/SQLite -> `MetadataRepository` contract;
- Alembic -> persistence migration mechanism only;
- local filesystem -> `ArtifactStore` contract;
- pytest plugins -> test harness only.

## 14. Explicit deferred empirical checks

These do not alter architecture and therefore do not keep planning open:

- credentialed OpenAI generation/edit smoke against the exact selected target;
- future lockfile/transitive dependency vulnerability review and hash verification before install;
- actual SQLite concurrency/load limits beyond first local single-process requirements;
- quantitative automated visual-evaluator calibration;
- exact Diffusers/PyTorch environment/version if local execution becomes a selected capability;
- solver selection only if a deterministic spatial case demonstrates need.

Any failed check may block or replan its affected integration, but none justifies broad semantic-architecture redesign in advance.

## 15. Planning completion claim

This plan is decision-complete only together with:

- `audits/IMPLEMENTATION_PLAN_RED_TEAM_2026-09-10.md` returning `PASS` or `PASS_AFTER_REPAIR`;
- `audits/IMPLEMENTATION_PLAN_INDEPENDENT_AUDIT_2026-09-10.md` finding no fresh authority conflict or architecture boundary inversion;
- continuity status recording the result.

Even after those conditions pass, **production implementation remains unauthorized until a separate user-authorized implementation slice**.
