# Contribution Log and Code Ownership Map

## Contribution Log

Solo project version:
- Project design and threat model
- Flask target API implementation
- Scanner and analyzer implementation
- Report generation
- Docker and Makefile reproducibility
- Tests and CI pipeline
- Documentation and artifacts

## Code Ownership Map

- `api_server/` -> target API and authentication behavior
- `scanner/` -> security probes, analyzer, and reports
- `tests/` -> unit and negative tests
- `.github/workflows/` -> CI pipeline
- `artifacts/release/` -> generated reproducibility evidence
