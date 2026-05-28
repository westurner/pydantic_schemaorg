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
from pydantic_schemaorg.Thing import Thing


class MedicalEntity(Thing):
    """The most generic type of entity related to health and the practice of medicine.

    See: https://schema.org/MedicalEntity
    Model depth: 2
    """
    valid_name: ClassVar[str] = "MedicalEntity"
    type_: str = Field("MedicalEntity", alias='@type')
    relevantSpecialty: Optional[Union[List[Union['MedicalSpecialty', str]], 'MedicalSpecialty', str]] = Field(
        default=None,
        description="If applicable, a medical specialty in which this entity is relevant.",
    )
    funding: Optional[Union[List[Union['Grant', str]], 'Grant', str]] = Field(
        default=None,
        description="A [[Grant]] that directly or indirectly provide funding or sponsorship for this item."
     "See also [[ownershipFundingInfo]].",
    )
    study: Optional[Union[List[Union['MedicalStudy', str]], 'MedicalStudy', str]] = Field(
        default=None,
        description="A medical study or trial related to this entity.",
    )
    recognizingAuthority: Optional[Union[List[Union['Organization', str]], 'Organization', str]] = Field(
        default=None,
        description="If applicable, the organization that officially recognizes this entity as part of its"
     "endorsed system of medicine.",
    )
    medicineSystem: Optional[Union[List[Union['MedicineSystem', str]], 'MedicineSystem', str]] = Field(
        default=None,
        description="The system of medicine that includes this MedicalEntity, for example 'evidence-based',"
     "'homeopathic', 'chiropractic', etc.",
    )
    code: Optional[Union[List[Union['MedicalCode', str]], 'MedicalCode', str]] = Field(
        default=None,
        description="A medical code for the entity, taken from a controlled vocabulary or ontology such as"
     "ICD-9, DiseasesDB, MeSH, SNOMED-CT, RxNorm, etc.",
    )
    legalStatus: Optional[Union[List[Union[str, 'Text', 'MedicalEnumeration', 'DrugLegalStatus']], str, 'Text', 'MedicalEnumeration', 'DrugLegalStatus']] = Field(
        default=None,
        description="The drug or supplement's legal status, including any controlled substance schedules"
     "that apply.",
    )
    guideline: Optional[Union[List[Union['MedicalGuideline', str]], 'MedicalGuideline', str]] = Field(
        default=None,
        description="A medical guideline related to this entity.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty
    from pydantic_schemaorg.Grant import Grant
    from pydantic_schemaorg.MedicalStudy import MedicalStudy
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.MedicineSystem import MedicineSystem
    from pydantic_schemaorg.MedicalCode import MedicalCode
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration
    from pydantic_schemaorg.DrugLegalStatus import DrugLegalStatus
    from pydantic_schemaorg.MedicalGuideline import MedicalGuideline


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
