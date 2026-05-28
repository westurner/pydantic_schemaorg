from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from pydantic import StrictInt, StrictFloat
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.EntertainmentBusiness import EntertainmentBusiness
from pydantic_schemaorg.CivicStructure import CivicStructure


class MovieTheater(EntertainmentBusiness, CivicStructure):
    """A movie theater.

    See: https://schema.org/MovieTheater
    Model depth: 4
    """
    valid_name: ClassVar[str] = "MovieTheater"
    type_: str = Field("MovieTheater", alias='@type')
    screenCount: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', str]], StrictInt, StrictFloat, 'Number', str]] = Field(
        default=None,
        description="The number of screens in the movie theater.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Number import Number


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
