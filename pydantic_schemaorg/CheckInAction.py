from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.CommunicateAction import CommunicateAction


class CheckInAction(CommunicateAction):
    """The act of an agent communicating (service provider, social media, etc) their arrival"
     "by registering/confirming for a previously reserved service (e.g. flight check-in)"
     "or at a place (e.g. hotel), possibly resulting in a result (boarding pass, etc). Related"
     "actions: * [[CheckOutAction]]: The antonym of CheckInAction. * [[ArriveAction]]:"
     "Unlike ArriveAction, CheckInAction implies that the agent is informing/confirming"
     "the start of a previously reserved service. * [[ConfirmAction]]: Unlike ConfirmAction,"
     "CheckInAction implies that the agent is informing/confirming the *start* of a previously"
     "reserved service rather than its validity/existence.

    See: https://schema.org/CheckInAction
    Model depth: 5
    """
    valid_name: ClassVar[str] = "CheckInAction"
    type_: str = Field("CheckInAction", alias='@type')
    



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
