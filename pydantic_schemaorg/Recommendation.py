from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from pydantic import AnyUrl
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.Review import Review


class Recommendation(Review):
    """[[Recommendation]] is a type of [[Review]] that suggests or proposes something as the"
     "best option or best course of action. Recommendations may be for products or services,"
     "or other concrete things, as in the case of a ranked list or product guide. A [[Guide]]"
     "may list multiple recommendations for different categories. For example, in a [[Guide]]"
     "about which TVs to buy, the author may have several [[Recommendation]]s.

    See: https://schema.org/Recommendation
    Model depth: 4
    """
    valid_name: ClassVar[str] = "Recommendation"
    type_: str = Field("Recommendation", alias='@type')
    category: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'Thing', 'PhysicalActivityCategory', 'CategoryCode']], AnyUrl, 'URL', str, 'Text', 'Thing', 'PhysicalActivityCategory', 'CategoryCode']] = Field(
        default=None,
        description="A category for the item. Greater signs or slashes can be used to informally indicate a"
     "category hierarchy.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Thing import Thing
    from pydantic_schemaorg.PhysicalActivityCategory import PhysicalActivityCategory
    from pydantic_schemaorg.CategoryCode import CategoryCode


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
