from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from datetime import date, datetime
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class Message(CreativeWork):
    """A single message from a sender to one or more organizations or people.

    See: https://schema.org/Message
    Model depth: 3
    """
    valid_name: ClassVar[str] = "Message"
    type_: str = Field("Message", alias='@type')
    dateReceived: Optional[Union[List[Union[datetime, 'DateTime', str]], datetime, 'DateTime', str]] = Field(
        default=None,
        description="The date/time the message was received if a single recipient exists.",
    )
    toRecipient: Optional[Union[List[Union['Audience', 'Person', 'ContactPoint', 'Organization', str]], 'Audience', 'Person', 'ContactPoint', 'Organization', str]] = Field(
        default=None,
        description="A sub property of recipient. The recipient who was directly sent the message.",
    )
    sender: Optional[Union[List[Union['Audience', 'Person', 'Organization', str]], 'Audience', 'Person', 'Organization', str]] = Field(
        default=None,
        description="A sub property of participant. The participant who is at the sending end of the action.",
    )
    bccRecipient: Optional[Union[List[Union['Person', 'ContactPoint', 'Organization', str]], 'Person', 'ContactPoint', 'Organization', str]] = Field(
        default=None,
        description="A sub property of recipient. The recipient blind copied on a message.",
    )
    ccRecipient: Optional[Union[List[Union['Person', 'ContactPoint', 'Organization', str]], 'Person', 'ContactPoint', 'Organization', str]] = Field(
        default=None,
        description="A sub property of recipient. The recipient copied on a message.",
    )
    dateSent: Optional[Union[List[Union[datetime, 'DateTime', str]], datetime, 'DateTime', str]] = Field(
        default=None,
        description="The date/time at which the message was sent.",
    )
    dateRead: Optional[Union[List[Union[datetime, 'DateTime', date, 'Date', str]], datetime, 'DateTime', date, 'Date', str]] = Field(
        default=None,
        description="The date/time at which the message has been read by the recipient if a single recipient"
     "exists.",
    )
    recipient: Optional[Union[List[Union['Audience', 'Person', 'ContactPoint', 'Organization', str]], 'Audience', 'Person', 'ContactPoint', 'Organization', str]] = Field(
        default=None,
        description="A sub property of participant. The participant who is at the receiving end of the action.",
    )
    messageAttachment: Optional[Union[List[Union['CreativeWork', str]], 'CreativeWork', str]] = Field(
        default=None,
        description="A CreativeWork attached to the message.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Audience import Audience
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.ContactPoint import ContactPoint
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.Date import Date
    from pydantic_schemaorg.CreativeWork import CreativeWork


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
