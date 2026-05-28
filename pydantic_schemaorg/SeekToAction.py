from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from pydantic import StrictInt, StrictFloat
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.Action import Action


class SeekToAction(Action):
    """This is the [[Action]] of navigating to a specific [[startOffset]] timestamp within"
     "a [[VideoObject]], typically represented with a URL template structure.

    See: https://schema.org/SeekToAction
    Model depth: 3
    """
    valid_name: ClassVar[str] = "SeekToAction"
    type_: str = Field("SeekToAction", alias='@type')
    startOffset: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', 'HyperTocEntry', str]], StrictInt, StrictFloat, 'Number', 'HyperTocEntry', str]] = Field(
        default=None,
        description="The start time of the clip expressed as the number of seconds from the beginning of the"
     "work.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.HyperTocEntry import HyperTocEntry


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
