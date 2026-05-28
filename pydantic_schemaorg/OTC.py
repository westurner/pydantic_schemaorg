from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.DrugPrescriptionStatus import DrugPrescriptionStatus


class OTC(DrugPrescriptionStatus):
    """The character of a medical substance, typically a medicine, of being available over"
     "the counter or not.

    See: https://schema.org/OTC
    Model depth: 6
    """
    valid_name: ClassVar[str] = "OTC"
    type_: str = Field("OTC", alias='@type')
    



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
