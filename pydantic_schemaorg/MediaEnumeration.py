from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class MediaEnumeration(Enumeration):
    """MediaEnumeration enumerations are lists of codes, labels etc. useful for describing"
     "media objects. They may be reflections of externally developed lists, or created at"
     "schema.org, or a combination.

    See: https://schema.org/MediaEnumeration
    Model depth: 4
    """
    valid_name: ClassVar[str] = "MediaEnumeration"
    type_: str = Field("MediaEnumeration", alias='@type')
    



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
