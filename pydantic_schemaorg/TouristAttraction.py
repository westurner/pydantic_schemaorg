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


class TouristAttraction(Place):
    """A tourist attraction. In principle any Thing can be a [[TouristAttraction]], from a"
     "[[Mountain]] and [[LandmarksOrHistoricalBuildings]] to a [[LocalBusiness]]. This"
     "Type can be used on its own to describe a general [[TouristAttraction]], or be used as"
     "an [[additionalType]] to add tourist attraction properties to any other type. (See"
     "examples below)

    See: https://schema.org/TouristAttraction
    Model depth: 3
    """
    valid_name: ClassVar[str] = "TouristAttraction"
    type_: str = Field("TouristAttraction", alias='@type')
    touristType: Optional[Union[List[Union[str, 'Text', 'Audience']], str, 'Text', 'Audience']] = Field(
        default=None,
        description="Attraction suitable for type(s) of tourist. E.g. children, visitors from a particular"
     "country, etc.",
    )
    availableLanguage: Optional[Union[List[Union[str, 'Text', 'Language']], str, 'Text', 'Language']] = Field(
        default=None,
        description="A language someone may use with or at the item, service or place. Please use one of the language"
     "codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also"
     "[[inLanguage]].",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Audience import Audience
    from pydantic_schemaorg.Language import Language


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
