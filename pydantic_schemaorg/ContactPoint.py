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


class ContactPoint(StructuredValue):
    """A contact point&#x2014;for example, a Customer Complaints department.

    See: https://schema.org/ContactPoint
    Model depth: 4
    """
    valid_name: ClassVar[str] = "ContactPoint"
    type_: str = Field("ContactPoint", alias='@type')
    serviceArea: Optional[Union[List[Union['Place', 'GeoShape', 'AdministrativeArea', str]], 'Place', 'GeoShape', 'AdministrativeArea', str]] = Field(
        default=None,
        description="The geographic area where the service is provided.",
    )
    email: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Email address.",
    )
    contactType: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="A person or organization can have different contact points, for different purposes."
     "For example, a sales contact point, a PR contact point and so on. This property is used"
     "to specify the kind of contact point.",
    )
    contactOption: Optional[Union[List[Union['ContactPointOption', str]], 'ContactPointOption', str]] = Field(
        default=None,
        description="An option available on this contact point (e.g. a toll-free number or support for hearing-impaired"
     "callers).",
    )
    telephone: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The telephone number.",
    )
    areaServed: Optional[Union[List[Union[str, 'Text', 'Place', 'GeoShape', 'AdministrativeArea']], str, 'Text', 'Place', 'GeoShape', 'AdministrativeArea']] = Field(
        default=None,
        description="The geographic area where a service or offered item is provided.",
    )
    productSupported: Optional[Union[List[Union[str, 'Text', 'Product']], str, 'Text', 'Product']] = Field(
        default=None,
        description="The product or service this support contact point is related to (such as product support"
     "for a particular product line). This can be a specific product or product line (e.g. \"iPhone\")"
     "or a general category of products or services (e.g. \"smartphones\").",
    )
    availableLanguage: Optional[Union[List[Union[str, 'Text', 'Language']], str, 'Text', 'Language']] = Field(
        default=None,
        description="A language someone may use with or at the item, service or place. Please use one of the language"
     "codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also"
     "[[inLanguage]].",
    )
    hoursAvailable: Optional[Union[List[Union['OpeningHoursSpecification', str]], 'OpeningHoursSpecification', str]] = Field(
        default=None,
        description="The hours during which this service or contact is available.",
    )
    faxNumber: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The fax number.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Place import Place
    from pydantic_schemaorg.GeoShape import GeoShape
    from pydantic_schemaorg.AdministrativeArea import AdministrativeArea
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.ContactPointOption import ContactPointOption
    from pydantic_schemaorg.Product import Product
    from pydantic_schemaorg.Language import Language
    from pydantic_schemaorg.OpeningHoursSpecification import OpeningHoursSpecification


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
