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
from pydantic_schemaorg.TransferAction import TransferAction


class GiveAction(TransferAction):
    """The act of transferring ownership of an object to a destination. Reciprocal of TakeAction."
     "Related actions: * [[TakeAction]]: Reciprocal of GiveAction. * [[SendAction]]: Unlike"
     "SendAction, GiveAction implies that ownership is being transferred (e.g. I may send"
     "my laptop to you, but that doesn't mean I'm giving it to you).

    See: https://schema.org/GiveAction
    Model depth: 4
    """
    valid_name: ClassVar[str] = "GiveAction"
    type_: str = Field("GiveAction", alias='@type')
    recipient: Optional[Union[List[Union['Audience', 'Person', 'ContactPoint', 'Organization', str]], 'Audience', 'Person', 'ContactPoint', 'Organization', str]] = Field(
        default=None,
        description="A sub property of participant. The participant who is at the receiving end of the action.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Audience import Audience
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.ContactPoint import ContactPoint
    from pydantic_schemaorg.Organization import Organization


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
