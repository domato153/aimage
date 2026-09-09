# AIMAGE Current Repository-Work Continuity

Status: repository-work continuity locator for the **completed concrete implementation-planning candidate**. The candidate has passed its bounded red-team and independent repository/architecture audit. It remains planning evidence only and does **not** authorize production implementation.

## 1. Authority / locator status

- Repository: `domato153/aimage`
- Authoritative branch: `main`
- Current factual `main` HEAD: **resolve fresh at receiver start**; this file must not encode its own eventual publication SHA as currentness authority.
- Governing entrypoint: `AGENTS.md`
- Continuity method: `governance/CONTINUITY.md`
- Repository-work profile: `governance/continuity/REPOSITORY_WORK.md`
- Architecture boundary: `architecture/BOUNDARIES.md`
- Accepted semantic contracts: `plans/SEMANTIC_CONTRACTS.md`
- External acquisition/integration plan: `plans/EXTERNAL_REUSE_PLAN.md`
- Base assurance plan: `plans/REUSE_AND_INTEGRATION_ASSURANCE.md`
- Bounded adversarial assurance: `plans/BOUNDED_RED_TEAM_ASSURANCE.md`
- Historical implementation-planning handoff packet:
  - immutable commit: `ecfeef00d830d65e9235832adf05b1c21d2bfc16`
  - path: `governance/continuity/handoffs/IMPLEMENTATION_PLANNING_NEXT_THREAD_2026-09-10.md`

Current candidate planning result:

- `plans/IMPLEMENTATION_PLAN_2026-09-10.md`
- `audits/IMPLEMENTATION_PLAN_RED_TEAM_2026-09-10.md`
- `audits/IMPLEMENTATION_PLAN_INDEPENDENT_AUDIT_2026-09-10.md`

Earlier accepted evidence remains:

- `audits/SEMANTIC_CONTRACT_TABLETOP_2026-09-10.md` — `PASS AFTER DESIGN REPAIR`;
- `audits/BOUNDED_PLAN_RED_TEAM_2026-09-10.md` — `PASS AFTER ASSURANCE HARDENING`;
- `audits/HANDOFF_CROSS_METHOD_AUDIT_2026-09-10.md` — handoff continuity review.

Fresh repository/platform state always governs current facts. Historical construction SHAs in handoffs/audits are provenance, not aliases for current `main`.

## 2. Current phase and authorization

Phase: **planning / design / research only — concrete implementation planning complete in this candidate**.

Production implementation remains **NOT AUTHORIZED** by this document, by the completed plan, or by the planning audits.

This candidate contains only planning/continuity/audit changes. It does not contain:

- production Image Engine code;
- provider adapter implementation;
- dependency installation;
- lockfile mutation;
- external source import/copy;
- live provider production integration;
- final Gate-D runtime V&V.

If this candidate is adopted into `main`, the next possible production work is a **separate, explicit user-authorized implementation slice**. Without that authorization, stop after fresh reconciliation.

## 3. Accepted foundation preserved by the candidate

The implementation plan does not reopen the accepted semantic architecture:

- Continuity/Handoff remains separate from Image Engine product semantics;
- product dependency direction remains `features/domain capabilities -> engine interfaces`;
- trivial OneShot remains ceremony-light;
- AIMAGE does not build a custom image-edit renderer;
- OpenAI official SDK/API remains the first hosted-provider direction;
- Diffusers remains optional local-provider direction;
- ComfyUI remains optional external backend/service direction;
- `VisualIntentState` remains the sole semantic SSoT;
- `RenderSpec`, `RequirementSet`, `ResolutionResult`, `ExecutionPlan`, `MutationFrame`, provider-native payloads/IDs/graphs, artifacts/runs and `ValidationReport` remain derived/execution/evidence state;
- validation remains separate from mutation/enforcement;
- provider-native state cannot become semantic authority;
- `ExecutionPlan` remains bounded, attempt-local and acyclic;
- final Gate-D integrated runtime V&V has not happened and no final system PASS is claimed.

## 4. Concrete implementation-plan decisions

Planning baseline selected in `plans/IMPLEMENTATION_PLAN_2026-09-10.md`:

- runtime: **CPython 3.13** baseline, with future 3.14 CI compatibility target;
- schema/validation: **Pydantic 2.13.5**;
- metadata persistence: **SQLite via SQLAlchemy 2.0.52 Core** with explicit transaction/currentness control;
- DB migration: **Alembic 1.19.2**, human-reviewed migrations only;
- blob/artifact storage: AIMAGE `ArtifactStore` interface + initial stdlib content-addressed local filesystem implementation;
- hosted provider SDK: **OpenAI Python SDK 3.11.0**;
- first capability target: **`gpt-image-2.5-sunburst-2026-09-08`**, descriptor/run evidence only;
- tests: **pytest 9.1.1 + pytest-asyncio 1.4.0**;
- first-slice solver: none;
- Diffusers/ComfyUI: not required dependencies for the first core path.

