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
from pydantic_schemaorg.PlayAction import PlayAction


class ExerciseAction(PlayAction):
    """The act of participating in exertive activity for the purposes of improving health and"
     "fitness.

    See: https://schema.org/ExerciseAction
    Model depth: 4
    """
    valid_name: ClassVar[str] = "ExerciseAction"
    type_: str = Field("ExerciseAction", alias='@type')
    exercisePlan: Optional[Union[List[Union['ExercisePlan', str]], 'ExercisePlan', str]] = Field(
        default=None,
        description="A sub property of instrument. The exercise plan used on this action.",
    )
    exerciseRelatedDiet: Optional[Union[List[Union['Diet', str]], 'Diet', str]] = Field(
        default=None,
        description="A sub property of instrument. The diet used in this action.",
    )
    sportsActivityLocation: Optional[Union[List[Union['SportsActivityLocation', str]], 'SportsActivityLocation', str]] = Field(
        default=None,
        description="A sub property of location. The sports activity location where this action occurred.",
    )
    course: Optional[Union[List[Union['Place', str]], 'Place', str]] = Field(
        default=None,
        description="A sub property of location. The course where this action was taken.",
    )
    exerciseType: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Type(s) of exercise or activity, such as strength training, flexibility training,"
     "aerobics, cardiac rehabilitation, etc.",
    )
    distance: Optional[Union[List[Union['Distance', str]], 'Distance', str]] = Field(
        default=None,
        description="The distance travelled, e.g. exercising or travelling.",
    )
    opponent: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="A sub property of participant. The opponent on this action.",
    )
    diet: Optional[Union[List[Union['Diet', str]], 'Diet', str]] = Field(
        default=None,
        description="A sub property of instrument. The diet used in this action.",
    )
    fromLocation: Optional[Union[List[Union['Place', str]], 'Place', str]] = Field(
        default=None,
        description="A sub property of location. The original location of the object or the agent before the"
     "action.",
    )
    sportsEvent: Optional[Union[List[Union['SportsEvent', str]], 'SportsEvent', str]] = Field(
        default=None,
        description="A sub property of location. The sports event where this action occurred.",
    )
    exerciseCourse: Optional[Union[List[Union['Place', str]], 'Place', str]] = Field(
        default=None,
        description="A sub property of location. The course where this action was taken.",
    )
    sportsTeam: Optional[Union[List[Union['SportsTeam', str]], 'SportsTeam', str]] = Field(
        default=None,
        description="A sub property of participant. The sports team that participated on this action.",
    )
    toLocation: Optional[Union[List[Union['Place', str]], 'Place', str]] = Field(
        default=None,
        description="A sub property of location. The final location of the object or the agent after the action.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.ExercisePlan import ExercisePlan
    from pydantic_schemaorg.Diet import Diet
    from pydantic_schemaorg.SportsActivityLocation import SportsActivityLocation
    from pydantic_schemaorg.Place import Place
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Distance import Distance
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.SportsEvent import SportsEvent
    from pydantic_schemaorg.SportsTeam import SportsTeam


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
