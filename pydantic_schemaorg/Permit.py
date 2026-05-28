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


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class Permit(Intangible):
    """A permit issued by an organization, e.g. a parking pass.

    See: https://schema.org/Permit
    Model depth: 3
    """
    valid_name: ClassVar[str] = "Permit"
    type_: str = Field("Permit", alias='@type')
    issuedBy: Optional[Union[List[Union['Organization', str]], 'Organization', str]] = Field(
        default=None,
        description="The organization issuing the item, for example a [[Permit]], [[Ticket]], or [[Certification]].",
    )
    validFrom: Optional[Union[List[Union[datetime, 'DateTime', date, 'Date', str]], datetime, 'DateTime', date, 'Date', str]] = Field(
        default=None,
        description="The date when the item becomes valid.",
    )
    issuedThrough: Optional[Union[List[Union['Service', str]], 'Service', str]] = Field(
        default=None,
        description="The service through which the permit was granted.",
    )
    validUntil: Optional[Union[List[Union[date, 'Date', str]], date, 'Date', str]] = Field(
        default=None,
        description="The date when the item is no longer valid.",
    )
    validFor: Optional[Union[List[Union['Duration', str]], 'Duration', str]] = Field(
        default=None,
        description="The duration of validity of a permit or similar thing.",
    )
    validIn: Optional[Union[List[Union['AdministrativeArea', str]], 'AdministrativeArea', str]] = Field(
        default=None,
        description="The geographic area where the item is valid. Applies for example to a [[Permit]], a [[Certification]],"
     "or an [[EducationalOccupationalCredential]].",
    )
    permitAudience: Optional[Union[List[Union['Audience', str]], 'Audience', str]] = Field(
        default=None,
        description="The target audience for this permit.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Date import Date
    from pydantic_schemaorg.Service import Service
    from pydantic_schemaorg.Duration import Duration
    from pydantic_schemaorg.AdministrativeArea import AdministrativeArea
    from pydantic_schemaorg.Audience import Audience


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
