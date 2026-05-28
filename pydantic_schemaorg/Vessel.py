from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.AnatomicalStructure import AnatomicalStructure


class Vessel(AnatomicalStructure):
    """A component of the human body circulatory system comprised of an intricate network of"
     "hollow tubes that transport blood throughout the entire body.

    See: https://schema.org/Vessel
    Model depth: 4
    """
    valid_name: ClassVar[str] = "Vessel"
    type_: str = Field("Vessel", alias='@type')
    



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
