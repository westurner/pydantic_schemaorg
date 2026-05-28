from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.MediaManipulationRatingEnumeration import MediaManipulationRatingEnumeration


class DecontextualizedContent(MediaManipulationRatingEnumeration):
    """Content coded 'missing context' in a [[MediaReview]], considered in the context of"
     "how it was published or shared. For a [[VideoObject]] to be 'missing context': Presenting"
     "unaltered video in an inaccurate manner that misrepresents the footage. For example,"
     "using incorrect dates or locations, altering the transcript or sharing brief clips"
     "from a longer video to mislead viewers. (A video rated 'original' can also be missing"
     "context.) For an [[ImageObject]] to be 'missing context': Presenting unaltered images"
     "in an inaccurate manner to misrepresent the image and mislead the viewer. For example,"
     "a common tactic is using an unaltered image but saying it came from a different time or"
     "place. (An image rated 'original' can also be missing context.) For an [[ImageObject]]"
     "with embedded text to be 'missing context': An unaltered image presented in an inaccurate"
     "manner to misrepresent the image and mislead the viewer. For example, a common tactic"
     "is using an unaltered image but saying it came from a different time or place. (An 'original'"
     "image with inaccurate text would generally fall in this category.) For an [[AudioObject]]"
     "to be 'missing context': Unaltered audio presented in an inaccurate manner that misrepresents"
     "it. For example, using incorrect dates or locations, or sharing brief clips from a longer"
     "recording to mislead viewers. (Audio rated “original” can also be missing context.)

    See: https://schema.org/DecontextualizedContent
    Model depth: 5
    """
    valid_name: ClassVar[str] = "DecontextualizedContent"
    type_: str = Field("DecontextualizedContent", alias='@type')
    



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
