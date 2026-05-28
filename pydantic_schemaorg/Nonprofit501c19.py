from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c19(USNonprofitType):
    """Nonprofit501c19: Non-profit type referring to Post or Organization of Past or Present"
     "Members of the Armed Forces.

    See: https://schema.org/Nonprofit501c19
    Model depth: 6
    """
    valid_name: ClassVar[str] = "Nonprofit501c19"
    type_: str = Field("Nonprofit501c19", alias='@type')
    



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
