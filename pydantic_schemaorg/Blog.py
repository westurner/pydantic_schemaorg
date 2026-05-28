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


class Blog(CreativeWork):
    """A [blog](https://en.wikipedia.org/wiki/Blog), sometimes known as a \"weblog\"."
     "Note that the individual posts ([[BlogPosting]]s) in a [[Blog]] are often colloquially"
     "referred to by the same term.

    See: https://schema.org/Blog
    Model depth: 3
    """
    valid_name: ClassVar[str] = "Blog"
    type_: str = Field("Blog", alias='@type')
    blogPost: Optional[Union[List[Union['BlogPosting', str]], 'BlogPosting', str]] = Field(
        default=None,
        description="A posting that is part of this blog.",
    )
    blogPosts: Optional[Union[List[Union['BlogPosting', str]], 'BlogPosting', str]] = Field(
        default=None,
        description="Indicates a post that is part of a [[Blog]]. Note that historically, what we term a \"Blog\""
     "was once known as a \"weblog\", and that what we term a \"BlogPosting\" is now often colloquially"
     "referred to as a \"blog\".",
    )
    issn: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The International Standard Serial Number (ISSN) that identifies this serial publication."
     "You can repeat this property to identify different formats of, or the linking ISSN (ISSN-L)"
     "for, this serial publication.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.BlogPosting import BlogPosting
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
