# AGENTS.md

This file provides guidance to agents when working with code in this repository.

- Tests must be run in both `src/` and `pydantic_schemaorg/` directories. See `[tool.pytest.ini_options]` in `pyproject.toml`.
- Model generation is performed with: `python src/main.py build all` (see `build` target in `Makefile`).
- All generated models in `pydantic_schemaorg/` use `from __future__ import annotations` at the top of each file.
- **Workflow Instructions:**
  You must source the virtual environment before running poetry, tests, or build scripts!
  Navigate to the project root (`/var/home/wturner/-wrk/-ve311/pydantic_schemaorg/`):
  `source bin/activate && poetry run <command>`
  Example full build: `source bin/activate && poetry run python src/main.py build all`
  Example test run: `source bin/activate && poetry run pytest src/test_classes.py`
- **Pydantic v2 Refactoring Notes:**
  We are migrating schema.org dynamically generated classes to Pydantic v2.
  - Generated files in `pydantic_schemaorg/` are build artifacts from templates in `src/templates/`.
  - The base class implementation is generated from `src/templates/schema_org_base.py.tpl`.
  - Type model modules (for example `CreativeWork.py`) are generated from `src/templates/model.py.tpl`.
  - For durable changes, edit templates first (especially `src/templates/schema_org_base.py.tpl`), then rebuild. Do not patch generated files like `pydantic_schemaorg/SchemaOrgBase.py` or `pydantic_schemaorg/CreativeWork.py` directly unless doing temporary debugging.
  - The Jinja2 templates are in `src/templates/` (e.g., `src/templates/schema_org_base.py.tpl`).
  - Generated schema files are deeply cyclical. Recursion depth (`sys.setrecursionlimit()`) and circular import safeguards are required.
  - When updating model rebuilding, ensure accurate matching of regex patterns in `_get_referenced_types` and guard `type_class.model_rebuild()` to avoid `RecursionError`.
