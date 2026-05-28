from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.DrugPregnancyCategory import DrugPregnancyCategory


class FDAcategoryD(DrugPregnancyCategory):
    """A designation by the US FDA signifying that there is positive evidence of human fetal"
     "risk based on adverse reaction data from investigational or marketing experience or"
     "studies in humans, but potential benefits may warrant use of the drug in pregnant women"
     "despite potential risks.

    See: https://schema.org/FDAcategoryD
    Model depth: 6
    """
    valid_name: ClassVar[str] = "FDAcategoryD"
    type_: str = Field("FDAcategoryD", alias='@type')
    



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
