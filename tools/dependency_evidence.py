from __future__ import annotations

import argparse
import json
import sys
import urllib.request
from pathlib import Path
from typing import Any

OSV_BATCH_URL = "https://api.osv.dev/v1/querybatch"


def _load_report(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def _records(report: dict[str, Any]) -> list[dict[str, str]]:
    records: list[dict[str, str]] = []
    for item in report.get("install", []):
        metadata = item.get("metadata") or {}
        download = item.get("download_info") or {}
        archive = download.get("archive_info") or {}
        hashes = archive.get("hashes") or {}
        sha256 = hashes.get("sha256")
        name = metadata.get("name")
        version = metadata.get("version")
        url = download.get("url")
        if not name or not version or not url or not sha256:
            raise RuntimeError(f"resolution entry lacks exact identity/hash evidence: {item!r}")
        records.append(
            {
                "name": str(name),
                "version": str(version),
                "url": str(url),
                "sha256": str(sha256),
                "license": str(metadata.get("license_expression") or metadata.get("license") or "UNKNOWN"),
            }
        )
    if not records:
        raise RuntimeError("pip report contained no install candidates")
    records.sort(key=lambda value: value["name"].lower())
    return records


def _query_osv(records: list[dict[str, str]]) -> list[list[dict[str, Any]]]:
    payload = {
        "queries": [
            {"package": {"ecosystem": "PyPI", "name": record["name"]}, "version": record["version"]}
            for record in records
        ]
    }
    request = urllib.request.Request(
        OSV_BATCH_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json", "User-Agent": "AIMAGE-Gate-B/1"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        result = json.loads(response.read().decode("utf-8"))
    responses = result.get("results")
    if not isinstance(responses, list) or len(responses) != len(records):
        raise RuntimeError("OSV batch response did not match resolved dependency set")
    return [list(response.get("vulns") or []) for response in responses]


def _lock_lines(records: list[dict[str, str]]) -> list[str]:
    lines = ["# Generated candidate from pip --dry-run --report; review before adoption."]
    for record in records:
        normalized = record["name"].replace("_", "-")
        lines.append(f"{normalized}=={record['version']} --hash=sha256:{record['sha256']}")
    return lines


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("report", type=Path)
    parser.add_argument("--platform-label", required=True)
    parser.add_argument("--lock-output", type=Path, required=True)
    args = parser.parse_args()

    report = _load_report(args.report)
    records = _records(report)
    osv = _query_osv(records)

    evidence: list[dict[str, Any]] = []
    vulnerable = False
    for record, vulns in zip(records, osv, strict=True):
        active = [vuln for vuln in vulns if not vuln.get("withdrawn")]
        vulnerable = vulnerable or bool(active)
        evidence.append({**record, "osv_active_ids": sorted(str(vuln.get("id")) for vuln in active)})

    args.lock_output.write_text("\n".join(_lock_lines(records)) + "\n", encoding="utf-8")

    summary = {
        "platform": args.platform_label,
        "pip_version": report.get("pip_version"),
        "dependency_count": len(records),
        "dependencies": evidence,
        "blocking_active_vulnerability": vulnerable,
    }
    print("AIMAGE_GATE_B_EVIDENCE_BEGIN")
    print(json.dumps(summary, indent=2, sort_keys=True))
    print("AIMAGE_GATE_B_EVIDENCE_END")
    print("AIMAGE_EXACT_LOCK_CANDIDATE_BEGIN")
    print(args.lock_output.read_text(encoding="utf-8"), end="")
    print("AIMAGE_EXACT_LOCK_CANDIDATE_END")

    if vulnerable:
        print("Gate B blocked: OSV reports at least one active vulnerability for the exact resolved set.", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
