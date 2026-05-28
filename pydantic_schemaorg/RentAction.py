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
from pydantic_schemaorg.TradeAction import TradeAction


class RentAction(TradeAction):
    """The act of giving money in return for temporary use, but not ownership, of an object such"
     "as a vehicle or property. For example, an agent rents a property from a landlord in exchange"
     "for a periodic payment.

    See: https://schema.org/RentAction
    Model depth: 4
    """
    valid_name: ClassVar[str] = "RentAction"
    type_: str = Field("RentAction", alias='@type')
    realEstateAgent: Optional[Union[List[Union['RealEstateAgent', str]], 'RealEstateAgent', str]] = Field(
        default=None,
        description="A sub property of participant. The real estate agent involved in the action.",
    )
    landlord: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="A sub property of participant. The owner of the real estate property.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.RealEstateAgent import RealEstateAgent
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
