from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class Quantity(Intangible):
    """Quantities such as distance, time, mass, weight, etc. Particular instances of say Mass"
     "are entities like '3 kg' or '4 milligrams'.

    See: https://schema.org/Quantity
    Model depth: 3
    """
    valid_name: ClassVar[str] = "Quantity"
    type_: str = Field("Quantity", alias='@type')
    



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
