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


class MedicalDevice(MedicalEntity):
    """Any object used in a medical capacity, such as to diagnose or treat a patient.

    See: https://schema.org/MedicalDevice
    Model depth: 3
    """
    valid_name: ClassVar[str] = "MedicalDevice"
    type_: str = Field("MedicalDevice", alias='@type')
    preOp: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="A description of the workup, testing, and other preparations required before implanting"
     "this device.",
    )
    postOp: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="A description of the postoperative procedures, care, and/or followups for this device.",
    )
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
    procedure: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="A description of the procedure involved in setting up, using, and/or installing the"
     "device.",
    )
    adverseOutcome: Optional[Union[List[Union['MedicalEntity', str]], 'MedicalEntity', str]] = Field(
        default=None,
        description="A possible complication and/or side effect of this therapy. If it is known that an adverse"
     "outcome is serious (resulting in death, disability, or permanent damage; requiring"
     "hospitalization; or otherwise life-threatening or requiring immediate medical attention),"
     "tag it as a seriousAdverseOutcome instead.",
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
