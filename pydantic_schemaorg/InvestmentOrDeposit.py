from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from pydantic import AnyUrl, StrictInt, StrictFloat
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.FinancialProduct import FinancialProduct


class InvestmentOrDeposit(FinancialProduct):
    """A type of financial product that typically requires the client to transfer funds to a"
     "financial service in return for potential beneficial financial return.

    See: https://schema.org/InvestmentOrDeposit
    Model depth: 5
    """
    valid_name: ClassVar[str] = "InvestmentOrDeposit"
    type_: str = Field("InvestmentOrDeposit", alias='@type')
    amount: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', 'MonetaryAmount', str]], StrictInt, StrictFloat, 'Number', 'MonetaryAmount', str]] = Field(
        default=None,
        description="The amount of money.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.MonetaryAmount import MonetaryAmount


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
