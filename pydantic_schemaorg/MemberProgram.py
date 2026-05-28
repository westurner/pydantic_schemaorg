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


class MemberProgram(Intangible):
    """A MemberProgram defines a loyalty (or membership) program that provides its members"
     "with certain benefits, for example better pricing, free shipping or returns, or the"
     "ability to earn loyalty points. Member programs may have multiple tiers, for example"
     "silver and gold members, each with different benefits.

    See: https://schema.org/MemberProgram
    Model depth: 3
    """
    valid_name: ClassVar[str] = "MemberProgram"
    type_: str = Field("MemberProgram", alias='@type')
    hasTiers: Optional[Union[List[Union['MemberProgramTier', str]], 'MemberProgramTier', str]] = Field(
        default=None,
        description="The tiers of a member program.",
    )
    hostingOrganization: Optional[Union[List[Union['Organization', str]], 'Organization', str]] = Field(
        default=None,
        description="The Organization (airline, travelers' club, retailer, etc.) the membership is made"
     "with or which offers the MemberProgram.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.MemberProgramTier import MemberProgramTier
    from pydantic_schemaorg.Organization import Organization


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
