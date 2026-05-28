from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from typing import List, Optional, Union
from pydantic import AnyUrl


from pydantic import Field
from pydantic_schemaorg.PerformingGroup import PerformingGroup


class MusicGroup(PerformingGroup):
    """A musical group, such as a band, an orchestra, or a choir. Can also be a solo musician.

    See: https://schema.org/MusicGroup
    Model depth: 4
    """
    valid_name: ClassVar[str] = "MusicGroup"
    type_: str = Field("MusicGroup", alias='@type')
    musicGroupMember: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="A member of a music group&#x2014;for example, John, Paul, George, or Ringo.",
    )
    tracks: Optional[Union[List[Union['MusicRecording', str]], 'MusicRecording', str]] = Field(
        default=None,
        description="A music recording (track)&#x2014;usually a single song.",
    )
    album: Optional[Union[List[Union['MusicAlbum', str]], 'MusicAlbum', str]] = Field(
        default=None,
        description="A music album.",
    )
    track: Optional[Union[List[Union['MusicRecording', 'ItemList', str]], 'MusicRecording', 'ItemList', str]] = Field(
        default=None,
        description="A music recording (track)&#x2014;usually a single song. If an ItemList is given, the"
     "list should contain items of type MusicRecording.",
    )
    albums: Optional[Union[List[Union['MusicAlbum', str]], 'MusicAlbum', str]] = Field(
        default=None,
        description="A collection of music albums.",
    )
    genre: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        default=None,
        description="Genre of the creative work, broadcast channel or group.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.MusicRecording import MusicRecording
    from pydantic_schemaorg.MusicAlbum import MusicAlbum
    from pydantic_schemaorg.ItemList import ItemList
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Text import Text


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
