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
from pydantic_schemaorg.CreativeWork import CreativeWork


class MathSolver(CreativeWork):
    """A math solver which is capable of solving a subset of mathematical problems.

    See: https://schema.org/MathSolver
    Model depth: 3
    """
    valid_name: ClassVar[str] = "MathSolver"
    type_: str = Field("MathSolver", alias='@type')
    mathExpression: Optional[Union[List[Union[str, 'Text', 'SolveMathAction']], str, 'Text', 'SolveMathAction']] = Field(
        default=None,
        description="A mathematical expression (e.g. 'x^2-3x=0') that may be solved for a specific variable,"
     "simplified, or transformed. This can take many formats, e.g. LaTeX, Ascii-Math, or"
     "math as you would write with a keyboard.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.SolveMathAction import SolveMathAction


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
