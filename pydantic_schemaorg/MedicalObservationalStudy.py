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
from pydantic_schemaorg.MedicalStudy import MedicalStudy


class MedicalObservationalStudy(MedicalStudy):
    """An observational study is a type of medical study that attempts to infer the possible"
     "effect of a treatment through observation of a cohort of subjects over a period of time."
     "In an observational study, the assignment of subjects into treatment groups versus"
     "control groups is outside the control of the investigator. This is in contrast with controlled"
     "studies, such as the randomized controlled trials represented by MedicalTrial, where"
     "each subject is randomly assigned to a treatment group or a control group before the start"
     "of the treatment.

    See: https://schema.org/MedicalObservationalStudy
    Model depth: 4
    """
    valid_name: ClassVar[str] = "MedicalObservationalStudy"
    type_: str = Field("MedicalObservationalStudy", alias='@type')
    studyDesign: Optional[Union[List[Union['MedicalObservationalStudyDesign', str]], 'MedicalObservationalStudyDesign', str]] = Field(
        default=None,
        description="Specifics about the observational study design (enumerated).",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.MedicalObservationalStudyDesign import MedicalObservationalStudyDesign


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
