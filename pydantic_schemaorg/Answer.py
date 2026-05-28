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
from pydantic_schemaorg.Comment import Comment


class Answer(Comment):
    """An answer offered to a question; perhaps correct, perhaps opinionated or wrong.

    See: https://schema.org/Answer
    Model depth: 4
    """
    valid_name: ClassVar[str] = "Answer"
    type_: str = Field("Answer", alias='@type')
    parentItem: Optional[Union[List[Union['CreativeWork', 'Comment', str]], 'CreativeWork', 'Comment', str]] = Field(
        default=None,
        description="The parent of a question, answer or item in general. Typically used for Q/A discussion"
     "threads e.g. a chain of comments with the first comment being an [[Article]] or other"
     "[[CreativeWork]]. See also [[comment]] which points from something to a comment about"
     "it.",
    )
    answerExplanation: Optional[Union[List[Union['WebContent', 'Comment', str]], 'WebContent', 'Comment', str]] = Field(
        default=None,
        description="A step-by-step or full explanation about Answer. Can outline how this Answer was achieved"
     "or contain more broad clarification or statement about it.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.CreativeWork import CreativeWork
    from pydantic_schemaorg.Comment import Comment
    from pydantic_schemaorg.WebContent import WebContent


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
