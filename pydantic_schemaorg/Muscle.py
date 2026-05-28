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


class Muscle(AnatomicalStructure):
    """A muscle is an anatomical structure consisting of a contractile form of tissue that animals"
     "use to effect movement.

    See: https://schema.org/Muscle
    Model depth: 4
    """
    valid_name: ClassVar[str] = "Muscle"
    type_: str = Field("Muscle", alias='@type')
    nerve: Optional[Union[List[Union['Nerve', str]], 'Nerve', str]] = Field(
        default=None,
        description="The underlying innervation associated with the muscle.",
    )
    antagonist: Optional[Union[List[Union['Muscle', str]], 'Muscle', str]] = Field(
        default=None,
        description="The muscle whose action counteracts the specified muscle.",
    )
    bloodSupply: Optional[Union[List[Union['Vessel', str]], 'Vessel', str]] = Field(
        default=None,
        description="The blood vessel that carries blood from the heart to the muscle.",
    )
    muscleAction: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The movement the muscle generates.",
    )
    insertion: Optional[Union[List[Union['AnatomicalStructure', str]], 'AnatomicalStructure', str]] = Field(
        default=None,
        description="The place of attachment of a muscle, or what the muscle moves.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Nerve import Nerve
    from pydantic_schemaorg.Vessel import Vessel
    from pydantic_schemaorg.Text import Text
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
