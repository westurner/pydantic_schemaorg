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
from pydantic_schemaorg.MoveAction import MoveAction


class TravelAction(MoveAction):
    """The act of traveling from a fromLocation to a destination by a specified mode of transport,"
     "optionally with participants.

    See: https://schema.org/TravelAction
    Model depth: 4
    """
    valid_name: ClassVar[str] = "TravelAction"
    type_: str = Field("TravelAction", alias='@type')
    distance: Optional[Union[List[Union['Distance', str]], 'Distance', str]] = Field(
        default=None,
        description="The distance travelled, e.g. exercising or travelling.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Distance import Distance


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
