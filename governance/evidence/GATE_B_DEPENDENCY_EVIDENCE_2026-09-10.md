# Gate B Exact Dependency Evidence — 2026-09-10

Status: exact transitive resolution and pre-install artifact/security review complete for the first implementation slice. Runtime installation/test acceptance is a separate next check.

## Authority and execution context

- Repository: `domato153/aimage`
- Implementation branch: `aimage-stage/first-openai-vertical-slice`
- Evidence workflow run: GitHub Actions `34410634058`, run #2
- Resolver interpreter: CPython `3.13.15`
- Resolver: pip `26.2.1`
- Linux runner: Ubuntu 24.04 x64
- Windows runner: Windows Server 2025 x64
- Python provisioning action: GitHub-owned `actions/setup-python`, immutable release `v7.0.0`, pinned commit `5fda3b95a4ea91299a34e894583c3862153e4b97`
- Resolution mode: `pip install --dry-run --ignore-installed --report`; no AIMAGE runtime dependencies were installed during the evidence run.

## Result

- Linux CPython 3.13: PASS, 25 exact resolved packages.
- Windows CPython 3.13: PASS, 26 exact resolved packages; the additional package is Windows-only `colorama==0.4.6`.
- Every resolved artifact had an exact SHA-256 from pip/PyPI download evidence.
- OSV batch queries reported no active vulnerability IDs for any exact resolved package in either platform set at the evidence time.
- The Windows resolver metadata did not expose a normalized license expression for `colorama==0.4.6`; the PyPI 0.4.6 project page explicitly identifies the project license as BSD 3-Clause. This manual license check closes the metadata-only gap.

## Adopted lock candidates

- `requirements-lock/linux-cp313.txt`
- `requirements-lock/windows-cp313.txt`

The two files intentionally pin the exact resolver-selected wheels by SHA-256. Native-wheel hashes differ where expected (`greenlet`, `MarkupSafe`, `pydantic-core`, `SQLAlchemy`, `jiter`), while universal wheels share hashes.

The locks are valid only for the named CPython 3.13 x64 platform families. A new interpreter/platform or dependency version requires fresh resolution/evidence rather than silent reuse.

## Next gate

The next workflow pass must:

1. reproduce the same dry-run candidate;
2. byte-compare it to the checked-in platform lock;
3. install only with `--only-binary=:all: --require-hashes`;
4. run the AIMAGE pytest suite on Linux and Windows;
5. on Linux, run the credentialed Sunburst generation/edit smoke only when `OPENAI_API_KEY` is actually configured.

No pytest PASS or live-provider PASS is claimed by this evidence document alone.
