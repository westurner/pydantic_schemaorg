from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.Action import Action


class OrganizeAction(Action):
    """The act of manipulating/administering/supervising/controlling one or more objects.

    See: https://schema.org/OrganizeAction
    Model depth: 3
    """
    valid_name: ClassVar[str] = "OrganizeAction"
    type_: str = Field("OrganizeAction", alias='@type')
    



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
