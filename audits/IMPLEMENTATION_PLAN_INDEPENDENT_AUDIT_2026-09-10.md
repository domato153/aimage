# AIMAGE Concrete Implementation Plan — Independent Repository/Architecture Audit — 2026-09-10

Status: independent second-pass planning audit of `plans/IMPLEMENTATION_PLAN_2026-09-10.md` after the bounded implementation-plan red-team. No production implementation, dependency installation, lockfile mutation, source import, or live provider execution occurred.

## 1. Verdict

**PASS**

The final concrete implementation plan is consistent with fresh repository authority, preserves the accepted semantic ownership/boundaries, closes the required Gate-B planning evidence without a blocking `UNRESOLVED` item, covers the first thin OpenAI vertical slice and retained adversarial obligations, and does not expand the authorized phase.

This PASS is a planning/architecture audit only. It is not implementation authorization and not Gate-D/system PASS.

## 2. Fresh authority check

Fresh factual state at the audit pass:

- repository: `domato153/aimage`;
- authoritative branch: `main`;
- fresh `main` HEAD: `a7f6343cd1315cedf81fc68d77862125f17468be`;
- open PR discovery before candidate publication: none;
- implementation-related branch discovery: this bounded candidate plus the prior implementation-planning handoff publication branch; no separate runtime/OpenAI implementation work was found;
- fresh `architecture/BOUNDARIES.md` still requires `features/domain capabilities -> engine interfaces`, keeps Continuity/Handoff separate from Image Engine semantics, and treats adapter authority leakage as an architecture smell;
- fresh `governance/continuity/CURRENT.md` still authorizes implementation planning only and names exactly this class of plan/audit as the next bounded action;
- fresh `plans/SEMANTIC_CONTRACTS.md` still makes `VisualIntentState` the sole semantic SSoT and all provider/derived objects revision-bound/noncanonical.

No authority movement or concurrent work invalidated the planning action during the audit.

## 3. Semantic ownership audit

### Canonical state

Plan result:

- `VisualIntentStateModel` is a typed representation of `VisualIntentState`, not a replacement owner;
- a semantic revision is created only by explicit semantic decision/change;
- SQL storage provides durability/current-pointer mechanics only;
- Pydantic supplies validation/serialization only.

Verdict: **PASS** — no competing semantic SSoT.

### Derived state

Plan result:

- `RenderSpec`, `RequirementSet`, `ProviderCapabilityDescriptor`, `ResolutionResult`, `ExecutionPlan`, `MutationFrame`, and `ValidationReport` are immutable derived/evidence objects bound to source revision/digest;
- old derived objects remain historical and cannot become future-executable without compatibility/currentness checks.

Verdict: **PASS**.

### Provider-native state

Plan result:

- OpenAI model snapshot/API/SDK capability identity lives in capability descriptors and run evidence;
- provider payload/request/image/request IDs stay under adapter/run evidence;
- provider IDs never substitute for AIMAGE job/artifact/semantic identity;
- provider replacement consumes the same AIMAGE contract boundary.

Verdict: **PASS** — no provider-state authority leakage.

### Continuity/Handoff

Plan result:

- implementation layout does not move image-production semantics into Continuity/Handoff;
- no Continuity/Handoff code/runtime change is required by the plan;
- continuity may transport semantic identities but does not define them.

Verdict: **PASS**.

## 4. Dependency-direction audit

Proposed module dependency shape:

```text
features/* -> engine/interfaces/*
providers/* -> engine/interfaces/* + contracts/*
persistence/* -> engine/interfaces/* + contracts/codec edge
engine/* -> contracts/* + engine/interfaces/*
contracts/* -> no provider/feature implementation
```

The plan explicitly forbids engine core imports of OpenAI/SQLAlchemy/Alembic/feature implementations and keeps the composition feature under `features/composition`.

Verdict: **PASS** — no `features/domain -> core` inversion and no provider implementation in the semantic layer.

