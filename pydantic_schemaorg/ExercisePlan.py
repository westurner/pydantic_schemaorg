from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from typing import List, Optional, Union
from pydantic import StrictInt, StrictFloat


from pydantic import Field
from pydantic_schemaorg.PhysicalActivity import PhysicalActivity
from pydantic_schemaorg.CreativeWork import CreativeWork


class ExercisePlan(PhysicalActivity, CreativeWork):
    """Fitness-related activity designed for a specific health-related purpose, including"
     "defined exercise routines as well as activity prescribed by a clinician.

    See: https://schema.org/ExercisePlan
    Model depth: 3
    """
    valid_name: ClassVar[str] = "ExercisePlan"
    type_: str = Field("ExercisePlan", alias='@type')
    activityFrequency: Optional[Union[List[Union[str, 'Text', 'QuantitativeValue']], str, 'Text', 'QuantitativeValue']] = Field(
        default=None,
        description="How often one should engage in the activity.",
    )
    additionalVariable: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Any additional component of the exercise prescription that may need to be articulated"
     "to the patient. This may include the order of exercises, the number of repetitions of"
     "movement, quantitative distance, progressions over time, etc.",
    )
    exerciseType: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Type(s) of exercise or activity, such as strength training, flexibility training,"
     "aerobics, cardiac rehabilitation, etc.",
    )
    restPeriods: Optional[Union[List[Union[str, 'Text', 'QuantitativeValue']], str, 'Text', 'QuantitativeValue']] = Field(
        default=None,
        description="How often one should break from the activity.",
    )
    repetitions: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', 'QuantitativeValue', str]], StrictInt, StrictFloat, 'Number', 'QuantitativeValue', str]] = Field(
        default=None,
        description="Number of times one should repeat the activity.",
    )
    activityDuration: Optional[Union[List[Union['QuantitativeValue', 'Duration', str]], 'QuantitativeValue', 'Duration', str]] = Field(
        default=None,
        description="Length of time to engage in the activity.",
    )
    intensity: Optional[Union[List[Union[str, 'Text', 'QuantitativeValue']], str, 'Text', 'QuantitativeValue']] = Field(
        default=None,
        description="Quantitative measure gauging the degree of force involved in the exercise, for example,"
     "heartbeats per minute. May include the velocity of the movement.",
    )
    workload: Optional[Union[List[Union['QuantitativeValue', 'Energy', str]], 'QuantitativeValue', 'Energy', str]] = Field(
        default=None,
        description="Quantitative measure of the physiologic output of the exercise; also referred to as"
     "energy expenditure.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.Duration import Duration
    from pydantic_schemaorg.Energy import Energy


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
