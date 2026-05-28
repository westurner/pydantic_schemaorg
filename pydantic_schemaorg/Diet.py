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
from pydantic_schemaorg.LifestyleModification import LifestyleModification
from pydantic_schemaorg.CreativeWork import CreativeWork


class Diet(LifestyleModification, CreativeWork):
    """A strategy of regulating the intake of food to achieve or maintain a specific health-related"
     "goal.

    See: https://schema.org/Diet
    Model depth: 3
    """
    valid_name: ClassVar[str] = "Diet"
    type_: str = Field("Diet", alias='@type')
    expertConsiderations: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Medical expert advice related to the plan.",
    )
    dietFeatures: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Nutritional information specific to the dietary plan. May include dietary recommendations"
     "on what foods to avoid, what foods to consume, and specific alterations/deviations"
     "from the USDA or other regulatory body's approved dietary guidelines.",
    )
    physiologicalBenefits: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Specific physiologic benefits associated to the plan.",
    )
    endorsers: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="People or organizations that endorse the plan.",
    )
    risks: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Specific physiologic risks associated to the diet plan.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Organization import Organization


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
