install:
	uv sync

build:
	uv build

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=hexlet_python_package --cov-report xml

package-install:
	uv tool install dist/*.whl

force:
	uv tool install --force dist/*.whl

run:
	uv run gendiff

lint:
	uv run ruff check

check: test lint

.PHONY: install test lint selfcheck check build