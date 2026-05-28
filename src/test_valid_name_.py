import importlib
import os
import pathlib
import pytest

MODELS_DIR = pathlib.Path(__file__).parent.parent / 'pydantic_schemaorg'


def get_model_files():
    skip_files = {'__init__.py', 'SchemaOrgBase.py', '__types__.py'} #, 'None.py'}
    return [f for f in os.listdir(MODELS_DIR)
            if f.endswith('.py') and f not in skip_files]


@pytest.mark.parametrize('filename', get_model_files())
def test_valid_name_populated(filename):
    module_name = f'pydantic_schemaorg.{filename[:-3]}'
    module = importlib.import_module(module_name)
    # Find the main class in the module
    cls = None
    for attr in dir(module):
        obj = getattr(module, attr)
        if isinstance(obj, type) and obj.__module__ == module_name and hasattr(obj, 'valid_name'):
            cls = obj
            break
    assert cls is not None, f"No class with 'valid_name' in {filename}"
    assert getattr(cls, 'valid_name', None) not in (None, '', 'None'), f"valid_name not populated in {cls} from {filename}"
