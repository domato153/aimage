# AIMAGE Handoff Skill — Source Provenance

Status: construction/audit provenance only. None of the sources below are runtime AIMAGE authority.

## 1. Original construction source repository

- repository: `domato153/translation`
- construction-time authoritative commit: `638e702d81b014fb32209c8ac44e907a7fbafe87`

## 2. Generic maintenance-handoff sources reviewed read-only

1. `.agents/skills/maintenance-regression-supervisor/SKILL.md`
   - blob: `e8c4cb3a3f40c5d75724c7d7fc7a128eb96c05a2`
   - relevant generic concept: handoff is a live transfer, not a static summary; resolve the governing method from its authoritative owner before packet use.

2. `.agents/skills/maintenance-regression-supervisor/references/handoff-continuity.md`
   - blob: `bb666da48247e6adb594f2a59d145f9adec799ac`
   - relevant generic concepts: canonical locator, bounded dependencies, situation model, decision/negative-boundary preservation, staleness, durability/recovery, receiver cold-start, one next action, acceptance semantics.
   - these concepts were already independently adopted into AIMAGE `governance/CONTINUITY.md`; the handoff skill routes to that AIMAGE owner rather than importing the translation file at runtime.

3. `docs/archive/coverage-v2/THREAD_HANDOFF__MAINTENANCE_SKILL__2026-08-15_2305_KST.md`
   - blob: `8451c4e45040c63d00975b8b8721089aaac993cf`
   - role: historical maintenance-thread handoff exemplar.
   - useful structure: immediate objective, user constraints, fresh live state, preserved behavior, round/completed history compressed around current work, next-stage route.

4. `docs/maintenance/THREAD_HANDOFF__GENERIC_CORE_REGRESSION_RECOVERY__2026-09-02.md`
   - blob: `a6728dc189ec7bc52eeeb49e44d5f878557cc004`
   - role: later maintenance handoff exemplar.
   - useful structure: user intent, exact authority snapshot, frozen/preserved state, confirmed regression set, current live continuity snapshot, current blocker, completed scope, cold-start route, exact next task fingerprint, first bounded actions, hard prohibitions, continuity precedence.

5. `docs/maintenance/HANDOFF_METHOD_OWNER_RESOLUTION_REVIEW_20260908.md`
   - blob: `fc52eb6c23ee5e9c769c299dcd6366949aacec95`
   - role: root-cause/method review for stale co-located handoff-method shadowing.
   - useful generic concept: packet/candidate/evidence co-location is not authority; method owner must be resolved before handoff semantics are applied.

6. `tests/test_handoff_continuity_contract.py`
   - blob: `9a035e3563774f7def85f36ab703959d80c52fda`
   - role: regression inventory exposing required handoff/continuity invariants and restraint counterexamples.

7. `tests/test_handoff_method_owner_bootstrap.py`
   - blob: `6a1e13a0b879ab398003630653d8e3c3759ac74c`
   - role: focused regression check for authoritative handoff-method owner resolution.

## 3. Explicitly reviewed but not adopted as generic handoff source

`40_seam_and_context_handoff.md`
- blob: `50bbf342cf4b78d2b70ddb563bc73805c50477c7`
- classification: translation-domain seam/context protocol.
- reason for exclusion: it owns source/target batch boundaries, POV/referent/literary continuity, translation state-model routing, and manuscript-specific seam behavior. Those semantics are not a generic cross-thread maintenance handoff method and would contaminate AIMAGE if mechanically imported.

## 4. Later external-method hardening evidence — not original construction provenance

After the AIMAGE-native handoff skill had already been adopted, it was re-audited against mature handoff methods from other fields. The audit and exact adaptations are recorded at:

- `audits/HANDOFF_EXTERNAL_METHOD_REAUDIT_2026-09-10.md`
- `.agents/skills/handoff/references/TRACEABILITY.md` rows `H-036` through `H-042`

External evidence families included:

- Google SRE incident-management handoff / living state-document practice;
- AHRQ TeamSTEPPS Handoff, I-PASS and SBAR;
- NASA mission-operations / human-factors shift-handover research;
- OpenAI Agents SDK handoff input/context filtering patterns.

These sources did **not** replace the original AIMAGE method owner and were not adopted wholesale. They were used only to test the already-AIMAGE-owned method for generic omissions. The resulting AIMAGE-owned hardening was limited to:

- completion/acceptance criteria;
- bounded research/review exit conditions;
- conditional urgency/deadline/commitment/ownership transfer;
- material successor delta;
- top-level Operational Header for dense handoffs;
- explicit context filtering and durable-state separation;
- stronger receiver synthesis/read-back before acceptance.

Domain-specific patient/incident/mission fields, synchronous overlap requirements, mnemonics, or SDK runtime mechanisms were not imported as AIMAGE runtime requirements.

## 5. Independence rule

The AIMAGE runtime owner is `.agents/skills/handoff/SKILL.md` plus AIMAGE-owned continuity/governance files routed by root `AGENTS.md`.

The `domato153/translation` repository and later external handoff sources are retained only as construction/audit evidence. No AIMAGE receiver may be required to read any of them to produce, consume, validate, or continue a handoff.