from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class SeeDoctorHealthAspect(HealthAspectEnumeration):
    """Information about questions that may be asked, when to see a professional, measures"
     "before seeing a doctor or content about the first consultation.

    See: https://schema.org/SeeDoctorHealthAspect
    Model depth: 5
    """
    valid_name: ClassVar[str] = "SeeDoctorHealthAspect"
    type_: str = Field("SeeDoctorHealthAspect", alias='@type')
    



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
