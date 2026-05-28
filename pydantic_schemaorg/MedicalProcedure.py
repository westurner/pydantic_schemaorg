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
from pydantic_schemaorg.MedicalEntity import MedicalEntity


class MedicalProcedure(MedicalEntity):
    """A process of care used in either a diagnostic, therapeutic, preventive or palliative"
     "capacity that relies on invasive (surgical), non-invasive, or other techniques.

    See: https://schema.org/MedicalProcedure
    Model depth: 3
    """
    valid_name: ClassVar[str] = "MedicalProcedure"
    type_: str = Field("MedicalProcedure", alias='@type')
    status: Optional[Union[List[Union[str, 'Text', 'EventStatusType', 'MedicalStudyStatus']], str, 'Text', 'EventStatusType', 'MedicalStudyStatus']] = Field(
        default=None,
        description="The status of the study (enumerated).",
    )
    procedureType: Optional[Union[List[Union['MedicalProcedureType', str]], 'MedicalProcedureType', str]] = Field(
        default=None,
        description="The type of procedure, for example Surgical, Noninvasive, or Percutaneous.",
    )
    preparation: Optional[Union[List[Union[str, 'Text', 'MedicalEntity']], str, 'Text', 'MedicalEntity']] = Field(
        default=None,
        description="Typical preparation that a patient must undergo before having the procedure performed.",
    )
    followup: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Typical or recommended followup care after the procedure is performed.",
    )
    howPerformed: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="How the procedure is performed.",
    )
    bodyLocation: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Location in the body of the anatomical structure.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.EventStatusType import EventStatusType
    from pydantic_schemaorg.MedicalStudyStatus import MedicalStudyStatus
    from pydantic_schemaorg.MedicalProcedureType import MedicalProcedureType
    from pydantic_schemaorg.MedicalEntity import MedicalEntity


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
