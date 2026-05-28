from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.IPTCDigitalSourceEnumeration import IPTCDigitalSourceEnumeration


class DigitalArtDigitalSource(IPTCDigitalSourceEnumeration):
    """Content coded as '<a href=\"https://cv.iptc.org/newscodes/digitalsourcetype/digitalArt\">digital"
     "art</a>' using the IPTC <a href=\"https://cv.iptc.org/newscodes/digitalsourcetype/\">digital"
     "source type</a> vocabulary.

    See: https://schema.org/DigitalArtDigitalSource
    Model depth: 6
    """
    valid_name: ClassVar[str] = "DigitalArtDigitalSource"
    type_: str = Field("DigitalArtDigitalSource", alias='@type')
    



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
