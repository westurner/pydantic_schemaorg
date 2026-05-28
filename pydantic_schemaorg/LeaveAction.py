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


class LeaveAction(InteractAction):
    """An agent leaves an event / group with participants/friends at a location. Related actions:"
     "* [[JoinAction]]: The antonym of LeaveAction. * [[UnRegisterAction]]: Unlike UnRegisterAction,"
     "LeaveAction implies leaving a group/team of people rather than a service.

    See: https://schema.org/LeaveAction
    Model depth: 4
    """
    valid_name: ClassVar[str] = "LeaveAction"
    type_: str = Field("LeaveAction", alias='@type')
    event: Optional[Union[List[Union['Event', str]], 'Event', str]] = Field(
        default=None,
        description="Upcoming or past event associated with this place, organization, or action.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Event import Event


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
