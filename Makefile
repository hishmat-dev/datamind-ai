.PHONY: install test lint ci data

install:
	poetry install --no-interaction --with dev

test:
	poetry run pytest --cov=datamind --cov-fail-under=80

lint:
	poetry run ruff check src tests

ci: lint test

data:
	poetry run python -c "from datamind.data.io import ensure_sample_dataset; print(ensure_sample_dataset())"
