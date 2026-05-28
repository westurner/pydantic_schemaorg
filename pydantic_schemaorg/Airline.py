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
from pydantic_schemaorg.Organization import Organization


class Airline(Organization):
    """An organization that provides flights for passengers.

    See: https://schema.org/Airline
    Model depth: 3
    """
    valid_name: ClassVar[str] = "Airline"
    type_: str = Field("Airline", alias='@type')
    boardingPolicy: Optional[Union[List[Union['BoardingPolicyType', str]], 'BoardingPolicyType', str]] = Field(
        default=None,
        description="The type of boarding policy used by the airline (e.g. zone-based or group-based).",
    )
    iataCode: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="IATA identifier for an airline or airport.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.BoardingPolicyType import BoardingPolicyType
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
