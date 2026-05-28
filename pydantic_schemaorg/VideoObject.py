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
from pydantic_schemaorg.MediaObject import MediaObject


class VideoObject(MediaObject):
    """A video file.

    See: https://schema.org/VideoObject
    Model depth: 4
    """
    valid_name: ClassVar[str] = "VideoObject"
    type_: str = Field("VideoObject", alias='@type')
    actor: Optional[Union[List[Union['Person', 'PerformingGroup', str]], 'Person', 'PerformingGroup', str]] = Field(
        default=None,
        description="An actor (individual or a group), e.g. in TV, radio, movie, video games etc., or in an event."
     "Actors can be associated with individual items or with a series, episode, clip.",
    )
    caption: Optional[Union[List[Union[str, 'Text', 'MediaObject']], str, 'Text', 'MediaObject']] = Field(
        default=None,
        description="The caption for this object. For downloadable machine formats (closed caption, subtitles"
     "etc.) use MediaObject and indicate the [[encodingFormat]].",
    )
    videoQuality: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The quality of the video.",
    )
    director: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="A director of e.g. TV, radio, movie, video gaming etc. content, or of an event. Directors"
     "can be associated with individual items or with a series, episode, clip.",
    )
    directors: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="A director of e.g. TV, radio, movie, video games etc. content. Directors can be associated"
     "with individual items or with a series, episode, clip.",
    )
    transcript: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="If this MediaObject is an AudioObject or VideoObject, the transcript of that object.",
    )
    musicBy: Optional[Union[List[Union['Person', 'MusicGroup', str]], 'Person', 'MusicGroup', str]] = Field(
        default=None,
        description="The composer of the soundtrack.",
    )
    videoFrameSize: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The frame size of the video.",
    )
    embeddedTextCaption: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Represents textual captioning from a [[MediaObject]], e.g. text of a 'meme'.",
    )
    actors: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="An actor, e.g. in TV, radio, movie, video games etc. Actors can be associated with individual"
     "items or with a series, episode, clip.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.PerformingGroup import PerformingGroup
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.MediaObject import MediaObject
    from pydantic_schemaorg.MusicGroup import MusicGroup


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
