from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from typing import List, Optional, Union
from datetime import date


from pydantic import Field
from pydantic_schemaorg.MedicalEntity import MedicalEntity


class MedicalGuideline(MedicalEntity):
    """Any recommendation made by a standard society (e.g. ACC/AHA) or consensus statement"
     "that denotes how to diagnose and treat a particular condition. Note: this type should"
     "be used to tag the actual guideline recommendation; if the guideline recommendation"
     "occurs in a larger scholarly article, use MedicalScholarlyArticle to tag the overall"
     "article, not this type. Note also: the organization making the recommendation should"
     "be captured in the recognizingAuthority base property of MedicalEntity.

    See: https://schema.org/MedicalGuideline
    Model depth: 3
    """
    valid_name: ClassVar[str] = "MedicalGuideline"
    type_: str = Field("MedicalGuideline", alias='@type')
    guidelineSubject: Optional[Union[List[Union['MedicalEntity', str]], 'MedicalEntity', str]] = Field(
        default=None,
        description="The medical conditions, treatments, etc. that are the subject of the guideline.",
    )
    evidenceOrigin: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Source of the data used to formulate the guidance, e.g. RCT, consensus opinion, etc.",
    )
    guidelineDate: Optional[Union[List[Union[date, 'Date', str]], date, 'Date', str]] = Field(
        default=None,
        description="Date on which this guideline's recommendation was made.",
    )
    evidenceLevel: Optional[Union[List[Union['MedicalEvidenceLevel', str]], 'MedicalEvidenceLevel', str]] = Field(
        default=None,
        description="Strength of evidence of the data used to formulate the guideline (enumerated).",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.MedicalEntity import MedicalEntity
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Date import Date
    from pydantic_schemaorg.MedicalEvidenceLevel import MedicalEvidenceLevel


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
