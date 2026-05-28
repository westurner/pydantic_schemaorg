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


class DeliveryChargeSpecification(PriceSpecification):
    """The price for the delivery of an offer using a particular delivery method.

    See: https://schema.org/DeliveryChargeSpecification
    Model depth: 5
    """
    valid_name: ClassVar[str] = "DeliveryChargeSpecification"
    type_: str = Field("DeliveryChargeSpecification", alias='@type')
    eligibleRegion: Optional[Union[List[Union[str, 'Text', 'Place', 'GeoShape']], str, 'Text', 'Place', 'GeoShape']] = Field(
        default=None,
        description="The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for"
     "the geo-political region(s) for which the offer or delivery charge specification is"
     "valid. See also [[ineligibleRegion]].",
    )
    areaServed: Optional[Union[List[Union[str, 'Text', 'Place', 'GeoShape', 'AdministrativeArea']], str, 'Text', 'Place', 'GeoShape', 'AdministrativeArea']] = Field(
        default=None,
        description="The geographic area where a service or offered item is provided.",
    )
    ineligibleRegion: Optional[Union[List[Union[str, 'Text', 'Place', 'GeoShape']], str, 'Text', 'Place', 'GeoShape']] = Field(
        default=None,
        description="The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for"
     "the geo-political region(s) for which the offer or delivery charge specification is"
     "not valid, e.g. a region where the transaction is not allowed. See also [[eligibleRegion]].",
    )
    appliesToDeliveryMethod: Optional[Union[List[Union['DeliveryMethod', str]], 'DeliveryMethod', str]] = Field(
        default=None,
        description="The delivery method(s) to which the delivery charge or payment charge specification"
     "applies.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Place import Place
    from pydantic_schemaorg.GeoShape import GeoShape
    from pydantic_schemaorg.AdministrativeArea import AdministrativeArea
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
