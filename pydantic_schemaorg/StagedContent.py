from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.MediaManipulationRatingEnumeration import MediaManipulationRatingEnumeration


class StagedContent(MediaManipulationRatingEnumeration):
    """Content coded 'staged content' in a [[MediaReview]], considered in the context of how"
     "it was published or shared. For a [[VideoObject]] to be 'staged content': A video that"
     "has been created using actors or similarly contrived. For an [[ImageObject]] to be 'staged"
     "content': An image that was created using actors or similarly contrived, such as a screenshot"
     "of a fake tweet. For an [[ImageObject]] with embedded text to be 'staged content': An"
     "image that was created using actors or similarly contrived, such as a screenshot of a"
     "fake tweet. For an [[AudioObject]] to be 'staged content': Audio that has been created"
     "using actors or similarly contrived.

    See: https://schema.org/StagedContent
    Model depth: 5
    """
    valid_name: ClassVar[str] = "StagedContent"
    type_: str = Field("StagedContent", alias='@type')
    



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
