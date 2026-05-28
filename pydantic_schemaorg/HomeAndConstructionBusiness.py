from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class HomeAndConstructionBusiness(LocalBusiness):
    """A construction business. A HomeAndConstructionBusiness is a [[LocalBusiness]] that"
     "provides services around homes and buildings. As a [[LocalBusiness]] it can be described"
     "as a [[provider]] of one or more [[Service]]\(s).

    See: https://schema.org/HomeAndConstructionBusiness
    Model depth: 4
    """
    valid_name: ClassVar[str] = "HomeAndConstructionBusiness"
    type_: str = Field("HomeAndConstructionBusiness", alias='@type')
    



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
