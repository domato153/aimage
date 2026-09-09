# AIMAGE Reuse and Integration Assurance Plan

Status: planning/design assurance contract for external capability selection, integration design review, and eventual end-to-end workflow validation. It does not authorize implementation, dependency installation, provider integration, or production execution.

## 1. Purpose

AIMAGE must not lose requirements while adopting external standards, libraries, services, methods, or schemas. It also must not declare the completed architecture sound merely because each component looked reasonable in isolation.

This plan therefore defines three distinct assurance layers:

1. **capability coverage audit** — prove every material AIMAGE requirement is either satisfied by external reuse, intentionally adapted, or retained as the smallest justified AIMAGE semantic residue;
2. **external acquisition due diligence** — prove every adopted/adapted component has a bounded, licensed, current, replaceable and testable integration boundary;
3. **integrated workflow validation** — after the design/implementation exists, simulate representative and adversarial end-to-end jobs and verify requirement/state/interaction coverage before treating the workflow as complete.

## 2. External assurance basis

The assurance logic is adapted from established practices rather than invented as an AIMAGE-only checklist.

### Software/component acquisition and provenance

- NIST Secure Software Development Framework (SSDF) SP 800-218: third-party software should be selected against explicit requirements and verified proportionally before use.
  - https://csrc.nist.gov/pubs/sp/800/218/final
- NIST Cybersecurity Supply Chain Risk Management publications: use due diligence and explicit supply-chain risk decisions for acquired components.
  - https://csrc.nist.gov/Projects/cyber-supply-chain-risk-management/publications
- SLSA provenance: record resolved dependency identity rather than only a floating project name.
  - https://slsa.dev/spec/v1.2/
- SPDX 3.0.1: use standardized license/component metadata concepts for software-bill/provenance records.
  - https://spdx.github.io/spdx-spec/
- OpenSSF Scorecard: use automated project-security/maintenance signals as evidence, not as an automatic acceptance score.
  - https://openssf.org/projects/scorecard/

### Architecture evaluation

- SEI Architecture Tradeoff Analysis Method (ATAM): evaluate architecture using concrete quality-attribute scenarios, risks, sensitivity points and tradeoffs before implementation hardens the design.
  - https://www.sei.cmu.edu/library/architecture-tradeoff-analysis-method-atam/
  - https://www.sei.cmu.edu/library/atam-method-for-architecture-evaluation/

### Verification, validation and integration

- NASA Systems Engineering Handbook V&V guidance: distinguish verification from validation, maintain requirements-to-verification traceability, use analysis/inspection/demonstration/testing, and explicitly validate the fully integrated system.
  - https://www.nasa.gov/reference/system-engineering-handbook-appendix/
- NIST combinatorial testing: interaction failures often require combinations of factors; use covering combinations rather than only happy-path examples.
  - https://www.nist.gov/publications/combinatorial-testing
  - https://csrc.nist.gov/projects/automated-combinatorial-testing-for-software/combinatorial-methods-in-testing/interactions-involved-in-software-failures
- W3C SCXML: use explicit state/transition/event/history semantics as a reference for state-transition coverage.
  - https://www.w3.org/TR/scxml/

These sources are methodological evidence. They do not become AIMAGE authority or mandatory runtime dependencies.

## 3. Evidence labels

Every material reuse decision should use one of these evidence states:

- `DIRECT` — confirmed in an official specification, primary documentation, exact source/license, or reproduced behavior;
- `CORROBORATED` — supported by more than one independent mature source or implementation but not a normative guarantee;
- `DESIGN_INFERENCE` — architecture judgment derived from confirmed evidence;
- `DEFERRED_IMPLEMENTATION_CHECK` — design boundary is settled, but language/version/source-file selection is intentionally deferred until implementation makes it meaningful;
- `UNRESOLVED` — evidence is insufficient; this is blocking if the item controls architecture, license, authority, or replacement behavior.

A planning row must not be treated as implementation-ready while it has a blocking `UNRESOLVED` item.

## 4. Gate A — capability coverage audit

Apply this gate to every materially `DESIGN`, partial-`DESIGN`, or AIMAGE-owned semantic claim.

### A1. Requirement decomposition

For each capability record:

- original AIMAGE capability name;
- concrete user-visible requirement/failure class it serves;
- abstract problem independent of AIMAGE terminology;
- dimensions that are generic engineering mechanics versus AIMAGE visual/domain semantics;
- explicit non-goals.

### A2. Cross-domain discovery

Search the mature field corresponding to the abstract problem. Record:

- fields searched;
- standards/specifications;
- mature maintained implementations;
- established industry methods;
- relevant technical/academic literature when useful;
- proprietary systems only as reference evidence when they add a missing pattern.

Do not count a search as complete because no project uses AIMAGE's exact vocabulary.

