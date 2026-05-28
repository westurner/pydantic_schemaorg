from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.FinancialProduct import FinancialProduct
from pydantic_schemaorg.PaymentMethod import PaymentMethod


class PaymentCard(FinancialProduct, PaymentMethod):
    """A payment method using a credit, debit, store or other card to associate the payment with"
     "an account.

    See: https://schema.org/PaymentCard
    Model depth: 4
    """
    valid_name: ClassVar[str] = "PaymentCard"
    type_: str = Field("PaymentCard", alias='@type')
    contactlessPayment: Optional[Union[List[Union[StrictBool, 'Boolean', str]], StrictBool, 'Boolean', str]] = Field(
        default=None,
        description="A secure method for consumers to purchase products or services via debit, credit or smartcards"
     "by using RFID or NFC technology.",
    )
    floorLimit: Optional[Union[List[Union['MonetaryAmount', str]], 'MonetaryAmount', str]] = Field(
        default=None,
        description="A floor limit is the amount of money above which credit card transactions must be authorized.",
    )
    cashBack: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', StrictBool, 'Boolean', str]], StrictInt, StrictFloat, 'Number', StrictBool, 'Boolean', str]] = Field(
        default=None,
        description="A cardholder benefit that pays the cardholder a small percentage of their net expenditures.",
    )
    monthlyMinimumRepaymentAmount: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', 'MonetaryAmount', str]], StrictInt, StrictFloat, 'Number', 'MonetaryAmount', str]] = Field(
        default=None,
        description="The minimum payment is the lowest amount of money that one is required to pay on a credit"
     "card statement each month.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Boolean import Boolean
    from pydantic_schemaorg.MonetaryAmount import MonetaryAmount
    from pydantic_schemaorg.Number import Number


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
