from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.MediaManipulationRatingEnumeration import MediaManipulationRatingEnumeration


class EditedOrCroppedContent(MediaManipulationRatingEnumeration):
    """Content coded 'edited or cropped content' in a [[MediaReview]], considered in the context"
     "of how it was published or shared. For a [[VideoObject]] to be 'edited or cropped content':"
     "The video has been edited or rearranged. This category applies to time edits, including"
     "editing multiple videos together to alter the story being told or editing out large portions"
     "from a video. For an [[ImageObject]] to be 'edited or cropped content': Presenting a"
     "part of an image from a larger whole to mislead the viewer. For an [[ImageObject]] with"
     "embedded text to be 'edited or cropped content': Presenting a part of an image from a larger"
     "whole to mislead the viewer. For an [[AudioObject]] to be 'edited or cropped content':"
     "The audio has been edited or rearranged. This category applies to time edits, including"
     "editing multiple audio clips together to alter the story being told or editing out large"
     "portions from the recording.

    See: https://schema.org/EditedOrCroppedContent
    Model depth: 5
    """
    valid_name: ClassVar[str] = "EditedOrCroppedContent"
    type_: str = Field("EditedOrCroppedContent", alias='@type')
    



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
