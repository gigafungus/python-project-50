install:
	uv sync

build:
	uv build

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report=xml

package-install:
	uv tool install dist/*.whl

force:
	uv tool install --force dist/*.whl

run:
	uv run gendiff

lint:
	uv run ruff check

fix:
	uv run ruff check --fix

check: test lint

.PHONY: install test lint selfcheck check build