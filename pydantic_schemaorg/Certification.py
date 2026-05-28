from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from typing import List, Optional, Union
from datetime import date, datetime
from pydantic import AnyUrl


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class Certification(CreativeWork):
    """A Certification is an official and authoritative statement about a subject, for example"
     "a product, service, person, or organization. A certification is typically issued by"
     "an indendent certification body, for example a professional organization or government."
     "It formally attests certain characteristics about the subject, for example Organizations"
     "can be ISO certified, Food products can be certified Organic or Vegan, a Person can be"
     "a certified professional, a Place can be certified for food processing. There are certifications"
     "for many domains: regulatory, organizational, recycling, food, efficiency, educational,"
     "ecological, etc. A certification is a form of credential, as are accreditations and"
     "licenses. Mapped from the [gs1:CertificationDetails](https://www.gs1.org/voc/CertificationDetails)"
     "class in the GS1 Web Vocabulary.

    See: https://schema.org/Certification
    Model depth: 3
    """
    valid_name: ClassVar[str] = "Certification"
    type_: str = Field("Certification", alias='@type')
    issuedBy: Optional[Union[List[Union['Organization', str]], 'Organization', str]] = Field(
        default=None,
        description="The organization issuing the item, for example a [[Permit]], [[Ticket]], or [[Certification]].",
    )
    about: Optional[Union[List[Union['Thing', str]], 'Thing', str]] = Field(
        default=None,
        description="The subject matter of the content.",
    )
    auditDate: Optional[Union[List[Union[datetime, 'DateTime', date, 'Date', str]], datetime, 'DateTime', date, 'Date', str]] = Field(
        default=None,
        description="Date when a certification was last audited. See also [gs1:certificationAuditDate](https://www.gs1.org/voc/certificationAuditDate).",
    )
    validFrom: Optional[Union[List[Union[datetime, 'DateTime', date, 'Date', str]], datetime, 'DateTime', date, 'Date', str]] = Field(
        default=None,
        description="The date when the item becomes valid.",
    )
    certificationIdentification: Optional[Union[List[Union[str, 'Text', 'DefinedTerm']], str, 'Text', 'DefinedTerm']] = Field(
        default=None,
        description="Identifier of a certification instance (as registered with an independent certification"
     "body). Typically this identifier can be used to consult and verify the certification"
     "instance. See also [gs1:certificationIdentification](https://www.gs1.org/voc/certificationIdentification).",
    )
    datePublished: Optional[Union[List[Union[datetime, 'DateTime', date, 'Date', str]], datetime, 'DateTime', date, 'Date', str]] = Field(
        default=None,
        description="Date of first publication or broadcast. For example the date a [[CreativeWork]] was"
     "broadcast or a [[Certification]] was issued.",
    )
    expires: Optional[Union[List[Union[datetime, 'DateTime', date, 'Date', str]], datetime, 'DateTime', date, 'Date', str]] = Field(
        default=None,
        description="Date the content expires and is no longer useful or available. For example a [[VideoObject]]"
     "or [[NewsArticle]] whose availability or relevance is time-limited, a [[ClaimReview]]"
     "fact check whose publisher wants to indicate that it may no longer be relevant (or helpful"
     "to highlight) after some date, or a [[Certification]] the validity has expired.",
    )
    certificationStatus: Optional[Union[List[Union['CertificationStatusEnumeration', str]], 'CertificationStatusEnumeration', str]] = Field(
        default=None,
        description="Indicates the current status of a certification: active or inactive. See also [gs1:certificationStatus](https://www.gs1.org/voc/certificationStatus).",
    )
    certificationRating: Optional[Union[List[Union['Rating', str]], 'Rating', str]] = Field(
        default=None,
        description="Rating of a certification instance (as defined by an independent certification body)."
     "Typically this rating can be used to rate the level to which the requirements of the certification"
     "instance are fulfilled. See also [gs1:certificationValue](https://www.gs1.org/voc/certificationValue).",
    )
    logo: Optional[Union[List[Union[AnyUrl, 'URL', 'ImageObject', str]], AnyUrl, 'URL', 'ImageObject', str]] = Field(
        default=None,
        description="An associated logo.",
    )
    hasMeasurement: Optional[Union[List[Union['QuantitativeValue', str]], 'QuantitativeValue', str]] = Field(
        default=None,
        description="A measurement of an item, For example, the inseam of pants, the wheel size of a bicycle,"
     "the gauge of a screw, or the carbon footprint measured for certification by an authority."
     "Usually an exact measurement, but can also be a range of measurements for adjustable"
     "products, for example belts and ski bindings.",
    )
    validIn: Optional[Union[List[Union['AdministrativeArea', str]], 'AdministrativeArea', str]] = Field(
        default=None,
        description="The geographic area where the item is valid. Applies for example to a [[Permit]], a [[Certification]],"
     "or an [[EducationalOccupationalCredential]].",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.Thing import Thing
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Date import Date
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.DefinedTerm import DefinedTerm
    from pydantic_schemaorg.CertificationStatusEnumeration import CertificationStatusEnumeration
    from pydantic_schemaorg.Rating import Rating
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.ImageObject import ImageObject
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.AdministrativeArea import AdministrativeArea


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
