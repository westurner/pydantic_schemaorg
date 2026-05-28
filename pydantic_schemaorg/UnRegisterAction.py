from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.InteractAction import InteractAction


class UnRegisterAction(InteractAction):
    """The act of un-registering from a service. Related actions: * [[RegisterAction]]: antonym"
     "of UnRegisterAction. * [[LeaveAction]]: Unlike LeaveAction, UnRegisterAction implies"
     "that you are unregistering from a service you were previously registered, rather than"
     "leaving a team/group of people.

    See: https://schema.org/UnRegisterAction
    Model depth: 4
    """
    valid_name: ClassVar[str] = "UnRegisterAction"
    type_: str = Field("UnRegisterAction", alias='@type')
    



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
