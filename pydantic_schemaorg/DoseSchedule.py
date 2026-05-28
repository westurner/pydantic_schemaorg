from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from typing import List, Optional, Union
from pydantic import AnyUrl, StrictInt, StrictFloat


from pydantic import Field
from pydantic_schemaorg.MedicalIntangible import MedicalIntangible


class DoseSchedule(MedicalIntangible):
    """A specific dosing schedule for a drug or supplement.

    See: https://schema.org/DoseSchedule
    Model depth: 4
    """
    valid_name: ClassVar[str] = "DoseSchedule"
    type_: str = Field("DoseSchedule", alias='@type')
    frequency: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="How often the dose is taken, e.g. 'daily'.",
    )
    targetPopulation: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Characteristics of the population for which this is intended, or which typically uses"
     "it, e.g. 'adults'.",
    )
    doseUnit: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The unit of the dose, e.g. 'mg'.",
    )
    doseValue: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', 'QualitativeValue', str]], StrictInt, StrictFloat, 'Number', 'QualitativeValue', str]] = Field(
        default=None,
        description="The value of the dose, e.g. 500.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.QualitativeValue import QualitativeValue


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
