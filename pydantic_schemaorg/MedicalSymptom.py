from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.MedicalSignOrSymptom import MedicalSignOrSymptom


class MedicalSymptom(MedicalSignOrSymptom):
    """Any complaint sensed and expressed by the patient (therefore defined as subjective)"
     "like stomachache, lower-back pain, or fatigue.

    See: https://schema.org/MedicalSymptom
    Model depth: 5
    """
    valid_name: ClassVar[str] = "MedicalSymptom"
    type_: str = Field("MedicalSymptom", alias='@type')
    



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
