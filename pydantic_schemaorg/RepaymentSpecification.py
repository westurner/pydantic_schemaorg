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
from pydantic_schemaorg.StructuredValue import StructuredValue


class RepaymentSpecification(StructuredValue):
    """A structured value representing repayment.

    See: https://schema.org/RepaymentSpecification
    Model depth: 4
    """
    valid_name: ClassVar[str] = "RepaymentSpecification"
    type_: str = Field("RepaymentSpecification", alias='@type')
    loanPaymentFrequency: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', str]], StrictInt, StrictFloat, 'Number', str]] = Field(
        default=None,
        description="Frequency of payments due, i.e. number of months between payments. This is defined as"
     "a frequency, i.e. the reciprocal of a period of time.",
    )
    downPayment: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', 'MonetaryAmount', str]], StrictInt, StrictFloat, 'Number', 'MonetaryAmount', str]] = Field(
        default=None,
        description="a type of payment made in cash during the onset of the purchase of an expensive good/service."
     "The payment typically represents only a percentage of the full purchase price.",
    )
    numberOfLoanPayments: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', str]], StrictInt, StrictFloat, 'Number', str]] = Field(
        default=None,
        description="The number of payments contractually required at origination to repay the loan. For"
     "monthly paying loans this is the number of months from the contractual first payment"
     "date to the maturity date.",
    )
    loanPaymentAmount: Optional[Union[List[Union['MonetaryAmount', str]], 'MonetaryAmount', str]] = Field(
        default=None,
        description="The amount of money to pay in a single payment.",
    )
    earlyPrepaymentPenalty: Optional[Union[List[Union['MonetaryAmount', str]], 'MonetaryAmount', str]] = Field(
        default=None,
        description="The amount to be paid as a penalty in the event of early payment of the loan.",
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
