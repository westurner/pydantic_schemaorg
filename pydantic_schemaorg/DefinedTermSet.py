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
from pydantic_schemaorg.CreativeWork import CreativeWork


class DefinedTermSet(CreativeWork):
    """A set of defined terms, for example a set of categories or a classification scheme, a glossary,"
     "dictionary or enumeration.

    See: https://schema.org/DefinedTermSet
    Model depth: 3
    """
    valid_name: ClassVar[str] = "DefinedTermSet"
    type_: str = Field("DefinedTermSet", alias='@type')
    hasDefinedTerm: Optional[Union[List[Union['DefinedTerm', str]], 'DefinedTerm', str]] = Field(
        default=None,
        description="A Defined Term contained in this term set.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.DefinedTerm import DefinedTerm


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
