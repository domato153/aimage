# AIMAGE Current Repository-Work Continuity

Status: first bounded CPython/OpenAI vertical-slice implementation is active on draft PR #18 after implementation planning was merged to `main` via PR #17.

## 1. Authority / locator status

- Repository: `domato153/aimage`
- Authoritative branch: `main`
- Current implementation branch: `aimage-stage/first-openai-vertical-slice`
- Current implementation PR: `#18` (`Implement first AIMAGE OpenAI vertical slice`), draft until implementation acceptance gates close.
- Governing entrypoint: `AGENTS.md`
- Continuity method: `governance/CONTINUITY.md`
- Repository-work profile: `governance/continuity/REPOSITORY_WORK.md`
- Architecture boundary: `architecture/BOUNDARIES.md`
- Accepted semantic contracts: `plans/SEMANTIC_CONTRACTS.md`
- Accepted implementation plan: `plans/IMPLEMENTATION_PLAN_2026-09-10.md`
- External acquisition/integration plan: `plans/EXTERNAL_REUSE_PLAN.md`
- Base assurance plan: `plans/REUSE_AND_INTEGRATION_ASSURANCE.md`
- Bounded adversarial assurance: `plans/BOUNDED_RED_TEAM_ASSURANCE.md`

Fresh repository/platform state always governs current facts. Historical construction SHAs in handoffs/audits are provenance, not aliases for current `main` or PR head.

## 2. Current phase and authorization

Phase: **first bounded production implementation slice authorized and in progress**.

User authorization occurred after PR #17 was merged. The authorized scope is the first thin CPython/OpenAI vertical implementation defined by `plans/IMPLEMENTATION_PLAN_2026-09-10.md`.

This authorization does not expand scope to Diffusers, ComfyUI, a custom renderer/editor, a constraint solver, broad semantic redesign, or final Gate-D/system PASS.

## 3. Implemented candidate state

The draft implementation candidate contains:

- provider-neutral semantic contract models with `VisualIntentState` as sole semantic SSoT;
- fail-closed semantic compilation and explicit spatial frame preservation;
- RequirementSet derivation, exact capability resolution, evidence/freshness/drift fences, and bounded acyclic execution planning;
- OpenAI adapter/lowering isolated under `providers/openai/` with hidden SDK retries disabled and explicit timeout ownership;
- content-addressed blob storage separated from AIMAGE artifact identity;
- SQLite metadata/currentness transaction fences and immutable historical records;
- revision-bound/idempotent composition approval, baseline reopen, reference replacement, and rejected-artifact non-resurrection rules;
- bounded repair/oscillation termination and final-artifact preservation regression requirements;
- tri-state validation plus correlated-oracle calibration/provenance fences;
- provider failure/run evidence persistence;
- contract/unit/integration/provider-contract regression tests;
- exact-dependency evidence tooling and GitHub Actions validation workflow.

## 4. Gate-B dependency evidence

A GitHub-hosted evidence run completed exact dry-run resolution for CPython 3.13.15 with pip 26.2.1 on Linux x64 and Windows x64.

Recorded evidence:

- workflow run: `34410634058`;
- Linux: 25 exact resolved packages, OSV active vulnerabilities reported: 0;
- Windows: 26 exact resolved packages, OSV active vulnerabilities reported: 0;
- Windows-only `colorama==0.4.6` license metadata gap was manually closed against the PyPI project license (BSD 3-Clause);
- exact wheel SHA-256 values are recorded in platform locks;
- evidence document: `governance/evidence/GATE_B_DEPENDENCY_EVIDENCE_2026-09-10.md`;
- Linux lock: `requirements-lock/linux-cp313.txt`;
- Windows lock: `requirements-lock/windows-cp313.txt`.

The workflow uses GitHub-owned `actions/setup-python` immutable release `v7.0.0`, pinned to commit `5fda3b95a4ea91299a34e894583c3862153e4b97`.

## 5. Current acceptance gate

The next validation run must reproduce the lock candidate byte-for-byte, install only exact reviewed wheels via `--only-binary=:all: --require-hashes`, and run the full pytest suite on Linux and Windows.

On Linux it also executes `tools/openai_smoke.py`. That probe is a no-op with an explicit SKIPPED evidence line if `OPENAI_API_KEY` is not configured; if the secret exists it performs exactly one generation and one edit against `gpt-image-2.5-sunburst-2026-09-08`, with SDK retries disabled, and records request IDs rather than image bytes.

Provider capability remains `declared_official_documentation` / not reproduced until that credentialed smoke succeeds. Normal engine execution requires reproduced capability evidence and therefore cannot silently use the declared-only descriptor.

## 6. Exact stop / next action

Do not merge PR #18 yet.

Immediate next action: run the lock-verified install/test workflow from the current implementation branch, inspect both platform results, repair any implementation regressions, and account for the credentialed Sunburst smoke result.

After tests pass, update the implementation evidence and PR status. Only mark PR #18 ready for review/merge when all required non-credential gates pass and the provider reproduction state is truthfully accounted for; do not claim live-provider PASS if the secret is absent.

Final Gate-D integrated runtime V&V remains out of scope and has not been run.
