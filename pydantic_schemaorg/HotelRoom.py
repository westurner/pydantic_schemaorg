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
from pydantic_schemaorg.Room import Room


class HotelRoom(Room):
    """A hotel room is a single room in a hotel. <br /><br /> See also the <a href=\"/docs/hotels.html\">dedicated"
     "document on the use of schema.org for marking up hotels and other forms of accommodations</a>.

    See: https://schema.org/HotelRoom
    Model depth: 5
    """
    valid_name: ClassVar[str] = "HotelRoom"
    type_: str = Field("HotelRoom", alias='@type')
    occupancy: Optional[Union[List[Union['QuantitativeValue', str]], 'QuantitativeValue', str]] = Field(
        default=None,
        description="The allowed total occupancy for the accommodation in persons (including infants etc)."
     "For individual accommodations, this is not necessarily the legal maximum but defines"
     "the permitted usage as per the contractual agreement (e.g. a double room used by a single"
     "person). Typical unit code(s): C62 for person.",
    )
    bed: Optional[Union[List[Union[str, 'Text', 'BedType', 'BedDetails']], str, 'Text', 'BedType', 'BedDetails']] = Field(
        default=None,
        description="The type of bed or beds included in the accommodation. For the single case of just one bed"
     "of a certain type, you use bed directly with a text. If you want to indicate the quantity"
     "of a certain kind of bed, use an instance of BedDetails. For more detailed information,"
     "use the amenityFeature property.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.BedType import BedType
    from pydantic_schemaorg.BedDetails import BedDetails


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
