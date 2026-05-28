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


class VideoGameSeries(CreativeWorkSeries):
    """A video game series.

    See: https://schema.org/VideoGameSeries
    Model depth: 4
    """
    valid_name: ClassVar[str] = "VideoGameSeries"
    type_: str = Field("VideoGameSeries", alias='@type')
    episodes: Optional[Union[List[Union['Episode', str]], 'Episode', str]] = Field(
        default=None,
        description="An episode of a TV/radio series or season.",
    )
    cheatCode: Optional[Union[List[Union['CreativeWork', str]], 'CreativeWork', str]] = Field(
        default=None,
        description="Cheat codes to the game.",
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
    characterAttribute: Optional[Union[List[Union['Thing', str]], 'Thing', str]] = Field(
        default=None,
        description="A piece of data that represents a particular aspect of a fictional character (skill,"
     "power, character points, advantage, disadvantage).",
    )
    playMode: Optional[Union[List[Union['GamePlayMode', str]], 'GamePlayMode', str]] = Field(
        default=None,
        description="Indicates whether this game is multi-player, co-op or single-player. The game can be"
     "marked as multi-player, co-op and single-player at the same time.",
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
    gamePlatform: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'Thing']], AnyUrl, 'URL', str, 'Text', 'Thing']] = Field(
        default=None,
        description="The electronic systems used to play <a href=\"http://en.wikipedia.org/wiki/Category:Video_game_platforms\">video"
     "games</a>.",
    )
    numberOfPlayers: Optional[Union[List[Union['QuantitativeValue', str]], 'QuantitativeValue', str]] = Field(
        default=None,
        description="Indicate how many people can play this game (minimum, maximum, or range).",
    )
    episode: Optional[Union[List[Union['Episode', str]], 'Episode', str]] = Field(
        default=None,
        description="An episode of a TV, radio or game media within a series or season.",
    )
    gameItem: Optional[Union[List[Union['Thing', str]], 'Thing', str]] = Field(
        default=None,
        description="An item is an object within the game world that can be collected by a player or, occasionally,"
     "a non-player character.",
    )
    numberOfEpisodes: Optional[Union[List[Union[int, 'Integer', str]], int, 'Integer', str]] = Field(
        default=None,
        description="The number of episodes in this season or series.",
    )
    musicBy: Optional[Union[List[Union['Person', 'MusicGroup', str]], 'Person', 'MusicGroup', str]] = Field(
        default=None,
        description="The composer of the soundtrack.",
    )
    gameLocation: Optional[Union[List[Union[AnyUrl, 'URL', 'Place', 'PostalAddress', str]], AnyUrl, 'URL', 'Place', 'PostalAddress', str]] = Field(
        default=None,
        description="Real or fictional location of the game (or part of game).",
    )
    quest: Optional[Union[List[Union['Thing', str]], 'Thing', str]] = Field(
        default=None,
        description="The task that a player-controlled character, or group of characters may complete in"
     "order to gain a reward.",
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
    from pydantic_schemaorg.CreativeWork import CreativeWork
    from pydantic_schemaorg.VideoObject import VideoObject
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.PerformingGroup import PerformingGroup
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.CreativeWorkSeason import CreativeWorkSeason
    from pydantic_schemaorg.Thing import Thing
    from pydantic_schemaorg.GamePlayMode import GamePlayMode
    from pydantic_schemaorg.Integer import Integer
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.MusicGroup import MusicGroup
    from pydantic_schemaorg.Place import Place
    from pydantic_schemaorg.PostalAddress import PostalAddress
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
