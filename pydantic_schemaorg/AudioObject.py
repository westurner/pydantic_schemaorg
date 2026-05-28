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


class AudioObject(MediaObject):
    """An audio file.

    See: https://schema.org/AudioObject
    Model depth: 4
    """
    valid_name: ClassVar[str] = "AudioObject"
    type_: str = Field("AudioObject", alias='@type')
    caption: Optional[Union[List[Union[str, 'Text', 'MediaObject']], str, 'Text', 'MediaObject']] = Field(
        default=None,
        description="The caption for this object. For downloadable machine formats (closed caption, subtitles"
     "etc.) use MediaObject and indicate the [[encodingFormat]].",
    )
    transcript: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="If this MediaObject is an AudioObject or VideoObject, the transcript of that object.",
    )
    embeddedTextCaption: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Represents textual captioning from a [[MediaObject]], e.g. text of a 'meme'.",
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
