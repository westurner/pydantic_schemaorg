from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from pydantic import AnyUrl, StrictBool
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.Substance import Substance
from pydantic_schemaorg.Product import Product


class Drug(Substance, Product):
    """A chemical or biologic substance, used as a medical therapy, that has a physiological"
     "effect on an organism. Here the term drug is used interchangeably with the term medicine"
     "although clinical knowledge makes a clear difference between them.

    See: https://schema.org/Drug
    Model depth: 3
    """
    valid_name: ClassVar[str] = "Drug"
    type_: str = Field("Drug", alias='@type')
    isProprietary: Optional[Union[List[Union[StrictBool, 'Boolean', str]], StrictBool, 'Boolean', str]] = Field(
        default=None,
        description="True if this item's name is a proprietary/brand name (vs. generic name).",
    )
    activeIngredient: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="An active ingredient, typically chemical compounds and/or biologic substances.",
    )
    pregnancyWarning: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Any precaution, guidance, contraindication, etc. related to this drug's use during"
     "pregnancy.",
    )
    foodWarning: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Any precaution, guidance, contraindication, etc. related to consumption of specific"
     "foods while taking this drug.",
    )
    relatedDrug: Optional[Union[List[Union['Drug', str]], 'Drug', str]] = Field(
        default=None,
        description="Any other drug related to this one, for example commonly-prescribed alternatives.",
    )
    clinicalPharmacology: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Description of the absorption and elimination of drugs, including their concentration"
     "(pharmacokinetics, pK) and biological effects (pharmacodynamics, pD).",
    )
    alcoholWarning: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Any precaution, guidance, contraindication, etc. related to consumption of alcohol"
     "while taking this drug.",
    )
    drugClass: Optional[Union[List[Union['DrugClass', str]], 'DrugClass', str]] = Field(
        default=None,
        description="The class of drug this belongs to (e.g., statins).",
    )
    dosageForm: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="A dosage form in which this drug/supplement is available, e.g. 'tablet', 'suspension',"
     "'injection'.",
    )
    interactingDrug: Optional[Union[List[Union['Drug', str]], 'Drug', str]] = Field(
        default=None,
        description="Another drug that is known to interact with this drug in a way that impacts the effect of"
     "this drug or causes a risk to the patient. Note: disease interactions are typically captured"
     "as contraindications.",
    )
    availableStrength: Optional[Union[List[Union['DrugStrength', str]], 'DrugStrength', str]] = Field(
        default=None,
        description="An available dosage strength for the drug.",
    )
    maximumIntake: Optional[Union[List[Union['MaximumDoseSchedule', str]], 'MaximumDoseSchedule', str]] = Field(
        default=None,
        description="Recommended intake of this supplement for a given population as defined by a specific"
     "recommending authority.",
    )
    rxcui: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The RxCUI drug identifier from RXNORM.",
    )
    administrationRoute: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="A route by which this drug may be administered, e.g. 'oral'.",
    )
    prescriptionStatus: Optional[Union[List[Union[str, 'Text', 'DrugPrescriptionStatus']], str, 'Text', 'DrugPrescriptionStatus']] = Field(
        default=None,
        description="Indicates the status of drug prescription, e.g. local catalogs classifications or"
     "whether the drug is available by prescription or over-the-counter, etc.",
    )
    drugUnit: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The unit in which the drug is measured, e.g. '5 mg tablet'.",
    )
    legalStatus: Optional[Union[List[Union[str, 'Text', 'MedicalEnumeration', 'DrugLegalStatus']], str, 'Text', 'MedicalEnumeration', 'DrugLegalStatus']] = Field(
        default=None,
        description="The drug or supplement's legal status, including any controlled substance schedules"
     "that apply.",
    )
    pregnancyCategory: Optional[Union[List[Union['DrugPregnancyCategory', str]], 'DrugPregnancyCategory', str]] = Field(
        default=None,
        description="Pregnancy category of this drug.",
    )
    warning: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        default=None,
        description="Any FDA or other warnings about the drug (text or URL).",
    )
    overdosage: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Any information related to overdose on a drug, including signs or symptoms, treatments,"
     "contact information for emergency response.",
    )
    isAvailableGenerically: Optional[Union[List[Union[StrictBool, 'Boolean', str]], StrictBool, 'Boolean', str]] = Field(
        default=None,
        description="True if the drug is available in a generic form (regardless of name).",
    )
    breastfeedingWarning: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Any precaution, guidance, contraindication, etc. related to this drug's use by breastfeeding"
     "mothers.",
    )
    proprietaryName: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Proprietary name given to the diet plan, typically by its originator or creator.",
    )
    includedInHealthInsurancePlan: Optional[Union[List[Union['HealthInsurancePlan', str]], 'HealthInsurancePlan', str]] = Field(
        default=None,
        description="The insurance plans that cover this drug.",
    )
    labelDetails: Optional[Union[List[Union[AnyUrl, 'URL', str]], AnyUrl, 'URL', str]] = Field(
        default=None,
        description="Link to the drug's label details.",
    )
    prescribingInfo: Optional[Union[List[Union[AnyUrl, 'URL', str]], AnyUrl, 'URL', str]] = Field(
        default=None,
        description="Link to prescribing information for the drug.",
    )
    doseSchedule: Optional[Union[List[Union['DoseSchedule', str]], 'DoseSchedule', str]] = Field(
        default=None,
        description="A dosing schedule for the drug for a given population, either observed, recommended,"
     "or maximum dose based on the type used.",
    )
    nonProprietaryName: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The generic name of this drug or supplement.",
    )
    clincalPharmacology: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Description of the absorption and elimination of drugs, including their concentration"
     "(pharmacokinetics, pK) and biological effects (pharmacodynamics, pD).",
    )
    mechanismOfAction: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The specific biochemical interaction through which this drug or supplement produces"
     "its pharmacological effect.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Boolean import Boolean
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.DrugClass import DrugClass
    from pydantic_schemaorg.DrugStrength import DrugStrength
    from pydantic_schemaorg.MaximumDoseSchedule import MaximumDoseSchedule
    from pydantic_schemaorg.DrugPrescriptionStatus import DrugPrescriptionStatus
    from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration
    from pydantic_schemaorg.DrugLegalStatus import DrugLegalStatus
    from pydantic_schemaorg.DrugPregnancyCategory import DrugPregnancyCategory
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.HealthInsurancePlan import HealthInsurancePlan
    from pydantic_schemaorg.DoseSchedule import DoseSchedule


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
