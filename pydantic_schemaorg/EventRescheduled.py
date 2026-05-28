from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.EventStatusType import EventStatusType


class EventRescheduled(EventStatusType):
    """The event has been rescheduled. The event's previousStartDate should be set to the old"
     "date and the startDate should be set to the event's new date. (If the event has been rescheduled"
     "multiple times, the previousStartDate property may be repeated.)

    See: https://schema.org/EventRescheduled
    Model depth: 6
    """
    valid_name: ClassVar[str] = "EventRescheduled"
    type_: str = Field("EventRescheduled", alias='@type')
    



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
