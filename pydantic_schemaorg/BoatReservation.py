from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.Reservation import Reservation


class BoatReservation(Reservation):
    """A reservation for boat travel. Note: This type is for information about actual reservations,"
     "e.g. in confirmation emails or HTML pages with individual confirmations of reservations."
     "For offers of tickets, use [[Offer]].

    See: https://schema.org/BoatReservation
    Model depth: 4
    """
    valid_name: ClassVar[str] = "BoatReservation"
    type_: str = Field("BoatReservation", alias='@type')
    



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
