install:
	uv sync

build:
	uv build

package-install:
	uv tool install dist/*.whl

force:
	uv tool install --force dist/*.whl

run:
	uv run gendiff