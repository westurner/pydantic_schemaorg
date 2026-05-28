from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class HyperTocEntry(CreativeWork):
    """A HyperToEntry is an item within a [[HyperToc]], which represents a hypertext table"
     "of contents for complex media objects, such as [[VideoObject]], [[AudioObject]]."
     "The media object itself is indicated using [[associatedMedia]]. Each section of interest"
     "within that content can be described with a [[HyperTocEntry]], with associated [[startOffset]]"
     "and [[endOffset]]. When several entries are all from the same file, [[associatedMedia]]"
     "is used on the overarching [[HyperTocEntry]]; if the content has been split into multiple"
     "files, they can be referenced using [[associatedMedia]] on each [[HyperTocEntry]].

    See: https://schema.org/HyperTocEntry
    Model depth: 3
    """
    valid_name: ClassVar[str] = "HyperTocEntry"
    type_: str = Field("HyperTocEntry", alias='@type')
    utterances: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Text of an utterances (spoken words, lyrics etc.) that occurs at a certain section of"
     "a media object, represented as a [[HyperTocEntry]].",
    )
    tocContinuation: Optional[Union[List[Union['HyperTocEntry', str]], 'HyperTocEntry', str]] = Field(
        default=None,
        description="A [[HyperTocEntry]] can have a [[tocContinuation]] indicated, which is another [[HyperTocEntry]]"
     "that would be the default next item to play or render.",
    )
    associatedMedia: Optional[Union[List[Union['MediaObject', str]], 'MediaObject', str]] = Field(
        default=None,
        description="A media object that encodes this CreativeWork. This property is a synonym for encoding.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.MediaObject import MediaObject


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
