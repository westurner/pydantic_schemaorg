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
from pydantic_schemaorg.StructuredValue import StructuredValue


class WarrantyPromise(StructuredValue):
    """A structured value representing the duration and scope of services that will be provided"
     "to a customer free of charge in case of a defect or malfunction of a product.

    See: https://schema.org/WarrantyPromise
    Model depth: 4
    """
    valid_name: ClassVar[str] = "WarrantyPromise"
    type_: str = Field("WarrantyPromise", alias='@type')
    durationOfWarranty: Optional[Union[List[Union['QuantitativeValue', str]], 'QuantitativeValue', str]] = Field(
        default=None,
        description="The duration of the warranty promise. Common unitCode values are ANN for year, MON for"
     "months, or DAY for days.",
    )
    warrantyScope: Optional[Union[List[Union['WarrantyScope', str]], 'WarrantyScope', str]] = Field(
        default=None,
        description="The scope of the warranty promise.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.WarrantyScope import WarrantyScope


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
