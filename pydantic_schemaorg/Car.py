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
from pydantic_schemaorg.Vehicle import Vehicle


class Car(Vehicle):
    """A car is a wheeled, self-powered motor vehicle used for transportation.

    See: https://schema.org/Car
    Model depth: 4
    """
    valid_name: ClassVar[str] = "Car"
    type_: str = Field("Car", alias='@type')
    roofLoad: Optional[Union[List[Union['QuantitativeValue', str]], 'QuantitativeValue', str]] = Field(
        default=None,
        description="The permitted total weight of cargo and installations (e.g. a roof rack) on top of the"
     "vehicle. Typical unit code(s): KGM for kilogram, LBR for pound * Note 1: You can indicate"
     "additional information in the [[name]] of the [[QuantitativeValue]] node. * Note 2:"
     "You may also link to a [[QualitativeValue]] node that provides additional information"
     "using [[valueReference]] * Note 3: Note that you can use [[minValue]] and [[maxValue]]"
     "to indicate ranges.",
    )
    acrissCode: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The ACRISS Car Classification Code is a code used by many car rental companies, for classifying"
     "vehicles. ACRISS stands for Association of Car Rental Industry Systems and Standards.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
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
