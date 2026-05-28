from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from typing import List, Optional, Union
from datetime import time


from pydantic import Field
from pydantic_schemaorg.StructuredValue import StructuredValue


class ServicePeriod(StructuredValue):
    """ServicePeriod represents a duration with some constraints about cutoff time and business"
     "days. This is used e.g. in shipping for handling times or transit time.

    See: https://schema.org/ServicePeriod
    Model depth: 4
    """
    valid_name: ClassVar[str] = "ServicePeriod"
    type_: str = Field("ServicePeriod", alias='@type')
    duration: Optional[Union[List[Union['QuantitativeValue', 'Duration', str]], 'QuantitativeValue', 'Duration', str]] = Field(
        default=None,
        description="The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 duration"
     "format](http://en.wikipedia.org/wiki/ISO_8601).",
    )
    cutoffTime: Optional[Union[List[Union[time, 'Time', str]], time, 'Time', str]] = Field(
        default=None,
        description="Order cutoff time allows merchants to describe the time after which they will no longer"
     "process orders received on that day. For orders processed after cutoff time, one day"
     "gets added to the delivery time estimate. This property is expected to be most typically"
     "used via the [[ShippingRateSettings]] publication pattern. The time is indicated"
     "using the ISO-8601 Time format, e.g. \"23:30:00-05:00\" would represent 6:30 pm Eastern"
     "Standard Time (EST) which is 5 hours behind Coordinated Universal Time (UTC).",
    )
    businessDays: Optional[Union[List[Union['OpeningHoursSpecification', 'DayOfWeek', str]], 'OpeningHoursSpecification', 'DayOfWeek', str]] = Field(
        default=None,
        description="Days of the week when the merchant typically operates, indicated via opening hours markup.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.Duration import Duration
    from pydantic_schemaorg.Time import Time
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
