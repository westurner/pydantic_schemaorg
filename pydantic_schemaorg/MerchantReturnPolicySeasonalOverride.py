from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from datetime import date, datetime
from typing import List, Optional, Union
from pydantic import StrictInt, StrictFloat


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class MerchantReturnPolicySeasonalOverride(Intangible):
    """A seasonal override of a return policy, for example used for holidays.

    See: https://schema.org/MerchantReturnPolicySeasonalOverride
    Model depth: 3
    """
    valid_name: ClassVar[str] = "MerchantReturnPolicySeasonalOverride"
    type_: str = Field("MerchantReturnPolicySeasonalOverride", alias='@type')
    endDate: Optional[Union[List[Union[datetime, 'DateTime', date, 'Date', str]], datetime, 'DateTime', date, 'Date', str]] = Field(
        default=None,
        description="The end date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).",
    )
    returnPolicyCategory: Optional[Union[List[Union['MerchantReturnEnumeration', str]], 'MerchantReturnEnumeration', str]] = Field(
        default=None,
        description="Specifies an applicable return policy (from an enumeration).",
    )
    returnMethod: Optional[Union[List[Union['ReturnMethodEnumeration', str]], 'ReturnMethodEnumeration', str]] = Field(
        default=None,
        description="The type of return method offered, specified from an enumeration.",
    )
    startDate: Optional[Union[List[Union[datetime, 'DateTime', date, 'Date', str]], datetime, 'DateTime', date, 'Date', str]] = Field(
        default=None,
        description="The start date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).",
    )
    returnFees: Optional[Union[List[Union['ReturnFeesEnumeration', str]], 'ReturnFeesEnumeration', str]] = Field(
        default=None,
        description="The type of return fees for purchased products (for any return reason).",
    )
    merchantReturnDays: Optional[Union[List[Union[datetime, 'DateTime', int, 'Integer', date, 'Date', str]], datetime, 'DateTime', int, 'Integer', date, 'Date', str]] = Field(
        default=None,
        description="Specifies either a fixed return date or the number of days (from the delivery date) that"
     "a product can be returned. Used when the [[returnPolicyCategory]] property is specified"
     "as [[MerchantReturnFiniteReturnWindow]].",
    )
    restockingFee: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', 'MonetaryAmount', str]], StrictInt, StrictFloat, 'Number', 'MonetaryAmount', str]] = Field(
        default=None,
        description="Use [[MonetaryAmount]] to specify a fixed restocking fee for product returns, or use"
     "[[Number]] to specify a percentage of the product price paid by the customer.",
    )
    refundType: Optional[Union[List[Union['RefundTypeEnumeration', str]], 'RefundTypeEnumeration', str]] = Field(
        default=None,
        description="A refund type, from an enumerated list.",
    )
    returnShippingFeesAmount: Optional[Union[List[Union['MonetaryAmount', str]], 'MonetaryAmount', str]] = Field(
        default=None,
        description="Amount of shipping costs for product returns (for any reason). Applicable when property"
     "[[returnFees]] equals [[ReturnShippingFees]].",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Date import Date
    from pydantic_schemaorg.MerchantReturnEnumeration import MerchantReturnEnumeration
    from pydantic_schemaorg.ReturnMethodEnumeration import ReturnMethodEnumeration
    from pydantic_schemaorg.ReturnFeesEnumeration import ReturnFeesEnumeration
    from pydantic_schemaorg.Integer import Integer
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.MonetaryAmount import MonetaryAmount
    from pydantic_schemaorg.RefundTypeEnumeration import RefundTypeEnumeration


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
