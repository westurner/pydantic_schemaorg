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
from pydantic_schemaorg.Clip import Clip


class TVClip(Clip):
    """A short TV program or a segment/part of a TV program.

    See: https://schema.org/TVClip
    Model depth: 4
    """
    valid_name: ClassVar[str] = "TVClip"
    type_: str = Field("TVClip", alias='@type')
    partOfTVSeries: Optional[Union[List[Union['TVSeries', str]], 'TVSeries', str]] = Field(
        default=None,
        description="The TV series to which this episode or season belongs.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.TVSeries import TVSeries


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
