from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.MedicalSpecialty import MedicalSpecialty


class SpeechPathology(MedicalSpecialty):
    """The scientific study and treatment of defects, disorders, and malfunctions of speech"
     "and voice, as stuttering, lisping, or lalling, and of language disturbances, as aphasia"
     "or delayed language acquisition.

    See: https://schema.org/SpeechPathology
    Model depth: 6
    """
    valid_name: ClassVar[str] = "SpeechPathology"
    type_: str = Field("SpeechPathology", alias='@type')
    



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
