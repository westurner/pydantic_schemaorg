from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.Periodical import Periodical


class Newspaper(Periodical):
    """A publication containing information about varied topics that are pertinent to general"
     "information, a geographic area, or a specific subject matter (i.e. business, culture,"
     "education). Often published daily.

    See: https://schema.org/Newspaper
    Model depth: 5
    """
    valid_name: ClassVar[str] = "Newspaper"
    type_: str = Field("Newspaper", alias='@type')
    



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
