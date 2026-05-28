from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from typing import List, Optional, Union
from pydantic import AnyUrl


from pydantic import Field
from pydantic_schemaorg.DefinedTerm import DefinedTerm


class CategoryCode(DefinedTerm):
    """A Category Code.

    See: https://schema.org/CategoryCode
    Model depth: 4
    """
    valid_name: ClassVar[str] = "CategoryCode"
    type_: str = Field("CategoryCode", alias='@type')
    codeValue: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="A short textual code that uniquely identifies the value.",
    )
    inCodeSet: Optional[Union[List[Union[AnyUrl, 'URL', 'CategoryCodeSet', str]], AnyUrl, 'URL', 'CategoryCodeSet', str]] = Field(
        default=None,
        description="A [[CategoryCodeSet]] that contains this category code.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.CategoryCodeSet import CategoryCodeSet


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
