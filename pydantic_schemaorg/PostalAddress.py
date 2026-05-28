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
from pydantic_schemaorg.ContactPoint import ContactPoint


class PostalAddress(ContactPoint):
    """The mailing address.

    See: https://schema.org/PostalAddress
    Model depth: 5
    """
    valid_name: ClassVar[str] = "PostalAddress"
    type_: str = Field("PostalAddress", alias='@type')
    postOfficeBoxNumber: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The post office box number for PO box addresses.",
    )
    streetAddress: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The street address. For example, 1600 Amphitheatre Pkwy.",
    )
    postalCode: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The postal code. For example, 94043.",
    )
    extendedAddress: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="An address extension such as an apartment number, C/O or alternative name.",
    )
    addressLocality: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The locality in which the street address is, and which is in the region. For example, Mountain"
     "View.",
    )
    addressCountry: Optional[Union[List[Union[str, 'Text', 'Country']], str, 'Text', 'Country']] = Field(
        default=None,
        description="The country. Recommended to be in 2-letter [ISO 3166-1 alpha-2](http://en.wikipedia.org/wiki/ISO_3166-1)"
     "format, for example \"US\". For backward compatibility, a 3-letter [ISO 3166-1 alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3)"
     "country code such as \"SGP\" or a full country name such as \"Singapore\" can also be used.",
    )
    addressRegion: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The region in which the locality is, and which is in the country. For example, California"
     "or another appropriate first-level [Administrative division](https://en.wikipedia.org/wiki/List_of_administrative_divisions_by_country).",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Country import Country


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
