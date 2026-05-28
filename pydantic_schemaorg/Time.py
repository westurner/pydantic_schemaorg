from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.DataType import DataType


class Time(DataType):
    """A point in time recurring on multiple days in the form hh:mm:ss[Z|(+|-)hh:mm] (see [XML"
     "schema for details](http://www.w3.org/TR/xmlschema-2/#time)).

    See: https://schema.org/Time
    Model depth: 5
    """
    valid_name: ClassVar[str] = "Time"
    type_: str = Field("Time", alias='@type')
    



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
