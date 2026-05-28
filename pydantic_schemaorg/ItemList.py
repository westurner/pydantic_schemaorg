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
from pydantic_schemaorg.Intangible import Intangible


class ItemList(Intangible):
    """A list of items of any sort&#x2014;for example, Top 10 Movies About Weathermen, or Top"
     "100 Party Songs. Not to be confused with HTML lists, which are often used only for formatting.

    See: https://schema.org/ItemList
    Model depth: 3
    """
    valid_name: ClassVar[str] = "ItemList"
    type_: str = Field("ItemList", alias='@type')
    aggregateElement: Optional[Union[List[Union['Thing', str]], 'Thing', str]] = Field(
        default=None,
        description="Indicates a prototype of the elements in the list that is used to hold aggregate information"
     "(ratings, offers, etc.).",
    )
    itemListOrder: Optional[Union[List[Union[str, 'Text', 'ItemListOrderType']], str, 'Text', 'ItemListOrderType']] = Field(
        default=None,
        description="Type of ordering (e.g. Ascending, Descending, Unordered).",
    )
    numberOfItems: Optional[Union[List[Union[int, 'Integer', str]], int, 'Integer', str]] = Field(
        default=None,
        description="The number of items in an ItemList. Note that some descriptions might not fully describe"
     "all items in a list (e.g., multi-page pagination); in such cases, the numberOfItems"
     "would be for the entire list.",
    )
    itemListElement: Optional[Union[List[Union[str, 'Text', 'ListItem', 'Thing']], str, 'Text', 'ListItem', 'Thing']] = Field(
        default=None,
        description="For itemListElement values, you can use simple strings (e.g. \"Peter\", \"Paul\","
     "\"Mary\"), existing entities, or use ListItem. Text values are best if the elements"
     "in the list are plain strings. Existing entities are best for a simple, unordered list"
     "of existing things in your data. ListItem is used with ordered lists when you want to provide"
     "additional context about the element in that list or when the same item might be in different"
     "places in different lists. Note: The order of elements in your mark-up is not sufficient"
     "for indicating the order or elements. Use ListItem with a 'position' property in such"
     "cases.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Thing import Thing
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.ItemListOrderType import ItemListOrderType
    from pydantic_schemaorg.Integer import Integer
    from pydantic_schemaorg.ListItem import ListItem


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
