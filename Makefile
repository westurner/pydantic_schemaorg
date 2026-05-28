.PHONY: test

PACKAGE_NAME ?= pydantic_schemaorg
REPORT_DIR ?= reports/$(shell date -Is | sed 's/:/-/g')

test:
	mkdir -p $(REPORT_DIR)
	python -m pytest --cov=$(PACKAGE_NAME) --cov-report=html:$(REPORT_DIR)/htmlcov --cov-report=term
