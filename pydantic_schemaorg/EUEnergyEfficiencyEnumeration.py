from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.EnergyEfficiencyEnumeration import EnergyEfficiencyEnumeration


class EUEnergyEfficiencyEnumeration(EnergyEfficiencyEnumeration):
    """Enumerates the EU energy efficiency classes A-G as well as A+, A++, and A+++ as defined"
     "in EU directive 2017/1369.

    See: https://schema.org/EUEnergyEfficiencyEnumeration
    Model depth: 5
    """
    valid_name: ClassVar[str] = "EUEnergyEfficiencyEnumeration"
    type_: str = Field("EUEnergyEfficiencyEnumeration", alias='@type')
    



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
