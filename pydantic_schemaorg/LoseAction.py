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
from pydantic_schemaorg.AchieveAction import AchieveAction


class LoseAction(AchieveAction):
    """The act of being defeated in a competitive activity.

    See: https://schema.org/LoseAction
    Model depth: 4
    """
    valid_name: ClassVar[str] = "LoseAction"
    type_: str = Field("LoseAction", alias='@type')
    winner: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="A sub property of participant. The winner of the action.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Person import Person


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
