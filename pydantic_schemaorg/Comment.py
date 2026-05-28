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


class Comment(CreativeWork):
    """A comment on an item - for example, a comment on a blog post. The comment's content is expressed"
     "via the [[text]] property, and its topic via [[about]], properties shared with all CreativeWorks.

    See: https://schema.org/Comment
    Model depth: 3
    """
    valid_name: ClassVar[str] = "Comment"
    type_: str = Field("Comment", alias='@type')
    parentItem: Optional[Union[List[Union['CreativeWork', 'Comment', str]], 'CreativeWork', 'Comment', str]] = Field(
        default=None,
        description="The parent of a question, answer or item in general. Typically used for Q/A discussion"
     "threads e.g. a chain of comments with the first comment being an [[Article]] or other"
     "[[CreativeWork]]. See also [[comment]] which points from something to a comment about"
     "it.",
    )
    upvoteCount: Optional[Union[List[Union[int, 'Integer', str]], int, 'Integer', str]] = Field(
        default=None,
        description="The number of upvotes this question, answer or comment has received from the community.",
    )
    downvoteCount: Optional[Union[List[Union[int, 'Integer', str]], int, 'Integer', str]] = Field(
        default=None,
        description="The number of downvotes this question, answer or comment has received from the community.",
    )
    sharedContent: Optional[Union[List[Union['CreativeWork', str]], 'CreativeWork', str]] = Field(
        default=None,
        description="A CreativeWork such as an image, video, or audio clip shared as part of this posting.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.CreativeWork import CreativeWork
    from pydantic_schemaorg.Integer import Integer


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
