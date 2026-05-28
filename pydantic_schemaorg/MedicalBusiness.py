from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class MedicalBusiness(LocalBusiness):
    """A particular physical or virtual business of an organization for medical purposes."
     "Examples of MedicalBusiness include different businesses run by health professionals.

    See: https://schema.org/MedicalBusiness
    Model depth: 4
    """
    valid_name: ClassVar[str] = "MedicalBusiness"
    type_: str = Field("MedicalBusiness", alias='@type')
    



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
