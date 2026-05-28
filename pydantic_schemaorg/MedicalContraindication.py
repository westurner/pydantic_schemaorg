from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.MedicalEntity import MedicalEntity


class MedicalContraindication(MedicalEntity):
    """A condition or factor that serves as a reason to withhold a certain medical therapy. Contraindications"
     "can be absolute (there are no reasonable circumstances for undertaking a course of action)"
     "or relative (the patient is at higher risk of complications, but these risks may be outweighed"
     "by other considerations or mitigated by other measures).

    See: https://schema.org/MedicalContraindication
    Model depth: 3
    """
    valid_name: ClassVar[str] = "MedicalContraindication"
    type_: str = Field("MedicalContraindication", alias='@type')
    



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
