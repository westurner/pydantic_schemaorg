from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.AllocateAction import AllocateAction


class AcceptAction(AllocateAction):
    """The act of committing to/adopting an object. Related actions: * [[RejectAction]]:"
     "The antonym of AcceptAction.

    See: https://schema.org/AcceptAction
    Model depth: 5
    """
    valid_name: ClassVar[str] = "AcceptAction"
    type_: str = Field("AcceptAction", alias='@type')
    



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
