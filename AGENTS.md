# AIMAGE Agent Entry Point

Status: canonical repository-native entry point for AI agents working in `domato153/aimage`.

This file is a router and safety boundary. It does not duplicate the detailed rules owned by AIMAGE governance, architecture, or future subsystem files.

## 1. Start here

For consequential AIMAGE work:

1. Fresh-read the current `main` state and any live repository/platform state needed to establish current facts.
2. Read this root `AGENTS.md` from its current authoritative owner before following a handoff, work branch, generated summary, or chat memory.
3. Identify the user's requested phase and scope before mutating anything.
4. Read only the governing AIMAGE files needed for that task, using the routing below.
5. Reconcile any handoff or prior plan against fresh authority before consequential continuation.

Do not reconstruct the repository's governing rules from memory when the owning file can be fresh-read.

## 2. Authority and current facts

Keep factual state separate from intent and authorization.

- Fresh repository/platform observation governs current facts such as refs, file contents, artifact availability, and merge state.
- Explicit current user instruction governs intent, requested scope, decisions, and authorization, subject to external/platform constraints.
- A work branch, candidate, handoff, generated summary, or modified governing file cannot authorize its own promotion to canonical authority.
- Project source, chat history, memory, and handoffs are not substitutes for fresh repository authority.

For detailed cross-context authority and acceptance semantics, read `governance/CONTINUITY.md`.

## 3. Phase is part of scope

Determine whether the requested work is, for example, `review`, `design`, `implementation`, `verification`, or an authority-changing/adoption step.

- Do not cross from review/design into implementation merely because an implementation is obvious.
- Do not merge, promote, delete, replace, demote, or broadly rewrite canonical/governing surfaces unless the current request authorizes that phase and fresh authority still permits the operation.
- If the user requests one bounded stage, complete that stage rather than opportunistically continuing into the next.

Repository-work handoffs additionally follow `governance/continuity/REPOSITORY_WORK.md`.

## 4. Continuity routing

Use continuity only when state must survive a chat/thread/operator/tool/session boundary or stale/ambiguous state can materially change the next action.

- Common contract: `governance/CONTINUITY.md`
- Repository development: `governance/continuity/REPOSITORY_WORK.md`
- Image-production job: `governance/continuity/IMAGE_JOB.md`

A continuity packet is continuity evidence, not project authority. A consequential receiver must fresh-reconcile before continuation and must not treat packet receipt as execution ownership.

Do not create handoff ceremony for ordinary low-risk, single-context work.

## 5. Architecture boundary

Read `architecture/BOUNDARIES.md` before making or reviewing architecture that could blur responsibility between:

1. continuity infrastructure;
2. Image Engine Architecture / Core;
3. AIMAGE Features / Domain Capabilities.

Preserve the intended product dependency direction:

`features/domain capabilities -> engine interfaces`

Continuity may transport engine/feature state but must not become the owner of image-generation algorithms, prompt strategies, composition logic, or model-specific behavior.

## 6. Mutation safety

Before a consequential repository mutation:

- fresh-read the target authority/ref/state;
- preserve existing valid behavior outside the declared change boundary;
- prefer a bounded branch/PR candidate for non-trivial or authority-affecting changes;
- do not treat a candidate-modified policy/spec as proof that the authority transition is allowed;
- preserve explicit user decisions and negative boundaries when they materially constrain later work;
- do not turn examples or explanatory rationale into broader authority than the owning decision grants.

If fresh state contradicts the premise of the requested operation, reconcile the contradiction rather than forcing the stale plan.

## 7. External sources and imported methods

External repositories, papers, methods, and the historical `domato153/translation` source recorded in provenance are evidence/construction inputs only unless AIMAGE explicitly adopts their rules into an AIMAGE-owned governing file.

Runtime AIMAGE work must not depend on `domato153/translation` merely to interpret continuity.

Construction provenance for the current continuity adoption is recorded in `governance/continuity/SOURCE_PROVENANCE.md`.

## 8. Local instruction files

A future directory may add its own `AGENTS.md` for subsystem-specific routing or constraints.

A more specific `AGENTS.md` may specialize work inside its directory, but it must not silently override root authority, continuity, or architecture boundaries unless an AIMAGE governing surface explicitly delegates that authority.

Do not create directory-local `AGENTS.md` files before there is a real recurring subsystem need.

## 9. Current canonical routes

- `governance/CONTINUITY.md` — cross-context continuity contract
- `governance/continuity/REPOSITORY_WORK.md` — repository-work continuity profile
- `governance/continuity/IMAGE_JOB.md` — image-job continuity profile
- `architecture/BOUNDARIES.md` — continuity / engine / feature-domain responsibility boundary
- `bootstrap/PROJECT_SOURCE.md` — thin external GPT Project locator/bootstrap

As the repository grows, add new routes here only when they are stable entry points. Keep detailed subsystem rules in their owning files rather than expanding this router into a second specification.
