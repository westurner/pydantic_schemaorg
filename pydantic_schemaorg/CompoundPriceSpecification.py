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


class CompoundPriceSpecification(PriceSpecification):
    """A compound price specification is one that bundles multiple prices that all apply in"
     "combination for different dimensions of consumption. Use the name property of the attached"
     "unit price specification for indicating the dimension of a price component (e.g. \"electricity\""
     "or \"final cleaning\").

    See: https://schema.org/CompoundPriceSpecification
    Model depth: 5
    """
    valid_name: ClassVar[str] = "CompoundPriceSpecification"
    type_: str = Field("CompoundPriceSpecification", alias='@type')
    priceType: Optional[Union[List[Union[str, 'Text', 'PriceTypeEnumeration']], str, 'Text', 'PriceTypeEnumeration']] = Field(
        default=None,
        description="Defines the type of a price specified for an offered product, for example a list price,"
     "a (temporary) sale price or a manufacturer suggested retail price. If multiple prices"
     "are specified for an offer the [[priceType]] property can be used to identify the type"
     "of each such specified price. The value of priceType can be specified as a value from enumeration"
     "PriceTypeEnumeration or as a free form text string for price types that are not already"
     "predefined in PriceTypeEnumeration.",
    )
    priceComponent: Optional[Union[List[Union['UnitPriceSpecification', str]], 'UnitPriceSpecification', str]] = Field(
        default=None,
        description="This property links to all [[UnitPriceSpecification]] nodes that apply in parallel"
     "for the [[CompoundPriceSpecification]] node.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.PriceTypeEnumeration import PriceTypeEnumeration
    from pydantic_schemaorg.UnitPriceSpecification import UnitPriceSpecification


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
