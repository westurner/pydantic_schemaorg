from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.MedicalIndication import MedicalIndication


class ApprovedIndication(MedicalIndication):
    """An indication for a medical therapy that has been formally specified or approved by a"
     "regulatory body that regulates use of the therapy; for example, the US FDA approves indications"
     "for most drugs in the US.

    See: https://schema.org/ApprovedIndication
    Model depth: 4
    """
    valid_name: ClassVar[str] = "ApprovedIndication"
    type_: str = Field("ApprovedIndication", alias='@type')
    



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
