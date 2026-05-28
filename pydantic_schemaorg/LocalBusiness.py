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
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.Place import Place


class LocalBusiness(Organization, Place):
    """A particular physical business or branch of an organization. Examples of LocalBusiness"
     "include a restaurant, a particular branch of a restaurant chain, a branch of a bank, a"
     "medical practice, a club, a bowling alley, etc.

    See: https://schema.org/LocalBusiness
    Model depth: 3
    """
    valid_name: ClassVar[str] = "LocalBusiness"
    type_: str = Field("LocalBusiness", alias='@type')
    currenciesAccepted: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The currency accepted. Use standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217),"
     "e.g. \"USD\"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies)"
     "for cryptocurrencies, e.g. \"BTC\"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system)"
     "(LETS) and other currency types, e.g. \"Ithaca HOUR\".",
    )
    openingHours: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The general opening hours for a business. Opening hours can be specified as a weekly time"
     "range, starting with days, then times per day. Multiple days can be listed with commas"
     "',' separating each day. Day or time ranges are specified using a hyphen '-'. * Days are"
     "specified using the following two-letter combinations: ```Mo```, ```Tu```, ```We```,"
     "```Th```, ```Fr```, ```Sa```, ```Su```. * Times are specified using 24:00 format."
     "For example, 3pm is specified as ```15:00```, 10am as ```10:00```. * Here is an example:"
     "<code>&lt;time itemprop=\"openingHours\" datetime=&quot;Tu,Th 16:00-20:00&quot;&gt;Tuesdays"
     "and Thursdays 4-8pm&lt;/time&gt;</code>. * If a business is open 7 days a week, then"
     "it can be specified as <code>&lt;time itemprop=&quot;openingHours&quot; datetime=&quot;Mo-Su&quot;&gt;Monday"
     "through Sunday, all day&lt;/time&gt;</code>.",
    )
    priceRange: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The price range of the business, for example ```$$$```.",
    )
    paymentAccepted: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Cash, Credit Card, Cryptocurrency, Local Exchange Tradings System, etc.",
    )
    branchOf: Optional[Union[List[Union['Organization', str]], 'Organization', str]] = Field(
        default=None,
        description="The larger organization that this local business is a branch of, if any. Not to be confused"
     "with (anatomical) [[branch]].",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Organization import Organization


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
