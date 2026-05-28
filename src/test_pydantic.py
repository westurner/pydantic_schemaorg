import pytest
import re
from typing import ForwardRef, Optional, Union, List, Any
from pydantic import BaseModel, Field, ConfigDict, AnyUrl
from pydantic_schemaorg.SchemaOrgBase import SchemaOrgBase
from pydantic_schemaorg.WebPage import WebPage


def test_schema_org_base_config():
    """Verify SchemaOrgBase Pydantic configuration settings."""
    assert SchemaOrgBase.model_config.get("populate_by_name") is True


@pytest.mark.parametrize(
    "class_to_test",
    [
        WebPage,
    ],
)
def test_model_rebuild_and_instantiation(class_to_test):
    """Test that generated models can be rebuilt and instantiated successfully under Pydantic."""
    # Ensure model rebuilding is successful
    class_to_test.model_rebuild()
    assert class_to_test.__pydantic_complete__ is True

    # Ensure instantiation works with defaults
    instance = class_to_test()
    assert instance is not None


def test_get_referenced_types():
    """Test that _get_referenced_types successfully extracts referenced types from a model's annotations."""
    referenced = WebPage._get_referenced_types()

    # Check that representative types are part of the referenced namespace
    assert "URL" in referenced
    assert "ImageObject" in referenced
    assert "Text" in referenced


def test_cyclical_references_resolution():
    """Verify that custom models with cyclical forward references can resolve and rebuild without recursion errors."""

    class A(BaseModel):
        b: Optional[ForwardRef("B")] = None

    class B(BaseModel):
        a: Optional[List[A]] = None
        c: Optional[ForwardRef("C")] = None

    class C(BaseModel):
        b: Optional[B] = None

    # Resolve cyclical references
    B.model_rebuild(
        _types_namespace={"A": A, "C": C, "List": List, "Optional": Optional}
    )
    A.model_rebuild(_types_namespace={"B": B, "Optional": Optional})
    C.model_rebuild(_types_namespace={"B": B, "Optional": Optional})

    assert A.__pydantic_complete__ is True
    assert B.__pydantic_complete__ is True
    assert C.__pydantic_complete__ is True


@pytest.mark.parametrize(
    "forward_ref_str, expected_extracted",
    [
        (
            "Optional[Union[List[Union[AnyUrl, 'URL', str]], AnyUrl, 'URL', str]]",
            ["URL"],
        ),
        (
            "Optional[Union[List[Union['WebPageElement', str]], 'WebPageElement', str]]",
            ["WebPageElement"],
        ),
    ],
)
def test_forward_ref_evaluation_with_locals(forward_ref_str, expected_extracted):
    """Test ForwardRef evaluation mechanics with custom types namespace."""
    f = ForwardRef(forward_ref_str)

    class MockURL:
        pass

    class MockWebPageElement:
        pass

    localns = {
        "URL": MockURL,
        "WebPageElement": MockWebPageElement,
        "AnyUrl": AnyUrl,
        "Optional": Optional,
        "Union": Union,
        "List": List,
    }

    # Evaluate ForwardRef inside typical namespaces (handling python 3.13 signature)
    evaluated = f._evaluate(globals(), localns, frozenset(), recursive_guard=set())
    assert evaluated is not None
