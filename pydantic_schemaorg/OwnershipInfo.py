from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from typing import List, Optional, Union
from datetime import datetime


from pydantic import Field
from pydantic_schemaorg.StructuredValue import StructuredValue


class OwnershipInfo(StructuredValue):
    """A structured value providing information about when a certain organization or person"
     "owned a certain product.

    See: https://schema.org/OwnershipInfo
    Model depth: 4
    """
    valid_name: ClassVar[str] = "OwnershipInfo"
    type_: str = Field("OwnershipInfo", alias='@type')
    acquiredFrom: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="The organization or person from which the product was acquired.",
    )
    typeOfGood: Optional[Union[List[Union['Product', 'Service', str]], 'Product', 'Service', str]] = Field(
        default=None,
        description="The product that this structured value is referring to.",
    )
    ownedThrough: Optional[Union[List[Union[datetime, 'DateTime', str]], datetime, 'DateTime', str]] = Field(
        default=None,
        description="The date and time of giving up ownership on the product.",
    )
    ownedFrom: Optional[Union[List[Union[datetime, 'DateTime', str]], datetime, 'DateTime', str]] = Field(
        default=None,
        description="The date and time of obtaining the product.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.Product import Product
    from pydantic_schemaorg.Service import Service
    from pydantic_schemaorg.DateTime import DateTime


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