### A3. Reuse ladder

Evaluate in this order:

1. direct `ADOPT`;
2. `ADAPT` an external schema/method/interface;
3. interoperability at the edge;
4. compose multiple mature primitives;
5. `ADAPT + small AIMAGE extension`;
6. only then retain `DESIGN`.

For a retained `DESIGN`, record why each preceding level fails and identify the smallest exact semantic residue.

### A4. Existence-value test

For every AIMAGE-owned semantic ask:

> What user-visible or cross-provider control is lost if AIMAGE uses the mature external primitives directly and does not own this semantic?

If the answer is only naming, wrapper convenience, preferred storage shape, duplicate metadata or internal implementation taste, remove the native semantic.

### A5. Coverage closure

The capability audit passes only if:

- every material requirement maps to at least one accepted mechanism or explicit retained residue;
- every accepted external mechanism maps back to a named requirement/use case;
- there are no orphan dependencies brought in merely because they are useful or popular;
- no `DESIGN` row lacks negative evidence against adoption/adaptation/composition;
- no external representation becomes canonical AIMAGE job authority merely for convenience.

## 5. Gate B — external acquisition due diligence

Run this gate before any dependency install, code import, bundled service, schema copy or production adapter work.

### B1. Exact identity

- exact upstream project/standard/provider;
- official distribution channel;
- version/tag/ref and immutable commit/digest where applicable;
- exact selected files/artifacts for any source/schema copy;
- currentness check date;
- authoritative upstream documentation URL.

### B2. Functional fit

- exact AIMAGE requirement satisfied;
- supported operations and known exclusions;
- whether behavior is guaranteed by specification or only observed;
- reproduction/contract test needed before relying on advertised behavior;
- failure/degradation behavior when the capability is absent.

### B3. License and distribution

- repository/package/file license identified;
- compatibility with intended AIMAGE distribution;
- attribution/notice requirements;
- model/checkpoint/content licenses tracked separately from framework/library licenses;
- process-boundary assumptions documented for external GPL services;
- no noncommercial/restricted source copied into a permissive core without explicit decision.

### B4. Supply-chain and maintenance risk

- active maintenance or stable-standard status;
- known-vulnerability review appropriate to the dependency;
- OpenSSF Scorecard or equivalent signals for material OSS dependencies where useful;
- release/signing/provenance information where available;
- transitive dependencies understood proportionally;
- abandonment/replacement plan.

### B5. Architectural coupling

- acquisition mode selected;
- runtime required/optional/reference-only;
- AIMAGE adapter/owner boundary;
- provider/domain data prevented from leaking into generic core;
- canonical state owner explicit;
- upgrade/migration surface explicit;
- replacement/fallback path explicit.

### B6. Validation obligation

- AIMAGE-owned contract tests defined;
- upstream tests are not treated as proof of AIMAGE integration correctness;
- fixtures/simulators identified where live-provider testing is expensive or nondeterministic;
- version-sensitive behavior has a regression trigger;
- provenance entry can identify exactly what was tested.

A candidate failing a material B-gate item is not implementation-ready even if its capability classification remains `ADOPT` or `ADAPT`.

## 6. Gate C — architecture scenario audit

Before treating the external-reuse architecture as final, perform a lightweight ATAM-style scenario audit against at least these quality attributes:

- modifiability/replacement;
- provider independence;
- correctness/preservation;
- recoverability;
- simplicity for one-shot use;
- observability/provenance;
- cost/latency control;
- license/distribution safety;
- testability;
- extensibility without core/domain inversion.

For each scenario record stimulus, environment, expected architectural response, affected components, risks, sensitivity points and tradeoffs.

Minimum architecture scenarios:

1. replace the first cloud provider without changing job authority or approval semantics;
2. provider lacks one requested capability and routing must fall back or fail explicitly;
3. optional ComfyUI/Diffusers backend is absent;
4. a provider changes or deprecates a request field;
5. user requests a trivial one-shot image and no production ceremony should be forced;
6. a long-running job pauses for human approval and resumes after context/process restart;
7. a repair changes only the failed variable while preserving locked dimensions;
8. an external asset/provenance system is unavailable while local AIMAGE identity remains valid;
9. a persisted schema is upgraded and old jobs must be read/migrated safely;
10. a candidate dependency becomes unmaintained or license-incompatible;
11. text/layout must be deterministic even when the image provider is poor at text;
12. a domain plugin introduces new QA semantics without importing itself into engine core.

Any scenario revealing an unbounded provider-specific leak, unrecoverable canonical state, no replacement path, or contradictory ownership is architecture-blocking.

## 7. Gate D — integrated end-to-end workflow validation

This gate is executed after a coherent implementation exists. The plan is defined now so the architecture is designed to be testable.

