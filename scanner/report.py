from __future__ import annotations

import csv
import json
from pathlib import Path


def write_reports(findings: list[dict], output_dir: str = "artifacts/release/reports") -> dict:
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)

    summary = {
        "total_tests": len(findings),
        "failed_tests": sum(1 for item in findings if not item["passed"]),
        "high_findings": sum(1 for item in findings if item["severity"] == "high"),
        "medium_findings": sum(1 for item in findings if item["severity"] == "medium"),
        "findings": findings,
    }

    json_path = out / "api_security_report.json"
    csv_path = out / "summary.csv"

    json_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["test", "status_code", "passed", "severity", "finding"])
        writer.writeheader()
        writer.writerows(findings)

    return {"json": str(json_path), "csv": str(csv_path), "summary": summary}
