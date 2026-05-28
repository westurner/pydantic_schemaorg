from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from pydantic import AnyUrl
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.LifestyleModification import LifestyleModification


class PhysicalActivity(LifestyleModification):
    """Any bodily activity that enhances or maintains physical fitness and overall health"
     "and wellness. Includes activity that is part of daily living and routine, structured"
     "exercise, and exercise prescribed as part of a medical treatment or recovery plan.

    See: https://schema.org/PhysicalActivity
    Model depth: 4
    """
    valid_name: ClassVar[str] = "PhysicalActivity"
    type_: str = Field("PhysicalActivity", alias='@type')
    category: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'Thing', 'PhysicalActivityCategory', 'CategoryCode']], AnyUrl, 'URL', str, 'Text', 'Thing', 'PhysicalActivityCategory', 'CategoryCode']] = Field(
        default=None,
        description="A category for the item. Greater signs or slashes can be used to informally indicate a"
     "category hierarchy.",
    )
    associatedAnatomy: Optional[Union[List[Union['SuperficialAnatomy', 'AnatomicalSystem', 'AnatomicalStructure', str]], 'SuperficialAnatomy', 'AnatomicalSystem', 'AnatomicalStructure', str]] = Field(
        default=None,
        description="The anatomy of the underlying organ system or structures associated with this entity.",
    )
    epidemiology: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The characteristics of associated patients, such as age, gender, race etc.",
    )
    pathophysiology: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Changes in the normal mechanical, physical, and biochemical functions that are associated"
     "with this activity or condition.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Thing import Thing
    from pydantic_schemaorg.PhysicalActivityCategory import PhysicalActivityCategory
    from pydantic_schemaorg.CategoryCode import CategoryCode
    from pydantic_schemaorg.SuperficialAnatomy import SuperficialAnatomy
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
