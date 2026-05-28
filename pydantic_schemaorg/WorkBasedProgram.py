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
from pydantic_schemaorg.EducationalOccupationalProgram import EducationalOccupationalProgram


class WorkBasedProgram(EducationalOccupationalProgram):
    """A program with both an educational and employment component. Typically based at a workplace"
     "and structured around work-based learning, with the aim of instilling competencies"
     "related to an occupation. WorkBasedProgram is used to distinguish programs such as"
     "apprenticeships from school, college or other classroom based educational programs.

    See: https://schema.org/WorkBasedProgram
    Model depth: 4
    """
    valid_name: ClassVar[str] = "WorkBasedProgram"
    type_: str = Field("WorkBasedProgram", alias='@type')
    occupationalCategory: Optional[Union[List[Union[str, 'Text', 'CategoryCode']], str, 'Text', 'CategoryCode']] = Field(
        default=None,
        description="A category describing the job, preferably using a term from a taxonomy such as [BLS O*NET-SOC](http://www.onetcenter.org/taxonomy.html),"
     "[ISCO-08](https://www.ilo.org/public/english/bureau/stat/isco/isco08/) or"
     "similar, with the property repeated for each applicable value. Ideally the taxonomy"
     "should be identified, and both the textual label and formal code for the category should"
     "be provided. Note: for historical reasons, any textual label and formal code provided"
     "as a literal may be assumed to be from O*NET-SOC.",
    )
    trainingSalary: Optional[Union[List[Union['MonetaryAmountDistribution', str]], 'MonetaryAmountDistribution', str]] = Field(
        default=None,
        description="The estimated salary earned while in the program.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.CategoryCode import CategoryCode
    from pydantic_schemaorg.MonetaryAmountDistribution import MonetaryAmountDistribution


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
