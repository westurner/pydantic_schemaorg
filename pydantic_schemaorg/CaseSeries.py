from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.MedicalObservationalStudyDesign import MedicalObservationalStudyDesign


class CaseSeries(MedicalObservationalStudyDesign):
    """A case series (also known as a clinical series) is a medical research study that tracks"
     "patients with a known exposure given similar treatment or examines their medical records"
     "for exposure and outcome. A case series can be retrospective or prospective and usually"
     "involves a smaller number of patients than the more powerful case-control studies or"
     "randomized controlled trials. Case series may be consecutive or non-consecutive,"
     "depending on whether all cases presenting to the reporting authors over a period of time"
     "were included, or only a selection.

    See: https://schema.org/CaseSeries
    Model depth: 6
    """
    valid_name: ClassVar[str] = "CaseSeries"
    type_: str = Field("CaseSeries", alias='@type')
    



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
