from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.IncentiveType import IncentiveType


class IncentiveTypeTaxWaiver(IncentiveType):
    """An incentive that reduces/exempts the recipient from taxation applicable to the incentivized"
     "good/service (e.g. luxury taxes, registration taxes, circulation tax).

    See: https://schema.org/IncentiveTypeTaxWaiver
    Model depth: 5
    """
    valid_name: ClassVar[str] = "IncentiveTypeTaxWaiver"
    type_: str = Field("IncentiveTypeTaxWaiver", alias='@type')
    



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
