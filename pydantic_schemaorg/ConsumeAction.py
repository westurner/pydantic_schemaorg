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
from pydantic_schemaorg.Action import Action


class ConsumeAction(Action):
    """The act of ingesting information/resources/food.

    See: https://schema.org/ConsumeAction
    Model depth: 3
    """
    valid_name: ClassVar[str] = "ConsumeAction"
    type_: str = Field("ConsumeAction", alias='@type')
    actionAccessibilityRequirement: Optional[Union[List[Union['ActionAccessSpecification', str]], 'ActionAccessSpecification', str]] = Field(
        default=None,
        description="A set of requirements that must be fulfilled in order to perform an Action. If more than"
     "one value is specified, fulfilling one set of requirements will allow the Action to be"
     "performed.",
    )
    expectsAcceptanceOf: Optional[Union[List[Union['Offer', str]], 'Offer', str]] = Field(
        default=None,
        description="An Offer which must be accepted before the user can perform the Action. For example, the"
     "user may need to buy a movie before being able to watch it.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.ActionAccessSpecification import ActionAccessSpecification
    from pydantic_schemaorg.Offer import Offer


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
