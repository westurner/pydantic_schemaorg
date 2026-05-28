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
from pydantic_schemaorg.Trip import Trip


class TrainTrip(Trip):
    """A trip on a commercial train line.

    See: https://schema.org/TrainTrip
    Model depth: 4
    """
    valid_name: ClassVar[str] = "TrainTrip"
    type_: str = Field("TrainTrip", alias='@type')
    arrivalStation: Optional[Union[List[Union['TrainStation', str]], 'TrainStation', str]] = Field(
        default=None,
        description="The station where the train trip ends.",
    )
    departureStation: Optional[Union[List[Union['TrainStation', str]], 'TrainStation', str]] = Field(
        default=None,
        description="The station from which the train departs.",
    )
    trainNumber: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The unique identifier for the train.",
    )
    departurePlatform: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The platform from which the train departs.",
    )
    trainName: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The name of the train (e.g. The Orient Express).",
    )
    arrivalPlatform: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The platform where the train arrives.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.TrainStation import TrainStation
    from pydantic_schemaorg.Text import Text


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
