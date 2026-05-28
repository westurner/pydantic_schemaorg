"""
test_classes.py
"""
import importlib
import inspect
import json
import re
import pytest
import sys
import pathlib
from functools import lru_cache
from typing import Dict, List, Union, Iterator

# Schema.org has a large cyclic class graph that hits recursion limits during Pydantic schema generation
# sys.setrecursionlimit(10000)

from src.main import get_from_disk_or_http

# TODO: is this still necessary?
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))

MODULE_DIR = pathlib.Path(__file__).parent.parent
SCHEMA_ORG_EXAMPLES_URL = "https://raw.githubusercontent.com/schemaorg/schemaorg/main/data/releases/30.0/schemaorg-all-examples.txt"
JSON_LD_PATTERN = re.compile(
    r'<script type\="application/ld\+json">(?P<json_ld>.*?)</script>',
    flags=re.DOTALL | re.M | re.UNICODE,
)


def get_modules_in_package(dir_name: str, package_name: str) -> Iterator[type]:
    for file_path in pathlib.Path(dir_name).glob("*.py"):
        file = file_path.name
        if file == "__init__.py" or file.startswith("test_"):
            continue
        file_name = file_path.stem
        module_name = package_name + "." + file_name
        for _, cls in inspect.getmembers(
            importlib.import_module(module_name), inspect.isclass
        ):
            if cls.__module__ == module_name:
                yield cls


def get_all_examples() -> Iterator[Union[List, Dict]]:
    content = get_from_disk_or_http(SCHEMA_ORG_EXAMPLES_URL, text=True)
    matches = JSON_LD_PATTERN.findall(content)
    for match in matches:
        m = match.replace('\n', '')
        b = json.loads(m)
        yield b


@lru_cache(maxsize=1)
def get_valid_examples() -> tuple[Dict, ...]:
    examples = list(get_all_examples())
    assert len(examples), "it should have loaded examples"
    return tuple(
        e
        for e in examples
        if isinstance(e, dict) and not isinstance(e.get("@type"), list)
    )


@lru_cache(maxsize=1)
def get_schema_modules() -> tuple[type, ...]:
    return tuple(get_modules_in_package(str(MODULE_DIR), "pydantic_schemaorg"))


@pytest.fixture(scope="session")
def valid_examples() -> tuple[Dict, ...]:
    return get_valid_examples()


@pytest.fixture(scope="session")
def schema_modules() -> tuple[type, ...]:
    return get_schema_modules()


def test_schemaorg_examples(valid_examples: tuple[Dict, ...]) -> None:
    for example in valid_examples:
        type_ = example.get("@type", "").split(":")[-1]
        if not type_:
            continue
        try:
            mod = importlib.import_module(f"pydantic_schemaorg.{type_}")
            class_ = getattr(mod, type_)
            model = class_(**example)
            assert model is not None
        except ModuleNotFoundError:
            # Some examples reference non-core/external vocab types.
            print("ERROR: Module not found {0!r}".format(type_))
            continue
        except Exception as e:
            print(f"Exception for type {type_}: {e}")
            raise


def test_update_all_fields(schema_modules: tuple[type, ...]) -> None:
    for module in schema_modules:
        try:
            module._update_all_fields()
            module()
        except Exception as e:
            pytest.fail(f"Exception in module {module}: {e}")
