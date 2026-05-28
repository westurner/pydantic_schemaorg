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


from pydantic import Field
from pydantic_schemaorg.PropertyValue import PropertyValue


class LocationFeatureSpecification(PropertyValue):
    """Specifies a location feature by providing a structured value representing a feature"
     "of an accommodation as a property-value pair of varying degrees of formality.

    See: https://schema.org/LocationFeatureSpecification
    Model depth: 5
    """
    valid_name: ClassVar[str] = "LocationFeatureSpecification"
    type_: str = Field("LocationFeatureSpecification", alias='@type')
    validFrom: Optional[Union[List[Union[datetime, 'DateTime', date, 'Date', str]], datetime, 'DateTime', date, 'Date', str]] = Field(
        default=None,
        description="The date when the item becomes valid.",
    )
    hoursAvailable: Optional[Union[List[Union['OpeningHoursSpecification', str]], 'OpeningHoursSpecification', str]] = Field(
        default=None,
        description="The hours during which this service or contact is available.",
    )
    validThrough: Optional[Union[List[Union[datetime, 'DateTime', date, 'Date', str]], datetime, 'DateTime', date, 'Date', str]] = Field(
        default=None,
        description="The date after when the item is not valid. For example the end of an offer, salary period,"
     "or a period of opening hours.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Date import Date
    from pydantic_schemaorg.OpeningHoursSpecification import OpeningHoursSpecification


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
