# 10-Minute Demo Script

1. Introduce the problem: APIs often fail to validate input, leak errors, or lack rate limiting.
2. Explain threat model: attacker sends crafted requests to abuse authentication endpoints.
3. Show architecture: target API, scanner, analyzer, report writer.
4. Run `make clean && make up && make demo`.
5. Show secure login happy path.
6. Show SQL-injection-style probe detected.
7. Show error leakage finding.
8. Show rate limiting check.
9. Open `artifacts/release/reports/api_security_report.json` and `summary.csv`.
10. Explain limitations and future work.
