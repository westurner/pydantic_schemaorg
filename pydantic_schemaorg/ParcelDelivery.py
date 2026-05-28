from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from datetime import date, datetime
from typing import List, Optional, Union
from pydantic import AnyUrl


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class ParcelDelivery(Intangible):
    """The delivery of a parcel either via the postal service or a commercial service.

    See: https://schema.org/ParcelDelivery
    Model depth: 3
    """
    valid_name: ClassVar[str] = "ParcelDelivery"
    type_: str = Field("ParcelDelivery", alias='@type')
    expectedArrivalUntil: Optional[Union[List[Union[datetime, 'DateTime', date, 'Date', str]], datetime, 'DateTime', date, 'Date', str]] = Field(
        default=None,
        description="The latest date the package may arrive.",
    )
    deliveryStatus: Optional[Union[List[Union['DeliveryEvent', str]], 'DeliveryEvent', str]] = Field(
        default=None,
        description="New entry added as the package passes through each leg of its journey (from shipment to"
     "final delivery).",
    )
    trackingNumber: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Shipper tracking number.",
    )
    provider: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="The service provider, service operator, or service performer; the goods producer."
     "Another party (a seller) may offer those services or goods on behalf of the provider."
     "A provider may also serve as the seller.",
    )
    carrier: Optional[Union[List[Union['Organization', str]], 'Organization', str]] = Field(
        default=None,
        description="'carrier' is an out-dated term indicating the 'provider' for parcel delivery and flights.",
    )
    hasDeliveryMethod: Optional[Union[List[Union['DeliveryMethod', str]], 'DeliveryMethod', str]] = Field(
        default=None,
        description="Method used for delivery or shipping.",
    )
    expectedArrivalFrom: Optional[Union[List[Union[datetime, 'DateTime', date, 'Date', str]], datetime, 'DateTime', date, 'Date', str]] = Field(
        default=None,
        description="The earliest date the package may arrive.",
    )
    trackingUrl: Optional[Union[List[Union[AnyUrl, 'URL', str]], AnyUrl, 'URL', str]] = Field(
        default=None,
        description="Tracking url for the parcel delivery.",
    )
    partOfOrder: Optional[Union[List[Union['Order', str]], 'Order', str]] = Field(
        default=None,
        description="The overall order the items in this delivery were included in.",
    )
    originAddress: Optional[Union[List[Union['PostalAddress', str]], 'PostalAddress', str]] = Field(
        default=None,
        description="Shipper's address.",
    )
    deliveryAddress: Optional[Union[List[Union['PostalAddress', str]], 'PostalAddress', str]] = Field(
        default=None,
        description="Destination address.",
    )
    itemShipped: Optional[Union[List[Union['Product', str]], 'Product', str]] = Field(
        default=None,
        description="Item(s) being shipped.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Date import Date
    from pydantic_schemaorg.DeliveryEvent import DeliveryEvent
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.DeliveryMethod import DeliveryMethod
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Order import Order
    from pydantic_schemaorg.PostalAddress import PostalAddress
    from pydantic_schemaorg.Product import Product


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
