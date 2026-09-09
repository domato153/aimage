# AIMAGE Implementation-Plan Bounded Red-Team Audit — 2026-09-10

Status: planning/design adversarial audit of `plans/IMPLEMENTATION_PLAN_2026-09-10.md`. No production code, dependency installation, lockfile mutation, provider execution, or source import occurred.

## 1. Verdict

**PASS_AFTER_REPAIR**

The runtime/dependency/module/schema/test/OpenAI-slice plan survives the bounded R1-R6 challenge after four material drafting risks were repaired in the final plan:

1. hidden SDK retry/timeout behavior was moved under explicit AIMAGE attempt policy;
2. SQLite legacy transaction behavior was fenced by explicit modern transaction/currentness semantics;
3. optional Diffusers runtime coupling was removed from the core dependency decision;
4. validation evidence was hardened so provider/generator self-report or an uncalibrated correlated evaluator cannot silently satisfy mandatory correctness.

No new semantic subsystem, workflow engine, solver, validator framework, storage abstraction package, or second semantic authority is justified.

Retained provider/dependency empirical checks are implementation-time risks, not unresolved architecture decisions.

## 2. Scope and attack method

Applied `plans/BOUNDED_RED_TEAM_ASSURANCE.md` lenses:

- R1 top-event / authority;
- R2 component/interface failure;
- R3 control-action/timing;
- R4 evidence/oracle;
- R5 tradeoff/complexity;
- R6 replacement/resume.

Top undesired outcomes challenged:

1. provider/library convenience becomes semantic authority;
2. an apparently legal plan silently drops mandatory intent or preservation obligations;
3. stale execution becomes current;
4. retry/repair becomes unbounded or cost-hidden;
5. provider capability/evaluator evidence produces a false legal/pass result;
6. persistence/migration/replacement makes old or provider-specific state canonical;
7. correctness machinery destroys S00 one-shot simplicity.

Decision-sufficiency, not attack count, is the stop criterion.

## 3. Attack record

### IPRT-01 — SDK retries hide attempts and cost

- `lens`: R3, R5
- `top_event_or_failure`: one AIMAGE execution attempt produces multiple provider calls without the engine recording them as separate attempts.
- `preconditions`: use the official OpenAI SDK defaults; transient 408/409/429/5xx/connection failure occurs.
- `attack_sequence`: AIMAGE starts one plan -> SDK internally retries -> multiple billable/observable calls occur -> AIMAGE's repair/retry budget still sees one attempt.
- `expected_bad_outcome`: bounded-repair and cost/latency controls become false; provider side effects/request IDs are under-counted.
- `existing_defense before repair`: generic bounded-repair requirement only.
- `finding_class`: `REPAIR_BEFORE_ADOPTION`.
- `required_repair_or_test`: final plan requires `max_retries=0`, explicit finite timeout, lifecycle-owned retry eligibility/budget, raw request-id evidence, and `T27_openai_hidden_retry_disabled`.
- `residual_risk`: provider-side behavior may still be nondeterministic, but every AIMAGE-initiated call is explicit and budgeted.
- `verdict_after_retest`: **PASS**.

### IPRT-02 — SQLite legacy transaction semantics weaken currentness fence

- `lens`: R2, R3, R6
- `top_event_or_failure`: late/stale decision or artifact is partially persisted/current because transaction boundaries are not what the application assumes.
- `preconditions`: default sqlite3 legacy transaction behavior; currentness check and acceptance update span operations that are not safely atomic under assumed semantics.
- `attack_sequence`: read current revision -> concurrent/new revision advances -> late result writes acceptance/current pointer under a loose transaction assumption.
- `expected_bad_outcome`: old in-flight result becomes current or a crash leaves partial acceptance metadata.
- `existing_defense before repair`: semantic revision fields and stale-decision rules.
- `finding_class`: `REPAIR_BEFORE_ADOPTION`.
- `required_repair_or_test`: explicit non-legacy transaction control; compare-and-advance of expected revision/digest and acceptance state in the same transaction; late evidence remains historical; `T21_sqlite_atomic_currentness` plus rollback tests.
- `residual_risk`: SQLite write-concurrency limits may constrain scale, but do not change correctness ownership for the first local slice.
- `verdict_after_retest`: **PASS**.

### IPRT-03 — optional Diffusers constrains the core runtime

