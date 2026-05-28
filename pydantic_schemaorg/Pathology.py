from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class Pathology(MedicalSpecialty):
    """A specific branch of medical science that is concerned with the study of the cause, origin"
     "and nature of a disease state, including its consequences as a result of manifestation"
     "of the disease. In clinical care, the term is used to designate a branch of medicine using"
     "laboratory tests to diagnose and determine the prognostic significance of illness.

    See: https://schema.org/Pathology
    Model depth: 6
    """
    valid_name: ClassVar[str] = "Pathology"
    type_: str = Field("Pathology", alias='@type')
    



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
