from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from typing import List, Optional, Union
from datetime import datetime


from pydantic import Field
from pydantic_schemaorg.Reservation import Reservation


class TaxiReservation(Reservation):
    """A reservation for a taxi. Note: This type is for information about actual reservations,"
     "e.g. in confirmation emails or HTML pages with individual confirmations of reservations."
     "For offers of tickets, use [[Offer]].

    See: https://schema.org/TaxiReservation
    Model depth: 4
    """
    valid_name: ClassVar[str] = "TaxiReservation"
    type_: str = Field("TaxiReservation", alias='@type')
    pickupLocation: Optional[Union[List[Union['Place', str]], 'Place', str]] = Field(
        default=None,
        description="Where a taxi will pick up a passenger or a rental car can be picked up.",
    )
    partySize: Optional[Union[List[Union[int, 'Integer', 'QuantitativeValue', str]], int, 'Integer', 'QuantitativeValue', str]] = Field(
        default=None,
        description="Number of people the reservation should accommodate.",
    )
    pickupTime: Optional[Union[List[Union[datetime, 'DateTime', str]], datetime, 'DateTime', str]] = Field(
        default=None,
        description="When a taxi will pick up a passenger or a rental car can be picked up.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Place import Place
    from pydantic_schemaorg.Integer import Integer
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.DateTime import DateTime


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
