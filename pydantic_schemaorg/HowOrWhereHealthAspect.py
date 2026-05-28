from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


class HowOrWhereHealthAspect(HealthAspectEnumeration):
    """Information about how or where to find a topic. Also may contain location data that can"
     "be used for where to look for help if the topic is observed.

    See: https://schema.org/HowOrWhereHealthAspect
    Model depth: 5
    """
    valid_name: ClassVar[str] = "HowOrWhereHealthAspect"
    type_: str = Field("HowOrWhereHealthAspect", alias='@type')
    



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
