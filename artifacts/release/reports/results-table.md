# API Security Auditor Results

| Test Case              | Status | Severity | Description |
|----------------------|--------|----------|-------------|
| Happy Path Login     | PASS   | Info     | Secure login accepted valid credentials |
| SQL Injection Probe  | FAIL   | High     | Vulnerable endpoint accepted malicious input |
| Error Leakage Probe  | FAIL   | Medium   | Response reveals implementation details |
| Rate Limit Probe     | PASS   | Info     | No issue detected |
