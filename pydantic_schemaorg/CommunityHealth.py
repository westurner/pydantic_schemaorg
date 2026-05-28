from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty
from pydantic_schemaorg.MedicalBusiness import MedicalBusiness


class CommunityHealth(MedicalSpecialty, MedicalBusiness):
    """A field of public health focusing on improving health characteristics of a defined population"
     "in relation with their geographical or environment areas.

    See: https://schema.org/CommunityHealth
    Model depth: 5
    """
    valid_name: ClassVar[str] = "CommunityHealth"
    type_: str = Field("CommunityHealth", alias='@type')
    



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
