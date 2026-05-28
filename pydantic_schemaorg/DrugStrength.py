from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from typing import List, Optional, Union
from pydantic import StrictInt, StrictFloat


from pydantic import Field
from pydantic_schemaorg.MedicalIntangible import MedicalIntangible


class DrugStrength(MedicalIntangible):
    """A specific strength in which a medical drug is available in a specific country.

    See: https://schema.org/DrugStrength
    Model depth: 4
    """
    valid_name: ClassVar[str] = "DrugStrength"
    type_: str = Field("DrugStrength", alias='@type')
    activeIngredient: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="An active ingredient, typically chemical compounds and/or biologic substances.",
    )
    strengthUnit: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The units of an active ingredient's strength, e.g. mg.",
    )
    maximumIntake: Optional[Union[List[Union['MaximumDoseSchedule', str]], 'MaximumDoseSchedule', str]] = Field(
        default=None,
        description="Recommended intake of this supplement for a given population as defined by a specific"
     "recommending authority.",
    )
    strengthValue: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', str]], StrictInt, StrictFloat, 'Number', str]] = Field(
        default=None,
        description="The value of an active ingredient's strength, e.g. 325.",
    )
    availableIn: Optional[Union[List[Union['AdministrativeArea', str]], 'AdministrativeArea', str]] = Field(
        default=None,
        description="The location in which the strength is available.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.MaximumDoseSchedule import MaximumDoseSchedule
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.AdministrativeArea import AdministrativeArea


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
