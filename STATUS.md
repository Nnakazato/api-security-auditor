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

## What's Next

- Add charts from the CSV summary
- Add optional PCAP capture for HTTP request evidence
- Expand vulnerability checks to headers, CORS, and authentication tokens
- Improve demo video and final report polish
