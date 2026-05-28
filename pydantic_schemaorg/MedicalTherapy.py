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
from pydantic_schemaorg.TherapeuticProcedure import TherapeuticProcedure


class MedicalTherapy(TherapeuticProcedure):
    """Any medical intervention designed to prevent, treat, and cure human diseases and medical"
     "conditions, including both curative and palliative therapies. Medical therapies"
     "are typically processes of care relying upon pharmacotherapy, behavioral therapy,"
     "supportive therapy (with fluid or nutrition for example), or detoxification (e.g."
     "hemodialysis) aimed at improving or preventing a health condition.

    See: https://schema.org/MedicalTherapy
    Model depth: 5
    """
    valid_name: ClassVar[str] = "MedicalTherapy"
    type_: str = Field("MedicalTherapy", alias='@type')
    contraindication: Optional[Union[List[Union[str, 'Text', 'MedicalContraindication']], str, 'Text', 'MedicalContraindication']] = Field(
        default=None,
        description="A contraindication for this therapy.",
    )
    seriousAdverseOutcome: Optional[Union[List[Union['MedicalEntity', str]], 'MedicalEntity', str]] = Field(
        default=None,
        description="A possible serious complication and/or serious side effect of this therapy. Serious"
     "adverse outcomes include those that are life-threatening; result in death, disability,"
     "or permanent damage; require hospitalization or prolong existing hospitalization;"
     "cause congenital anomalies or birth defects; or jeopardize the patient and may require"
     "medical or surgical intervention to prevent one of the outcomes in this definition.",
    )
    duplicateTherapy: Optional[Union[List[Union['MedicalTherapy', str]], 'MedicalTherapy', str]] = Field(
        default=None,
        description="A therapy that duplicates or overlaps this one.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.MedicalContraindication import MedicalContraindication
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
