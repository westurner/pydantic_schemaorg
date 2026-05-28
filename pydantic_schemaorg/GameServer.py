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
from pydantic_schemaorg.Intangible import Intangible


class GameServer(Intangible):
    """Server that provides game interaction in a multiplayer game.

    See: https://schema.org/GameServer
    Model depth: 3
    """
    valid_name: ClassVar[str] = "GameServer"
    type_: str = Field("GameServer", alias='@type')
    game: Optional[Union[List[Union['VideoGame', str]], 'VideoGame', str]] = Field(
        default=None,
        description="Video game which is played on this server.",
    )
    playersOnline: Optional[Union[List[Union[int, 'Integer', str]], int, 'Integer', str]] = Field(
        default=None,
        description="Number of players on the server.",
    )
    serverStatus: Optional[Union[List[Union['GameServerStatus', str]], 'GameServerStatus', str]] = Field(
        default=None,
        description="Status of a game server.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.VideoGame import VideoGame
    from pydantic_schemaorg.Integer import Integer
    from pydantic_schemaorg.GameServerStatus import GameServerStatus


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