- `lens`: R5, R6
- `top_event_or_failure`: a future optional local-provider package dictates the core interpreter/platform and turns an optional backend into architectural coupling.
- `preconditions`: choose Python partly for Diffusers, then require Diffusers/PyTorch to share the core environment on every platform.
- `attack_sequence`: local-provider dependency has platform/interpreter/model constraints -> core runtime is downgraded or frozen -> hosted-provider-only deployments inherit unnecessary heavy dependencies.
- `expected_bad_outcome`: optional capability becomes required and replacement/modifiability degrade.
- `existing_defense before repair`: Diffusers already classified optional in accepted reuse plan.
- `finding_class`: `REPAIR_BEFORE_ADOPTION`.
- `required_repair_or_test`: final plan explicitly excludes Diffusers from the first dependency set; future Diffusers Gate B may choose a separate environment/service boundary; core CPython version is not selected by Diffusers.
- `residual_risk`: a future in-process local adapter may require a narrower runtime, which will be an isolated Gate-B/replacement decision.
- `verdict_after_retest`: **PASS**.

### IPRT-04 — correlated validation oracle false-pass

- `lens`: R4
- `top_event_or_failure`: an output is accepted because the same provider/model family that generated it reports it as correct.
- `preconditions`: model-assisted or provider feedback is treated as independent mandatory evidence.
- `attack_sequence`: generator produces semantic error -> correlated evaluator repeats/endorses generation -> validation marks pass -> artifact accepted.
- `expected_bad_outcome`: mandatory visual constraint receives false independent proof.
- `existing_defense before repair`: tri-state validation and evaluator classes.
- `finding_class`: `REPAIR_BEFORE_ADOPTION`.
- `required_repair_or_test`: first slice uses deterministic schema/currentness/provenance checks + explicit human composition approval; evaluator identity/version/provenance/evidence class/correlation/calibration fields are stored; provider self-report is not independent proof by default; `T19_validation_false_pass_defense`.
- `residual_risk`: automated visual validation accuracy is still empirical and remains a later evaluator-specific Gate-B/calibration task.
- `verdict_after_retest`: **PASS**.

### IPRT-05 — official capability declaration is stale at execution time

- `lens`: R4, R6
- `top_event_or_failure`: planning evidence says the model can edit, but the actual configured target/capability changes after resolution.
- `preconditions`: descriptor created from official documentation or prior reproduction; provider state changes before execution.
- `attack_sequence`: resolve legal plan -> descriptor/model/config changes -> execute stale lowering.
- `expected_bad_outcome`: illegal provider call or silent fallback.
- `existing_defense`: version-sensitive descriptor and accepted capability-drift obligation.
- `finding_class`: `DEFERRED_IMPLEMENTATION_RISK` with required runtime fence.
- `required_repair_or_test`: exact model snapshot/evidence/digest in descriptor; pre-execution freshness compatibility check; re-resolution or explicit bounded failure; `T18_capability_drift_before_execute`; credentialed T30/T31 before production integration.
- `residual_risk`: live service behavior can change; it is intentionally handled as runtime evidence rather than semantic truth.
- `verdict_after_retest`: **PASS for planning**.

### IPRT-06 — provider snapshot/config leaks into semantic SSoT

- `lens`: R1, R2, R6
- `top_event_or_failure`: `gpt-image-2.5-sunburst-2026-09-08` becomes part of canonical user intent and prevents provider replacement.
- `preconditions`: adapter configuration persisted in `VisualIntentState` or baseline.
- `attack_sequence`: first provider works -> model ID copied into core semantic path -> replacement provider cannot satisfy model-specific semantic value.
- `expected_bad_outcome`: provider-native state becomes authority.
- `existing_defense`: accepted provider-independence rule.
- `finding_class`: `REJECTED_ATTACK` after inspection of the final layout.
- `required_repair_or_test`: none beyond planned storage separation; model/version lives in capability descriptor/run evidence only. `T23_provider_adapter_replacement_contract` guards it.
- `residual_risk`: implementation convenience could violate this later, so contract tests remain mandatory.
- `verdict_after_retest`: **PASS**.

### IPRT-07 — Pydantic model becomes a second semantic authority

- `lens`: R1, R2, R6
- `top_event_or_failure`: library defaults/validators silently invent semantic precedence or migration meaning.
- `preconditions`: treat generated schema/model defaults as canonical product semantics.
- `attack_sequence`: version changes or permissive parsing accepts/drops a field -> normalized model differs semantically -> persistence promotes it.
- `expected_bad_outcome`: schema library decides user intent.
- `existing_defense`: final plan makes Pydantic a contract codec/validator only; explicit `schema_version`; AIMAGE migration functions; unknown mandatory fail-safe.
- `finding_class`: `REJECTED_ATTACK` because the proposed boundary already blocks it.
- `required_repair_or_test`: T09/T25 plus schema/round-trip tests.
- `residual_risk`: future validators/defaults must be reviewed as semantic code, not accepted from library behavior automatically.
- `verdict_after_retest`: **PASS**.

