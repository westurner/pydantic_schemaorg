from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from datetime import datetime, time
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.Reservation import Reservation


class FoodEstablishmentReservation(Reservation):
    """A reservation to dine at a food-related business. Note: This type is for information"
     "about actual reservations, e.g. in confirmation emails or HTML pages with individual"
     "confirmations of reservations.

    See: https://schema.org/FoodEstablishmentReservation
    Model depth: 4
    """
    valid_name: ClassVar[str] = "FoodEstablishmentReservation"
    type_: str = Field("FoodEstablishmentReservation", alias='@type')
    startTime: Optional[Union[List[Union[datetime, 'DateTime', time, 'Time', str]], datetime, 'DateTime', time, 'Time', str]] = Field(
        default=None,
        description="The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation),"
     "the time that it is expected to start. For actions that span a period of time, when the action"
     "was performed. E.g. John wrote a book from *January* to December. For media, including"
     "audio and video, it's the time offset of the start of a clip within a larger file. Note that"
     "Event uses startDate/endDate instead of startTime/endTime, even when describing"
     "dates with times. This situation may be clarified in future revisions.",
    )
    partySize: Optional[Union[List[Union[int, 'Integer', 'QuantitativeValue', str]], int, 'Integer', 'QuantitativeValue', str]] = Field(
        default=None,
        description="Number of people the reservation should accommodate.",
    )
    endTime: Optional[Union[List[Union[datetime, 'DateTime', time, 'Time', str]], datetime, 'DateTime', time, 'Time', str]] = Field(
        default=None,
        description="The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation),"
     "the time that it is expected to end. For actions that span a period of time, when the action"
     "was performed. E.g. John wrote a book from January to *December*. For media, including"
     "audio and video, it's the time offset of the end of a clip within a larger file. Note that"
     "Event uses startDate/endDate instead of startTime/endTime, even when describing"
     "dates with times. This situation may be clarified in future revisions.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Time import Time
    from pydantic_schemaorg.Integer import Integer
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
