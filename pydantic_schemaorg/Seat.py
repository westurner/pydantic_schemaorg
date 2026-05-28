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


class Seat(Intangible):
    """Used to describe a seat, such as a reserved seat in an event reservation.

    See: https://schema.org/Seat
    Model depth: 3
    """
    valid_name: ClassVar[str] = "Seat"
    type_: str = Field("Seat", alias='@type')
    seatSection: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The section location of the reserved seat (e.g. Orchestra).",
    )
    seatRow: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The row location of the reserved seat (e.g., B).",
    )
    seatingType: Optional[Union[List[Union[str, 'Text', 'QualitativeValue']], str, 'Text', 'QualitativeValue']] = Field(
        default=None,
        description="The type/class of the seat.",
    )
    seatNumber: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The location of the reserved seat (e.g., 27).",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.QualitativeValue import QualitativeValue


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
