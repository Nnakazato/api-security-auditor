# Runbook

## Prerequisites

- Docker
- Docker Compose
- Python 3.11+

## Rebuild and Run

```bash
make clean && make up && make demo
```

## Run Tests

```bash
make test
```

## Stop Services

```bash
make down
```

## Output Locations

- Logs: `artifacts/release/logs/demo.log`
- JSON report: `artifacts/release/reports/api_security_report.json`
- CSV summary: `artifacts/release/reports/summary.csv`

## Troubleshooting

If port 5001 is already in use, stop the conflicting service or change the mapped port in `docker-compose.yml` and update the Makefile demo URL.
