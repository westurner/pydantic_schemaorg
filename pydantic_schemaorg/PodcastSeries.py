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


class PodcastSeries(CreativeWorkSeries):
    """A podcast is an episodic series of digital audio or video files which a user can download"
     "and listen to.

    See: https://schema.org/PodcastSeries
    Model depth: 4
    """
    valid_name: ClassVar[str] = "PodcastSeries"
    type_: str = Field("PodcastSeries", alias='@type')
    actor: Optional[Union[List[Union['Person', 'PerformingGroup', str]], 'Person', 'PerformingGroup', str]] = Field(
        default=None,
        description="An actor (individual or a group), e.g. in TV, radio, movie, video games etc., or in an event."
     "Actors can be associated with individual items or with a series, episode, clip.",
    )
    webFeed: Optional[Union[List[Union[AnyUrl, 'URL', 'DataFeed', str]], AnyUrl, 'URL', 'DataFeed', str]] = Field(
        default=None,
        description="The URL for a feed, e.g. associated with a podcast series, blog, or series of date-stamped"
     "updates. This is usually RSS or Atom.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.PerformingGroup import PerformingGroup
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.DataFeed import DataFeed


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
