from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from datetime import time
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.StructuredValue import StructuredValue


class ShippingDeliveryTime(StructuredValue):
    """ShippingDeliveryTime provides various pieces of information about delivery times"
     "for shipping.

    See: https://schema.org/ShippingDeliveryTime
    Model depth: 4
    """
    valid_name: ClassVar[str] = "ShippingDeliveryTime"
    type_: str = Field("ShippingDeliveryTime", alias='@type')
    cutoffTime: Optional[Union[List[Union[time, 'Time', str]], time, 'Time', str]] = Field(
        default=None,
        description="Order cutoff time allows merchants to describe the time after which they will no longer"
     "process orders received on that day. For orders processed after cutoff time, one day"
     "gets added to the delivery time estimate. This property is expected to be most typically"
     "used via the [[ShippingRateSettings]] publication pattern. The time is indicated"
     "using the ISO-8601 Time format, e.g. \"23:30:00-05:00\" would represent 6:30 pm Eastern"
     "Standard Time (EST) which is 5 hours behind Coordinated Universal Time (UTC).",
    )
    transitTime: Optional[Union[List[Union['QuantitativeValue', 'ServicePeriod', str]], 'QuantitativeValue', 'ServicePeriod', str]] = Field(
        default=None,
        description="The typical delay the order has been sent for delivery and the goods reach the final customer."
     "In the context of [[ShippingDeliveryTime]], use the [[QuantitativeValue]]. Typical"
     "properties: minValue, maxValue, unitCode (d for DAY). In the context of [[ShippingConditions]],"
     "use the [[ServicePeriod]]. It has a duration (as a [[QuantitativeValue]]) and also"
     "business days and a cut-off time.",
    )
    businessDays: Optional[Union[List[Union['OpeningHoursSpecification', 'DayOfWeek', str]], 'OpeningHoursSpecification', 'DayOfWeek', str]] = Field(
        default=None,
        description="Days of the week when the merchant typically operates, indicated via opening hours markup.",
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
    from pydantic_schemaorg.Time import Time
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.ServicePeriod import ServicePeriod
    from pydantic_schemaorg.OpeningHoursSpecification import OpeningHoursSpecification
    from pydantic_schemaorg.DayOfWeek import DayOfWeek


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
