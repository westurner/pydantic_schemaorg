from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from typing import List, Optional, Union
from pydantic import StrictBool


from pydantic import Field
from pydantic_schemaorg.StructuredValue import StructuredValue


class OfferShippingDetails(StructuredValue):
    """OfferShippingDetails represents information about shipping destinations. Multiple"
     "of these entities can be used to represent different shipping rates for different destinations:"
     "One entity for Alaska/Hawaii. A different one for continental US. A different one for"
     "all France. Multiple of these entities can be used to represent different shipping costs"
     "and delivery times. Two entities that are identical but differ in rate and time: E.g."
     "Cheaper and slower: $5 in 5-7 days or Fast and expensive: $15 in 1-2 days.

    See: https://schema.org/OfferShippingDetails
    Model depth: 4
    """
    valid_name: ClassVar[str] = "OfferShippingDetails"
    type_: str = Field("OfferShippingDetails", alias='@type')
    deliveryTime: Optional[Union[List[Union['ShippingDeliveryTime', str]], 'ShippingDeliveryTime', str]] = Field(
        default=None,
        description="The total delay between the receipt of the order and the goods reaching the final customer.",
    )
    shippingRate: Optional[Union[List[Union['MonetaryAmount', 'ShippingRateSettings', str]], 'MonetaryAmount', 'ShippingRateSettings', str]] = Field(
        default=None,
        description="The shipping rate is the cost of shipping to the specified destination. Typically, the"
     "maxValue and currency values (of the [[MonetaryAmount]]) are most appropriate.",
    )
    shippingDestination: Optional[Union[List[Union['DefinedRegion', str]], 'DefinedRegion', str]] = Field(
        default=None,
        description="indicates (possibly multiple) shipping destinations. These can be defined in several"
     "ways, e.g. postalCode ranges.",
    )
    hasShippingService: Optional[Union[List[Union['ShippingService', str]], 'ShippingService', str]] = Field(
        default=None,
        description="Specification of a shipping service offered by the organization.",
    )
    height: Optional[Union[List[Union['QuantitativeValue', 'Distance', str]], 'QuantitativeValue', 'Distance', str]] = Field(
        default=None,
        description="The height of the item.",
    )
    shippingOrigin: Optional[Union[List[Union['DefinedRegion', str]], 'DefinedRegion', str]] = Field(
        default=None,
        description="Indicates the origin of a shipment, i.e. where it should be coming from.",
    )
    width: Optional[Union[List[Union['QuantitativeValue', 'Distance', str]], 'QuantitativeValue', 'Distance', str]] = Field(
        default=None,
        description="The width of the item.",
    )
    depth: Optional[Union[List[Union['QuantitativeValue', 'Distance', str]], 'QuantitativeValue', 'Distance', str]] = Field(
        default=None,
        description="The depth of the item.",
    )
    weight: Optional[Union[List[Union['QuantitativeValue', 'Mass', str]], 'QuantitativeValue', 'Mass', str]] = Field(
        default=None,
        description="The weight of the product or person.",
    )
    validForMemberTier: Optional[Union[List[Union['MemberProgramTier', str]], 'MemberProgramTier', str]] = Field(
        default=None,
        description="The membership program tier an Offer (or a PriceSpecification, OfferShippingDetails,"
     "or MerchantReturnPolicy under an Offer) is valid for.",
    )
    doesNotShip: Optional[Union[List[Union[StrictBool, 'Boolean', str]], StrictBool, 'Boolean', str]] = Field(
        default=None,
        description="Indicates when shipping to a particular [[shippingDestination]] is not available.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.ShippingDeliveryTime import ShippingDeliveryTime
    from pydantic_schemaorg.MonetaryAmount import MonetaryAmount
    from pydantic_schemaorg.ShippingRateSettings import ShippingRateSettings
    from pydantic_schemaorg.DefinedRegion import DefinedRegion
    from pydantic_schemaorg.ShippingService import ShippingService
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.Distance import Distance
    from pydantic_schemaorg.Mass import Mass
    from pydantic_schemaorg.MemberProgramTier import MemberProgramTier
    from pydantic_schemaorg.Boolean import Boolean


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