### D1. Requirements verification matrix

Maintain a bidirectional matrix:

`requirement / failure class -> owning semantic -> implementation surface -> verification method -> scenario(s) -> result/evidence`

Every acceptance goal in `plans/WORKFLOW_TARGET.md` must have at least one verification scenario. Every scenario must map back to one or more requirements.

Use multiple verification methods where appropriate:

- `INSPECTION` — schema/record/ownership/provenance review;
- `ANALYSIS` — state/constraint/lineage/tradeoff evaluation;
- `DEMONSTRATION` — operator-visible workflow behavior;
- `TEST` — automated or reproducible execution.

### D2. Canonical workflow simulations

At minimum simulate:

- `S00 OneShot` — direct generation with no unnecessary workflow stages;
- `S01 CompositionSensitive` — explore distinct directions, establish geometry, approve, render;
- `S02 UserBlockingAuthority` — user supplies/replaces a blocking sketch and approves only its structural role;
- `S03 CrossProviderReroute` — reroute the same accepted intent to a different capability set without silently changing authority;
- `S04 MinimalDeltaRepair` — one variable fails, successful dimensions lock, provider-native edit executes, re-review detects regression;
- `S05 ReferenceRoleSeparation` — identity/style/composition references are independent and one replacement does not mutate the others;
- `S06 CapabilityFallback` — required feature absent, deterministic fallback/escalation or explicit unsatisfied-plan result;
- `S07 TextLayout` — exact text/layout uses deterministic layout primitives where required rather than repeated whole-image rerolls;
- `S08 CrossContextResume` — handoff/continuity recovers approved artifacts, locks, active failure and one next action;
- `S09 SchemaMigration` — prior persisted job/config remains readable or follows an explicit migration path;
- `S10 BackendUnavailable` — optional external service disappears without corrupting AIMAGE state;
- `S11 ProvenanceExport` — internal lineage remains valid and optional C2PA/export provenance can be emitted without becoming internal authority;
- `S12 RejectedArtifact` — rejected/superseded candidate cannot silently become current after resume/retry;
- `S13 DuplicateOrLateApproval` — duplicate/late approval input is idempotent or explicitly rejected;
- `S14 DependencyReplacement` — substitute an external component behind the same boundary and prove unchanged AIMAGE semantics.

### D3. State-transition coverage

Inspired by explicit statechart semantics, cover:

- every legal transition at least once;
- every approval/rejection/reopen branch;
- pause/resume/history restoration paths;
- retry versus user-correctable failure distinction;
- repair loop exit and escalation;
- finalization only after valid approval;
- illegal/stale transition rejection.

The purpose is semantic coverage, not adoption of SCXML as AIMAGE's storage format.

### D4. Interaction/combinatorial coverage

Use pairwise or stronger covering arrays for interacting factors where exhaustive Cartesian testing is impractical. Candidate factors include:

- provider/backend;
- generation versus edit;
- reference count and role combination;
- geometry lock present/absent;
- human approval state;
- requested capability set;
- persistence/resume state;
- failure class;
- fallback available/unavailable;
- output text/layout requirement;
- domain profile.

Increase interaction strength for combinations that history or risk analysis identifies as failure-prone. Do not rely only on a few hand-authored happy paths.

### D5. Fault and regression injection

Inject or simulate at least:

- provider timeout/error/rate limit;
- capability report drift;
- missing optional backend;
- stale provider conversation/image identifier;
- missing/changed external artifact while digest identity is known;
- schema-version mismatch;
- failed edit that regresses a locked dimension;
- duplicated event/approval;
- corrupted or incompatible external workflow artifact;
- dependency version change across a previously passing fixture.

The expected outcome must be explicit fallback, bounded failure, repair/escalation, or `STALE_REPLAN` where continuity is involved — never silent semantic degradation.

## 8. Final integrated audit verdict

After implementation and simulation, return exactly one architecture/workflow verdict:

- `PASS` — all material requirements, boundaries, scenarios and regression obligations close;
- `PASS_WITH_DEFERRED_NONBLOCKERS` — only explicitly non-blocking future capabilities remain and they cannot alter current correctness/authority;
- `FAIL_REPLAN` — a material requirement, boundary, reuse assumption, replacement path, license obligation or integrated scenario remains unresolved.

A successful component test suite alone is insufficient for `PASS`.

## 9. Records that must survive the planning slice

Before implementation begins, the accepted planning set should make it possible to answer without fresh invention:

- what is adopted, adapted, reference-only, optional, or AIMAGE-native;
- why each classification exists;
- exact acquisition mode and expected coupling;
- what is intentionally not copied or depended upon;
- what implementation-time check is still deferred and why that deferral does not change architecture;
- how each external component can be replaced;
- how the integrated workflow will later be verified and validated.
