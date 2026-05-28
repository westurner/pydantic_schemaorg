from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from typing import List, Optional, Union
from pydantic import StrictInt, StrictFloat


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class OrderItem(Intangible):
    """An order item is a line of an order. It includes the quantity and shipping details of a bought"
     "offer.

    See: https://schema.org/OrderItem
    Model depth: 3
    """
    valid_name: ClassVar[str] = "OrderItem"
    type_: str = Field("OrderItem", alias='@type')
    orderItemNumber: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The identifier of the order item.",
    )
    orderedItem: Optional[Union[List[Union['Product', 'OrderItem', 'Service', str]], 'Product', 'OrderItem', 'Service', str]] = Field(
        default=None,
        description="The item ordered.",
    )
    orderDelivery: Optional[Union[List[Union['ParcelDelivery', str]], 'ParcelDelivery', str]] = Field(
        default=None,
        description="The delivery of the parcel related to this order or order item.",
    )
    orderItemStatus: Optional[Union[List[Union['OrderStatus', str]], 'OrderStatus', str]] = Field(
        default=None,
        description="The current status of the order item.",
    )
    orderQuantity: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', 'QuantitativeValue', str]], StrictInt, StrictFloat, 'Number', 'QuantitativeValue', str]] = Field(
        default=None,
        description="The number of the item ordered. If the property is not set, assume the quantity is one.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Product import Product
    from pydantic_schemaorg.Service import Service
    from pydantic_schemaorg.ParcelDelivery import ParcelDelivery
    from pydantic_schemaorg.OrderStatus import OrderStatus
    from pydantic_schemaorg.Number import Number
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
