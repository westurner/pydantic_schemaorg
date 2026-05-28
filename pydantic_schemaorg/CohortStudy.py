from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.MedicalObservationalStudyDesign import MedicalObservationalStudyDesign


class CohortStudy(MedicalObservationalStudyDesign):
    """Also known as a panel study. A cohort study is a form of longitudinal study used in medicine"
     "and social science. It is one type of study design and should be compared with a cross-sectional"
     "study. A cohort is a group of people who share a common characteristic or experience within"
     "a defined period (e.g., are born, leave school, lose their job, are exposed to a drug or"
     "a vaccine, etc.). The comparison group may be the general population from which the cohort"
     "is drawn, or it may be another cohort of persons thought to have had little or no exposure"
     "to the substance under investigation, but otherwise similar. Alternatively, subgroups"
     "within the cohort may be compared with each other.

    See: https://schema.org/CohortStudy
    Model depth: 6
    """
    valid_name: ClassVar[str] = "CohortStudy"
    type_: str = Field("CohortStudy", alias='@type')
    



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
