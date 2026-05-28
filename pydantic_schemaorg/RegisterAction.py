from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.InteractAction import InteractAction


class RegisterAction(InteractAction):
    """The act of registering to be a user of a service, product or web page. Related actions:"
     "* [[JoinAction]]: Unlike JoinAction, RegisterAction implies you are registering"
     "to be a user of a service, *not* a group/team of people. * [[FollowAction]]: Unlike FollowAction,"
     "RegisterAction doesn't imply that the agent is expecting to poll for updates from the"
     "object. * [[SubscribeAction]]: Unlike SubscribeAction, RegisterAction doesn't"
     "imply that the agent is expecting updates from the object.

    See: https://schema.org/RegisterAction
    Model depth: 4
    """
    valid_name: ClassVar[str] = "RegisterAction"
    type_: str = Field("RegisterAction", alias='@type')
    



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
