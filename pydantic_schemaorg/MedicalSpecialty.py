from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.Specialty import Specialty
from pydantic_schemaorg.MedicalEnumeration import MedicalEnumeration


class MedicalSpecialty(Specialty, MedicalEnumeration):
    """Any specific branch of medical science or practice. Medical specialities include clinical"
     "specialties that pertain to particular organ systems and their respective disease"
     "states, as well as allied health specialties. Enumerated type.

    See: https://schema.org/MedicalSpecialty
    Model depth: 5
    """
    valid_name: ClassVar[str] = "MedicalSpecialty"
    type_: str = Field("MedicalSpecialty", alias='@type')
    



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
