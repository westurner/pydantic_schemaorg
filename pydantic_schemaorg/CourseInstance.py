from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from typing import List, Optional, Union
from pydantic import AnyUrl


from pydantic import Field
from pydantic_schemaorg.Event import Event


class CourseInstance(Event):
    """An instance of a [[Course]] which is distinct from other instances because it is offered"
     "at a different time or location or through different media or modes of study or to a specific"
     "section of students.

    See: https://schema.org/CourseInstance
    Model depth: 3
    """
    valid_name: ClassVar[str] = "CourseInstance"
    type_: str = Field("CourseInstance", alias='@type')
    instructor: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="A person assigned to instruct or provide instructional assistance for the [[CourseInstance]].",
    )
    courseSchedule: Optional[Union[List[Union['Schedule', str]], 'Schedule', str]] = Field(
        default=None,
        description="Represents the length and pace of a course, expressed as a [[Schedule]].",
    )
    courseWorkload: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The amount of work expected of students taking the course, often provided as a figure"
     "per week or per month, and may be broken down by type. For example, \"2 hours of lectures,"
     "1 hour of lab work and 3 hours of independent study per week\".",
    )
    courseMode: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        default=None,
        description="The medium or means of delivery of the course instance or the mode of study, either as a"
     "text label (e.g. \"online\", \"onsite\" or \"blended\"; \"synchronous\" or \"asynchronous\";"
     "\"full-time\" or \"part-time\") or as a URL reference to a term from a controlled vocabulary"
     "(e.g. https://ceds.ed.gov/element/001311#Asynchronous).",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Schedule import Schedule
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.URL import URL


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
