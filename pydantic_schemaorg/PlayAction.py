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
from pydantic_schemaorg.Action import Action


class PlayAction(Action):
    """The act of playing/exercising/training/performing for enjoyment, leisure, recreation,"
     "competition or exercise. Related actions: * [[ListenAction]]: Unlike ListenAction"
     "(which is under ConsumeAction), PlayAction refers to performing for an audience or"
     "at an event, rather than consuming music. * [[WatchAction]]: Unlike WatchAction (which"
     "is under ConsumeAction), PlayAction refers to showing/displaying for an audience"
     "or at an event, rather than consuming visual content.

    See: https://schema.org/PlayAction
    Model depth: 3
    """
    valid_name: ClassVar[str] = "PlayAction"
    type_: str = Field("PlayAction", alias='@type')
    event: Optional[Union[List[Union['Event', str]], 'Event', str]] = Field(
        default=None,
        description="Upcoming or past event associated with this place, organization, or action.",
    )
    audience: Optional[Union[List[Union['Audience', str]], 'Audience', str]] = Field(
        default=None,
        description="An intended audience, i.e. a group for whom something was created.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Event import Event
    from pydantic_schemaorg.Audience import Audience


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
