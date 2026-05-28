from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.PlanAction import PlanAction


class ScheduleAction(PlanAction):
    """Scheduling future actions, events, or tasks. Related actions: * [[ReserveAction]]:"
     "Unlike ReserveAction, ScheduleAction allocates future actions (e.g. an event, a task,"
     "etc) towards a time slot / spatial allocation.

    See: https://schema.org/ScheduleAction
    Model depth: 5
    """
    valid_name: ClassVar[str] = "ScheduleAction"
    type_: str = Field("ScheduleAction", alias='@type')
    



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
