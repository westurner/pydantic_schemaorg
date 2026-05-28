from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.ListItem import ListItem
from pydantic_schemaorg.CreativeWork import CreativeWork


class HowToTip(ListItem, CreativeWork):
    """An explanation in the instructions for how to achieve a result. It provides supplementary"
     "information about a technique, supply, author's preference, etc. It can explain what"
     "could be done, or what should not be done, but doesn't specify what should be done (see"
     "HowToDirection).

    See: https://schema.org/HowToTip
    Model depth: 3
    """
    valid_name: ClassVar[str] = "HowToTip"
    type_: str = Field("HowToTip", alias='@type')
    



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
