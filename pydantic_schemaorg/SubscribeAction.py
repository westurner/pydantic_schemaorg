from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.InteractAction import InteractAction


class SubscribeAction(InteractAction):
    """The act of forming a personal connection with someone/something (object) unidirectionally/asymmetrically"
     "to get updates pushed to. Related actions: * [[FollowAction]]: Unlike FollowAction,"
     "SubscribeAction implies that the subscriber acts as a passive agent being constantly/actively"
     "pushed for updates. * [[RegisterAction]]: Unlike RegisterAction, SubscribeAction"
     "implies that the agent is interested in continuing receiving updates from the object."
     "* [[JoinAction]]: Unlike JoinAction, SubscribeAction implies that the agent is interested"
     "in continuing receiving updates from the object.

    See: https://schema.org/SubscribeAction
    Model depth: 4
    """
    valid_name: ClassVar[str] = "SubscribeAction"
    type_: str = Field("SubscribeAction", alias='@type')
    



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
