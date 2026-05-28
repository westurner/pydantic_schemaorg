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
from pydantic_schemaorg.MusicPlaylist import MusicPlaylist


class MusicAlbum(MusicPlaylist):
    """A collection of music tracks.

    See: https://schema.org/MusicAlbum
    Model depth: 4
    """
    valid_name: ClassVar[str] = "MusicAlbum"
    type_: str = Field("MusicAlbum", alias='@type')
    albumReleaseType: Optional[Union[List[Union['MusicAlbumReleaseType', str]], 'MusicAlbumReleaseType', str]] = Field(
        default=None,
        description="The kind of release which this album is: single, EP or album.",
    )
    byArtist: Optional[Union[List[Union['Person', 'MusicGroup', str]], 'Person', 'MusicGroup', str]] = Field(
        default=None,
        description="The artist that performed this album or recording.",
    )
    albumProductionType: Optional[Union[List[Union['MusicAlbumProductionType', str]], 'MusicAlbumProductionType', str]] = Field(
        default=None,
        description="Classification of the album by its type of content: soundtrack, live album, studio album,"
     "etc.",
    )
    albumRelease: Optional[Union[List[Union['MusicRelease', str]], 'MusicRelease', str]] = Field(
        default=None,
        description="A release of this album.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.MusicAlbumReleaseType import MusicAlbumReleaseType
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.MusicGroup import MusicGroup
    from pydantic_schemaorg.MusicAlbumProductionType import MusicAlbumProductionType
    from pydantic_schemaorg.MusicRelease import MusicRelease


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
