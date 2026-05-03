# What Works / What's Next

## What Works

- Dockerized Flask target API
- Secure login endpoint with password hashing and rate limiting
- Intentionally vulnerable endpoint for repeatable testing
- Scanner probes API behavior and analyzes responses
- JSON and CSV reports are generated automatically
- Demo logs are saved under `artifacts/release/logs/`
- Unit tests and negative tests are included
- CI runs tests with coverage

## Initial Evaluation Results

| Test Case | Expected Behavior | Observed Result |
|---|---|---|
| Valid login | Accepted | PASS |
| Invalid input | Rejected or logged | PASS |
| SQL-injection-style input | Detected as suspicious | ALERT |
| Error leakage | Detected if server exposes internal error | ALERT |
| Rate limiting | Repeated attempts are restricted | CHECKED |

## Draft Results

The initial evaluation shows that API Security Auditor can run a full vertical slice from request generation to report export. The scanner sends normal and suspicious API requests, records responses, analyzes security behavior, and saves JSON/CSV evidence under `artifacts/release/`. The intentionally vulnerable endpoint provides repeatable evidence for detecting unsafe API behavior, while the secure endpoint demonstrates expected safe behavior.

## What's Next

- Add charts from the CSV summary
- Add optional PCAP capture for HTTP request evidence
- Expand vulnerability checks to headers, CORS, and authentication tokens
- Improve demo video and final report polish