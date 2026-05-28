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
from pydantic_schemaorg.CreateAction import CreateAction


class CookAction(CreateAction):
    """The act of producing/preparing food.

    See: https://schema.org/CookAction
    Model depth: 4
    """
    valid_name: ClassVar[str] = "CookAction"
    type_: str = Field("CookAction", alias='@type')
    recipe: Optional[Union[List[Union['Recipe', str]], 'Recipe', str]] = Field(
        default=None,
        description="A sub property of instrument. The recipe/instructions used to perform the action.",
    )
    foodEstablishment: Optional[Union[List[Union['Place', 'FoodEstablishment', str]], 'Place', 'FoodEstablishment', str]] = Field(
        default=None,
        description="A sub property of location. The specific food establishment where the action occurred.",
    )
    foodEvent: Optional[Union[List[Union['FoodEvent', str]], 'FoodEvent', str]] = Field(
        default=None,
        description="A sub property of location. The specific food event where the action occurred.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Recipe import Recipe
    from pydantic_schemaorg.Place import Place
    from pydantic_schemaorg.FoodEstablishment import FoodEstablishment
    from pydantic_schemaorg.FoodEvent import FoodEvent


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
