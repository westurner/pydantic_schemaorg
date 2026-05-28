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
from pydantic_schemaorg.CreativeWorkSeries import CreativeWorkSeries


class MovieSeries(CreativeWorkSeries):
    """A series of movies. Included movies can be indicated with the hasPart property.

    See: https://schema.org/MovieSeries
    Model depth: 4
    """
    valid_name: ClassVar[str] = "MovieSeries"
    type_: str = Field("MovieSeries", alias='@type')
    trailer: Optional[Union[List[Union['VideoObject', str]], 'VideoObject', str]] = Field(
        default=None,
        description="The trailer of a movie or TV/radio series, season, episode, etc.",
    )
    actor: Optional[Union[List[Union['Person', 'PerformingGroup', str]], 'Person', 'PerformingGroup', str]] = Field(
        default=None,
        description="An actor (individual or a group), e.g. in TV, radio, movie, video games etc., or in an event."
     "Actors can be associated with individual items or with a series, episode, clip.",
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
    musicBy: Optional[Union[List[Union['Person', 'MusicGroup', str]], 'Person', 'MusicGroup', str]] = Field(
        default=None,
        description="The composer of the soundtrack.",
    )
    actors: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="An actor, e.g. in TV, radio, movie, video games etc. Actors can be associated with individual"
     "items or with a series, episode, clip.",
    )
    productionCompany: Optional[Union[List[Union['Organization', str]], 'Organization', str]] = Field(
        default=None,
        description="The production company or studio responsible for the item, e.g. series, video game,"
     "episode etc.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.VideoObject import VideoObject
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.PerformingGroup import PerformingGroup
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
