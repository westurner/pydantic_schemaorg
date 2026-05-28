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
from pydantic_schemaorg.Trip import Trip


class TouristTrip(Trip):
    """A tourist trip. A created itinerary of visits to one or more places of interest ([[TouristAttraction]]/[[TouristDestination]])"
     "often linked by a similar theme, geographic area, or interest to a particular [[touristType]]."
     "The [UNWTO](http://www2.unwto.org/) defines tourism trip as the Trip taken by visitors."
     "(See examples below.)

    See: https://schema.org/TouristTrip
    Model depth: 4
    """
    valid_name: ClassVar[str] = "TouristTrip"
    type_: str = Field("TouristTrip", alias='@type')
    touristType: Optional[Union[List[Union[str, 'Text', 'Audience']], str, 'Text', 'Audience']] = Field(
        default=None,
        description="Attraction suitable for type(s) of tourist. E.g. children, visitors from a particular"
     "country, etc.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Audience import Audience


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