Version values are planning baselines, not permission to install. A separately authorized implementation slice must fresh-check affected Gate-B evidence before acquiring dependencies.

## 5. Gate-B status

No selected dependency/provider integration has a blocking `UNRESOLVED` item in the planning evidence.

Key controls preserved:

- OpenAI SDK automatic retries are disabled in the planned adapter (`max_retries=0`); timeout/retry budgets are AIMAGE-owned;
- provider capability evidence records exact target/model/version/applicability/evidence and has a pre-execution freshness fence;
- provider model/request/image IDs stay below semantic authority;
- Pydantic is a contract codec/validator, not semantic or migration authority;
- SQLite currentness transitions compare expected semantic revision/digest atomically in explicit transactions;
- SQLAlchemy/Alembic provenance limitations are recorded and require future exact hash/lock/security review rather than being hidden;
- Alembic autogenerate is advisory, not migration correctness authority;
- future automated visual evaluators require their own evidence/provenance/correlation/calibration policy before mandatory auto-acceptance.

Deferred empirical checks that remain nonblocking for architecture:

- credentialed OpenAI generation/edit smoke for the exact selected target;
- future exact lock/transitive vulnerability + artifact-hash review before install;
- measured SQLite concurrency/scale;
- automated visual-evaluator calibration;
- future optional Diffusers/PyTorch environment if selected;
- solver selection only if a concrete deterministic spatial case demonstrates need.

A failed deferred check blocks/replans its affected integration before production adoption; it never permits silent semantic weakening.

## 6. First OpenAI vertical slice planned

The plan covers one thin but real end-to-end path:

1. OneShot generation without irrelevant ceremony;
2. composition-sensitive intent;
3. scoped composition approval and baseline;
4. viewer-relative spatial placement;
5. explicit `viewer_deictic` versus `screen_image` distinction;
6. fail-closed RenderSpec compilation;
7. RequirementSet derivation and exact capability resolution;
8. OpenAI lowering/execution behind an adapter;
9. artifact/blob + RunRecord linkage;
10. immutable tri-state ValidationReport;
11. explicit provider retry/reroute/unsatisfied behavior without intent mutation;
12. minimal-delta repair through a MutationFrame;
13. regression validation on the final externally-visible artifact.

Human approval, repair loops and durable resume remain lifecycle/orchestration concerns rather than `ExecutionPlan` steps.

## 7. Eight adversarial obligations and test closure

All eight retained hardening obligations are represented in the implementation plan and test inventory:

1. fail-closed semantic compilation;
2. currentness fence for old in-flight work;
3. conditional capability matching;
4. validation-oracle provenance/correlation/calibration defense;
5. bounded repair with non-improvement/oscillation stop and best-known retention;
6. bounded acyclic attempt-local composite execution;
7. final-artifact preservation regression validation;
8. capability-drift race freshness/re-resolution fence.

The inventory also preserves the four tabletop repairs: composite strategy, revision-bound idempotent decisions, explicit artifact disposition, and tri-state validation; viewer-relative S15 is traced explicitly.

## 8. Planning assurance verdicts

- implementation-plan bounded red-team: **`PASS_AFTER_REPAIR`**;
- affected R3/R4/R5/R6 lens rerun: **PASS**;
- independent fresh repository/architecture audit: **PASS**;
- fresh authority drift during the audit: none observed;
- overlapping open PR during the audit before candidate publication: none observed.

Material drafting repairs were limited to policy/boundary/test hardening; no new semantic subsystem was introduced.

## 9. Recoverability

Decision-relevant state for future continuation is **DURABLE** in repository artifacts listed in section 1.

Do not assume:

- hidden previous-chat state;
- local-only uncommitted files;
- provider-session-only state;
- cache-only evidence;
- previous worker machine state.

A future receiver fresh-reads `main`, `AGENTS.md`, Continuity/CURRENT, the accepted plan/audits if adopted, and current provider/dependency evidence before action.

## 10. Exact next bounded action / stop point

**Current stop point: implementation planning is complete; production implementation remains stopped.**

There is no automatically authorized production action after this plan.

If and only if the user separately authorizes implementation after adoption, the next bounded slice is the first thin CPython/OpenAI vertical implementation defined by `plans/IMPLEMENTATION_PLAN_2026-09-10.md`, beginning with fresh authority + Gate-B refresh and ending at its explicitly bounded implementation/test scope.

Replan instead if fresh authority, concurrent work, package/provider security/currentness, capability reproduction, or architecture evidence invalidates a material assumption.
