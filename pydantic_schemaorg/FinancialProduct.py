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
from pydantic_schemaorg.Service import Service


class FinancialProduct(Service):
    """A product provided to consumers and businesses by financial institutions such as banks,"
     "insurance companies, brokerage firms, consumer finance companies, and investment"
     "companies which comprise the financial services industry.

    See: https://schema.org/FinancialProduct
    Model depth: 4
    """
    valid_name: ClassVar[str] = "FinancialProduct"
    type_: str = Field("FinancialProduct", alias='@type')
    interestRate: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', 'QuantitativeValue', str]], StrictInt, StrictFloat, 'Number', 'QuantitativeValue', str]] = Field(
        default=None,
        description="The interest rate, charged or paid, applicable to the financial product. Note: This"
     "is different from the calculated annualPercentageRate.",
    )
    feesAndCommissionsSpecification: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        default=None,
        description="Description of fees, commissions, and other terms applied either to a class of financial"
     "product, or by a financial service organization.",
    )
    annualPercentageRate: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', 'QuantitativeValue', str]], StrictInt, StrictFloat, 'Number', 'QuantitativeValue', str]] = Field(
        default=None,
        description="The annual rate that is charged for borrowing (or made by investing), expressed as a single"
     "percentage number that represents the actual yearly cost of funds over the term of a loan."
     "This includes any fees or additional costs associated with the transaction.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.URL import URL
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
