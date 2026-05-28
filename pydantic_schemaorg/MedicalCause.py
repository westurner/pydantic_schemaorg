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


class MedicalCause(MedicalEntity):
    """The causative agent(s) that are responsible for the pathophysiologic process that"
     "eventually results in a medical condition, symptom or sign. In this schema, unless otherwise"
     "specified this is meant to be the proximate cause of the medical condition, symptom or"
     "sign. The proximate cause is defined as the causative agent that most directly results"
     "in the medical condition, symptom or sign. For example, the HIV virus could be considered"
     "a cause of AIDS. Or in a diagnostic context, if a patient fell and sustained a hip fracture"
     "and two days later sustained a pulmonary embolism which eventuated in a cardiac arrest,"
     "the cause of the cardiac arrest (the proximate cause) would be the pulmonary embolism"
     "and not the fall. Medical causes can include cardiovascular, chemical, dermatologic,"
     "endocrine, environmental, gastroenterologic, genetic, hematologic, gynecologic,"
     "iatrogenic, infectious, musculoskeletal, neurologic, nutritional, obstetric,"
     "oncologic, otolaryngologic, pharmacologic, psychiatric, pulmonary, renal, rheumatologic,"
     "toxic, traumatic, or urologic causes; medical conditions can be causes as well.

    See: https://schema.org/MedicalCause
    Model depth: 3
    """
    valid_name: ClassVar[str] = "MedicalCause"
    type_: str = Field("MedicalCause", alias='@type')
    causeOf: Optional[Union[List[Union['MedicalEntity', str]], 'MedicalEntity', str]] = Field(
        default=None,
        description="The condition, complication, symptom, sign, etc. caused.",
    )
    


if TYPE_CHECKING:
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