## 5. Runtime/dependency decision audit

### Runtime

CPython 3.13 is justified against the actual accepted needs:

- official typed/async OpenAI SDK support;
- direct JSON Schema 2020-12 contract generation through Pydantic;
- mature SQLite metadata/migration stack;
- optional future Diffusers without making it mandatory;
- ComfyUI remains external-service neutral.

Node/TypeScript remains a viable alternative, but selecting it would not materially improve the first slice and would create another runtime-schema/persistence selection surface while not improving provider neutrality.

Verdict: **PASS**.

### Minimum dependency set

Selected required runtime libraries are bounded to:

- Pydantic;
- SQLAlchemy;
- Alembic;
- official OpenAI SDK.

Selected dev/test libraries:

- pytest;
- pytest-asyncio.

Not selected without measured need:

- constraint solver;
- Diffusers/ComfyUI core runtime;
- image-processing framework;
- filesystem abstraction package;
- workflow engine;
- OSGi/SHACL/OPA/JML/LLVM/MLIR/etc. runtimes.

Verdict: **PASS** — no orphan dependency/overengineering.

## 6. Gate-B closure audit

| Integration | Identity/version policy | License/provenance | Fit/exclusions | Maintenance/supply chain | Coupling/replacement | AIMAGE tests | Blocking unresolved? |
|---|---|---|---|---|---|---|---|
| OpenAI SDK 3.11.0 | exact planning baseline, refresh before install | Apache-2.0; Trusted Publishing/attestation/hash recorded | typed async provider transport; hidden retry disabled | official maintained SDK; future exact-lock scan required | provider adapter only | lowering/error/retry/request-id/descriptor/smoke | No |
| OpenAI GPT-Image-2.5 Sunburst snapshot | exact dated capability target | provider service; official docs evidence | generation + editing officially declared; live reproduction deferred | capability evidence freshness fence | descriptor/run only; provider replaceable | credentialed generate/edit smoke before production integration | No |
| Pydantic 2.13.5 | exact planning baseline | MIT; Trusted Publishing/provenance | Draft 2020-12 validation/schema; not migration authority | active maintained; future lock scan | codec boundary | strict parse/schema/roundtrip/migration fail-safe | No |
| SQLAlchemy 2.0.52 | exact planning baseline | MIT; reviewed wheel not Trusted Publishing, hash binding required later | SQLite metadata only; no semantic ORM authority | active maintained; explicit supply-chain note | repository boundary | atomicity/currentness/roundtrip/replacement | No |
| Alembic 1.19.2 | exact planning baseline | MIT; reviewed PyPI artifact provenance limitation recorded | DB migration only; autogenerate advisory | active maintained; future hash/lock check | persistence migration only | migration fixtures/constraint preservation | No |
| pytest 9.1.1 | exact dev baseline | MIT; Trusted Publishing | test runner only; known large-suite regression watch | maintained | test harness only | entire inventory | No |
| pytest-asyncio 1.4.0 | exact dev baseline | Apache-2.0; Trusted Publishing | default asyncio-loop tests; custom-loop edge excluded | maintained | test-only | async provider/orchestration tests | No |

The only deferred items are evidence that cannot be truthfully produced before the separately authorized implementation environment exists: credentialed provider smoke, exact transitive lock scan, scale/calibration probes, and future optional-provider environments. They do not control semantic architecture and have explicit stop conditions before production adoption.

Verdict: **PASS** — no blocking `UNRESOLVED` acquisition item.

## 7. First vertical-slice audit

Required path versus plan:

