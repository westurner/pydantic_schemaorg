from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.StructuredValue import StructuredValue


class NutritionInformation(StructuredValue):
    """Nutritional information about the recipe.

    See: https://schema.org/NutritionInformation
    Model depth: 4
    """
    valid_name: ClassVar[str] = "NutritionInformation"
    type_: str = Field("NutritionInformation", alias='@type')
    saturatedFatContent: Optional[Union[List[Union['Mass', str]], 'Mass', str]] = Field(
        default=None,
        description="The number of grams of saturated fat.",
    )
    unsaturatedFatContent: Optional[Union[List[Union['Mass', str]], 'Mass', str]] = Field(
        default=None,
        description="The number of grams of unsaturated fat.",
    )
    sodiumContent: Optional[Union[List[Union['Mass', str]], 'Mass', str]] = Field(
        default=None,
        description="The number of milligrams of sodium.",
    )
    fatContent: Optional[Union[List[Union['Mass', str]], 'Mass', str]] = Field(
        default=None,
        description="The number of grams of fat.",
    )
    transFatContent: Optional[Union[List[Union['Mass', str]], 'Mass', str]] = Field(
        default=None,
        description="The number of grams of trans fat.",
    )
    servingSize: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The serving size, in terms of the number of volume or mass.",
    )
    sugarContent: Optional[Union[List[Union['Mass', str]], 'Mass', str]] = Field(
        default=None,
        description="The number of grams of sugar.",
    )
    proteinContent: Optional[Union[List[Union['Mass', str]], 'Mass', str]] = Field(
        default=None,
        description="The number of grams of protein.",
    )
    calories: Optional[Union[List[Union['Energy', str]], 'Energy', str]] = Field(
        default=None,
        description="The number of calories.",
    )
    carbohydrateContent: Optional[Union[List[Union['Mass', str]], 'Mass', str]] = Field(
        default=None,
        description="The number of grams of carbohydrates.",
    )
    fiberContent: Optional[Union[List[Union['Mass', str]], 'Mass', str]] = Field(
        default=None,
        description="The number of grams of fiber.",
    )
    cholesterolContent: Optional[Union[List[Union['Mass', str]], 'Mass', str]] = Field(
        default=None,
        description="The number of milligrams of cholesterol.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Mass import Mass
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Energy import Energy


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