### IPRT-08 — Alembic autogenerate silently changes semantic storage meaning

- `lens`: R2, R6
- `top_event_or_failure`: autogenerated DB migration drops/changes constraints or makes an old semantic document unreadable.
- `preconditions`: accept autogenerate output as authoritative migration.
- `attack_sequence`: model diff -> generated migration -> SQLite reflection/batch edge case -> semantic metadata corrupted or constraint lost.
- `expected_bad_outcome`: migration changes meaning without explicit review.
- `existing_defense`: final plan treats Alembic migration as persistence-only and autogenerate as advisory; migrations are reviewed and tested end-to-end.
- `finding_class`: `DEFERRED_IMPLEMENTATION_RISK`, bounded by tests.
- `required_repair_or_test`: migration fixtures, constraints-after-migration, semantic-document compatibility; T25.
- `residual_risk`: future schema complexity may reveal Alembic/SQLite limitations and trigger metadata-store replan.
- `verdict_after_retest`: **PASS for planning**.

### IPRT-09 — repair oscillates while every individual attempt is legal

- `lens`: R5
- `top_event_or_failure`: expression/identity repairs alternate indefinitely or newest candidate replaces a less-regressed artifact.
- `preconditions`: valid MutationFrames but no progress/stop ordering.
- `attack_sequence`: A fixes target/regresses preserve -> B fixes preserve/regresses target -> loop.
- `expected_bad_outcome`: unbounded cost and destruction of best-known good work.
- `existing_defense`: final plan uses hard budget, failure-signature/non-improvement detection, partial-order improvement, best-known retention, escalation.
- `finding_class`: `REJECTED_ATTACK` after plan hardening.
- `required_repair_or_test`: T20 plus T15.
- `residual_risk`: visual candidates can be incomparable; policy deliberately escalates instead of inventing a scalar quality score.
- `verdict_after_retest`: **PASS**.

### IPRT-10 — composite ExecutionPlan grows into durable workflow engine

- `lens`: R5
- `top_event_or_failure`: DAG support accumulates waits/retries/repair/resume loops.
- `preconditions`: implementation puts orchestration inside `ExecutionPlan` for convenience.
- `attack_sequence`: add branch -> add retry -> add human wait -> persist plan as workflow state.
- `expected_bad_outcome`: second workflow engine and authority confusion.
- `existing_defense`: final plan requires finite acyclic max-step plan for one attempt; all waits/retries/repair/resume are lifecycle/orchestration owned.
- `finding_class`: `REJECTED_ATTACK` after boundary inspection.
- `required_repair_or_test`: T11 structural graph bounds.
- `residual_risk`: materially richer future orchestration must reopen the generic orchestration decision rather than extending the plan ad hoc.
- `verdict_after_retest`: **PASS**.

### IPRT-11 — final compositor/edit step regresses a locked dimension

- `lens`: R2, R4
- `top_event_or_failure`: each intermediate step passes but final externally-visible artifact violates baseline.
- `preconditions`: validation is run only after provider generation, not after complete strategy.
- `attack_sequence`: generation passes composition -> later edit/composition changes crop/geometry -> final artifact escapes revalidation.
- `expected_bad_outcome`: accepted final artifact violates preservation obligation.
- `existing_defense`: final plan requires final-artifact validation after complete strategy and repair.
- `finding_class`: `REJECTED_ATTACK` after inspection.
- `required_repair_or_test`: T28/T15.
- `residual_risk`: evaluator adequacy remains evidence-specific.
- `verdict_after_retest`: **PASS**.

### IPRT-12 — late provider result resurrects rejected/stale state

- `lens`: R1, R3, R6
- `top_event_or_failure`: old render completes after new revision and is accepted because it is newest.
- `preconditions`: in-flight rev N while user advances to rev N+1.
- `attack_sequence`: rev N starts -> rev N+1 becomes current -> rev N completes last -> naive `latest` pointer advances.
- `expected_bad_outcome`: stale artifact becomes current.
- `existing_defense`: transaction-bound expected revision/digest compare; disposition/DecisionRecord currentness; late evidence persists historical only.
- `finding_class`: `REJECTED_ATTACK` after IPRT-02 repair.
- `required_repair_or_test`: T16/T21.
- `residual_risk`: external blob may exist before metadata reconciliation; blob existence alone has no acceptance semantics.
- `verdict_after_retest`: **PASS**.

