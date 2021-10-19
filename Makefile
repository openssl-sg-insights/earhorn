.PHONY: install format lint test

SHELL = bash
CPU_CORES = $(shell nproc)

all: install format lint test

INSTALL_STAMP := .installed
install: $(INSTALL_STAMP)
$(INSTALL_STAMP):
	poetry install
	touch $(INSTALL_STAMP)

format: install
	poetry run black .
	poetry run isort . --profile black

lint: install
	poetry run black . --diff --check
	poetry run isort . --profile black --check
	poetry run pylint earhorn tests
	poetry run mypy earhorn tests || true

test: install
	poetry run pytest -n $(CPU_CORES) --color=yes -v --cov=earhorn tests

e2e: install
	poetry run pytest -n $(CPU_CORES) --color=yes -v --cov=earhorn e2e

ci-publish:
	poetry publish --no-interaction --build


howler-build:
	cd howler && docker build -t howler .

howler-run:
	docker run -it --rm \
		-p 8000:8000 \
		-v $(shell pwd)/howler/icecast.xml:/etc/icecast/icecast.xml \
		-v $(shell pwd)/howler/sample.ogg:/sample.ogg \
		howler
