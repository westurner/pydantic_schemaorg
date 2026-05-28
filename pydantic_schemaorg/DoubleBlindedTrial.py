from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.MedicalTrialDesign import MedicalTrialDesign


class DoubleBlindedTrial(MedicalTrialDesign):
    """A trial design in which neither the researcher nor the patient knows the details of the"
     "treatment the patient was randomly assigned to.

    See: https://schema.org/DoubleBlindedTrial
    Model depth: 6
    """
    valid_name: ClassVar[str] = "DoubleBlindedTrial"
    type_: str = Field("DoubleBlindedTrial", alias='@type')
    



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
