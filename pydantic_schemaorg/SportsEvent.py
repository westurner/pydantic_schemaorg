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
from pydantic_schemaorg.Event import Event


class SportsEvent(Event):
    """Event type: Sports event.

    See: https://schema.org/SportsEvent
    Model depth: 3
    """
    valid_name: ClassVar[str] = "SportsEvent"
    type_: str = Field("SportsEvent", alias='@type')
    referee: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="An official who watches a game or match closely to enforce the rules and arbitrate on matters"
     "arising from the play such as referees, umpires or judges. The name of the effective function"
     "can vary according to the sport.",
    )
    sport: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        default=None,
        description="A type of sport (e.g. Baseball).",
    )
    homeTeam: Optional[Union[List[Union['SportsTeam', 'Person', str]], 'SportsTeam', 'Person', str]] = Field(
        default=None,
        description="The home team in a sports event.",
    )
    competitor: Optional[Union[List[Union['SportsTeam', 'Person', str]], 'SportsTeam', 'Person', str]] = Field(
        default=None,
        description="A competitor in a sports event.",
    )
    awayTeam: Optional[Union[List[Union['SportsTeam', 'Person', str]], 'SportsTeam', 'Person', str]] = Field(
        default=None,
        description="The away team in a sports event.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.SportsTeam import SportsTeam


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
