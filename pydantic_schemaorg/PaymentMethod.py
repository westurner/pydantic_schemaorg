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
from pydantic_schemaorg.Intangible import Intangible


class PaymentMethod(Intangible):
    """A payment method is a standardized procedure for transferring the monetary amount for"
     "a purchase. Payment methods are characterized by the legal and technical structures"
     "used, and by the organization or group carrying out the transaction. The following legacy"
     "values should be accepted: * http://purl.org/goodrelations/v1#ByBankTransferInAdvance"
     "* http://purl.org/goodrelations/v1#ByInvoice * http://purl.org/goodrelations/v1#Cash"
     "* http://purl.org/goodrelations/v1#CheckInAdvance * http://purl.org/goodrelations/v1#COD"
     "* http://purl.org/goodrelations/v1#DirectDebit * http://purl.org/goodrelations/v1#GoogleCheckout"
     "* http://purl.org/goodrelations/v1#PayPal * http://purl.org/goodrelations/v1#PaySwarm"
     "Structured values are recommended for newer payment methods.

    See: https://schema.org/PaymentMethod
    Model depth: 3
    """
    valid_name: ClassVar[str] = "PaymentMethod"
    type_: str = Field("PaymentMethod", alias='@type')
    paymentMethodType: Optional[Union[List[Union['PaymentMethodType', str]], 'PaymentMethodType', str]] = Field(
        default=None,
        description="The type of a payment method.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.PaymentMethodType import PaymentMethodType


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