1. OneShot generation -> V0: present.
2. Composition-sensitive intent -> V1: present.
3. Composition approval/baseline -> V1: explicit DecisionRecord/BaselineRecord, human wait outside ExecutionPlan.
4. Viewer-relative placement -> V1/V2: explicit viewer entity/frame.
5. `viewer_deictic` vs `screen_image` -> V2 + T07: explicit non-alias rule.
6. RenderSpec compilation -> V0 + 7.1: present, fail-closed.
7. RequirementSet + resolution -> V0 + 7.2-7.4: present.
8. OpenAI lowering/execution -> V0/V3/V4: present behind adapter.
9. artifact/run linkage -> V0 + persistence schema: present.
10. ValidationReport -> V0/V3 + validation policy: present.
11. provider failure/reroute/unsatisfied -> V4: explicit, no intent mutation.
12. minimal-delta repair -> V3 + bounded repair policy: present.
13. preservation regression -> V3 + T15/T28: final artifact revalidated.

Diffusers and ComfyUI are not required to prove the path.

Verdict: **PASS** — thin enough to implement incrementally but still genuinely end-to-end.

## 8. Eight adversarial obligations audit

| Obligation | Plan surface | Test evidence planned | Verdict |
|---|---|---|---|
| fail-closed semantic compilation | 7.1 | T08/T09 | PASS |
| currentness fence | 6.2 | T03/T16/T21 | PASS |
| conditional capability matching | 7.3 | T17 | PASS |
| validation-oracle defense | 10 | T19 | PASS |
| bounded repair | 9 | T20 | PASS |
| bounded composite execution | 7.5 | T11 | PASS |
| final-artifact regression | V3/12 | T15/T28 | PASS |
| capability-drift race | 11 | T18 | PASS |

The bounded red-team independently returned `PASS_AFTER_REPAIR`; the repaired surfaces are now represented in the plan and tests.

## 9. Prior tabletop repair preservation

The four prior tabletop repairs remain preserved:

- multi-target/composite legal strategy -> `ResolutionResult` + T11;
- revision-bound idempotent decisions -> T02/T03;
- explicit rejected/superseded artifact disposition -> T05;
- tri-state validation -> T13/T19.

Viewer-relative S15 remains explicit through T07.

Verdict: **PASS** — implementation planning did not regress prior design repairs.

## 10. Persistence/currentness audit

The SQLite plan avoids two common authority inversions:

1. relational/ORM rows do not define semantic precedence;
2. latest timestamp/provider completion does not define currentness.

Acceptance/current transitions compare expected semantic revision/digest inside one explicit transaction. Late runs/artifacts/reports remain immutable historical evidence when the compare fails.

Blob storage uses content digest/AIMAGE artifact identity rather than provider identifier.

Verdict: **PASS**.

## 11. Complexity/replacement audit

- OneShot has no mandatory baseline/red-team/repair ceremony: PASS.
- ExecutionPlan is bounded, acyclic and one-attempt only: PASS.
- Repair loops/human waits/resume stay lifecycle-owned: PASS.
- provider replacement boundary is explicit: PASS.
- metadata repository/blob store/schema codec/test harness each have replacement boundaries: PASS.
- optional backend absence does not corrupt core state: PASS.

No new generic framework is justified.

## 12. Phase-boundary audit

Observed changes are planning/audit documents only. The branch contains no production provider implementation, no dependency installation, no package/lockfile mutation, no external source copy, and no live provider integration.

A successful plan still requires a separate explicit user-authorized implementation slice.

Verdict: **PASS**.

## 13. Remaining uncertainty

Remaining uncertainty is restricted to implementation-time empirical evidence that does not change current architecture unless it fails:

- live OpenAI generation/edit smoke and actual capability evidence;
- exact future lock/transitive vulnerability scan;
- measured SQLite concurrency scale;
- automated visual-evaluator calibration;
- future optional Diffusers environment;
- solver only on demonstrated need.

These checks each have a stop/replan boundary and do not justify continuing broad research now.

## 14. Final decision

Fresh repository/architecture audit verdict: **PASS**.

The planning slice is decision-complete after continuity records this plan + red-team + audit and the candidate is published for review. Production implementation remains stopped.
