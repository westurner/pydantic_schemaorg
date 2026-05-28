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
from pydantic_schemaorg.WebPage import WebPage


class MedicalWebPage(WebPage):
    """A web page that provides medical information.

    See: https://schema.org/MedicalWebPage
    Model depth: 4
    """
    valid_name: ClassVar[str] = "MedicalWebPage"
    type_: str = Field("MedicalWebPage", alias='@type')
    medicalAudience: Optional[Union[List[Union['MedicalAudienceType', 'MedicalAudience', str]], 'MedicalAudienceType', 'MedicalAudience', str]] = Field(
        default=None,
        description="Medical audience for page.",
    )
    aspect: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="An aspect of medical practice that is considered on the page, such as 'diagnosis', 'treatment',"
     "'causes', 'prognosis', 'etiology', 'epidemiology', etc.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.MedicalAudienceType import MedicalAudienceType
    from pydantic_schemaorg.MedicalAudience import MedicalAudience
    from pydantic_schemaorg.Text import Text


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
