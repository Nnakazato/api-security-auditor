from __future__ import annotations

SENSITIVE_ERROR_TERMS = ["sqlite", "query", "table", "traceback", "exception", "stack"]


def analyze_response(name: str, status_code: int, body: str) -> dict:
    lower_body = body.lower()
    finding = {
        "test": name,
        "status_code": status_code,
        "passed": True,
        "severity": "info",
        "finding": "No issue detected",
    }

    if name == "sql_injection_probe" and "login accepted" in lower_body:
        finding.update({
            "passed": False,
            "severity": "high",
            "finding": "Possible injection bypass accepted by vulnerable endpoint",
        })
    elif name == "error_leakage_probe" and any(term in lower_body for term in SENSITIVE_ERROR_TERMS):
        finding.update({
            "passed": False,
            "severity": "medium",
            "finding": "Response appears to leak implementation details",
        })
    elif name == "rate_limit_probe" and status_code != 429:
        finding.update({
            "passed": False,
            "severity": "medium",
            "finding": "Rate limiting was not observed after repeated failed logins",
        })

    return finding
