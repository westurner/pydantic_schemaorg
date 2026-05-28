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


class SellAction(TradeAction):
    """The act of taking money from a buyer in exchange for goods or services rendered. An agent"
     "sells an object, product, or service to a buyer for a price. Reciprocal of BuyAction.

    See: https://schema.org/SellAction
    Model depth: 4
    """
    valid_name: ClassVar[str] = "SellAction"
    type_: str = Field("SellAction", alias='@type')
    buyer: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="A sub property of participant. The participant/person/organization that bought the"
     "object.",
    )
    warrantyPromise: Optional[Union[List[Union['WarrantyPromise', str]], 'WarrantyPromise', str]] = Field(
        default=None,
        description="The warranty promise(s) included in the offer.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.WarrantyPromise import WarrantyPromise


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
