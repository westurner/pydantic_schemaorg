# Makefile for Poetry-based Python project

SHELL := /bin/bash



.PHONY: \
  help \
  install-poetry \
  install \
  build \
  test \
	coverage \
  test-x \
  test-src \
  test-built-models \
  test-models \
  test-classes \
  test-valid-names \
  test-main \
  build-test \
  clean \
  clean-schem



help:
	@echo "pydantic_schemaorg Makefile"
	@echo "---------------------------"
	@echo "Available targets:"
	@echo "  install-poetry      Install Poetry using pip"
	@echo "  install             Install dependencies via Poetry"
	@echo "  build               Build the package using Poetry and generate models"
	@echo "  test                Run all tests using pytest via Poetry"
	@echo "  coverage            Run pytest with coverage and write reports to reports/<timestamp>/"
	@echo "  test-x              Run tests, stop after first failure"
	@echo "  test-main           Run src/test_main.py"
	@echo "  test-src            Run tests in src/ directory"
	@echo "  test-models         Run src/test_models.py"
	@echo ""
	@echo "  test-built-models   Run tests in pydantic_schemaorg/ directory"
	@echo "  test-classes        Run src/test_classes.py"
	@echo "  test-valid-names    Run src/test_valid_name.py"
	@echo ""
	@echo "  build-test          Build and then test"
	@echo "  clean               Remove build artifacts"
	@echo "  clean-schema        Remove build artifacts: rm -fv src/schema/*.txt"


install-poetry:
	python -m pip install poetry

install:
	. ../../bin/activate && poetry install

# build:
# 	poetry build


# NOTE: pytest.ini settings are in pyproject.toml > [tool.pytest.ini_options]

REPORTS_DIR := reports/$(shell date -Is)

buildtest:
	$(MAKE) build 2>&1 > build.log
	$(MAKE) test 2>&1 >> build.log

test:
	. ../../bin/activate && poetry run pytest

coverage:
	mkdir -p "$(REPORTS_DIR)"
	set -o pipefail; . ../../bin/activate && poetry run pytest \
		--cov=src \
		--cov=pydantic_schemaorg \
		--cov-report=term-missing \
		--cov-report=html:"$(REPORTS_DIR)/html" \
		--cov-report=xml:"$(REPORTS_DIR)/coverage.xml" \
		2>&1 | tee "$(REPORTS_DIR)/pytest.log"

testv:
	. ../../bin/activate && poetry run pytest -v

test-x:
	. ../../bin/activate && poetry run pytest -x -l

testx: test-x


test-src:
	. ../../bin/activate && poetry run pytest -v src/

test-built-models:
	. ../../bin/activate && poetry run pytest -v pydantic_schemaorg/



test-classes:
	. ../../bin/activate && poetry run pytest -v src/test_classes.py

test-models:
	. ../../bin/activate && poetry run pytest -v src/test_models.py


test-valid-names:
	. ../../bin/activate && poetry run pytest -v src/test_valid_name.py

test-main:
	. ../../bin/activate && poetry run pytest -v src/test_main.py

build:
	python src/main.py build all
	test -f pydantic_schemaorg/SchemaOrgBase.py
	test -f pydantic_schemaorg/CreativeWork.py
	test ! -f pydantic_scemaorg/None.py


build-test:
	$(MAKE) build
	$(MAKE) test


clean-schema:
	rm -fv src/schema/*.txt

clean:
	rm -rf dist *.egg-info __pycache__ .pytest_cache
