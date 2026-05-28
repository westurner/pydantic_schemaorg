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
from pydantic_schemaorg.DefinedTermSet import DefinedTermSet


class CategoryCodeSet(DefinedTermSet):
    """A set of Category Code values.

    See: https://schema.org/CategoryCodeSet
    Model depth: 4
    """
    valid_name: ClassVar[str] = "CategoryCodeSet"
    type_: str = Field("CategoryCodeSet", alias='@type')
    hasCategoryCode: Optional[Union[List[Union['CategoryCode', str]], 'CategoryCode', str]] = Field(
        default=None,
        description="A Category code contained in this code set.",
    )
    


if TYPE_CHECKING:
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
