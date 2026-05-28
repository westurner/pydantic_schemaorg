from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from typing import List, Optional, Union
from pydantic import AnyUrl, StrictBool
from datetime import date, datetime, time


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class ActionAccessSpecification(Intangible):
    """A set of requirements that must be fulfilled in order to perform an Action.

    See: https://schema.org/ActionAccessSpecification
    Model depth: 3
    """
    valid_name: ClassVar[str] = "ActionAccessSpecification"
    type_: str = Field("ActionAccessSpecification", alias='@type')
    eligibleRegion: Optional[Union[List[Union[str, 'Text', 'Place', 'GeoShape']], str, 'Text', 'Place', 'GeoShape']] = Field(
        default=None,
        description="The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for"
     "the geo-political region(s) for which the offer or delivery charge specification is"
     "valid. See also [[ineligibleRegion]].",
    )
    requiresSubscription: Optional[Union[List[Union[StrictBool, 'Boolean', 'MediaSubscription', str]], StrictBool, 'Boolean', 'MediaSubscription', str]] = Field(
        default=None,
        description="Indicates if use of the media require a subscription (either paid or free). Allowed values"
     "are ```true``` or ```false``` (note that an earlier version had 'yes', 'no').",
    )
    ineligibleRegion: Optional[Union[List[Union[str, 'Text', 'Place', 'GeoShape']], str, 'Text', 'Place', 'GeoShape']] = Field(
        default=None,
        description="The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for"
     "the geo-political region(s) for which the offer or delivery charge specification is"
     "not valid, e.g. a region where the transaction is not allowed. See also [[eligibleRegion]].",
    )
    availabilityStarts: Optional[Union[List[Union[datetime, 'DateTime', date, 'Date', time, 'Time', str]], datetime, 'DateTime', date, 'Date', time, 'Time', str]] = Field(
        default=None,
        description="The beginning of the availability of the product or service included in the offer.",
    )
    availabilityEnds: Optional[Union[List[Union[datetime, 'DateTime', date, 'Date', time, 'Time', str]], datetime, 'DateTime', date, 'Date', time, 'Time', str]] = Field(
        default=None,
        description="The end of the availability of the product or service included in the offer.",
    )
    category: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'Thing', 'PhysicalActivityCategory', 'CategoryCode']], AnyUrl, 'URL', str, 'Text', 'Thing', 'PhysicalActivityCategory', 'CategoryCode']] = Field(
        default=None,
        description="A category for the item. Greater signs or slashes can be used to informally indicate a"
     "category hierarchy.",
    )
    expectsAcceptanceOf: Optional[Union[List[Union['Offer', str]], 'Offer', str]] = Field(
        default=None,
        description="An Offer which must be accepted before the user can perform the Action. For example, the"
     "user may need to buy a movie before being able to watch it.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Place import Place
    from pydantic_schemaorg.GeoShape import GeoShape
    from pydantic_schemaorg.Boolean import Boolean
    from pydantic_schemaorg.MediaSubscription import MediaSubscription
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Date import Date
    from pydantic_schemaorg.Time import Time
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Thing import Thing
    from pydantic_schemaorg.PhysicalActivityCategory import PhysicalActivityCategory
    from pydantic_schemaorg.CategoryCode import CategoryCode
    from pydantic_schemaorg.Offer import Offer


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
