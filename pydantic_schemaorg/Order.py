from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from typing import List, Optional, Union
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat
from datetime import date, datetime


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class Order(Intangible):
    """An order is a confirmation of a transaction (a receipt), which can contain multiple line"
     "items, each represented by an Offer that has been accepted by the customer.

    See: https://schema.org/Order
    Model depth: 3
    """
    valid_name: ClassVar[str] = "Order"
    type_: str = Field("Order", alias='@type')
    paymentMethodId: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="An identifier for the method of payment used (e.g. the last 4 digits of the credit card).",
    )
    billingAddress: Optional[Union[List[Union['PostalAddress', str]], 'PostalAddress', str]] = Field(
        default=None,
        description="The billing address for the order.",
    )
    confirmationNumber: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="A number that confirms the given order or payment has been received.",
    )
    paymentMethod: Optional[Union[List[Union[str, 'Text', 'PaymentMethod']], str, 'Text', 'PaymentMethod']] = Field(
        default=None,
        description="The name of the credit card or other method of payment for the order.",
    )
    discountCurrency: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The currency of the discount. Use standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217),"
     "e.g. \"USD\"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies)"
     "for cryptocurrencies, e.g. \"BTC\"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system)"
     "(LETS) and other currency types, e.g. \"Ithaca HOUR\".",
    )
    orderedItem: Optional[Union[List[Union['Product', 'OrderItem', 'Service', str]], 'Product', 'OrderItem', 'Service', str]] = Field(
        default=None,
        description="The item ordered.",
    )
    merchant: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="'merchant' is an out-dated term for 'seller'.",
    )
    seller: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="An entity which offers (sells / leases / lends / loans) the services / goods. A seller may"
     "also be a provider.",
    )
    partOfInvoice: Optional[Union[List[Union['Invoice', str]], 'Invoice', str]] = Field(
        default=None,
        description="The order is being paid as part of the referenced Invoice.",
    )
    isGift: Optional[Union[List[Union[StrictBool, 'Boolean', str]], StrictBool, 'Boolean', str]] = Field(
        default=None,
        description="Indicates whether the offer was accepted as a gift for someone other than the buyer.",
    )
    orderDelivery: Optional[Union[List[Union['ParcelDelivery', str]], 'ParcelDelivery', str]] = Field(
        default=None,
        description="The delivery of the parcel related to this order or order item.",
    )
    discountCode: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Code used to redeem a discount.",
    )
    paymentDueDate: Optional[Union[List[Union[datetime, 'DateTime', date, 'Date', str]], datetime, 'DateTime', date, 'Date', str]] = Field(
        default=None,
        description="The date that payment is due.",
    )
    broker: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="An entity that arranges for an exchange between a buyer and a seller. In most cases a broker"
     "never acquires or releases ownership of a product or service involved in an exchange."
     "If it is not clear whether an entity is a broker, seller, or buyer, the latter two terms"
     "are preferred.",
    )
    discount: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', str, 'Text']], StrictInt, StrictFloat, 'Number', str, 'Text']] = Field(
        default=None,
        description="Any discount applied (to an Order).",
    )
    orderDate: Optional[Union[List[Union[datetime, 'DateTime', date, 'Date', str]], datetime, 'DateTime', date, 'Date', str]] = Field(
        default=None,
        description="Date order was placed.",
    )
    acceptedOffer: Optional[Union[List[Union['Offer', str]], 'Offer', str]] = Field(
        default=None,
        description="The offer(s) -- e.g., product, quantity and price combinations -- included in the order.",
    )
    customer: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="Party placing the order or paying the invoice.",
    )
    paymentUrl: Optional[Union[List[Union[AnyUrl, 'URL', str]], AnyUrl, 'URL', str]] = Field(
        default=None,
        description="The URL for sending a payment.",
    )
    orderNumber: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The identifier of the transaction.",
    )
    orderStatus: Optional[Union[List[Union['OrderStatus', str]], 'OrderStatus', str]] = Field(
        default=None,
        description="The current status of the order.",
    )
    paymentDue: Optional[Union[List[Union[datetime, 'DateTime', str]], datetime, 'DateTime', str]] = Field(
        default=None,
        description="The date that payment is due.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.PostalAddress import PostalAddress
    from pydantic_schemaorg.PaymentMethod import PaymentMethod
    from pydantic_schemaorg.Product import Product
    from pydantic_schemaorg.OrderItem import OrderItem
    from pydantic_schemaorg.Service import Service
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.Invoice import Invoice
    from pydantic_schemaorg.Boolean import Boolean
    from pydantic_schemaorg.ParcelDelivery import ParcelDelivery
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Date import Date
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.Offer import Offer
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.OrderStatus import OrderStatus


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
