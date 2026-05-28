from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from typing import List, Optional, Union
from pydantic import AnyUrl


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class HealthInsurancePlan(Intangible):
    """A US-style health insurance plan, including PPOs, EPOs, and HMOs.

    See: https://schema.org/HealthInsurancePlan
    Model depth: 3
    """
    valid_name: ClassVar[str] = "HealthInsurancePlan"
    type_: str = Field("HealthInsurancePlan", alias='@type')
    healthPlanDrugOption: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="TODO.",
    )
    healthPlanId: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The 14-character, HIOS-generated Plan ID number. (Plan IDs must be unique, even across"
     "different markets.)",
    )
    healthPlanMarketingUrl: Optional[Union[List[Union[AnyUrl, 'URL', str]], AnyUrl, 'URL', str]] = Field(
        default=None,
        description="The URL that goes directly to the plan brochure for the specific standard plan or plan"
     "variation.",
    )
    healthPlanDrugTier: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The tier(s) of drugs offered by this formulary or insurance plan.",
    )
    usesHealthPlanIdStandard: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        default=None,
        description="The standard for interpreting the Plan ID. The preferred is \"HIOS\". See the Centers"
     "for Medicare & Medicaid Services for more details.",
    )
    includesHealthPlanFormulary: Optional[Union[List[Union['HealthPlanFormulary', str]], 'HealthPlanFormulary', str]] = Field(
        default=None,
        description="Formularies covered by this plan.",
    )
    contactPoint: Optional[Union[List[Union['ContactPoint', str]], 'ContactPoint', str]] = Field(
        default=None,
        description="A contact point for a person or organization.",
    )
    benefitsSummaryUrl: Optional[Union[List[Union[AnyUrl, 'URL', str]], AnyUrl, 'URL', str]] = Field(
        default=None,
        description="The URL that goes directly to the summary of benefits and coverage for the specific standard"
     "plan or plan variation.",
    )
    includesHealthPlanNetwork: Optional[Union[List[Union['HealthPlanNetwork', str]], 'HealthPlanNetwork', str]] = Field(
        default=None,
        description="Networks covered by this plan.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.HealthPlanFormulary import HealthPlanFormulary
    from pydantic_schemaorg.ContactPoint import ContactPoint
    from pydantic_schemaorg.HealthPlanNetwork import HealthPlanNetwork


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
