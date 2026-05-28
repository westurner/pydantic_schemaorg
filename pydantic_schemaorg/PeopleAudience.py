from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from typing import List, Optional, Union
from pydantic import AnyUrl, StrictInt, StrictFloat


from pydantic import Field
from pydantic_schemaorg.Audience import Audience


class PeopleAudience(Audience):
    """A set of characteristics belonging to people, e.g. who compose an item's target audience.

    See: https://schema.org/PeopleAudience
    Model depth: 4
    """
    valid_name: ClassVar[str] = "PeopleAudience"
    type_: str = Field("PeopleAudience", alias='@type')
    suggestedGender: Optional[Union[List[Union[str, 'Text', 'GenderType']], str, 'Text', 'GenderType']] = Field(
        default=None,
        description="The suggested gender of the intended person or audience, for example \"male\", \"female\","
     "or \"unisex\".",
    )
    suggestedAge: Optional[Union[List[Union['QuantitativeValue', str]], 'QuantitativeValue', str]] = Field(
        default=None,
        description="The age or age range for the intended audience or person, for example 3-12 months for infants,"
     "1-5 years for toddlers.",
    )
    requiredMaxAge: Optional[Union[List[Union[int, 'Integer', str]], int, 'Integer', str]] = Field(
        default=None,
        description="Audiences defined by a person's maximum age.",
    )
    requiredMinAge: Optional[Union[List[Union[int, 'Integer', str]], int, 'Integer', str]] = Field(
        default=None,
        description="Audiences defined by a person's minimum age.",
    )
    healthCondition: Optional[Union[List[Union['MedicalCondition', str]], 'MedicalCondition', str]] = Field(
        default=None,
        description="Specifying the health condition(s) of a patient, medical study, or other target audience.",
    )
    suggestedMinAge: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', str]], StrictInt, StrictFloat, 'Number', str]] = Field(
        default=None,
        description="Minimum recommended age in years for the audience or user.",
    )
    suggestedMeasurement: Optional[Union[List[Union['QuantitativeValue', str]], 'QuantitativeValue', str]] = Field(
        default=None,
        description="A suggested range of body measurements for the intended audience or person, for example"
     "inseam between 32 and 34 inches or height between 170 and 190 cm. Typically found on a size"
     "chart for wearable products.",
    )
    suggestedMaxAge: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', str]], StrictInt, StrictFloat, 'Number', str]] = Field(
        default=None,
        description="Maximum recommended age in years for the audience or user.",
    )
    requiredGender: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Audiences defined by a person's gender.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.GenderType import GenderType
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.Integer import Integer
    from pydantic_schemaorg.MedicalCondition import MedicalCondition
    from pydantic_schemaorg.Number import Number


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
