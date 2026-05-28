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


class Map(CreativeWork):
    """A map.

    See: https://schema.org/Map
    Model depth: 3
    """
    valid_name: ClassVar[str] = "Map"
    type_: str = Field("Map", alias='@type')
    mapType: Optional[Union[List[Union['MapCategoryType', str]], 'MapCategoryType', str]] = Field(
        default=None,
        description="Indicates the kind of Map, from the MapCategoryType Enumeration.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.MapCategoryType import MapCategoryType


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
