from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from datetime import date, datetime, time
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.StructuredValue import StructuredValue


class OpeningHoursSpecification(StructuredValue):
    """A structured value providing information about the opening hours of a place or a certain"
     "service inside a place. The place is __open__ if the [[opens]] property is specified,"
     "and __closed__ otherwise. If the value for the [[closes]] property is less than the value"
     "for the [[opens]] property then the hour range is assumed to span over the next day.

    See: https://schema.org/OpeningHoursSpecification
    Model depth: 4
    """
    valid_name: ClassVar[str] = "OpeningHoursSpecification"
    type_: str = Field("OpeningHoursSpecification", alias='@type')
    opens: Optional[Union[List[Union[time, 'Time', str]], time, 'Time', str]] = Field(
        default=None,
        description="The opening hour of the place or service on the given day(s) of the week.",
    )
    closes: Optional[Union[List[Union[time, 'Time', str]], time, 'Time', str]] = Field(
        default=None,
        description="The closing hour of the place or service on the given day(s) of the week.",
    )
    dayOfWeek: Optional[Union[List[Union['DayOfWeek', str]], 'DayOfWeek', str]] = Field(
        default=None,
        description="The day of the week for which these opening hours are valid.",
    )
    validFrom: Optional[Union[List[Union[datetime, 'DateTime', date, 'Date', str]], datetime, 'DateTime', date, 'Date', str]] = Field(
        default=None,
        description="The date when the item becomes valid.",
    )
    validThrough: Optional[Union[List[Union[datetime, 'DateTime', date, 'Date', str]], datetime, 'DateTime', date, 'Date', str]] = Field(
        default=None,
        description="The date after when the item is not valid. For example the end of an offer, salary period,"
     "or a period of opening hours.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Time import Time
    from pydantic_schemaorg.DayOfWeek import DayOfWeek
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Date import Date


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
