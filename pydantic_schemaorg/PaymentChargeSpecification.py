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
from pydantic_schemaorg.PriceSpecification import PriceSpecification


class PaymentChargeSpecification(PriceSpecification):
    """The costs of settling the payment using a particular payment method.

    See: https://schema.org/PaymentChargeSpecification
    Model depth: 5
    """
    valid_name: ClassVar[str] = "PaymentChargeSpecification"
    type_: str = Field("PaymentChargeSpecification", alias='@type')
    appliesToPaymentMethod: Optional[Union[List[Union['PaymentMethod', str]], 'PaymentMethod', str]] = Field(
        default=None,
        description="The payment method(s) to which the payment charge specification applies.",
    )
    appliesToDeliveryMethod: Optional[Union[List[Union['DeliveryMethod', str]], 'DeliveryMethod', str]] = Field(
        default=None,
        description="The delivery method(s) to which the delivery charge or payment charge specification"
     "applies.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.PaymentMethod import PaymentMethod
    from pydantic_schemaorg.DeliveryMethod import DeliveryMethod


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
