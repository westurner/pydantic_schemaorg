from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class DigitalPlatformEnumeration(Enumeration):
    """Enumerates some common technology platforms, for use with properties such as [[actionPlatform]]."
     "It is not supposed to be comprehensive - when a suitable code is not enumerated here, textual"
     "or URL values can be used instead. These codes are at a fairly high level and do not deal"
     "with versioning and other nuance. Additional codes can be suggested [in github](https://github.com/schemaorg/schemaorg/issues/3057).

    See: https://schema.org/DigitalPlatformEnumeration
    Model depth: 4
    """
    valid_name: ClassVar[str] = "DigitalPlatformEnumeration"
    type_: str = Field("DigitalPlatformEnumeration", alias='@type')
    



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
