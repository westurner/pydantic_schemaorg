from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from typing import List, Optional, Union
from pydantic import StrictInt, StrictFloat


from pydantic import Field
from pydantic_schemaorg.TransferAction import TransferAction


class MoneyTransfer(TransferAction):
    """The act of transferring money from one place to another place. This may occur electronically"
     "or physically.

    See: https://schema.org/MoneyTransfer
    Model depth: 4
    """
    valid_name: ClassVar[str] = "MoneyTransfer"
    type_: str = Field("MoneyTransfer", alias='@type')
    beneficiaryBank: Optional[Union[List[Union[str, 'Text', 'BankOrCreditUnion']], str, 'Text', 'BankOrCreditUnion']] = Field(
        default=None,
        description="A bank or bank’s branch, financial institution or international financial institution"
     "operating the beneficiary’s bank account or releasing funds for the beneficiary.",
    )
    amount: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', 'MonetaryAmount', str]], StrictInt, StrictFloat, 'Number', 'MonetaryAmount', str]] = Field(
        default=None,
        description="The amount of money.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.BankOrCreditUnion import BankOrCreditUnion
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
