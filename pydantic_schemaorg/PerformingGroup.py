from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.Organization import Organization


class PerformingGroup(Organization):
    """A performance group, such as a band, an orchestra, or a circus.

    See: https://schema.org/PerformingGroup
    Model depth: 3
    """
    valid_name: ClassVar[str] = "PerformingGroup"
    type_: str = Field("PerformingGroup", alias='@type')
    



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
