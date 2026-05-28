from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty
from pydantic_schemaorg.MedicalBusiness import MedicalBusiness


class PrimaryCare(MedicalSpecialty, MedicalBusiness):
    """The medical care by a physician, or other health-care professional, who is the patient's"
     "first contact with the health-care system and who may recommend a specialist if necessary.

    See: https://schema.org/PrimaryCare
    Model depth: 5
    """
    valid_name: ClassVar[str] = "PrimaryCare"
    type_: str = Field("PrimaryCare", alias='@type')
    



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
