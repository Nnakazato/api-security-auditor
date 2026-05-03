.PHONY: clean up demo test down

clean:
	docker compose down -v --remove-orphans || true
	rm -rf artifacts/release/logs/*
	rm -rf artifacts/release/reports/*
	rm -rf artifacts/release/charts/*

up:
	docker compose up -d --build
	python -c "import time; time.sleep(3)"

demo:
	python -m scanner.main --base-url http://localhost:5001

test:
	pytest --cov=scanner --cov=api_server --cov-report=term-missing

down:
	docker compose down -v --remove-orphans