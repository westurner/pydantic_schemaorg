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
from pydantic_schemaorg.MedicalTest import MedicalTest


class MedicalTestPanel(MedicalTest):
    """Any collection of tests commonly ordered together.

    See: https://schema.org/MedicalTestPanel
    Model depth: 4
    """
    valid_name: ClassVar[str] = "MedicalTestPanel"
    type_: str = Field("MedicalTestPanel", alias='@type')
    subTest: Optional[Union[List[Union['MedicalTest', str]], 'MedicalTest', str]] = Field(
        default=None,
        description="A component test of the panel.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.MedicalTest import MedicalTest


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
