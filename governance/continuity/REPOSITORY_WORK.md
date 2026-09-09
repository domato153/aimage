# Repository-Work Continuity Profile

This profile specializes `../CONTINUITY.md` for development of the AIMAGE repository itself. It does not redefine the core continuity contract.

## Apply when

Use this profile when work crosses a context boundary while changing or reviewing AIMAGE source, schemas, governance, adapters, tests, documentation, or architecture.

## Minimum transfer state

Record only fields that materially affect continuation:

- repository and authoritative branch/ref;
- exact accepted/base commit;
- active work branch/ref and exact commit when applicable;
- requested phase (`design`, `implementation`, `verification`, `review`, or equivalent);
- current objective/problem;
- files/surfaces whose authority or behavior matters to the next action;
- preserved decisions and negative boundaries;
- unresolved blockers/uncertainties;
- decision-relevant verification evidence, if the next action depends on it;
- exactly one next action and rationale;
- stop/replan condition.

## Dependency and supersession scope

A repository handoff should normally re-check:

1. the authoritative base ref;
2. the active work ref, if any;
3. the governing AIMAGE method files needed for the proposed next action;
4. a bounded discovery surface for newer upstream work touching the same authority/capability boundary.

Do not crawl every branch merely because branches exist.

## Competing work states

Use `ACTIVE / BLOCKED / SUPERSEDED / REJECTED / HISTORICAL` only when more than one reachable plan, branch, patch, or artifact could reasonably be mistaken for the continuation target.

A branch's continued existence is not evidence that it is current.

## Verification state

Preserve verification only when it is decision-relevant. Bind reusable verification to the exact code/configuration identity it actually evaluated.

A previous PASS must not be reused after a material input or authority change unless the current verification contract makes that reuse valid.

Do not invent proof-receipt or promotion machinery merely because the source continuity method used those concepts in another repository.

## Receiver synthesis

A fresh receiver must be able to state, in plain language:

- what repository state is current;
- what phase it is in;
- what remains unresolved;
- the one next repository action;
- why that action is next;
- what movement or contradiction would force re-planning.

Only after this survives fresh reconciliation should consequential repository mutation continue.
