from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class VirtualLocation(Intangible):
    """An online or virtual location for attending events. For example, one may attend an online"
     "seminar or educational event. While a virtual location may be used as the location of"
     "an event, virtual locations should not be confused with physical locations in the real"
     "world.

    See: https://schema.org/VirtualLocation
    Model depth: 3
    """
    valid_name: ClassVar[str] = "VirtualLocation"
    type_: str = Field("VirtualLocation", alias='@type')
    



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
