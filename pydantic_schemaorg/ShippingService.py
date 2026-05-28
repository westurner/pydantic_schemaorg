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
from pydantic_schemaorg.StructuredValue import StructuredValue


class ShippingService(StructuredValue):
    """ShippingService represents the criteria used to determine if and how an offer could"
     "be shipped to a customer.

    See: https://schema.org/ShippingService
    Model depth: 4
    """
    valid_name: ClassVar[str] = "ShippingService"
    type_: str = Field("ShippingService", alias='@type')
    fulfillmentType: Optional[Union[List[Union['FulfillmentTypeEnumeration', str]], 'FulfillmentTypeEnumeration', str]] = Field(
        default=None,
        description="Type of fulfillment applicable to the [[ShippingService]].",
    )
    shippingConditions: Optional[Union[List[Union['ShippingConditions', str]], 'ShippingConditions', str]] = Field(
        default=None,
        description="The conditions (constraints, price) applicable to the [[ShippingService]].",
    )
    validForMemberTier: Optional[Union[List[Union['MemberProgramTier', str]], 'MemberProgramTier', str]] = Field(
        default=None,
        description="The membership program tier an Offer (or a PriceSpecification, OfferShippingDetails,"
     "or MerchantReturnPolicy under an Offer) is valid for.",
    )
    handlingTime: Optional[Union[List[Union['QuantitativeValue', 'ServicePeriod', str]], 'QuantitativeValue', 'ServicePeriod', str]] = Field(
        default=None,
        description="The typical delay between the receipt of the order and the goods either leaving the warehouse"
     "or being prepared for pickup, in case the delivery method is on site pickup. In the context"
     "of [[ShippingDeliveryTime]], Typical properties: minValue, maxValue, unitCode"
     "(d for DAY). This is by common convention assumed to mean business days (if a unitCode"
     "is used, coded as \"d\"), i.e. only counting days when the business normally operates."
     "In the context of [[ShippingService]], use the [[ServicePeriod]] format, that contains"
     "the same information in a structured form, with cut-off time, business days and duration.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.FulfillmentTypeEnumeration import FulfillmentTypeEnumeration
    from pydantic_schemaorg.ShippingConditions import ShippingConditions
    from pydantic_schemaorg.MemberProgramTier import MemberProgramTier
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.ServicePeriod import ServicePeriod


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
