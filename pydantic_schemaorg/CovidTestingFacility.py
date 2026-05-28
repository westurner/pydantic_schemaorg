from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.MedicalClinic import MedicalClinic


class CovidTestingFacility(MedicalClinic):
    """A CovidTestingFacility is a [[MedicalClinic]] where testing for the COVID-19 Coronavirus"
     "disease is available. If the facility is being made available from an established [[Pharmacy]],"
     "[[Hotel]], or other non-medical organization, multiple types can be listed. This makes"
     "it easier to re-use existing schema.org information about that place, e.g. contact"
     "info, address, opening hours. Note that in an emergency, such information may not always"
     "be reliable.

    See: https://schema.org/CovidTestingFacility
    Model depth: 5
    """
    valid_name: ClassVar[str] = "CovidTestingFacility"
    type_: str = Field("CovidTestingFacility", alias='@type')
    



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
