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
from pydantic_schemaorg.CreativeWork import CreativeWork


class Claim(CreativeWork):
    """A [[Claim]] in Schema.org represents a specific, factually-oriented claim that could"
     "be the [[itemReviewed]] in a [[ClaimReview]]. The content of a claim can be summarized"
     "with the [[text]] property. Variations on well known claims can have their common identity"
     "indicated via [[sameAs]] links, and summarized with a [[name]]. Ideally, a [[Claim]]"
     "description includes enough contextual information to minimize the risk of ambiguity"
     "or inclarity. In practice, many claims are better understood in the context in which"
     "they appear or the interpretations provided by claim reviews. Beyond [[ClaimReview]],"
     "the Claim type can be associated with related creative works - for example a [[ScholarlyArticle]]"
     "or [[Question]] might be [[about]] some [[Claim]]. At this time, Schema.org does not"
     "define any types of relationship between claims. This is a natural area for future exploration.

    See: https://schema.org/Claim
    Model depth: 3
    """
    valid_name: ClassVar[str] = "Claim"
    type_: str = Field("Claim", alias='@type')
    appearance: Optional[Union[List[Union['CreativeWork', str]], 'CreativeWork', str]] = Field(
        default=None,
        description="Indicates an occurrence of a [[Claim]] in some [[CreativeWork]].",
    )
    firstAppearance: Optional[Union[List[Union['CreativeWork', str]], 'CreativeWork', str]] = Field(
        default=None,
        description="Indicates the first known occurrence of a [[Claim]] in some [[CreativeWork]].",
    )
    claimInterpreter: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="For a [[Claim]] interpreted from [[MediaObject]] content, the [[interpretedAsClaim]]"
     "property can be used to indicate a claim contained, implied or refined from the content"
     "of a [[MediaObject]].",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.CreativeWork import CreativeWork
    from pydantic_schemaorg.Person import Person
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
