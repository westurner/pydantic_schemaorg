from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.Accommodation import Accommodation


class CampingPitch(Accommodation):
    """A [[CampingPitch]] is an individual place for overnight stay in the outdoors, typically"
     "being part of a larger camping site, or [[Campground]]. In British English a campsite,"
     "or campground, is an area, usually divided into a number of pitches, where people can"
     "camp overnight using tents or camper vans or caravans; this British English use of the"
     "word is synonymous with the American English expression campground. In American English"
     "the term campsite generally means an area where an individual, family, group, or military"
     "unit can pitch a tent or park a camper; a campground may contain many campsites. (Source:"
     "Wikipedia, see [https://en.wikipedia.org/wiki/Campsite](https://en.wikipedia.org/wiki/Campsite).)"
     "See also the dedicated [document on the use of schema.org for marking up hotels and other"
     "forms of accommodations](/docs/hotels.html).

    See: https://schema.org/CampingPitch
    Model depth: 4
    """
    valid_name: ClassVar[str] = "CampingPitch"
    type_: str = Field("CampingPitch", alias='@type')
    



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
