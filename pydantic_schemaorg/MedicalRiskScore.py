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
from pydantic_schemaorg.MedicalRiskEstimator import MedicalRiskEstimator


class MedicalRiskScore(MedicalRiskEstimator):
    """A simple system that adds up the number of risk factors to yield a score that is associated"
     "with prognosis, e.g. CHAD score, TIMI risk score.

    See: https://schema.org/MedicalRiskScore
    Model depth: 4
    """
    valid_name: ClassVar[str] = "MedicalRiskScore"
    type_: str = Field("MedicalRiskScore", alias='@type')
    algorithm: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The algorithm or rules to follow to compute the score.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text


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
