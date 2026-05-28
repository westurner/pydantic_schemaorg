from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.LocalBusiness import LocalBusiness


class LegalService(LocalBusiness):
    """A LegalService is a business that provides legally-oriented services, advice and representation,"
     "e.g. law firms. As a [[LocalBusiness]] it can be described as a [[provider]] of one or"
     "more [[Service]]\(s).

    See: https://schema.org/LegalService
    Model depth: 4
    """
    valid_name: ClassVar[str] = "LegalService"
    type_: str = Field("LegalService", alias='@type')
    



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
