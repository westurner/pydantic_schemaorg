from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.MediaEnumeration import MediaEnumeration


class IPTCDigitalSourceEnumeration(MediaEnumeration):
    """<a href=\"https://www.iptc.org/\">IPTC</a> \"Digital Source\" codes for use with"
     "the [[digitalSourceType]] property, providing information about the source for a"
     "digital media object. In general these codes are not declared here to be mutually exclusive,"
     "although some combinations would be contradictory if applied simultaneously, or might"
     "be considered mutually incompatible by upstream maintainers of the definitions. See"
     "the IPTC <a href=\"https://www.iptc.org/std/photometadata/documentation/userguide/\">documentation</a>"
     "for <a href=\"https://cv.iptc.org/newscodes/digitalsourcetype/\">detailed"
     "definitions</a> of all terms.

    See: https://schema.org/IPTCDigitalSourceEnumeration
    Model depth: 5
    """
    valid_name: ClassVar[str] = "IPTCDigitalSourceEnumeration"
    type_: str = Field("IPTCDigitalSourceEnumeration", alias='@type')
    



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
