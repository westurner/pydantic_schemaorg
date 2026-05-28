from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class MedicalEnumeration(Enumeration):
    """Enumerations related to health and the practice of medicine: A concept that is used to"
     "attribute a quality to another concept, as a qualifier, a collection of items or a listing"
     "of all of the elements of a set in medicine practice.

    See: https://schema.org/MedicalEnumeration
    Model depth: 4
    """
    valid_name: ClassVar[str] = "MedicalEnumeration"
    type_: str = Field("MedicalEnumeration", alias='@type')
    



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
