from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from pydantic import AnyUrl
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.Review import Review


class MediaReview(Review):
    """A [[MediaReview]] is a more specialized form of Review dedicated to the evaluation of"
     "media content online, typically in the context of fact-checking and misinformation."
     "For more general reviews of media in the broader sense, use [[UserReview]], [[CriticReview]]"
     "or other [[Review]] types. This definition is a work in progress. While the [[MediaManipulationRatingEnumeration]]"
     "list reflects significant community review amongst fact-checkers and others working"
     "to combat misinformation, the specific structures for representing media objects,"
     "their versions and publication context, are still evolving. Similarly, best practices"
     "for the relationship between [[MediaReview]] and [[ClaimReview]] markup have not"
     "yet been finalized.

    See: https://schema.org/MediaReview
    Model depth: 4
    """
    valid_name: ClassVar[str] = "MediaReview"
    type_: str = Field("MediaReview", alias='@type')
    originalMediaLink: Optional[Union[List[Union[AnyUrl, 'URL', 'WebPage', 'MediaObject', str]], AnyUrl, 'URL', 'WebPage', 'MediaObject', str]] = Field(
        default=None,
        description="Link to the page containing an original version of the content, or directly to an online"
     "copy of the original [[MediaObject]] content, e.g. video file.",
    )
    originalMediaContextDescription: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Describes, in a [[MediaReview]] when dealing with [[DecontextualizedContent]],"
     "background information that can contribute to better interpretation of the [[MediaObject]].",
    )
    mediaAuthenticityCategory: Optional[Union[List[Union['MediaManipulationRatingEnumeration', str]], 'MediaManipulationRatingEnumeration', str]] = Field(
        default=None,
        description="Indicates a MediaManipulationRatingEnumeration classification of a media object"
     "(in the context of how it was published or shared).",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.WebPage import WebPage
    from pydantic_schemaorg.MediaObject import MediaObject
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.MediaManipulationRatingEnumeration import MediaManipulationRatingEnumeration


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
