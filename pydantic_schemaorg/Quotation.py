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


class Quotation(CreativeWork):
    """A quotation. Often but not necessarily from some written work, attributable to a real"
     "world author and - if associated with a fictional character - to any fictional Person."
     "Use [[isBasedOn]] to link to source/origin. The [[recordedIn]] property can be used"
     "to reference a Quotation from an [[Event]].

    See: https://schema.org/Quotation
    Model depth: 3
    """
    valid_name: ClassVar[str] = "Quotation"
    type_: str = Field("Quotation", alias='@type')
    spokenByCharacter: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="The (e.g. fictional) character, Person or Organization to whom the quotation is attributed"
     "within the containing CreativeWork.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Organization import Organization


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
