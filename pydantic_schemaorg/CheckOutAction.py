from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.CommunicateAction import CommunicateAction


class CheckOutAction(CommunicateAction):
    """The act of an agent communicating (service provider, social media, etc) their departure"
     "of a previously reserved service (e.g. flight check-in) or place (e.g. hotel). Related"
     "actions: * [[CheckInAction]]: The antonym of CheckOutAction. * [[DepartAction]]:"
     "Unlike DepartAction, CheckOutAction implies that the agent is informing/confirming"
     "the end of a previously reserved service. * [[CancelAction]]: Unlike CancelAction,"
     "CheckOutAction implies that the agent is informing/confirming the end of a previously"
     "reserved service.

    See: https://schema.org/CheckOutAction
    Model depth: 5
    """
    valid_name: ClassVar[str] = "CheckOutAction"
    type_: str = Field("CheckOutAction", alias='@type')
    



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
