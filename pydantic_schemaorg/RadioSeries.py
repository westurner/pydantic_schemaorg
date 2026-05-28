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
from pydantic_schemaorg.CreativeWorkSeries import CreativeWorkSeries


class RadioSeries(CreativeWorkSeries):
    """CreativeWorkSeries dedicated to radio broadcast and associated online delivery.

    See: https://schema.org/RadioSeries
    Model depth: 4
    """
    valid_name: ClassVar[str] = "RadioSeries"
    type_: str = Field("RadioSeries", alias='@type')
    episodes: Optional[Union[List[Union['Episode', str]], 'Episode', str]] = Field(
        default=None,
        description="An episode of a TV/radio series or season.",
    )
    trailer: Optional[Union[List[Union['VideoObject', str]], 'VideoObject', str]] = Field(
        default=None,
        description="The trailer of a movie or TV/radio series, season, episode, etc.",
    )
    actor: Optional[Union[List[Union['Person', 'PerformingGroup', str]], 'Person', 'PerformingGroup', str]] = Field(
        default=None,
        description="An actor (individual or a group), e.g. in TV, radio, movie, video games etc., or in an event."
     "Actors can be associated with individual items or with a series, episode, clip.",
    )
    season: Optional[Union[List[Union[AnyUrl, 'URL', 'CreativeWorkSeason', str]], AnyUrl, 'URL', 'CreativeWorkSeason', str]] = Field(
        default=None,
        description="A season in a media series.",
    )
    director: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="A director of e.g. TV, radio, movie, video gaming etc. content, or of an event. Directors"
     "can be associated with individual items or with a series, episode, clip.",
    )
    numberOfSeasons: Optional[Union[List[Union[int, 'Integer', str]], int, 'Integer', str]] = Field(
        default=None,
        description="The number of seasons in this series.",
    )
    directors: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="A director of e.g. TV, radio, movie, video games etc. content. Directors can be associated"
     "with individual items or with a series, episode, clip.",
    )
    episode: Optional[Union[List[Union['Episode', str]], 'Episode', str]] = Field(
        default=None,
        description="An episode of a TV, radio or game media within a series or season.",
    )
    numberOfEpisodes: Optional[Union[List[Union[int, 'Integer', str]], int, 'Integer', str]] = Field(
        default=None,
        description="The number of episodes in this season or series.",
    )
    musicBy: Optional[Union[List[Union['Person', 'MusicGroup', str]], 'Person', 'MusicGroup', str]] = Field(
        default=None,
        description="The composer of the soundtrack.",
    )
    containsSeason: Optional[Union[List[Union['CreativeWorkSeason', str]], 'CreativeWorkSeason', str]] = Field(
        default=None,
        description="A season that is part of the media series.",
    )
    actors: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="An actor, e.g. in TV, radio, movie, video games etc. Actors can be associated with individual"
     "items or with a series, episode, clip.",
    )
    seasons: Optional[Union[List[Union['CreativeWorkSeason', str]], 'CreativeWorkSeason', str]] = Field(
        default=None,
        description="A season in a media series.",
    )
    productionCompany: Optional[Union[List[Union['Organization', str]], 'Organization', str]] = Field(
        default=None,
        description="The production company or studio responsible for the item, e.g. series, video game,"
     "episode etc.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Episode import Episode
    from pydantic_schemaorg.VideoObject import VideoObject
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.PerformingGroup import PerformingGroup
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.CreativeWorkSeason import CreativeWorkSeason
    from pydantic_schemaorg.Integer import Integer
    from pydantic_schemaorg.MusicGroup import MusicGroup
    from pydantic_schemaorg.Organization import Organization


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
