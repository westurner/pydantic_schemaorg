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
from pydantic_schemaorg.AnatomicalStructure import AnatomicalStructure


class Nerve(AnatomicalStructure):
    """A common pathway for the electrochemical nerve impulses that are transmitted along"
     "each of the axons.

    See: https://schema.org/Nerve
    Model depth: 4
    """
    valid_name: ClassVar[str] = "Nerve"
    type_: str = Field("Nerve", alias='@type')
    nerveMotor: Optional[Union[List[Union['Muscle', str]], 'Muscle', str]] = Field(
        default=None,
        description="The neurological pathway extension that involves muscle control.",
    )
    sourcedFrom: Optional[Union[List[Union['BrainStructure', str]], 'BrainStructure', str]] = Field(
        default=None,
        description="The neurological pathway that originates the neurons.",
    )
    sensoryUnit: Optional[Union[List[Union['SuperficialAnatomy', 'AnatomicalStructure', str]], 'SuperficialAnatomy', 'AnatomicalStructure', str]] = Field(
        default=None,
        description="The neurological pathway extension that inputs and sends information to the brain or"
     "spinal cord.",
    )
    branch: Optional[Union[List[Union['AnatomicalStructure', str]], 'AnatomicalStructure', str]] = Field(
        default=None,
        description="The branches that delineate from the nerve bundle. Not to be confused with [[branchOf]].",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Muscle import Muscle
    from pydantic_schemaorg.BrainStructure import BrainStructure
    from pydantic_schemaorg.SuperficialAnatomy import SuperficialAnatomy
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
