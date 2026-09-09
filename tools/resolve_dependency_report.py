from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Resolve AIMAGE dependency candidate without installing it")
    parser.add_argument("--requirements", default="requirements-dev.txt")
    parser.add_argument("--report", default="build/dependency-resolution-report.json")
    parser.add_argument("--summary", default="build/dependency-lock-candidate.json")
    args = parser.parse_args()
    report = Path(args.report); summary = Path(args.summary); report.parent.mkdir(parents=True, exist_ok=True); summary.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run([sys.executable, "-m", "pip", "install", "--dry-run", "--ignore-installed", "--report", str(report), "-r", args.requirements], check=True)
    raw = json.loads(report.read_text(encoding="utf-8")); records = []
    for item in raw.get("install", []):
        metadata = item.get("metadata", {}); download = item.get("download_info", {}); hashes = download.get("archive_info", {}).get("hashes", {})
        sha256 = hashes.get("sha256")
        if not sha256: raise SystemExit(f"resolved artifact lacks sha256: {metadata.get('name')} {metadata.get('version')}")
        records.append({"name": metadata.get("name"), "version": metadata.get("version"), "url": download.get("url"), "sha256": sha256, "requested": bool(item.get("requested"))})
    records.sort(key=lambda row: (str(row["name"]).lower(), str(row["version"])))
    summary.write_text(json.dumps({"python": raw.get("environment", {}), "artifacts": records}, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {summary} with {len(records)} resolved artifacts; no packages were installed")
    return 0

if __name__ == "__main__": raise SystemExit(main())
