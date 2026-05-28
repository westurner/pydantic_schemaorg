from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from pydantic import AnyUrl, StrictBool
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.Event import Event


class PublicationEvent(Event):
    """A PublicationEvent corresponds indifferently to the event of publication for a CreativeWork"
     "of any type, e.g. a broadcast event, an on-demand event, a book/journal publication"
     "via a variety of delivery media.

    See: https://schema.org/PublicationEvent
    Model depth: 3
    """
    valid_name: ClassVar[str] = "PublicationEvent"
    type_: str = Field("PublicationEvent", alias='@type')
    free: Optional[Union[List[Union[StrictBool, 'Boolean', str]], StrictBool, 'Boolean', str]] = Field(
        default=None,
        description="A flag to signal that the item, event, or place is accessible for free.",
    )
    publishedOn: Optional[Union[List[Union['BroadcastService', str]], 'BroadcastService', str]] = Field(
        default=None,
        description="A broadcast service associated with the publication event.",
    )
    publishedBy: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="An agent associated with the publication event.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Boolean import Boolean
    from pydantic_schemaorg.BroadcastService import BroadcastService
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
