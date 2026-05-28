from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from typing import List, Optional, Union
from datetime import datetime, time


from pydantic import Field
from pydantic_schemaorg.Reservation import Reservation


class LodgingReservation(Reservation):
    """A reservation for lodging at a hotel, motel, inn, etc. Note: This type is for information"
     "about actual reservations, e.g. in confirmation emails or HTML pages with individual"
     "confirmations of reservations.

    See: https://schema.org/LodgingReservation
    Model depth: 4
    """
    valid_name: ClassVar[str] = "LodgingReservation"
    type_: str = Field("LodgingReservation", alias='@type')
    lodgingUnitType: Optional[Union[List[Union[str, 'Text', 'QualitativeValue']], str, 'Text', 'QualitativeValue']] = Field(
        default=None,
        description="Textual description of the unit type (including suite vs. room, size of bed, etc.).",
    )
    lodgingUnitDescription: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="A full description of the lodging unit.",
    )
    numChildren: Optional[Union[List[Union[int, 'Integer', 'QuantitativeValue', str]], int, 'Integer', 'QuantitativeValue', str]] = Field(
        default=None,
        description="The number of children staying in the unit.",
    )
    numAdults: Optional[Union[List[Union[int, 'Integer', 'QuantitativeValue', str]], int, 'Integer', 'QuantitativeValue', str]] = Field(
        default=None,
        description="The number of adults staying in the unit.",
    )
    checkoutTime: Optional[Union[List[Union[datetime, 'DateTime', time, 'Time', str]], datetime, 'DateTime', time, 'Time', str]] = Field(
        default=None,
        description="The latest someone may check out of a lodging establishment.",
    )
    checkinTime: Optional[Union[List[Union[datetime, 'DateTime', time, 'Time', str]], datetime, 'DateTime', time, 'Time', str]] = Field(
        default=None,
        description="The earliest someone may check into a lodging establishment.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.QualitativeValue import QualitativeValue
    from pydantic_schemaorg.Integer import Integer
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Time import Time


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
