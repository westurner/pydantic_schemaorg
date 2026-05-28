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
from pydantic_schemaorg.SportsOrganization import SportsOrganization


class SportsTeam(SportsOrganization):
    """Organization: Sports team.

    See: https://schema.org/SportsTeam
    Model depth: 4
    """
    valid_name: ClassVar[str] = "SportsTeam"
    type_: str = Field("SportsTeam", alias='@type')
    coach: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="A person that acts in a coaching role for a sports team.",
    )
    gender: Optional[Union[List[Union[str, 'Text', 'GenderType']], str, 'Text', 'GenderType']] = Field(
        default=None,
        description="Gender of something, typically a [[Person]], but possibly also fictional characters,"
     "animals, etc. While https://schema.org/Male and https://schema.org/Female may"
     "be used, text strings are also acceptable for people who are not a binary gender. The [[gender]]"
     "property can also be used in an extended sense to cover e.g. the gender of sports teams."
     "As with the gender of individuals, we do not try to enumerate all possibilities. A mixed-gender"
     "[[SportsTeam]] can be indicated with a text value of \"Mixed\".",
    )
    athlete: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="A person that acts as performing member of a sports team; a player as opposed to a coach.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.GenderType import GenderType


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
