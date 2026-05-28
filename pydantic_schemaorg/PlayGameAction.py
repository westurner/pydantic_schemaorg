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
from pydantic_schemaorg.ConsumeAction import ConsumeAction


class PlayGameAction(ConsumeAction):
    """The act of playing a video game.

    See: https://schema.org/PlayGameAction
    Model depth: 4
    """
    valid_name: ClassVar[str] = "PlayGameAction"
    type_: str = Field("PlayGameAction", alias='@type')
    gameAvailabilityType: Optional[Union[List[Union[str, 'Text', 'GameAvailabilityEnumeration']], str, 'Text', 'GameAvailabilityEnumeration']] = Field(
        default=None,
        description="Indicates the availability type of the game content associated with this action, such"
     "as whether it is a full version or a demo.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.GameAvailabilityEnumeration import GameAvailabilityEnumeration


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
