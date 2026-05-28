from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.MedicalObservationalStudyDesign import MedicalObservationalStudyDesign


class Longitudinal(MedicalObservationalStudyDesign):
    """Unlike cross-sectional studies, longitudinal studies track the same people, and therefore"
     "the differences observed in those people are less likely to be the result of cultural"
     "differences across generations. Longitudinal studies are also used in medicine to"
     "uncover predictors of certain diseases.

    See: https://schema.org/Longitudinal
    Model depth: 6
    """
    valid_name: ClassVar[str] = "Longitudinal"
    type_: str = Field("Longitudinal", alias='@type')
    



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
