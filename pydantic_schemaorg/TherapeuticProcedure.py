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
from pydantic_schemaorg.MedicalProcedure import MedicalProcedure


class TherapeuticProcedure(MedicalProcedure):
    """A medical procedure intended primarily for therapeutic purposes, aimed at improving"
     "a health condition.

    See: https://schema.org/TherapeuticProcedure
    Model depth: 4
    """
    valid_name: ClassVar[str] = "TherapeuticProcedure"
    type_: str = Field("TherapeuticProcedure", alias='@type')
    drug: Optional[Union[List[Union['Drug', str]], 'Drug', str]] = Field(
        default=None,
        description="Specifying a drug or medicine used in a medication procedure.",
    )
    adverseOutcome: Optional[Union[List[Union['MedicalEntity', str]], 'MedicalEntity', str]] = Field(
        default=None,
        description="A possible complication and/or side effect of this therapy. If it is known that an adverse"
     "outcome is serious (resulting in death, disability, or permanent damage; requiring"
     "hospitalization; or otherwise life-threatening or requiring immediate medical attention),"
     "tag it as a seriousAdverseOutcome instead.",
    )
    doseSchedule: Optional[Union[List[Union['DoseSchedule', str]], 'DoseSchedule', str]] = Field(
        default=None,
        description="A dosing schedule for the drug for a given population, either observed, recommended,"
     "or maximum dose based on the type used.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Drug import Drug
    from pydantic_schemaorg.MedicalEntity import MedicalEntity
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
