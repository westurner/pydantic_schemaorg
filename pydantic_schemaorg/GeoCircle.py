from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from pydantic import StrictInt, StrictFloat
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.GeoShape import GeoShape


class GeoCircle(GeoShape):
    """A GeoCircle is a GeoShape representing a circular geographic area. As it is a GeoShape"
     "it provides the simple textual property 'circle', but also allows the combination of"
     "postalCode alongside geoRadius. The center of the circle can be indicated via the 'geoMidpoint'"
     "property, or more approximately using 'address', 'postalCode'.

    See: https://schema.org/GeoCircle
    Model depth: 5
    """
    valid_name: ClassVar[str] = "GeoCircle"
    type_: str = Field("GeoCircle", alias='@type')
    geoRadius: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', str, 'Text', 'Distance']], StrictInt, StrictFloat, 'Number', str, 'Text', 'Distance']] = Field(
        default=None,
        description="Indicates the approximate radius of a GeoCircle (metres unless indicated otherwise"
     "via Distance notation).",
    )
    geoMidpoint: Optional[Union[List[Union['GeoCoordinates', str]], 'GeoCoordinates', str]] = Field(
        default=None,
        description="Indicates the GeoCoordinates at the centre of a GeoShape, e.g. GeoCircle.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Distance import Distance
    from pydantic_schemaorg.GeoCoordinates import GeoCoordinates


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
