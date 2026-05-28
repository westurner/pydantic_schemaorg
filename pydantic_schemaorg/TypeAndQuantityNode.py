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
from pydantic_schemaorg.StructuredValue import StructuredValue


class TypeAndQuantityNode(StructuredValue):
    """A structured value indicating the quantity, unit of measurement, and business function"
     "of goods included in a bundle offer.

    See: https://schema.org/TypeAndQuantityNode
    Model depth: 4
    """
    valid_name: ClassVar[str] = "TypeAndQuantityNode"
    type_: str = Field("TypeAndQuantityNode", alias='@type')
    amountOfThisGood: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', str]], StrictInt, StrictFloat, 'Number', str]] = Field(
        default=None,
        description="The quantity of the goods included in the offer.",
    )
    businessFunction: Optional[Union[List[Union['BusinessFunction', str]], 'BusinessFunction', str]] = Field(
        default=None,
        description="The business function (e.g. sell, lease, repair, dispose) of the offer or component"
     "of a bundle (TypeAndQuantityNode). The default is http://purl.org/goodrelations/v1#Sell.",
    )
    unitText: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="A string or text indicating the unit of measurement. Useful if you cannot provide a standard"
     "unit code for <a href='unitCode'>unitCode</a>.",
    )
    typeOfGood: Optional[Union[List[Union['Product', 'Service', str]], 'Product', 'Service', str]] = Field(
        default=None,
        description="The product that this structured value is referring to.",
    )
    unitCode: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        default=None,
        description="The unit of measurement given using the UN/CEFACT Common Code (3 characters) or a URL."
     "Other codes than the UN/CEFACT Common Code may be used with a prefix followed by a colon.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.BusinessFunction import BusinessFunction
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Product import Product
    from pydantic_schemaorg.Service import Service
    from pydantic_schemaorg.URL import URL


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
