from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.EventStatusType import EventStatusType


class EventScheduled(EventStatusType):
    """The event is taking place or has taken place on the startDate as scheduled. Use of this"
     "value is optional, as it is assumed by default.

    See: https://schema.org/EventScheduled
    Model depth: 6
    """
    valid_name: ClassVar[str] = "EventScheduled"
    type_: str = Field("EventScheduled", alias='@type')
    



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
