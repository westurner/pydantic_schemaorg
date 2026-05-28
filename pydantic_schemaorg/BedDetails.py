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
from pydantic_schemaorg.Intangible import Intangible


class BedDetails(Intangible):
    """An entity holding detailed information about the available bed types, e.g. the quantity"
     "of twin beds for a hotel room. For the single case of just one bed of a certain type, you can"
     "use bed directly with a text. See also [[BedType]] (under development).

    See: https://schema.org/BedDetails
    Model depth: 3
    """
    valid_name: ClassVar[str] = "BedDetails"
    type_: str = Field("BedDetails", alias='@type')
    typeOfBed: Optional[Union[List[Union[str, 'Text', 'BedType']], str, 'Text', 'BedType']] = Field(
        default=None,
        description="The type of bed to which the BedDetail refers, i.e. the type of bed available in the quantity"
     "indicated by quantity.",
    )
    numberOfBeds: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', str]], StrictInt, StrictFloat, 'Number', str]] = Field(
        default=None,
        description="The quantity of the given bed type available in the HotelRoom, Suite, House, or Apartment.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.BedType import BedType
    from pydantic_schemaorg.Number import Number


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
