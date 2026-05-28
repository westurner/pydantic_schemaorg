from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from pydantic import StrictBool, StrictInt, StrictFloat
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class PropertyValueSpecification(Intangible):
    """A Property value specification.

    See: https://schema.org/PropertyValueSpecification
    Model depth: 3
    """
    valid_name: ClassVar[str] = "PropertyValueSpecification"
    type_: str = Field("PropertyValueSpecification", alias='@type')
    valueMaxLength: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', str]], StrictInt, StrictFloat, 'Number', str]] = Field(
        default=None,
        description="Specifies the allowed range for number of characters in a literal value.",
    )
    readonlyValue: Optional[Union[List[Union[StrictBool, 'Boolean', str]], StrictBool, 'Boolean', str]] = Field(
        default=None,
        description="Whether or not a property is mutable. Default is false. Specifying this for a property"
     "that also has a value makes it act similar to a \"hidden\" input in an HTML form.",
    )
    valueRequired: Optional[Union[List[Union[StrictBool, 'Boolean', str]], StrictBool, 'Boolean', str]] = Field(
        default=None,
        description="Whether the property must be filled in to complete the action. Default is false.",
    )
    valueMinLength: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', str]], StrictInt, StrictFloat, 'Number', str]] = Field(
        default=None,
        description="Specifies the minimum allowed range for number of characters in a literal value.",
    )
    minValue: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', str]], StrictInt, StrictFloat, 'Number', str]] = Field(
        default=None,
        description="The lower value of some characteristic or property.",
    )
    multipleValues: Optional[Union[List[Union[StrictBool, 'Boolean', str]], StrictBool, 'Boolean', str]] = Field(
        default=None,
        description="Whether multiple values are allowed for the property. Default is false.",
    )
    defaultValue: Optional[Union[List[Union[str, 'Text', 'Thing']], str, 'Text', 'Thing']] = Field(
        default=None,
        description="The default value of the input. For properties that expect a literal, the default is a"
     "literal value, for properties that expect an object, it's an ID reference to one of the"
     "current values.",
    )
    maxValue: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', str]], StrictInt, StrictFloat, 'Number', str]] = Field(
        default=None,
        description="The upper value of some characteristic or property.",
    )
    valueName: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Indicates the name of the PropertyValueSpecification to be used in URL templates and"
     "form encoding in a manner analogous to HTML's input@name.",
    )
    stepValue: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', str]], StrictInt, StrictFloat, 'Number', str]] = Field(
        default=None,
        description="The stepValue attribute indicates the granularity that is expected (and required)"
     "of the value in a PropertyValueSpecification.",
    )
    valuePattern: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Specifies a regular expression for testing literal values according to the HTML spec.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.Boolean import Boolean
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Thing import Thing


def __getattr__(name: str) -> Any:
    from pydantic_schemaorg.__types__ import types
    if name in types:
        import sys
        mod_name = types[name][1]
        mod = sys.modules.get(mod_name)
        if not mod:
            __import__(mod_name, fromlist=[name])
            mod = sys.modules[mod_name]
        val = getattr(mod, name)
        globals()[name] = val
        return val
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
