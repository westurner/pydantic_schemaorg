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
from pydantic_schemaorg.Event import Event


class ScreeningEvent(Event):
    """A screening of a movie or other video.

    See: https://schema.org/ScreeningEvent
    Model depth: 3
    """
    valid_name: ClassVar[str] = "ScreeningEvent"
    type_: str = Field("ScreeningEvent", alias='@type')
    workPresented: Optional[Union[List[Union['Movie', str]], 'Movie', str]] = Field(
        default=None,
        description="The movie presented during this event.",
    )
    subtitleLanguage: Optional[Union[List[Union[str, 'Text', 'Language']], str, 'Text', 'Language']] = Field(
        default=None,
        description="Languages in which subtitles/captions are available, in [IETF BCP 47 standard format](http://tools.ietf.org/html/bcp47).",
    )
    videoFormat: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The type of screening or video broadcast used (e.g. IMAX, 3D, SD, HD, etc.).",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Movie import Movie
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Language import Language


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
