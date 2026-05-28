from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.AdultOrientedEnumeration import AdultOrientedEnumeration


class ReducedRelevanceForChildrenConsideration(AdultOrientedEnumeration):
    """A general code for cases where relevance to children is reduced, e.g. adult education,"
     "mortgages, retirement-related products, etc.

    See: https://schema.org/ReducedRelevanceForChildrenConsideration
    Model depth: 5
    """
    valid_name: ClassVar[str] = "ReducedRelevanceForChildrenConsideration"
    type_: str = Field("ReducedRelevanceForChildrenConsideration", alias='@type')
    



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
