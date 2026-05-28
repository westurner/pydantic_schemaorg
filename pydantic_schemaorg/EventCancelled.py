from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.EventStatusType import EventStatusType


class EventCancelled(EventStatusType):
    """The event has been cancelled. If the event has multiple startDate values, all are assumed"
     "to be cancelled. Either startDate or previousStartDate may be used to specify the event's"
     "cancelled date(s).

    See: https://schema.org/EventCancelled
    Model depth: 6
    """
    valid_name: ClassVar[str] = "EventCancelled"
    type_: str = Field("EventCancelled", alias='@type')
    



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
