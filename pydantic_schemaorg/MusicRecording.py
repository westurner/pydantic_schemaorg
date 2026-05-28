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


class MusicRecording(CreativeWork):
    """A music recording (track), usually a single song.

    See: https://schema.org/MusicRecording
    Model depth: 3
    """
    valid_name: ClassVar[str] = "MusicRecording"
    type_: str = Field("MusicRecording", alias='@type')
    isrcCode: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The International Standard Recording Code for the recording.",
    )
    duration: Optional[Union[List[Union['QuantitativeValue', 'Duration', str]], 'QuantitativeValue', 'Duration', str]] = Field(
        default=None,
        description="The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 duration"
     "format](http://en.wikipedia.org/wiki/ISO_8601).",
    )
    recordingOf: Optional[Union[List[Union['MusicComposition', str]], 'MusicComposition', str]] = Field(
        default=None,
        description="The composition this track is a recording of.",
    )
    inAlbum: Optional[Union[List[Union['MusicAlbum', str]], 'MusicAlbum', str]] = Field(
        default=None,
        description="The album to which this recording belongs.",
    )
    byArtist: Optional[Union[List[Union['Person', 'MusicGroup', str]], 'Person', 'MusicGroup', str]] = Field(
        default=None,
        description="The artist that performed this album or recording.",
    )
    inPlaylist: Optional[Union[List[Union['MusicPlaylist', str]], 'MusicPlaylist', str]] = Field(
        default=None,
        description="The playlist to which this recording belongs.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.Duration import Duration
    from pydantic_schemaorg.MusicComposition import MusicComposition
    from pydantic_schemaorg.MusicAlbum import MusicAlbum
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.MusicGroup import MusicGroup
    from pydantic_schemaorg.MusicPlaylist import MusicPlaylist


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
