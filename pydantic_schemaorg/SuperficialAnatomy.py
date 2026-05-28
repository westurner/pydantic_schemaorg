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


class SuperficialAnatomy(MedicalEntity):
    """Anatomical features that can be observed by sight (without dissection), including"
     "the form and proportions of the human body as well as surface landmarks that correspond"
     "to deeper subcutaneous structures. Superficial anatomy plays an important role in"
     "sports medicine, phlebotomy, and other medical specialties as underlying anatomical"
     "structures can be identified through surface palpation. For example, during back surgery,"
     "superficial anatomy can be used to palpate and count vertebrae to find the site of incision."
     "Or in phlebotomy, superficial anatomy can be used to locate an underlying vein; for example,"
     "the median cubital vein can be located by palpating the borders of the cubital fossa (such"
     "as the epicondyles of the humerus) and then looking for the superficial signs of the vein,"
     "such as size, prominence, ability to refill after depression, and feel of surrounding"
     "tissue support. As another example, in a subluxation (dislocation) of the glenohumeral"
     "joint, the bony structure becomes pronounced with the deltoid muscle failing to cover"
     "the glenohumeral joint allowing the edges of the scapula to be superficially visible."
     "Here, the superficial anatomy is the visible edges of the scapula, implying the underlying"
     "dislocation of the joint (the related anatomical structure).

    See: https://schema.org/SuperficialAnatomy
    Model depth: 3
    """
    valid_name: ClassVar[str] = "SuperficialAnatomy"
    type_: str = Field("SuperficialAnatomy", alias='@type')
    relatedAnatomy: Optional[Union[List[Union['AnatomicalSystem', 'AnatomicalStructure', str]], 'AnatomicalSystem', 'AnatomicalStructure', str]] = Field(
        default=None,
        description="Anatomical systems or structures that relate to the superficial anatomy.",
    )
    associatedPathophysiology: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="If applicable, a description of the pathophysiology associated with the anatomical"
     "system, including potential abnormal changes in the mechanical, physical, and biochemical"
     "functions of the system.",
    )
    relatedTherapy: Optional[Union[List[Union['MedicalTherapy', str]], 'MedicalTherapy', str]] = Field(
        default=None,
        description="A medical therapy related to this anatomy.",
    )
    relatedCondition: Optional[Union[List[Union['MedicalCondition', str]], 'MedicalCondition', str]] = Field(
        default=None,
        description="A medical condition associated with this anatomy.",
    )
    significance: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The significance associated with the superficial anatomy; as an example, how characteristics"
     "of the superficial anatomy can suggest underlying medical conditions or courses of"
     "treatment.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.AnatomicalSystem import AnatomicalSystem
    from pydantic_schemaorg.AnatomicalStructure import AnatomicalStructure
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.MedicalTherapy import MedicalTherapy
    from pydantic_schemaorg.MedicalCondition import MedicalCondition


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
