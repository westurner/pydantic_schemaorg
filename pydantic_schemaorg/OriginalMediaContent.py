from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.MediaManipulationRatingEnumeration import MediaManipulationRatingEnumeration


class OriginalMediaContent(MediaManipulationRatingEnumeration):
    """Content coded 'as original media content' in a [[MediaReview]], considered in the context"
     "of how it was published or shared. For a [[VideoObject]] to be 'original': No evidence"
     "the footage has been misleadingly altered or manipulated, though it may contain false"
     "or misleading claims. For an [[ImageObject]] to be 'original': No evidence the image"
     "has been misleadingly altered or manipulated, though it may still contain false or misleading"
     "claims. For an [[ImageObject]] with embedded text to be 'original': No evidence the"
     "image has been misleadingly altered or manipulated, though it may still contain false"
     "or misleading claims. For an [[AudioObject]] to be 'original': No evidence the audio"
     "has been misleadingly altered or manipulated, though it may contain false or misleading"
     "claims.

    See: https://schema.org/OriginalMediaContent
    Model depth: 5
    """
    valid_name: ClassVar[str] = "OriginalMediaContent"
    type_: str = Field("OriginalMediaContent", alias='@type')
    



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
