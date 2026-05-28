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
from pydantic_schemaorg.CategoryCode import CategoryCode
from pydantic_schemaorg.MedicalIntangible import MedicalIntangible


class MedicalCode(CategoryCode, MedicalIntangible):
    """A code for a medical entity.

    See: https://schema.org/MedicalCode
    Model depth: 4
    """
    valid_name: ClassVar[str] = "MedicalCode"
    type_: str = Field("MedicalCode", alias='@type')
    codingSystem: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The coding system, e.g. 'ICD-10'.",
    )
    codeValue: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="A short textual code that uniquely identifies the value.",
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
