from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from typing import List, Optional, Union
from pydantic import AnyUrl, StrictInt, StrictFloat
from datetime import datetime


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class Reservation(Intangible):
    """Describes a reservation for travel, dining or an event. Some reservations require tickets."
     "Note: This type is for information about actual reservations, e.g. in confirmation"
     "emails or HTML pages with individual confirmations of reservations. For offers of tickets,"
     "restaurant reservations, flights, or rental cars, use [[Offer]].

    See: https://schema.org/Reservation
    Model depth: 3
    """
    valid_name: ClassVar[str] = "Reservation"
    type_: str = Field("Reservation", alias='@type')
    provider: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="The service provider, service operator, or service performer; the goods producer."
     "Another party (a seller) may offer those services or goods on behalf of the provider."
     "A provider may also serve as the seller.",
    )
    totalPrice: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', str, 'Text', 'PriceSpecification']], StrictInt, StrictFloat, 'Number', str, 'Text', 'PriceSpecification']] = Field(
        default=None,
        description="The total price for the reservation or ticket, including applicable taxes, shipping,"
     "etc. Usage guidelines: * Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030)"
     "to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols. * Use"
     "'.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid"
     "using these symbols as a readability separator.",
    )
    priceCurrency: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The currency of the price, or a price component when attached to [[PriceSpecification]]"
     "and its subtypes. Use standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217),"
     "e.g. \"USD\"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies)"
     "for cryptocurrencies, e.g. \"BTC\"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system)"
     "(LETS) and other currency types, e.g. \"Ithaca HOUR\".",
    )
    modifiedTime: Optional[Union[List[Union[datetime, 'DateTime', str]], datetime, 'DateTime', str]] = Field(
        default=None,
        description="The date and time the reservation was modified.",
    )
    reservedTicket: Optional[Union[List[Union['Ticket', str]], 'Ticket', str]] = Field(
        default=None,
        description="A ticket associated with the reservation.",
    )
    bookingAgent: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="'bookingAgent' is an out-dated term indicating a 'broker' that serves as a booking agent.",
    )
    reservationStatus: Optional[Union[List[Union['ReservationStatusType', str]], 'ReservationStatusType', str]] = Field(
        default=None,
        description="The current status of the reservation.",
    )
    underName: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="The person or organization the reservation or ticket is for.",
    )
    reservationFor: Optional[Union[List[Union['Thing', str]], 'Thing', str]] = Field(
        default=None,
        description="The thing -- flight, event, restaurant, etc. being reserved.",
    )
    broker: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="An entity that arranges for an exchange between a buyer and a seller. In most cases a broker"
     "never acquires or releases ownership of a product or service involved in an exchange."
     "If it is not clear whether an entity is a broker, seller, or buyer, the latter two terms"
     "are preferred.",
    )
    programMembershipUsed: Optional[Union[List[Union['ProgramMembership', str]], 'ProgramMembership', str]] = Field(
        default=None,
        description="Any membership in a frequent flyer, hotel loyalty program, etc. being applied to the"
     "reservation.",
    )
    bookingTime: Optional[Union[List[Union[datetime, 'DateTime', str]], datetime, 'DateTime', str]] = Field(
        default=None,
        description="The date and time the reservation was booked.",
    )
    reservationId: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="A unique identifier for the reservation.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.PriceSpecification import PriceSpecification
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Ticket import Ticket
    from pydantic_schemaorg.ReservationStatusType import ReservationStatusType
    from pydantic_schemaorg.Thing import Thing
    from pydantic_schemaorg.ProgramMembership import ProgramMembership


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
