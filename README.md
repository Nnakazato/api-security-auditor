# API Security Auditor

API Security Auditor is a Dockerized CECS 478 security project that demonstrates automated detection of common web API security problems. The project includes a local target API with secure and intentionally vulnerable endpoints, plus a scanner that probes the API, logs behavior, and exports reproducible JSON/CSV evidence.

## Vertical Slice

```text
request -> validate -> test -> analyze -> report
```

## Quick Start

```bash
make clean && make up && make demo
```

Expected result:
- valid login succeeds on the secure endpoint
- SQL-injection-style input is detected against the vulnerable endpoint
- implementation error leakage is detected
- rate limiting behavior is checked
- reports are written under `artifacts/release/reports/`
- logs are written under `artifacts/release/logs/`

## Project Structure

```text
api_server/              local Flask target API
scanner/                 auditor, analyzer, and report writer
tests/                   unit and negative tests
artifacts/release/       generated logs, CSV/JSON reports, charts
.github/workflows/       CI pipeline
```

## Security Scope

This project runs only against a local Docker lab target. It does not scan third-party systems and does not exploit real services. The vulnerable endpoint exists only to create repeatable evidence for evaluation.
