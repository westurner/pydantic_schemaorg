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
from pydantic_schemaorg.Trip import Trip


class Flight(Trip):
    """An airline flight.

    See: https://schema.org/Flight
    Model depth: 4
    """
    valid_name: ClassVar[str] = "Flight"
    type_: str = Field("Flight", alias='@type')
    flightNumber: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The unique identifier for a flight including the airline IATA code. For example, if describing"
     "United flight 110, where the IATA code for United is 'UA', the flightNumber is 'UA110'.",
    )
    mealService: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Description of the meals that will be provided or available for purchase.",
    )
    estimatedFlightDuration: Optional[Union[List[Union[str, 'Text', 'Duration']], str, 'Text', 'Duration']] = Field(
        default=None,
        description="The estimated time the flight will take.",
    )
    webCheckinTime: Optional[Union[List[Union[datetime, 'DateTime', str]], datetime, 'DateTime', str]] = Field(
        default=None,
        description="The time when a passenger can check into the flight online.",
    )
    boardingPolicy: Optional[Union[List[Union['BoardingPolicyType', str]], 'BoardingPolicyType', str]] = Field(
        default=None,
        description="The type of boarding policy used by the airline (e.g. zone-based or group-based).",
    )
    carrier: Optional[Union[List[Union['Organization', str]], 'Organization', str]] = Field(
        default=None,
        description="'carrier' is an out-dated term indicating the 'provider' for parcel delivery and flights.",
    )
    seller: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="An entity which offers (sells / leases / lends / loans) the services / goods. A seller may"
     "also be a provider.",
    )
    arrivalGate: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Identifier of the flight's arrival gate.",
    )
    departureTerminal: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Identifier of the flight's departure terminal.",
    )
    arrivalAirport: Optional[Union[List[Union['Airport', str]], 'Airport', str]] = Field(
        default=None,
        description="The airport where the flight terminates.",
    )
    departureGate: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Identifier of the flight's departure gate.",
    )
    aircraft: Optional[Union[List[Union[str, 'Text', 'Vehicle']], str, 'Text', 'Vehicle']] = Field(
        default=None,
        description="The kind of aircraft (e.g., \"Boeing 747\").",
    )
    flightDistance: Optional[Union[List[Union[str, 'Text', 'Distance']], str, 'Text', 'Distance']] = Field(
        default=None,
        description="The distance of the flight.",
    )
    arrivalTerminal: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Identifier of the flight's arrival terminal.",
    )
    departureAirport: Optional[Union[List[Union['Airport', str]], 'Airport', str]] = Field(
        default=None,
        description="The airport where the flight originates.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Duration import Duration
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.BoardingPolicyType import BoardingPolicyType
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Airport import Airport
    from pydantic_schemaorg.Vehicle import Vehicle
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
