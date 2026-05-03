from __future__ import annotations

import argparse
import json
import logging
import sys
from pathlib import Path
from urllib.parse import urlparse

import requests

from scanner.analyzer import analyze_response
from scanner.report import write_reports

LOG_DIR = Path("artifacts/release/logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(LOG_DIR / "demo.log", mode="w", encoding="utf-8"),
    ],
)
logger = logging.getLogger("api-security-auditor")


def validate_base_url(base_url: str) -> str:
    parsed = urlparse(base_url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError("base-url must be a valid http(s) URL")
    return base_url.rstrip("/")


def post_json(base_url: str, path: str, payload: dict) -> tuple[int, str]:
    response = requests.post(f"{base_url}{path}", json=payload, timeout=5)
    return response.status_code, response.text


def run_audit(base_url: str) -> list[dict]:
    base_url = validate_base_url(base_url)
    findings: list[dict] = []

    logger.info("Starting API Security Auditor scan against %s", base_url)

    logger.info("[1] Happy path login against secure endpoint")
    code, body = post_json(base_url, "/login-secure", {
        "username": "alice",
        "password": "CorrectHorseBatteryStaple!23",
    })
    findings.append({
        "test": "happy_path_secure_login",
        "status_code": code,
        "passed": code == 200 and "login accepted" in body.lower(),
        "severity": "info",
        "finding": "Secure login accepted valid credentials" if code == 200 else "Secure login failed unexpectedly",
    })

    logger.info("[2] SQL injection probe against vulnerable endpoint")
    code, body = post_json(base_url, "/login-vulnerable", {
        "username": "' OR '1'='1",
        "password": "anything",
    })
    findings.append(analyze_response("sql_injection_probe", code, body))

    logger.info("[3] Error leakage probe against vulnerable endpoint")
    code, body = post_json(base_url, "/login-vulnerable", {
        "username": "nobody",
        "password": "bad-password",
    })
    findings.append(analyze_response("error_leakage_probe", code, body))

    logger.info("[4] Rate limit probe against secure endpoint")
    last_code = 0
    last_body = ""
    for _ in range(6):
        last_code, last_body = post_json(base_url, "/login-secure", {
            "username": "mallory",
            "password": "wrong-password",
        })
    findings.append(analyze_response("rate_limit_probe", last_code, last_body))

    logger.info("Audit complete: %s", json.dumps(findings))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Run API security audit demo")
    parser.add_argument("--base-url", default="http://localhost:5001")
    args = parser.parse_args()

    try:
        findings = run_audit(args.base_url)
        paths = write_reports(findings)
        logger.info("Reports written: JSON=%s CSV=%s", paths["json"], paths["csv"])
        print("\n=== API Security Auditor Summary ===")
        print(json.dumps(paths["summary"], indent=2))
        return 0
    except Exception as exc:
        logger.exception("Audit failed: %s", exc)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
