from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty
from pydantic_schemaorg.MedicalBusiness import MedicalBusiness


class Midwifery(MedicalSpecialty, MedicalBusiness):
    """A nurse-like health profession that deals with pregnancy, childbirth, and the postpartum"
     "period (including care of the newborn), besides sexual and reproductive health of women"
     "throughout their lives.

    See: https://schema.org/Midwifery
    Model depth: 5
    """
    valid_name: ClassVar[str] = "Midwifery"
    type_: str = Field("Midwifery", alias='@type')
    



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
