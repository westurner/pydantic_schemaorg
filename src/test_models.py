import pytest
from src.models import PydanticBase


def test_model_validator_sets_valid_name():
    # Case 1: normal name
    obj = PydanticBase(name="TestName", description="desc")
    assert obj.valid_name == "TestName"

    # Case 2: reserved keyword
    obj2 = PydanticBase(name="class", description="desc")
    assert obj2.valid_name == "class_"

    # Case 3: starts with digit
    obj3 = PydanticBase(name="1Test", description="desc")
    assert obj3.valid_name == "_1Test"

    # Case 4: valid_name provided
    obj4 = PydanticBase(name="Test", description="desc", valid_name="CustomName")
    assert obj4.valid_name == "CustomName"

    # Case 5: missing name should raise
    with pytest.raises(ValueError):
        PydanticBase(name=None, description="desc")
