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


class Joint(AnatomicalStructure):
    """The anatomical location at which two or more bones make contact.

    See: https://schema.org/Joint
    Model depth: 4
    """
    valid_name: ClassVar[str] = "Joint"
    type_: str = Field("Joint", alias='@type')
    biomechnicalClass: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The biomechanical properties of the bone.",
    )
    structuralClass: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The name given to how bone physically connects to each other.",
    )
    functionalClass: Optional[Union[List[Union[str, 'Text', 'MedicalEntity']], str, 'Text', 'MedicalEntity']] = Field(
        default=None,
        description="The degree of mobility the joint allows.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.MedicalEntity import MedicalEntity


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
