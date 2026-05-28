from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.MedicalIndication import MedicalIndication


class PreventionIndication(MedicalIndication):
    """An indication for preventing an underlying condition, symptom, etc.

    See: https://schema.org/PreventionIndication
    Model depth: 4
    """
    valid_name: ClassVar[str] = "PreventionIndication"
    type_: str = Field("PreventionIndication", alias='@type')
    



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
