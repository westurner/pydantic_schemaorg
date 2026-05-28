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
from pydantic_schemaorg.InteractAction import InteractAction


class FollowAction(InteractAction):
    """The act of forming a personal connection with someone/something (object) unidirectionally/asymmetrically"
     "to get updates polled from. Related actions: * [[BefriendAction]]: Unlike BefriendAction,"
     "FollowAction implies that the connection is *not* necessarily reciprocal. * [[SubscribeAction]]:"
     "Unlike SubscribeAction, FollowAction implies that the follower acts as an active agent"
     "constantly/actively polling for updates. * [[RegisterAction]]: Unlike RegisterAction,"
     "FollowAction implies that the agent is interested in continuing receiving updates"
     "from the object. * [[JoinAction]]: Unlike JoinAction, FollowAction implies that the"
     "agent is interested in getting updates from the object. * [[TrackAction]]: Unlike TrackAction,"
     "FollowAction refers to the polling of updates of all aspects of animate objects rather"
     "than the location of inanimate objects (e.g. you track a package, but you don't follow"
     "it).

    See: https://schema.org/FollowAction
    Model depth: 4
    """
    valid_name: ClassVar[str] = "FollowAction"
    type_: str = Field("FollowAction", alias='@type')
    followee: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="A sub property of object. The person or organization being followed.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Person import Person
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
