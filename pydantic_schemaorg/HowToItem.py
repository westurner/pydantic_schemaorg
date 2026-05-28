from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.ListItem import ListItem


class HowToItem(ListItem):
    """An item used as either a tool or supply when performing the instructions for how to achieve"
     "a result.

    See: https://schema.org/HowToItem
    Model depth: 4
    """
    valid_name: ClassVar[str] = "HowToItem"
    type_: str = Field("HowToItem", alias='@type')
    requiredQuantity: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', str, 'Text', 'QuantitativeValue']], StrictInt, StrictFloat, 'Number', str, 'Text', 'QuantitativeValue']] = Field(
        default=None,
        description="The required quantity of the item(s).",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue


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
