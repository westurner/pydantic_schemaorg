from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from datetime import datetime
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.BlogPosting import BlogPosting


class LiveBlogPosting(BlogPosting):
    """A [[LiveBlogPosting]] is a [[BlogPosting]] intended to provide a rolling textual coverage"
     "of an ongoing event through continuous updates.

    See: https://schema.org/LiveBlogPosting
    Model depth: 6
    """
    valid_name: ClassVar[str] = "LiveBlogPosting"
    type_: str = Field("LiveBlogPosting", alias='@type')
    coverageEndTime: Optional[Union[List[Union[datetime, 'DateTime', str]], datetime, 'DateTime', str]] = Field(
        default=None,
        description="The time when the live blog will stop covering the Event. Note that coverage may continue"
     "after the Event concludes.",
    )
    liveBlogUpdate: Optional[Union[List[Union['BlogPosting', str]], 'BlogPosting', str]] = Field(
        default=None,
        description="An update to the LiveBlog.",
    )
    coverageStartTime: Optional[Union[List[Union[datetime, 'DateTime', str]], datetime, 'DateTime', str]] = Field(
        default=None,
        description="The time when the live blog will begin covering the Event. Note that coverage may begin"
     "before the Event's start time. The LiveBlogPosting may also be created before coverage"
     "begins.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.BlogPosting import BlogPosting


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
