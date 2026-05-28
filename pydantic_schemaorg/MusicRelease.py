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


class MusicRelease(MusicPlaylist):
    """A MusicRelease is a specific release of a music album.

    See: https://schema.org/MusicRelease
    Model depth: 4
    """
    valid_name: ClassVar[str] = "MusicRelease"
    type_: str = Field("MusicRelease", alias='@type')
    catalogNumber: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The catalog number for the release.",
    )
    duration: Optional[Union[List[Union['QuantitativeValue', 'Duration', str]], 'QuantitativeValue', 'Duration', str]] = Field(
        default=None,
        description="The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 duration"
     "format](http://en.wikipedia.org/wiki/ISO_8601).",
    )
    creditedTo: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="The group the release is credited to if different than the byArtist. For example, Red"
     "and Blue is credited to \"Stefani Germanotta Band\", but by Lady Gaga.",
    )
    musicReleaseFormat: Optional[Union[List[Union['MusicReleaseFormatType', str]], 'MusicReleaseFormatType', str]] = Field(
        default=None,
        description="Format of this release (the type of recording media used, i.e. compact disc, digital"
     "media, LP, etc.).",
    )
    recordLabel: Optional[Union[List[Union['Organization', str]], 'Organization', str]] = Field(
        default=None,
        description="The label that issued the release.",
    )
    releaseOf: Optional[Union[List[Union['MusicAlbum', str]], 'MusicAlbum', str]] = Field(
        default=None,
        description="The album this is a release of.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.Duration import Duration
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.MusicReleaseFormatType import MusicReleaseFormatType
    from pydantic_schemaorg.MusicAlbum import MusicAlbum


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
