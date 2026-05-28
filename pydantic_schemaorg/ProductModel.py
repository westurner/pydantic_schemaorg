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


class ProductModel(Product):
    """A datasheet or vendor specification of a product (in the sense of a prototypical description).

    See: https://schema.org/ProductModel
    Model depth: 3
    """
    valid_name: ClassVar[str] = "ProductModel"
    type_: str = Field("ProductModel", alias='@type')
    successorOf: Optional[Union[List[Union['ProductModel', str]], 'ProductModel', str]] = Field(
        default=None,
        description="A pointer from a newer variant of a product to its previous, often discontinued predecessor.",
    )
    isVariantOf: Optional[Union[List[Union['ProductGroup', 'ProductModel', str]], 'ProductGroup', 'ProductModel', str]] = Field(
        default=None,
        description="Indicates the kind of product that this is a variant of. In the case of [[ProductModel]],"
     "this is a pointer (from a ProductModel) to a base product from which this product is a variant."
     "It is safe to infer that the variant inherits all product features from the base model,"
     "unless defined locally. This is not transitive. In the case of a [[ProductGroup]], the"
     "group description also serves as a template, representing a set of Products that vary"
     "on explicitly defined, specific dimensions only (so it defines both a set of variants,"
     "as well as which values distinguish amongst those variants). When used with [[ProductGroup]],"
     "this property can apply to any [[Product]] included in the group.",
    )
    predecessorOf: Optional[Union[List[Union['ProductModel', str]], 'ProductModel', str]] = Field(
        default=None,
        description="A pointer from a previous, often discontinued variant of the product to its newer variant.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.ProductGroup import ProductGroup


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
