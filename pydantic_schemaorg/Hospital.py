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
from pydantic_schemaorg.EmergencyService import EmergencyService
from pydantic_schemaorg.MedicalOrganization import MedicalOrganization
from pydantic_schemaorg.CivicStructure import CivicStructure


class Hospital(EmergencyService, MedicalOrganization, CivicStructure):
    """A hospital.

    See: https://schema.org/Hospital
    Model depth: 4
    """
    valid_name: ClassVar[str] = "Hospital"
    type_: str = Field("Hospital", alias='@type')
    healthcareReportingData: Optional[Union[List[Union['Dataset', 'CDCPMDRecord', str]], 'Dataset', 'CDCPMDRecord', str]] = Field(
        default=None,
        description="Indicates data describing a hospital, e.g. a CDC [[CDCPMDRecord]] or as some kind of"
     "[[Dataset]].",
    )
    medicalSpecialty: Optional[Union[List[Union['MedicalSpecialty', str]], 'MedicalSpecialty', str]] = Field(
        default=None,
        description="A medical specialty of the provider.",
    )
    availableService: Optional[Union[List[Union['MedicalTherapy', 'MedicalProcedure', 'MedicalTest', str]], 'MedicalTherapy', 'MedicalProcedure', 'MedicalTest', str]] = Field(
        default=None,
        description="A medical service available from this provider.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Dataset import Dataset
    from pydantic_schemaorg.CDCPMDRecord import CDCPMDRecord
    from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty
    from pydantic_schemaorg.MedicalTherapy import MedicalTherapy
    from pydantic_schemaorg.MedicalProcedure import MedicalProcedure
    from pydantic_schemaorg.MedicalTest import MedicalTest


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
