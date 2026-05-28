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


class SearchAction(Action):
    """The act of searching for an object. Related actions: * [[FindAction]]: SearchAction"
     "generally leads to a FindAction, but not necessarily.

    See: https://schema.org/SearchAction
    Model depth: 3
    """
    valid_name: ClassVar[str] = "SearchAction"
    type_: str = Field("SearchAction", alias='@type')
    query: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="A sub property of instrument. The query used on this action.",
    )
    


if TYPE_CHECKING:
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
