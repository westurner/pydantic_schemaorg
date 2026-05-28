from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.MedicalRiskEstimator import MedicalRiskEstimator


class MedicalRiskCalculator(MedicalRiskEstimator):
    """A complex mathematical calculation requiring an online calculator, used to assess"
     "prognosis. Note: use the url property of Thing to record any URLs for online calculators.

    See: https://schema.org/MedicalRiskCalculator
    Model depth: 4
    """
    valid_name: ClassVar[str] = "MedicalRiskCalculator"
    type_: str = Field("MedicalRiskCalculator", alias='@type')
    



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
