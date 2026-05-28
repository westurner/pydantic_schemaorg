from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.MedicalProcedureType import MedicalProcedureType


class PercutaneousProcedure(MedicalProcedureType):
    """A type of medical procedure that involves percutaneous techniques, where access to"
     "organs or tissue is achieved via needle-puncture of the skin. For example, catheter-based"
     "procedures like stent delivery.

    See: https://schema.org/PercutaneousProcedure
    Model depth: 6
    """
    valid_name: ClassVar[str] = "PercutaneousProcedure"
    type_: str = Field("PercutaneousProcedure", alias='@type')
    



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
