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


class ListItem(Intangible):
    """An list item, e.g. a step in a checklist or how-to description.

    See: https://schema.org/ListItem
    Model depth: 3
    """
    valid_name: ClassVar[str] = "ListItem"
    type_: str = Field("ListItem", alias='@type')
    nextItem: Optional[Union[List[Union['ListItem', str]], 'ListItem', str]] = Field(
        default=None,
        description="A link to the ListItem that follows the current one.",
    )
    position: Optional[Union[List[Union[int, 'Integer', str, 'Text']], int, 'Integer', str, 'Text']] = Field(
        default=None,
        description="The position of an item in a series or sequence of items.",
    )
    item: Optional[Union[List[Union['Thing', str]], 'Thing', str]] = Field(
        default=None,
        description="An entity represented by an entry in a list or data feed (e.g. an 'artist' in a list of 'artists').",
    )
    previousItem: Optional[Union[List[Union['ListItem', str]], 'ListItem', str]] = Field(
        default=None,
        description="A link to the ListItem that precedes the current one.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Integer import Integer
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
