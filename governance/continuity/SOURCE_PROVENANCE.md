# Continuity Source Provenance

This file records construction provenance for the initial AIMAGE continuity design. These sources are evidence and design inputs, not runtime authority for AIMAGE.

## 1. Read-only source repository

Repository: `domato153/translation`

Construction-time governing ref: `main`

Construction-time commit:

`638e702d81b014fb32209c8ac44e907a7fbafe87`

Read-only source files used:

| Source | Blob SHA | Use in AIMAGE |
|---|---|---|
| `.agents/skills/maintenance-regression-supervisor/SKILL.md` | `e8c4cb3a3f40c5d75724c7d7fc7a128eb96c05a2` | parent principles and owner-resolution context |
| `.agents/skills/maintenance-regression-supervisor/references/handoff-continuity.md` | `bb666da48247e6adb594f2a59d145f9adec799ac` | primary continuity contract source |
| `.agents/skills/maintenance-regression-supervisor/references/handoff-continuity-regression-cases.md` | `04a75545ba9166ef6a81740495599598872e6880` | confirmed continuity failure classes used to seed bounded adversarial cases |

The source repository must remain unmodified by this adoption.

## 2. Runtime-dependency boundary

AIMAGE MUST NOT require access to `domato153/translation` to:

- interpret `governance/CONTINUITY.md`;
- produce or receive an AIMAGE handoff;
- select an AIMAGE next action;
- interpret repository-work continuity;
- interpret image-job continuity;
- run future AIMAGE continuity tests.

References to `translation` are permitted only for provenance, historical comparison, or an explicitly requested future re-audit.

If an AIMAGE governing file needs a rule originally learned from `translation`, that rule must be independently stated in AIMAGE rather than imported by runtime reference.

## 3. External audit methods

The initial adoption uses selected parts of established external methods. AIMAGE does not claim conformance to the full frameworks.

### NASA Systems Engineering Handbook — Requirements Verification Matrix

Source: https://www.nasa.gov/reference/system-engineering-handbook-appendix/

Use: unique requirement IDs, explicit source attribution, and a defined verification method for normative continuity requirements.

Not adopted: NASA program governance, lifecycle, or document ceremony unrelated to AIMAGE.

### Carnegie Mellon SEI — Architecture Tradeoff Analysis Method (ATAM)

Source: https://www.sei.cmu.edu/library/the-architecture-tradeoff-analysis-method/

Use: scenario-based architecture risk and quality-attribute tradeoff review, particularly fidelity vs. complexity, independence vs. provenance, and safety vs. ceremony.

Not adopted: a claim that this lightweight project review is a full formal ATAM engagement.

### SLSA Build Provenance

Source: https://slsa.dev/spec/v1.2-rc2/build-provenance

Use: resolved source/dependency identity and separation of provenance from operational authority.

Not adopted: SLSA build-level certification or software supply-chain controls not relevant to continuity documents.

### NIST Secure Software Development Framework (SSDF)

Source: https://csrc.nist.gov/pubs/sp/800/218/final

Use: high-level provenance/dependency and third-party component/source awareness as an audit lens.

Not adopted: full SSDF compliance or security-process ceremony for ordinary image generation.

## 4. Provenance rule

Construction provenance answers "where did this design input come from?" It does not answer "what is AIMAGE required to do now?"

Current AIMAGE governing files answer the latter.

A future external-source change does not automatically modify AIMAGE. Re-adoption requires an explicit AIMAGE review and authority transition.
