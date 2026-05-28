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
from pydantic_schemaorg.CreativeWork import CreativeWork


class Game(CreativeWork):
    """The Game type represents things which are games. These are typically rule-governed"
     "recreational activities, e.g. role-playing games in which players assume the role"
     "of characters in a fictional setting.

    See: https://schema.org/Game
    Model depth: 3
    """
    valid_name: ClassVar[str] = "Game"
    type_: str = Field("Game", alias='@type')
    characterAttribute: Optional[Union[List[Union['Thing', str]], 'Thing', str]] = Field(
        default=None,
        description="A piece of data that represents a particular aspect of a fictional character (skill,"
     "power, character points, advantage, disadvantage).",
    )
    numberOfPlayers: Optional[Union[List[Union['QuantitativeValue', str]], 'QuantitativeValue', str]] = Field(
        default=None,
        description="Indicate how many people can play this game (minimum, maximum, or range).",
    )
    gameItem: Optional[Union[List[Union['Thing', str]], 'Thing', str]] = Field(
        default=None,
        description="An item is an object within the game world that can be collected by a player or, occasionally,"
     "a non-player character.",
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
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Thing import Thing
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Place import Place
    from pydantic_schemaorg.PostalAddress import PostalAddress


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
