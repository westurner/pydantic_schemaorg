from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.DataType import DataType


class DateTime(DataType):
    """A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm]"
     "(see Chapter 5.4 of ISO 8601).

    See: https://schema.org/DateTime
    Model depth: 5
    """
    valid_name: ClassVar[str] = "DateTime"
    type_: str = Field("DateTime", alias='@type')
    



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
