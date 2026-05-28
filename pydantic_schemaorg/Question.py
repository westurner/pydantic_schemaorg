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


class Question(Comment):
    """A specific question - e.g. from a user seeking answers online, or collected in a Frequently"
     "Asked Questions (FAQ) document.

    See: https://schema.org/Question
    Model depth: 4
    """
    valid_name: ClassVar[str] = "Question"
    type_: str = Field("Question", alias='@type')
    parentItem: Optional[Union[List[Union['CreativeWork', 'Comment', str]], 'CreativeWork', 'Comment', str]] = Field(
        default=None,
        description="The parent of a question, answer or item in general. Typically used for Q/A discussion"
     "threads e.g. a chain of comments with the first comment being an [[Article]] or other"
     "[[CreativeWork]]. See also [[comment]] which points from something to a comment about"
     "it.",
    )
    answerCount: Optional[Union[List[Union[int, 'Integer', str]], int, 'Integer', str]] = Field(
        default=None,
        description="The number of answers this question has received.",
    )
    suggestedAnswer: Optional[Union[List[Union['Answer', 'ItemList', str]], 'Answer', 'ItemList', str]] = Field(
        default=None,
        description="An answer (possibly one of several, possibly incorrect) to a Question, e.g. on a Question/Answer"
     "site.",
    )
    eduQuestionType: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="For questions that are part of learning resources (e.g. Quiz), eduQuestionType indicates"
     "the format of question being given. Example: \"Multiple choice\", \"Open ended\","
     "\"Flashcard\".",
    )
    acceptedAnswer: Optional[Union[List[Union['Answer', 'ItemList', str]], 'Answer', 'ItemList', str]] = Field(
        default=None,
        description="The answer(s) that has been accepted as best, typically on a Question/Answer site. Sites"
     "vary in their selection mechanisms, e.g. drawing on community opinion and/or the view"
     "of the Question author.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.CreativeWork import CreativeWork
    from pydantic_schemaorg.Comment import Comment
    from pydantic_schemaorg.Integer import Integer
    from pydantic_schemaorg.Answer import Answer
    from pydantic_schemaorg.ItemList import ItemList
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
