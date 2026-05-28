from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.DrugPregnancyCategory import DrugPregnancyCategory


class FDAcategoryA(DrugPregnancyCategory):
    """A designation by the US FDA signifying that adequate and well-controlled studies have"
     "failed to demonstrate a risk to the fetus in the first trimester of pregnancy (and there"
     "is no evidence of risk in later trimesters).

    See: https://schema.org/FDAcategoryA
    Model depth: 6
    """
    valid_name: ClassVar[str] = "FDAcategoryA"
    type_: str = Field("FDAcategoryA", alias='@type')
    



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
