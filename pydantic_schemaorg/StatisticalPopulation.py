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
from pydantic_schemaorg.Intangible import Intangible


class StatisticalPopulation(Intangible):
    """A StatisticalPopulation is a set of instances of a certain given type that satisfy some"
     "set of constraints. The property [[populationType]] is used to specify the type. Any"
     "property that can be used on instances of that type can appear on the statistical population."
     "For example, a [[StatisticalPopulation]] representing all [[Person]]s with a [[homeLocation]]"
     "of East Podunk California would be described by applying the appropriate [[homeLocation]]"
     "and [[populationType]] properties to a [[StatisticalPopulation]] item that stands"
     "for that set of people. The properties [[numConstraints]] and [[constraintProperty]]"
     "are used to specify which of the populations properties are used to specify the population."
     "Note that the sense of \"population\" used here is the general sense of a statistical"
     "population, and does not imply that the population consists of people. For example,"
     "a [[populationType]] of [[Event]] or [[NewsArticle]] could be used. See also [[Observation]],"
     "where a [[populationType]] such as [[Person]] or [[Event]] can be indicated directly."
     "In most cases it may be better to use [[StatisticalVariable]] instead of [[StatisticalPopulation]].

    See: https://schema.org/StatisticalPopulation
    Model depth: 3
    """
    valid_name: ClassVar[str] = "StatisticalPopulation"
    type_: str = Field("StatisticalPopulation", alias='@type')
    populationType: Optional[Union[List[Union['Class', str]], 'Class', str]] = Field(
        default=None,
        description="Indicates the populationType common to all members of a [[StatisticalPopulation]]"
     "or all cases within the scope of a [[StatisticalVariable]].",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Class import Class


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
