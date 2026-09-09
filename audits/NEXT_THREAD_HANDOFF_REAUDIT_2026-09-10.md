# AIMAGE Next-Thread Handoff Re-audit — 2026-09-10

Status: **PASS AFTER REPAIR REQUIRED**. The previous handoff captured the current reuse-first direction and provider-native repair decision, but a second cold-reader audit found that its research method was still too candidate-driven and could allow unnecessary AIMAGE-native design to survive.

This audit is about the next-thread planning handoff only. It does not reopen Continuity/Handoff infrastructure or authorize Image Engine implementation.

## 1. Audited authority

Construction authority checked against current accepted AIMAGE state at the start of this audit:

- repository: `domato153/aimage`
- authoritative branch: `main`
- accepted `main`: `09edfa4a0b0760640c11280f721aaaa475a6fb52`
- root router: `AGENTS.md`
- handoff method: `.agents/skills/handoff/SKILL.md`
- continuity: `governance/CONTINUITY.md`
- repository profile: `governance/continuity/REPOSITORY_WORK.md`
- current state: `governance/continuity/CURRENT.md`
- audited predecessor packet: `handoffs/2026-09-10_REUSE_MATRIX_REAUDIT_NEXT_THREAD.md`

Fresh authority always wins if these literals later move.

## 2. What the predecessor packet already got right

The predecessor packet correctly preserved:

- planning/design/research-only phase;
- reuse-first `ADOPT / ADAPT / DESIGN` policy;
- external providers remaining below AIMAGE-owned semantics;
- no provider/core implementation during the handoff slice;
- GPT Image/OpenAI targeted editing as provider capability rather than a reason to build an AIMAGE repair renderer;
- AIMAGE repair responsibility as failure diagnosis, preservation intent, capability selection, orchestration, and re-review;
- broader evidence targets including InvokeAI, OpenAssetIO, W3C PROV, OpenUSD, Temporal/equivalent workflow systems, capability negotiation, and provider-native editing;
- one bounded next action, expected transition, cold-start route, and stop/replan conditions;
- no decision-relevant chat-only/local artifact dependency.

Those decisions remain valid unless fresh evidence contradicts them.

## 3. Findings

### F-01 — research was still candidate-first rather than capability-first

**Severity: material.**

The predecessor packet named several strong candidates, but a receiver could satisfy it by checking those names and then return to AIMAGE-native design for anything they did not cover.

That is weaker than the user's actual rule:

> for every capability that appears to require AIMAGE design, first ask whether another mature field already solves the same abstract problem, even if that field has nothing to do with image generation.

#### Required repair

The successor handoff must require a **capability-first cross-domain search** for every materially retained `DESIGN` item.

The receiver should translate AIMAGE terminology into an abstract problem statement before searching. Examples:

- `RenderSpec` -> intermediate representation / compiler IR / execution plan / job specification;
- provider capability model -> plugin/driver/protocol feature negotiation;
- partial approval/lock -> layered override, policy/constraint, review-state, or selective locking systems;
- composition geometry -> scene graph, CAD/game transforms, UI/layout constraints, spatial relationship models;
- artifact identity/lineage -> DAM/MAM, version control, content-addressed storage, build provenance, data provenance;
- workflow state -> statecharts, BPMN/user tasks, durable workflows, event sourcing;
- repair planning -> diagnosis/planning, minimum-change repair, transaction compensation, or planner/executor separation.

Do not search only for exact AIMAGE vocabulary.

### F-02 — several mature adjacent-domain families were not explicitly in the discovery surface

**Severity: material.**

The predecessor named creative tools, VFX/DCC, provenance, durable workflow, and provider editing, but did not explicitly require review of several other mature problem domains that could reduce AIMAGE-native semantics.

The successor handoff should include, where relevant:

1. **compiler / IR / build-system architecture**
   - provider-neutral intent compiled into provider-specific execution;
   - validation, lowering, capability-dependent compilation, execution plans.
2. **statecharts / BPMN / durable workflow / event sourcing**
   - long-running state, human gates, pause/resume, transitions, retry, history.
3. **DAM/MAM / version control / content-addressed storage / supply-chain provenance**
   - artifact identity, immutable content identity, versions, derivation, publish/resolve boundaries.
4. **scene graphs / CAD / game transforms / UI constraint solvers and layout engines**
   - camera, transforms, relative positioning, constraints such as same-row/right-of/distance/alignment.
5. **plugin, driver, protocol, and hardware capability-negotiation systems**
   - feature discovery, optional capability sets, fallback, compatibility/version negotiation.
6. **policy, layered configuration, override, lock, and creative-review systems**
   - dimensional authority, selective lock/unlock, review/approval state, non-destructive overrides.
7. **schema evolution / configuration overlays / serialization ecosystems**
   - versioned contracts and persistence without inventing custom storage machinery.
