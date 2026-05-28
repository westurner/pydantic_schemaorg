from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from typing import List, Optional, Union
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class Clip(CreativeWork):
    """A short TV or radio program or a segment/part of a program.

    See: https://schema.org/Clip
    Model depth: 3
    """
    valid_name: ClassVar[str] = "Clip"
    type_: str = Field("Clip", alias='@type')
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
    clipNumber: Optional[Union[List[Union[int, 'Integer', str, 'Text']], int, 'Integer', str, 'Text']] = Field(
        default=None,
        description="Position of the clip within an ordered group of clips.",
    )
    directors: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="A director of e.g. TV, radio, movie, video games etc. content. Directors can be associated"
     "with individual items or with a series, episode, clip.",
    )
    endOffset: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', 'HyperTocEntry', str]], StrictInt, StrictFloat, 'Number', 'HyperTocEntry', str]] = Field(
        default=None,
        description="The end time of the clip expressed as the number of seconds from the beginning of the work.",
    )
    partOfSeries: Optional[Union[List[Union['CreativeWorkSeries', str]], 'CreativeWorkSeries', str]] = Field(
        default=None,
        description="The series to which this episode or season belongs.",
    )
    startOffset: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', 'HyperTocEntry', str]], StrictInt, StrictFloat, 'Number', 'HyperTocEntry', str]] = Field(
        default=None,
        description="The start time of the clip expressed as the number of seconds from the beginning of the"
     "work.",
    )
    partOfEpisode: Optional[Union[List[Union['Episode', str]], 'Episode', str]] = Field(
        default=None,
        description="The episode to which this clip belongs.",
    )
    musicBy: Optional[Union[List[Union['Person', 'MusicGroup', str]], 'Person', 'MusicGroup', str]] = Field(
        default=None,
        description="The composer of the soundtrack.",
    )
    partOfSeason: Optional[Union[List[Union['CreativeWorkSeason', str]], 'CreativeWorkSeason', str]] = Field(
        default=None,
        description="The season to which this episode belongs.",
    )
    actors: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="An actor, e.g. in TV, radio, movie, video games etc. Actors can be associated with individual"
     "items or with a series, episode, clip.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.PerformingGroup import PerformingGroup
    from pydantic_schemaorg.Integer import Integer
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.HyperTocEntry import HyperTocEntry
    from pydantic_schemaorg.CreativeWorkSeries import CreativeWorkSeries
    from pydantic_schemaorg.Episode import Episode
    from pydantic_schemaorg.MusicGroup import MusicGroup
    from pydantic_schemaorg.CreativeWorkSeason import CreativeWorkSeason


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
