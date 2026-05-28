from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.MediaManipulationRatingEnumeration import MediaManipulationRatingEnumeration


class SatireOrParodyContent(MediaManipulationRatingEnumeration):
    """Content coded 'satire or parody content' in a [[MediaReview]], considered in the context"
     "of how it was published or shared. For a [[VideoObject]] to be 'satire or parody content':"
     "A video that was created as political or humorous commentary and is presented in that"
     "context. (Reshares of satire/parody content that do not include relevant context are"
     "more likely to fall under the “missing context” rating.) For an [[ImageObject]] to be"
     "'satire or parody content': An image that was created as political or humorous commentary"
     "and is presented in that context. (Reshares of satire/parody content that do not include"
     "relevant context are more likely to fall under the “missing context” rating.) For an"
     "[[ImageObject]] with embedded text to be 'satire or parody content': An image that was"
     "created as political or humorous commentary and is presented in that context. (Reshares"
     "of satire/parody content that do not include relevant context are more likely to fall"
     "under the “missing context” rating.) For an [[AudioObject]] to be 'satire or parody"
     "content': Audio that was created as political or humorous commentary and is presented"
     "in that context. (Reshares of satire/parody content that do not include relevant context"
     "are more likely to fall under the “missing context” rating.)

    See: https://schema.org/SatireOrParodyContent
    Model depth: 5
    """
    valid_name: ClassVar[str] = "SatireOrParodyContent"
    type_: str = Field("SatireOrParodyContent", alias='@type')
    



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
