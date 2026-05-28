from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.ReactAction import ReactAction


class LikeAction(ReactAction):
    """The act of expressing a positive sentiment about the object. An agent likes an object"
     "(a proposition, topic or theme) with participants.

    See: https://schema.org/LikeAction
    Model depth: 5
    """
    valid_name: ClassVar[str] = "LikeAction"
    type_: str = Field("LikeAction", alias='@type')
    



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
