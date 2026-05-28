import pytest
from src.models import PydanticClass, PydanticField, Import
from src.schema_org import SchemaOrg

# Dummy schema_org data for testing
SCHEMA_ORG_DUMMY = {
    "schema:TestClass": {
        "@type": "schema:Thing",
        "rdfs:comment": "A test class."
    },
    "schema:TestField": {
        "@type": "rdf:Property",
        "rdfs:comment": "A test field.",
        "schema:domainIncludes": [
            {"@id": "schema:TestClass"}
        ],
        "schema:rangeIncludes": [
            {"@id": "schema:Text"}
        ]
    }
}

def test_valid_name():
    cls = PydanticClass(name="class", description="desc", fields=[], parents=[], parent_imports=[], field_imports=[])
    assert cls.valid_name == "class_"
    cls2 = PydanticClass(name="1abc", description="desc", fields=[], parents=[], parent_imports=[], field_imports=[])
    assert cls2.valid_name == "_1abc"
    cls3 = PydanticClass(name="MyClass", description="desc", fields=[], parents=[], parent_imports=[], field_imports=[])
    assert cls3.valid_name == "MyClass"

def test_schema_org_load_type():
    schema_org_api = SchemaOrg(
        schema_org=SCHEMA_ORG_DUMMY,
        type_map={},
        type_specificity={}
    )
    result = schema_org_api.load_type("TestClass")
    assert isinstance(result, PydanticClass)
    assert result.name == "TestClass"
    assert result.valid_name == "TestClass"
    assert result.description == "A test class."

def test_schema_org_get_all_classes():
    schema_org_api = SchemaOrg(
        schema_org=SCHEMA_ORG_DUMMY,
        type_map={},
        type_specificity={}
    )
    classes = schema_org_api.get_all_classes()
    assert "TestClass" in classes
    for cls in classes:
        assert cls is not None
