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


class LymphaticVessel(Vessel):
    """A type of blood vessel that specifically carries lymph fluid unidirectionally toward"
     "the heart.

    See: https://schema.org/LymphaticVessel
    Model depth: 5
    """
    valid_name: ClassVar[str] = "LymphaticVessel"
    type_: str = Field("LymphaticVessel", alias='@type')
    originatesFrom: Optional[Union[List[Union['Vessel', str]], 'Vessel', str]] = Field(
        default=None,
        description="The vasculature the lymphatic structure originates, or afferents, from.",
    )
    regionDrained: Optional[Union[List[Union['AnatomicalSystem', 'AnatomicalStructure', str]], 'AnatomicalSystem', 'AnatomicalStructure', str]] = Field(
        default=None,
        description="The anatomical or organ system drained by this vessel; generally refers to a specific"
     "part of an organ.",
    )
    runsTo: Optional[Union[List[Union['Vessel', str]], 'Vessel', str]] = Field(
        default=None,
        description="The vasculature the lymphatic structure runs, or efferents, to.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Vessel import Vessel
    from pydantic_schemaorg.AnatomicalSystem import AnatomicalSystem
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
