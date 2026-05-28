from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty
from pydantic_schemaorg.MedicalBusiness import MedicalBusiness


class PublicHealth(MedicalSpecialty, MedicalBusiness):
    """Branch of medicine that pertains to the health services to improve and protect community"
     "health, especially epidemiology, sanitation, immunization, and preventive medicine.

    See: https://schema.org/PublicHealth
    Model depth: 5
    """
    valid_name: ClassVar[str] = "PublicHealth"
    type_: str = Field("PublicHealth", alias='@type')
    



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
