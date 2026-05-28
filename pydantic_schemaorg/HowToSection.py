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
from pydantic_schemaorg.ListItem import ListItem
from pydantic_schemaorg.ItemList import ItemList
from pydantic_schemaorg.CreativeWork import CreativeWork


class HowToSection(ListItem, ItemList, CreativeWork):
    """A sub-grouping of steps in the instructions for how to achieve a result (e.g. steps for"
     "making a pie crust within a pie recipe).

    See: https://schema.org/HowToSection
    Model depth: 3
    """
    valid_name: ClassVar[str] = "HowToSection"
    type_: str = Field("HowToSection", alias='@type')
    steps: Optional[Union[List[Union[str, 'Text', 'CreativeWork', 'ItemList']], str, 'Text', 'CreativeWork', 'ItemList']] = Field(
        default=None,
        description="A single step item (as HowToStep, text, document, video, etc.) or a HowToSection (originally"
     "misnamed 'steps'; 'step' is preferred).",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.CreativeWork import CreativeWork
    from pydantic_schemaorg.ItemList import ItemList


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
