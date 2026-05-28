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
from pydantic_schemaorg.Intangible import Intangible


class Class(Intangible):
    """A class, also often called a 'Type'; equivalent to rdfs:Class.

    See: https://schema.org/Class
    Model depth: 3
    """
    valid_name: ClassVar[str] = "Class"
    type_: str = Field("Class", alias='@type')
    supersededBy: Optional[Union[List[Union['Property', 'Class', 'Enumeration', str]], 'Property', 'Class', 'Enumeration', str]] = Field(
        default=None,
        description="Relates a term (i.e. a property, class or enumeration) to one that supersedes it.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Property import Property
    from pydantic_schemaorg.Enumeration import Enumeration


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
