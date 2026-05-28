from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class Series(Intangible):
    """A Series in schema.org is a group of related items, typically but not necessarily of the"
     "same kind. See also [[CreativeWorkSeries]], [[EventSeries]].

    See: https://schema.org/Series
    Model depth: 3
    """
    valid_name: ClassVar[str] = "Series"
    type_: str = Field("Series", alias='@type')
    



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
