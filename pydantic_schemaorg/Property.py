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


class Property(Intangible):
    """A property, used to indicate attributes and relationships of some Thing; equivalent"
     "to rdf:Property.

    See: https://schema.org/Property
    Model depth: 3
    """
    valid_name: ClassVar[str] = "Property"
    type_: str = Field("Property", alias='@type')
    supersededBy: Optional[Union[List[Union['Property', 'Class', 'Enumeration', str]], 'Property', 'Class', 'Enumeration', str]] = Field(
        default=None,
        description="Relates a term (i.e. a property, class or enumeration) to one that supersedes it.",
    )
    domainIncludes: Optional[Union[List[Union['Class', str]], 'Class', str]] = Field(
        default=None,
        description="Relates a property to a class that is (one of) the type(s) the property is expected to be"
     "used on.",
    )
    inverseOf: Optional[Union[List[Union['Property', str]], 'Property', str]] = Field(
        default=None,
        description="Relates a property to a property that is its inverse. Inverse properties relate the same"
     "pairs of items to each other, but in reversed direction. For example, the 'alumni' and"
     "'alumniOf' properties are inverseOf each other. Some properties don't have explicit"
     "inverses; in these situations RDFa and JSON-LD syntax for reverse properties can be"
     "used.",
    )
    rangeIncludes: Optional[Union[List[Union['Class', str]], 'Class', str]] = Field(
        default=None,
        description="Relates a property to a class that constitutes (one of) the expected type(s) for values"
     "of the property.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Class import Class
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
