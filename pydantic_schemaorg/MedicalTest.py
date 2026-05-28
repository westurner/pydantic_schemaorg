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


class MedicalTest(MedicalEntity):
    """Any medical test, typically performed for diagnostic purposes.

    See: https://schema.org/MedicalTest
    Model depth: 3
    """
    valid_name: ClassVar[str] = "MedicalTest"
    type_: str = Field("MedicalTest", alias='@type')
    usedToDiagnose: Optional[Union[List[Union['MedicalCondition', str]], 'MedicalCondition', str]] = Field(
        default=None,
        description="A condition the test is used to diagnose.",
    )
    normalRange: Optional[Union[List[Union[str, 'Text', 'MedicalEnumeration']], str, 'Text', 'MedicalEnumeration']] = Field(
        default=None,
        description="Range of acceptable values for a typical patient, when applicable.",
    )
    affectedBy: Optional[Union[List[Union['Drug', str]], 'Drug', str]] = Field(
        default=None,
        description="Drugs that affect the test's results.",
    )
    signDetected: Optional[Union[List[Union['MedicalSign', str]], 'MedicalSign', str]] = Field(
        default=None,
        description="A sign detected by the test.",
    )
    usesDevice: Optional[Union[List[Union['MedicalDevice', str]], 'MedicalDevice', str]] = Field(
        default=None,
        description="Device used to perform the test.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.MedicalCondition import MedicalCondition
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration
    from pydantic_schemaorg.Drug import Drug
    from pydantic_schemaorg.MedicalSign import MedicalSign
    from pydantic_schemaorg.MedicalDevice import MedicalDevice


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
