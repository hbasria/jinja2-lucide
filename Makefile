.PHONY: test build

build-env:
	python3 -m venv .venv
	.venv/bin/pip install poetry
	.venv/bin/poetry install

test: build-env
	.venv/bin/poetry run pytest

build: build-env
	.venv/bin/poetry build