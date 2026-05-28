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
from pydantic_schemaorg.CommunicateAction import CommunicateAction


class CommentAction(CommunicateAction):
    """The act of generating a comment about a subject.

    See: https://schema.org/CommentAction
    Model depth: 5
    """
    valid_name: ClassVar[str] = "CommentAction"
    type_: str = Field("CommentAction", alias='@type')
    resultComment: Optional[Union[List[Union['Comment', str]], 'Comment', str]] = Field(
        default=None,
        description="A sub property of result. The Comment created or sent as a result of this action.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Comment import Comment


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
