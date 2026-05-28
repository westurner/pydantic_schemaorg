from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.MedicalTherapy import MedicalTherapy


class OccupationalTherapy(MedicalTherapy):
    """A treatment of people with physical, emotional, or social problems, using purposeful"
     "activity to help them overcome or learn to deal with their problems.

    See: https://schema.org/OccupationalTherapy
    Model depth: 6
    """
    valid_name: ClassVar[str] = "OccupationalTherapy"
    type_: str = Field("OccupationalTherapy", alias='@type')
    



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
