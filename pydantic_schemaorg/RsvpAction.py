from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from pydantic import StrictInt, StrictFloat
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.InformAction import InformAction


class RsvpAction(InformAction):
    """The act of notifying an event organizer as to whether you expect to attend the event.

    See: https://schema.org/RsvpAction
    Model depth: 6
    """
    valid_name: ClassVar[str] = "RsvpAction"
    type_: str = Field("RsvpAction", alias='@type')
    additionalNumberOfGuests: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', str]], StrictInt, StrictFloat, 'Number', str]] = Field(
        default=None,
        description="If responding yes, the number of guests who will attend in addition to the invitee.",
    )
    rsvpResponse: Optional[Union[List[Union['RsvpResponseType', str]], 'RsvpResponseType', str]] = Field(
        default=None,
        description="The response (yes, no, maybe) to the RSVP.",
    )
    comment: Optional[Union[List[Union['Comment', str]], 'Comment', str]] = Field(
        default=None,
        description="Comments, typically from users.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.RsvpResponseType import RsvpResponseType
    from pydantic_schemaorg.Comment import Comment


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
