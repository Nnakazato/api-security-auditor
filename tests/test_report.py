import json
from scanner.report import write_reports


def test_write_reports_creates_json_and_csv(tmp_path):
    findings = [{
        "test": "sample",
        "status_code": 200,
        "passed": True,
        "severity": "info",
        "finding": "ok",
    }]
    result = write_reports(findings, str(tmp_path))
    assert result["summary"]["total_tests"] == 1
    assert result["summary"]["failed_tests"] == 0
    assert json.loads((tmp_path / "api_security_report.json").read_text())["total_tests"] == 1
    assert (tmp_path / "summary.csv").exists()
