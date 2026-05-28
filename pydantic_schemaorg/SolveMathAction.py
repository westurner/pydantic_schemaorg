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


class SolveMathAction(Action):
    """The action that takes in a math expression and directs users to a page potentially capable"
     "of solving/simplifying that expression.

    See: https://schema.org/SolveMathAction
    Model depth: 3
    """
    valid_name: ClassVar[str] = "SolveMathAction"
    type_: str = Field("SolveMathAction", alias='@type')
    eduQuestionType: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="For questions that are part of learning resources (e.g. Quiz), eduQuestionType indicates"
     "the format of question being given. Example: \"Multiple choice\", \"Open ended\","
     "\"Flashcard\".",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text


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
