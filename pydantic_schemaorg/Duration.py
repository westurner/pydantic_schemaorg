from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.Quantity import Quantity


class Duration(Quantity):
    """Quantity: Duration (use [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601)).

    See: https://schema.org/Duration
    Model depth: 4
    """
    valid_name: ClassVar[str] = "Duration"
    type_: str = Field("Duration", alias='@type')
    



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
