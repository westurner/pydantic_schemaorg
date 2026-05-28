from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.InteractAction import InteractAction


class BefriendAction(InteractAction):
    """The act of forming a personal connection with someone (object) mutually/bidirectionally/symmetrically."
     "Related actions: * [[FollowAction]]: Unlike FollowAction, BefriendAction implies"
     "that the connection is reciprocal.

    See: https://schema.org/BefriendAction
    Model depth: 4
    """
    valid_name: ClassVar[str] = "BefriendAction"
    type_: str = Field("BefriendAction", alias='@type')
    



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
