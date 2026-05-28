.PHONY: test

PYTHON ?= python
PACKAGE_NAME ?= pydantic_schemaorg
REPORT_DIR ?= reports/$(shell date -Is | sed 's/:/-/g')

test:
	mkdir -p $(REPORT_DIR)
	$(PYTHON) -m pytest --cov=$(PACKAGE_NAME) --cov-report=term:$(REPORT_DIR)/results.log --cov-report=json:$(REPORT_DIR)/results.json
