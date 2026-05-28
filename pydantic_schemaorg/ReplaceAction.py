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
from pydantic_schemaorg.UpdateAction import UpdateAction


class ReplaceAction(UpdateAction):
    """The act of editing a recipient by replacing an old object with a new object.

    See: https://schema.org/ReplaceAction
    Model depth: 4
    """
    valid_name: ClassVar[str] = "ReplaceAction"
    type_: str = Field("ReplaceAction", alias='@type')
    replacee: Optional[Union[List[Union['Thing', str]], 'Thing', str]] = Field(
        default=None,
        description="A sub property of object. The object that is being replaced.",
    )
    replacer: Optional[Union[List[Union['Thing', str]], 'Thing', str]] = Field(
        default=None,
        description="A sub property of object. The object that replaces.",
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
