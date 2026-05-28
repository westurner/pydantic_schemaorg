from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.MedicineSystem import MedicineSystem


class Ayurvedic(MedicineSystem):
    """A system of medicine that originated in India over thousands of years and that focuses"
     "on integrating and balancing the body, mind, and spirit.

    See: https://schema.org/Ayurvedic
    Model depth: 6
    """
    valid_name: ClassVar[str] = "Ayurvedic"
    type_: str = Field("Ayurvedic", alias='@type')
    



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
