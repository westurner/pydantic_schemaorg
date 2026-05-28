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


class MusicPlaylist(CreativeWork):
    """A collection of music tracks in playlist form.

    See: https://schema.org/MusicPlaylist
    Model depth: 3
    """
    valid_name: ClassVar[str] = "MusicPlaylist"
    type_: str = Field("MusicPlaylist", alias='@type')
    tracks: Optional[Union[List[Union['MusicRecording', str]], 'MusicRecording', str]] = Field(
        default=None,
        description="A music recording (track)&#x2014;usually a single song.",
    )
    track: Optional[Union[List[Union['MusicRecording', 'ItemList', str]], 'MusicRecording', 'ItemList', str]] = Field(
        default=None,
        description="A music recording (track)&#x2014;usually a single song. If an ItemList is given, the"
     "list should contain items of type MusicRecording.",
    )
    numTracks: Optional[Union[List[Union[int, 'Integer', str]], int, 'Integer', str]] = Field(
        default=None,
        description="The number of tracks in this album or playlist.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.MusicRecording import MusicRecording
    from pydantic_schemaorg.ItemList import ItemList
    from pydantic_schemaorg.Integer import Integer


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
