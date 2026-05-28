from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class MediaManipulationRatingEnumeration(Enumeration):
    """Codes for use with the [[mediaAuthenticityCategory]] property, indicating the authenticity"
     "of a media object (in the context of how it was published or shared). In general these codes"
     "are not mutually exclusive, although some combinations (such as 'original' versus"
     "'transformed', 'edited' and 'staged') would be contradictory if applied in the same"
     "[[MediaReview]]. Note that the application of these codes is with regard to a piece of"
     "media shared or published in a particular context.

    See: https://schema.org/MediaManipulationRatingEnumeration
    Model depth: 4
    """
    valid_name: ClassVar[str] = "MediaManipulationRatingEnumeration"
    type_: str = Field("MediaManipulationRatingEnumeration", alias='@type')
    



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
