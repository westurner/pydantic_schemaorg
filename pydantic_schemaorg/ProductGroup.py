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
from pydantic_schemaorg.Product import Product


class ProductGroup(Product):
    """A ProductGroup represents a group of [[Product]]s that vary only in certain well-described"
     "ways, such as by [[size]], [[color]], [[material]] etc. While a ProductGroup itself"
     "is not directly offered for sale, the various varying products that it represents can"
     "be. The ProductGroup serves as a prototype or template, standing in for all of the products"
     "who have an [[isVariantOf]] relationship to it. As such, properties (including additional"
     "types) can be applied to the ProductGroup to represent characteristics shared by each"
     "of the (possibly very many) variants. Properties that reference a ProductGroup are"
     "not included in this mechanism; neither are the following specific properties [[variesBy]],"
     "[[hasVariant]], [[url]].

    See: https://schema.org/ProductGroup
    Model depth: 3
    """
    valid_name: ClassVar[str] = "ProductGroup"
    type_: str = Field("ProductGroup", alias='@type')
    hasVariant: Optional[Union[List[Union['Product', str]], 'Product', str]] = Field(
        default=None,
        description="Indicates a [[Product]] that is a member of this [[ProductGroup]] (or [[ProductModel]]).",
    )
    variesBy: Optional[Union[List[Union[str, 'Text', 'DefinedTerm']], str, 'Text', 'DefinedTerm']] = Field(
        default=None,
        description="Indicates the property or properties by which the variants in a [[ProductGroup]] vary,"
     "e.g. their size, color etc. Schema.org properties can be referenced by their short name"
     "e.g. \"color\"; terms defined elsewhere can be referenced with their URIs.",
    )
    productGroupID: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Indicates a textual identifier for a ProductGroup.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Product import Product
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.DefinedTerm import DefinedTerm


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
