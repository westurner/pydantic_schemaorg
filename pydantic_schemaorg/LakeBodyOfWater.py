from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.BodyOfWater import BodyOfWater


class LakeBodyOfWater(BodyOfWater):
    """A lake (for example, Lake Pontrachain).

    See: https://schema.org/LakeBodyOfWater
    Model depth: 5
    """
    valid_name: ClassVar[str] = "LakeBodyOfWater"
    type_: str = Field("LakeBodyOfWater", alias='@type')
    



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
