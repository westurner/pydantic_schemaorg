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
from pydantic_schemaorg.Action import Action


class UpdateAction(Action):
    """The act of managing by changing/editing the state of the object.

    See: https://schema.org/UpdateAction
    Model depth: 3
    """
    valid_name: ClassVar[str] = "UpdateAction"
    type_: str = Field("UpdateAction", alias='@type')
    collection: Optional[Union[List[Union['Thing', str]], 'Thing', str]] = Field(
        default=None,
        description="A sub property of object. The collection target of the action.",
    )
    targetCollection: Optional[Union[List[Union['Thing', str]], 'Thing', str]] = Field(
        default=None,
        description="A sub property of object. The collection target of the action.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Thing import Thing


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
