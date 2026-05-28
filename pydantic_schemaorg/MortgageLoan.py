from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from typing import List, Optional, Union
from pydantic import StrictBool


from pydantic import Field
from pydantic_schemaorg.LoanOrCredit import LoanOrCredit


class MortgageLoan(LoanOrCredit):
    """A loan in which property or real estate is used as collateral. (A loan securitized against"
     "some real estate.)

    See: https://schema.org/MortgageLoan
    Model depth: 6
    """
    valid_name: ClassVar[str] = "MortgageLoan"
    type_: str = Field("MortgageLoan", alias='@type')
    loanMortgageMandateAmount: Optional[Union[List[Union['MonetaryAmount', str]], 'MonetaryAmount', str]] = Field(
        default=None,
        description="Amount of mortgage mandate that can be converted into a proper mortgage at a later stage.",
    )
    domiciledMortgage: Optional[Union[List[Union[StrictBool, 'Boolean', str]], StrictBool, 'Boolean', str]] = Field(
        default=None,
        description="Whether borrower is a resident of the jurisdiction where the property is located.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.MonetaryAmount import MonetaryAmount
    from pydantic_schemaorg.Boolean import Boolean


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
