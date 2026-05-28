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
from datetime import date, datetime


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class Ticket(Intangible):
    """Used to describe a ticket to an event, a flight, a bus ride, etc.

    See: https://schema.org/Ticket
    Model depth: 3
    """
    valid_name: ClassVar[str] = "Ticket"
    type_: str = Field("Ticket", alias='@type')
    issuedBy: Optional[Union[List[Union['Organization', str]], 'Organization', str]] = Field(
        default=None,
        description="The organization issuing the item, for example a [[Permit]], [[Ticket]], or [[Certification]].",
    )
    ticketToken: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        default=None,
        description="Reference to an asset (e.g., Barcode, QR code image or PDF) usable for entrance.",
    )
    ticketNumber: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The unique identifier for the ticket.",
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
    underName: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="The person or organization the reservation or ticket is for.",
    )
    dateIssued: Optional[Union[List[Union[datetime, 'DateTime', date, 'Date', str]], datetime, 'DateTime', date, 'Date', str]] = Field(
        default=None,
        description="The date the ticket was issued.",
    )
    ticketedSeat: Optional[Union[List[Union['Seat', str]], 'Seat', str]] = Field(
        default=None,
        description="The seat associated with the ticket.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.PriceSpecification import PriceSpecification
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Date import Date
    from pydantic_schemaorg.Seat import Seat


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
