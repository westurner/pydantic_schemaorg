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
from pydantic_schemaorg.Collection import Collection
from pydantic_schemaorg.Product import Product


class ProductCollection(Collection, Product):
    """A set of products (either [[ProductGroup]]s or specific variants) that are listed together"
     "e.g. in an [[Offer]].

    See: https://schema.org/ProductCollection
    Model depth: 3
    """
    valid_name: ClassVar[str] = "ProductCollection"
    type_: str = Field("ProductCollection", alias='@type')
    includesObject: Optional[Union[List[Union['TypeAndQuantityNode', str]], 'TypeAndQuantityNode', str]] = Field(
        default=None,
        description="This links to a node or nodes indicating the exact quantity of the products included in"
     "an [[Offer]] or [[ProductCollection]].",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.TypeAndQuantityNode import TypeAndQuantityNode


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
