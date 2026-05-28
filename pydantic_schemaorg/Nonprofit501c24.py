from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.USNonprofitType import USNonprofitType


class Nonprofit501c24(USNonprofitType):
    """Nonprofit501c24: Non-profit type referring to Section 4049 ERISA Trusts.

    See: https://schema.org/Nonprofit501c24
    Model depth: 6
    """
    valid_name: ClassVar[str] = "Nonprofit501c24"
    type_: str = Field("Nonprofit501c24", alias='@type')
    



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
