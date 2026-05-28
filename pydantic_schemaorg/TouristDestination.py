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
from pydantic_schemaorg.Place import Place


class TouristDestination(Place):
    """A tourist destination. In principle any [[Place]] can be a [[TouristDestination]]"
     "from a [[City]], Region or [[Country]] to an [[AmusementPark]] or [[Hotel]]. This Type"
     "can be used on its own to describe a general [[TouristDestination]], or be used as an [[additionalType]]"
     "to add tourist relevant properties to any other [[Place]]. A [[TouristDestination]]"
     "is defined as a [[Place]] that contains, or is colocated with, one or more [[TouristAttraction]]s,"
     "often linked by a similar theme or interest to a particular [[touristType]]. The [UNWTO](http://www2.unwto.org/)"
     "defines Destination (main destination of a tourism trip) as the place visited that is"
     "central to the decision to take the trip. (See examples below.)

    See: https://schema.org/TouristDestination
    Model depth: 3
    """
    valid_name: ClassVar[str] = "TouristDestination"
    type_: str = Field("TouristDestination", alias='@type')
    touristType: Optional[Union[List[Union[str, 'Text', 'Audience']], str, 'Text', 'Audience']] = Field(
        default=None,
        description="Attraction suitable for type(s) of tourist. E.g. children, visitors from a particular"
     "country, etc.",
    )
    includesAttraction: Optional[Union[List[Union['TouristAttraction', str]], 'TouristAttraction', str]] = Field(
        default=None,
        description="Attraction located at destination.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Audience import Audience
    from pydantic_schemaorg.TouristAttraction import TouristAttraction


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
