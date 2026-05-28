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
from pydantic_schemaorg.MedicalEntity import MedicalEntity


class AnatomicalStructure(MedicalEntity):
    """Any part of the human body, typically a component of an anatomical system. Organs, tissues,"
     "and cells are all anatomical structures.

    See: https://schema.org/AnatomicalStructure
    Model depth: 3
    """
    valid_name: ClassVar[str] = "AnatomicalStructure"
    type_: str = Field("AnatomicalStructure", alias='@type')
    subStructure: Optional[Union[List[Union['AnatomicalStructure', str]], 'AnatomicalStructure', str]] = Field(
        default=None,
        description="Component (sub-)structure(s) that comprise this anatomical structure.",
    )
    associatedPathophysiology: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="If applicable, a description of the pathophysiology associated with the anatomical"
     "system, including potential abnormal changes in the mechanical, physical, and biochemical"
     "functions of the system.",
    )
    diagram: Optional[Union[List[Union['ImageObject', str]], 'ImageObject', str]] = Field(
        default=None,
        description="An image containing a diagram that illustrates the structure and/or its component substructures"
     "and/or connections with other structures.",
    )
    relatedTherapy: Optional[Union[List[Union['MedicalTherapy', str]], 'MedicalTherapy', str]] = Field(
        default=None,
        description="A medical therapy related to this anatomy.",
    )
    relatedCondition: Optional[Union[List[Union['MedicalCondition', str]], 'MedicalCondition', str]] = Field(
        default=None,
        description="A medical condition associated with this anatomy.",
    )
    connectedTo: Optional[Union[List[Union['AnatomicalStructure', str]], 'AnatomicalStructure', str]] = Field(
        default=None,
        description="Other anatomical structures to which this structure is connected.",
    )
    partOfSystem: Optional[Union[List[Union['AnatomicalSystem', str]], 'AnatomicalSystem', str]] = Field(
        default=None,
        description="The anatomical or organ system that this structure is part of.",
    )
    bodyLocation: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Location in the body of the anatomical structure.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.ImageObject import ImageObject
    from pydantic_schemaorg.MedicalTherapy import MedicalTherapy
    from pydantic_schemaorg.MedicalCondition import MedicalCondition
    from pydantic_schemaorg.AnatomicalSystem import AnatomicalSystem


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
