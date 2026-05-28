from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.Organization import Organization


class OnlineBusiness(Organization):
    """A particular online business, either standalone or the online part of a broader organization."
     "Examples include an eCommerce site, an online travel booking site, an online learning"
     "site, an online logistics and shipping provider, an online (virtual) doctor, etc.

    See: https://schema.org/OnlineBusiness
    Model depth: 3
    """
    valid_name: ClassVar[str] = "OnlineBusiness"
    type_: str = Field("OnlineBusiness", alias='@type')
    



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
