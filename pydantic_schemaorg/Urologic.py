from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class Urologic(MedicalSpecialty):
    """A specific branch of medical science that is concerned with the diagnosis and treatment"
     "of diseases pertaining to the urinary tract and the urogenital system.

    See: https://schema.org/Urologic
    Model depth: 6
    """
    valid_name: ClassVar[str] = "Urologic"
    type_: str = Field("Urologic", alias='@type')
    



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
