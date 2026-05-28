from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from pydantic import StrictBool
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.Substance import Substance
from pydantic_schemaorg.Product import Product


class DietarySupplement(Substance, Product):
    """A product taken by mouth that contains a dietary ingredient intended to supplement the"
     "diet. Dietary ingredients may include vitamins, minerals, herbs or other botanicals,"
     "amino acids, and substances such as enzymes, organ tissues, glandulars and metabolites.

    See: https://schema.org/DietarySupplement
    Model depth: 3
    """
    valid_name: ClassVar[str] = "DietarySupplement"
    type_: str = Field("DietarySupplement", alias='@type')
    isProprietary: Optional[Union[List[Union[StrictBool, 'Boolean', str]], StrictBool, 'Boolean', str]] = Field(
        default=None,
        description="True if this item's name is a proprietary/brand name (vs. generic name).",
    )
    activeIngredient: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="An active ingredient, typically chemical compounds and/or biologic substances.",
    )
    safetyConsideration: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Any potential safety concern associated with the supplement. May include interactions"
     "with other drugs and foods, pregnancy, breastfeeding, known adverse reactions, and"
     "documented efficacy of the supplement.",
    )
    recommendedIntake: Optional[Union[List[Union['RecommendedDoseSchedule', str]], 'RecommendedDoseSchedule', str]] = Field(
        default=None,
        description="Recommended intake of this supplement for a given population as defined by a specific"
     "recommending authority.",
    )
    maximumIntake: Optional[Union[List[Union['MaximumDoseSchedule', str]], 'MaximumDoseSchedule', str]] = Field(
        default=None,
        description="Recommended intake of this supplement for a given population as defined by a specific"
     "recommending authority.",
    )
    legalStatus: Optional[Union[List[Union[str, 'Text', 'MedicalEnumeration', 'DrugLegalStatus']], str, 'Text', 'MedicalEnumeration', 'DrugLegalStatus']] = Field(
        default=None,
        description="The drug or supplement's legal status, including any controlled substance schedules"
     "that apply.",
    )
    targetPopulation: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Characteristics of the population for which this is intended, or which typically uses"
     "it, e.g. 'adults'.",
    )
    proprietaryName: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Proprietary name given to the diet plan, typically by its originator or creator.",
    )
    nonProprietaryName: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The generic name of this drug or supplement.",
    )
    mechanismOfAction: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The specific biochemical interaction through which this drug or supplement produces"
     "its pharmacological effect.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Boolean import Boolean
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.RecommendedDoseSchedule import RecommendedDoseSchedule
    from pydantic_schemaorg.MaximumDoseSchedule import MaximumDoseSchedule
    from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration
    from pydantic_schemaorg.DrugLegalStatus import DrugLegalStatus


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
