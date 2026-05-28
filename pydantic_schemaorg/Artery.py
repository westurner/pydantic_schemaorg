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
from pydantic_schemaorg.Vessel import Vessel


class Artery(Vessel):
    """A type of blood vessel that specifically carries blood away from the heart.

    See: https://schema.org/Artery
    Model depth: 5
    """
    valid_name: ClassVar[str] = "Artery"
    type_: str = Field("Artery", alias='@type')
    arterialBranch: Optional[Union[List[Union['AnatomicalStructure', str]], 'AnatomicalStructure', str]] = Field(
        default=None,
        description="The branches that comprise the arterial structure.",
    )
    supplyTo: Optional[Union[List[Union['AnatomicalStructure', str]], 'AnatomicalStructure', str]] = Field(
        default=None,
        description="The area to which the artery supplies blood.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.AnatomicalStructure import AnatomicalStructure


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
