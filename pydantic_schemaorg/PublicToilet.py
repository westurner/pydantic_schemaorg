from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.CivicStructure import CivicStructure


class PublicToilet(CivicStructure):
    """A public toilet is a room or small building containing one or more toilets (and possibly"
     "also urinals) which is available for use by the general public, or by customers or employees"
     "of certain businesses.

    See: https://schema.org/PublicToilet
    Model depth: 4
    """
    valid_name: ClassVar[str] = "PublicToilet"
    type_: str = Field("PublicToilet", alias='@type')
    



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
