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
from pydantic_schemaorg.CreativeWork import CreativeWork


class Menu(CreativeWork):
    """A structured representation of food or drink items available from a FoodEstablishment.

    See: https://schema.org/Menu
    Model depth: 3
    """
    valid_name: ClassVar[str] = "Menu"
    type_: str = Field("Menu", alias='@type')
    hasMenuItem: Optional[Union[List[Union['MenuItem', str]], 'MenuItem', str]] = Field(
        default=None,
        description="A food or drink item contained in a menu or menu section.",
    )
    hasMenuSection: Optional[Union[List[Union['MenuSection', str]], 'MenuSection', str]] = Field(
        default=None,
        description="A subgrouping of the menu (by dishes, course, serving time period, etc.).",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.MenuItem import MenuItem
    from pydantic_schemaorg.MenuSection import MenuSection


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
