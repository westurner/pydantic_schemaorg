from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501q(USNonprofitType):
    """Nonprofit501q: Non-profit type referring to Credit Counseling Organizations.

    See: https://schema.org/Nonprofit501q
    Model depth: 6
    """
    valid_name: ClassVar[str] = "Nonprofit501q"
    type_: str = Field("Nonprofit501q", alias='@type')
    



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
