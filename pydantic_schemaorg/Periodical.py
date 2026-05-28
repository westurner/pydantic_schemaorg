from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.CreativeWorkSeries import CreativeWorkSeries


class Periodical(CreativeWorkSeries):
    """A publication in any medium issued in successive parts bearing numerical or chronological"
     "designations and intended to continue indefinitely, such as a magazine, scholarly"
     "journal, or newspaper. See also [blog post](http://blog.schema.org/2014/09/schemaorg-support-for-bibliographic_2.html).

    See: https://schema.org/Periodical
    Model depth: 4
    """
    valid_name: ClassVar[str] = "Periodical"
    type_: str = Field("Periodical", alias='@type')
    



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
