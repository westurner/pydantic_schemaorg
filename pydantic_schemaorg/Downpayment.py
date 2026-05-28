from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.PriceComponentTypeEnumeration import PriceComponentTypeEnumeration


class Downpayment(PriceComponentTypeEnumeration):
    """Represents the downpayment (up-front payment) price component of the total price for"
     "an offered product that has additional installment payments.

    See: https://schema.org/Downpayment
    Model depth: 5
    """
    valid_name: ClassVar[str] = "Downpayment"
    type_: str = Field("Downpayment", alias='@type')
    



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
