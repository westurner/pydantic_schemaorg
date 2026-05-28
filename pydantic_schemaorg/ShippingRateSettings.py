from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from typing import List, Optional, Union
from pydantic import StrictBool, StrictInt, StrictFloat


from pydantic import Field
from pydantic_schemaorg.StructuredValue import StructuredValue


class ShippingRateSettings(StructuredValue):
    """A ShippingRateSettings represents re-usable pieces of shipping information. It is"
     "designed for publication on an URL that may be referenced via the [[shippingSettingsLink]]"
     "property of an [[OfferShippingDetails]]. Several occurrences can be published, distinguished"
     "and matched (i.e. identified/referenced) by their different values for [[shippingLabel]].

    See: https://schema.org/ShippingRateSettings
    Model depth: 4
    """
    valid_name: ClassVar[str] = "ShippingRateSettings"
    type_: str = Field("ShippingRateSettings", alias='@type')
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
    weightPercentage: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', str]], StrictInt, StrictFloat, 'Number', str]] = Field(
        default=None,
        description="Fraction of the weight that is used to compute the shipping price.",
    )
    isUnlabelledFallback: Optional[Union[List[Union[StrictBool, 'Boolean', str]], StrictBool, 'Boolean', str]] = Field(
        default=None,
        description="This can be marked 'true' to indicate that some published [[DeliveryTimeSettings]]"
     "or [[ShippingRateSettings]] are intended to apply to all [[OfferShippingDetails]]"
     "published by the same merchant, when referenced by a [[shippingSettingsLink]] in those"
     "settings. It is not meaningful to use a 'true' value for this property alongside a transitTimeLabel"
     "(for [[DeliveryTimeSettings]]) or shippingLabel (for [[ShippingRateSettings]]),"
     "since this property is for use with unlabelled settings.",
    )
    freeShippingThreshold: Optional[Union[List[Union['MonetaryAmount', 'DeliveryChargeSpecification', str]], 'MonetaryAmount', 'DeliveryChargeSpecification', str]] = Field(
        default=None,
        description="A monetary value above (or at) which the shipping rate becomes free. Intended to be used"
     "via an [[OfferShippingDetails]] with [[shippingSettingsLink]] matching this [[ShippingRateSettings]].",
    )
    orderPercentage: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', str]], StrictInt, StrictFloat, 'Number', str]] = Field(
        default=None,
        description="Fraction of the value of the order that is charged as shipping cost.",
    )
    doesNotShip: Optional[Union[List[Union[StrictBool, 'Boolean', str]], StrictBool, 'Boolean', str]] = Field(
        default=None,
        description="Indicates when shipping to a particular [[shippingDestination]] is not available.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.MonetaryAmount import MonetaryAmount
    from pydantic_schemaorg.DefinedRegion import DefinedRegion
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.Boolean import Boolean
    from pydantic_schemaorg.DeliveryChargeSpecification import DeliveryChargeSpecification


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