8. **diagnosis/planning/executor separation and minimum-change repair patterns**
   - AIMAGE chooses a repair action; provider/tool executes it.
9. **content provenance standards such as C2PA when relevant to exported artifact provenance**
   - optional external provenance, distinct from internal workflow state.

These are discovery families, not mandatory dependencies.

### F-03 — retaining `DESIGN` had no explicit burden of proof

**Severity: material.**

The current matrix permits `DESIGN` when no suitable solution is found, but the handoff did not require a recorded negative result strong enough to distinguish “not found yet” from “genuinely AIMAGE-specific.”

#### Required repair

A materially retained `DESIGN` classification must state:

- the abstract problem being solved;
- adjacent fields/standards/implementations searched;
- best external candidates found;
- why `ADOPT`, `ADAPT`, or composition of multiple mature components does not adequately close the requirement;
- the smallest AIMAGE-specific semantic residue that remains.

“Nothing with the exact AIMAGE name exists” is not sufficient evidence for `DESIGN`.

### F-04 — composition of existing solutions was under-emphasized

**Severity: moderate.**

A capability need not map one-to-one to a single external project. AIMAGE may be able to compose a standard data model, a workflow pattern, and a provider capability while owning only a thin glue semantic.

#### Required repair

The re-audit must consider:

- direct adoption;
- adaptation;
- method/schema reuse;
- interoperability boundary;
- **composition of multiple mature solutions**;
- only then native design.

Do not force a single upstream project to solve the whole AIMAGE requirement before reuse is credited.

### F-05 — AIMAGE-specific value test should be explicit

**Severity: material architecture guard.**

The predecessor correctly says not to collapse AIMAGE into one provider wrapper, but the inverse test was not explicit enough: a proposed AIMAGE semantic should not survive merely because it is provider-neutral.

#### Required repair

For every remaining AIMAGE-owned semantic, ask:

> What user-visible or cross-provider control would be lost if AIMAGE did not own this semantic and instead used mature external primitives directly?

If the answer is only naming, storage preference, wrapper convenience, or duplication of an existing system, it should not remain native core design.

Likely legitimate residues may include cross-provider user-intent authority, partial-dimension approval/lock meaning, provider-neutral preservation intent, and capability-aware orchestration — but even these must be challenged rather than assumed.

### F-06 — workflow stages themselves need a redundancy check

**Severity: moderate.**

The current workflow target is accepted as a product goal, but some stages may exist only because earlier planning assumed missing infrastructure.

#### Required repair

During the reuse re-audit, do not rewrite `WORKFLOW_TARGET.md` casually, but check whether mature external capabilities allow stages to be:

- collapsed;
- made optional;
- represented as state rather than a separate phase;
- delegated entirely to an external tool/provider.

Update the workflow only if evidence shows a material simplification or correction.

### F-07 — evidence-source hierarchy should not be GitHub-project-only

**Severity: moderate.**

The next audit should search mature evidence across multiple source types:

1. official standards/specifications and primary documentation;
2. mature maintained open-source implementations;
3. established industry production patterns/tools;
4. relevant academic/technical literature;
5. proprietary systems as reference-only evidence when useful.

External evidence remains evidence, not AIMAGE authority.

### F-08 — canonical packet locator could be stronger

**Severity: low / operational.**

The predecessor packet itself says the exact immutable commit will be supplied by the derived prompt. The derived prompt did supply `09edfa4a0b0760640c11280f721aaaa475a6fb52`, so the actual transfer was usable, but packet-alone recovery is weaker than ideal.

#### Required repair

The successor packet should have an immutable locator established externally in current continuity/derived prompt from the exact commit that first contains the finalized packet, and the predecessor should be classified as `SUPERSEDED` once the successor is adopted.

This avoids self-referential commit-ID problems while preserving one immutable packet locator.

## 4. Regression checks against the handoff skill

After the above repairs, the successor handoff must still preserve:

- one immediate objective;
- one authorized phase and explicit stop boundary;
- bounded fresh authority snapshot;
- completed scope distinct from remaining work;
- decisions and negative boundaries;
- no hidden local/temporary dependency;
- exactly one next bounded action;
- expected transition;
- stop/replan conditions;
- bounded cold-start route;
- no execution before `ACCEPTED`;
- no runtime dependence on `domato153/translation`.

## 5. Final re-audit verdict

The current direction is sound, but the predecessor handoff is **superseded once a successor packet closes F-01 through F-08**.

The successor's central rule should be:

> Before AIMAGE designs any remaining capability, search the mature non-image domain that solves the same abstract problem; retain native `DESIGN` only after external adoption, adaptation, and composition have been ruled out with evidence.

The next thread should therefore be a **cross-domain reuse re-audit**, not an Image Engine design session.