from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class FoodEstablishment(LocalBusiness):
    """A food-related business.

    See: https://schema.org/FoodEstablishment
    Model depth: 4
    """
    valid_name: ClassVar[str] = "FoodEstablishment"
    type_: str = Field("FoodEstablishment", alias='@type')
    menu: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'Menu']], AnyUrl, 'URL', str, 'Text', 'Menu']] = Field(
        default=None,
        description="Either the actual menu as a structured representation, as text, or a URL of the menu.",
    )
    servesCuisine: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The cuisine of the restaurant.",
    )
    acceptsReservations: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', StrictBool, 'Boolean']], AnyUrl, 'URL', str, 'Text', StrictBool, 'Boolean']] = Field(
        default=None,
        description="Indicates whether a FoodEstablishment accepts reservations. Values can be Boolean,"
     "an URL at which reservations can be made or (for backwards compatibility) the strings"
     "```Yes``` or ```No```.",
    )
    starRating: Optional[Union[List[Union['Rating', str]], 'Rating', str]] = Field(
        default=None,
        description="An official rating for a lodging business or food establishment, e.g. from national"
     "associations or standards bodies. Use the author property to indicate the rating organization,"
     "e.g. as an Organization with name such as (e.g. HOTREC, DEHOGA, WHR, or Hotelstars).",
    )
    hasMenu: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'Menu']], AnyUrl, 'URL', str, 'Text', 'Menu']] = Field(
        default=None,
        description="Either the actual menu as a structured representation, as text, or a URL of the menu.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Menu import Menu
    from pydantic_schemaorg.Boolean import Boolean
    from pydantic_schemaorg.Rating import Rating


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