### IPRT-13 — supply-chain metadata is mistaken for safety proof

- `lens`: R4, R6
- `top_event_or_failure`: Trusted Publishing or official PyPI status is treated as proof that a dependency version is vulnerability-free.
- `preconditions`: acquisition audit stops at provenance.
- `attack_sequence`: authentic package has vulnerable transitive version -> provenance verifies authenticity only -> integration proceeds without lock scan.
- `expected_bad_outcome`: known vulnerable dependency enters implementation.
- `existing_defense`: Gate B separates provenance from security/currentness; future exact lock must receive vulnerability/transitive review before installation/adoption.
- `finding_class`: `DEFERRED_IMPLEMENTATION_RISK`.
- `required_repair_or_test`: implementation-entry lock/hash/advisory review; if blocking, stop before install/adoption.
- `residual_risk`: vulnerability databases can lag; normal dependency-update/security process remains necessary.
- `verdict_after_retest`: **PASS for planning**.

### IPRT-14 — correctness machinery forces ceremony onto OneShot

- `lens`: R5
- `top_event_or_failure`: simple generation must create baselines, repair policy, red-team evidence, human gates and composite plans before execution.
- `preconditions`: implement all logical capabilities as mandatory user-visible stages.
- `attack_sequence`: S00 request enters general engine -> every optional gate runs.
- `expected_bad_outcome`: accepted one-shot simplicity invariant violated.
- `existing_defense`: V0/T29 explicitly permits one generation plan + lightweight deterministic validation with no irrelevant baseline/approval/red-team ceremony.
- `finding_class`: `REJECTED_ATTACK`.
- `required_repair_or_test`: T29.
- `residual_risk`: default profile configuration must not accidentally mark irrelevant validation/baseline steps mandatory.
- `verdict_after_retest`: **PASS**.

## 4. Affected-lens rerun after repairs

Only the lenses changed by material repairs were rerun.

### R3 timing/control rerun

- hidden provider retries: blocked by SDK `max_retries=0` + lifecycle-owned retry budget;
- stale currentness: blocked by transaction-bound expected revision/digest comparison;
- old in-flight result remains historical.

Result: **PASS**.

### R4 evidence/oracle rerun

- provider capability descriptor is evidence-classed and version/digest bound;
- planning documentation is `declared`, not misreported as reproduced;
- mandatory visual acceptance cannot treat provider self-report as independent proof;
- mandatory unevaluable validation stays indeterminate.

Result: **PASS**.

### R5 complexity/tradeoff rerun

- repair is budgeted and stops on non-improvement/oscillation;
- `ExecutionPlan` is acyclic, attempt-local, structurally bounded;
- S00 remains ceremony-light;
- solver/blob framework/extra image library were not added without measured need.

Result: **PASS**.

### R6 replacement/resume rerun

- Diffusers/ComfyUI are absent from the required first path;
- provider/model identity remains descriptor/run evidence only;
- metadata/artifact/provider/schema/test implementations have replacement boundaries;
- stale in-flight execution cannot cross the semantic-revision fence.

Result: **PASS**.

No materially new failure class appeared on rerun, so the bounded red-team stops here.

## 5. Eight mandatory obligation closure

1. Fail-closed semantic compilation -> plan 7.1 + T08: **closed**.
2. Currentness fence -> plan 6.2 + T16/T21: **closed**.
3. Conditional capability matching -> plan 7.3 + T17: **closed**.
4. Validation-oracle defense -> plan 10 + T19: **closed**.
5. Bounded repair -> plan 9 + T20: **closed**.
6. Bounded composite execution -> plan 7.5 + T11: **closed**.
7. Final-artifact regression validation -> plan V3/12 + T15/T28: **closed**.
8. Capability-drift race -> plan 11 + T18: **closed**.

## 6. Remaining nonblocking implementation-time risks

These are explicit empirical checks, not architecture gaps:

- credentialed OpenAI generation/edit reproduction against the selected model snapshot;
- exact future lock/transitive vulnerability and hash review;
- measured SQLite concurrency/scale limit;
- future automated visual-evaluator calibration/correlation evidence;
- future Diffusers/PyTorch exact environment if local provider is selected;
- constraint solver only if a failing deterministic constraint case appears.

If any becomes blocking, stop/replan its affected integration rather than weakening semantic requirements.

## 7. Final bounded verdict

`PASS_AFTER_REPAIR`

The plan is ready for an independent fresh repository/architecture audit. This verdict is **not** implementation authorization and is **not** final Gate-D/system PASS.
