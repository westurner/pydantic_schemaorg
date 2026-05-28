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


class ShippingConditions(StructuredValue):
    """ShippingConditions represent a set of constraints and information about the conditions"
     "of shipping a product. Such conditions may apply to only a subset of the products being"
     "shipped, depending on aspects of the product like weight, size, price, destination,"
     "and others. All the specified conditions must be met for this ShippingConditions to"
     "apply.

    See: https://schema.org/ShippingConditions
    Model depth: 4
    """
    valid_name: ClassVar[str] = "ShippingConditions"
    type_: str = Field("ShippingConditions", alias='@type')
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
    transitTime: Optional[Union[List[Union['QuantitativeValue', 'ServicePeriod', str]], 'QuantitativeValue', 'ServicePeriod', str]] = Field(
        default=None,
        description="The typical delay the order has been sent for delivery and the goods reach the final customer."
     "In the context of [[ShippingDeliveryTime]], use the [[QuantitativeValue]]. Typical"
     "properties: minValue, maxValue, unitCode (d for DAY). In the context of [[ShippingConditions]],"
     "use the [[ServicePeriod]]. It has a duration (as a [[QuantitativeValue]]) and also"
     "business days and a cut-off time.",
    )
    height: Optional[Union[List[Union['QuantitativeValue', 'Distance', str]], 'QuantitativeValue', 'Distance', str]] = Field(
        default=None,
        description="The height of the item.",
    )
    seasonalOverride: Optional[Union[List[Union['OpeningHoursSpecification', str]], 'OpeningHoursSpecification', str]] = Field(
        default=None,
        description="Limited period during which these shipping conditions apply.",
    )
    shippingOrigin: Optional[Union[List[Union['DefinedRegion', str]], 'DefinedRegion', str]] = Field(
        default=None,
        description="Indicates the origin of a shipment, i.e. where it should be coming from.",
    )
    numItems: Optional[Union[List[Union['QuantitativeValue', str]], 'QuantitativeValue', str]] = Field(
        default=None,
        description="Limits the number of items being shipped for which these conditions apply.",
    )
    width: Optional[Union[List[Union['QuantitativeValue', 'Distance', str]], 'QuantitativeValue', 'Distance', str]] = Field(
        default=None,
        description="The width of the item.",
    )
    orderValue: Optional[Union[List[Union['MonetaryAmount', str]], 'MonetaryAmount', str]] = Field(
        default=None,
        description="Minimum and maximum order value for which these shipping conditions are valid.",
    )
    depth: Optional[Union[List[Union['QuantitativeValue', 'Distance', str]], 'QuantitativeValue', 'Distance', str]] = Field(
        default=None,
        description="The depth of the item.",
    )
    weight: Optional[Union[List[Union['QuantitativeValue', 'Mass', str]], 'QuantitativeValue', 'Mass', str]] = Field(
        default=None,
        description="The weight of the product or person.",
    )
    doesNotShip: Optional[Union[List[Union[StrictBool, 'Boolean', str]], StrictBool, 'Boolean', str]] = Field(
        default=None,
        description="Indicates when shipping to a particular [[shippingDestination]] is not available.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.MonetaryAmount import MonetaryAmount
    from pydantic_schemaorg.ShippingRateSettings import ShippingRateSettings
    from pydantic_schemaorg.DefinedRegion import DefinedRegion
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.ServicePeriod import ServicePeriod
    from pydantic_schemaorg.Distance import Distance
    from pydantic_schemaorg.OpeningHoursSpecification import OpeningHoursSpecification
    from pydantic_schemaorg.Mass import Mass
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
