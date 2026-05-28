from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from typing import List, Optional, Union
from datetime import date, datetime
from pydantic import AnyUrl


from pydantic import Field
from pydantic_schemaorg.UserInteraction import UserInteraction


class UserComments(UserInteraction):
    """UserInteraction and its subtypes is an old way of talking about users interacting with"
     "pages. It is generally better to use [[Action]]-based vocabulary, alongside types"
     "such as [[Comment]].

    See: https://schema.org/UserComments
    Model depth: 4
    """
    valid_name: ClassVar[str] = "UserComments"
    type_: str = Field("UserComments", alias='@type')
    discusses: Optional[Union[List[Union['CreativeWork', str]], 'CreativeWork', str]] = Field(
        default=None,
        description="Specifies the CreativeWork associated with the UserComment.",
    )
    creator: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="The creator/author of this CreativeWork. This is the same as the Author property for"
     "CreativeWork.",
    )
    commentTime: Optional[Union[List[Union[datetime, 'DateTime', date, 'Date', str]], datetime, 'DateTime', date, 'Date', str]] = Field(
        default=None,
        description="The time at which the UserComment was made.",
    )
    commentText: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The text of the UserComment.",
    )
    replyToUrl: Optional[Union[List[Union[AnyUrl, 'URL', str]], AnyUrl, 'URL', str]] = Field(
        default=None,
        description="The URL at which a reply may be posted to the specified UserComment.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.CreativeWork import CreativeWork
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Date import Date
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.URL import URL


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
