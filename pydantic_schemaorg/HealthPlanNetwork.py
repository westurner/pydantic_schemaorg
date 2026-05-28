from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from typing import List, Optional, Union
from pydantic import StrictBool


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class HealthPlanNetwork(Intangible):
    """A US-style health insurance plan network.

    See: https://schema.org/HealthPlanNetwork
    Model depth: 3
    """
    valid_name: ClassVar[str] = "HealthPlanNetwork"
    type_: str = Field("HealthPlanNetwork", alias='@type')
    healthPlanNetworkId: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Name or unique ID of network. (Networks are often reused across different insurance"
     "plans.)",
    )
    healthPlanCostSharing: Optional[Union[List[Union[StrictBool, 'Boolean', str]], StrictBool, 'Boolean', str]] = Field(
        default=None,
        description="The costs to the patient for services under this network or formulary.",
    )
    healthPlanNetworkTier: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The tier(s) for this network.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Boolean import Boolean


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
