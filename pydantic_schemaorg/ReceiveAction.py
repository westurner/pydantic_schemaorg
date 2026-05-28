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


class ReceiveAction(TransferAction):
    """The act of physically/electronically taking delivery of an object that has been transferred"
     "from an origin to a destination. Reciprocal of SendAction. Related actions: * [[SendAction]]:"
     "The reciprocal of ReceiveAction. * [[TakeAction]]: Unlike TakeAction, ReceiveAction"
     "does not imply that the ownership has been transferred (e.g. I can receive a package,"
     "but it does not mean the package is now mine).

    See: https://schema.org/ReceiveAction
    Model depth: 4
    """
    valid_name: ClassVar[str] = "ReceiveAction"
    type_: str = Field("ReceiveAction", alias='@type')
    sender: Optional[Union[List[Union['Audience', 'Person', 'Organization', str]], 'Audience', 'Person', 'Organization', str]] = Field(
        default=None,
        description="A sub property of participant. The participant who is at the sending end of the action.",
    )
    deliveryMethod: Optional[Union[List[Union['DeliveryMethod', str]], 'DeliveryMethod', str]] = Field(
        default=None,
        description="A sub property of instrument. The method of delivery.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Audience import Audience
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.DeliveryMethod import DeliveryMethod


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
