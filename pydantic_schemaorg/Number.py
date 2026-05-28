from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.DataType import DataType


class Number(DataType):
    """Data type: Number. Usage guidelines: * Use values from 0123456789 (Unicode 'DIGIT ZERO'"
     "(U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols."
     "* Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point."
     "Avoid using these symbols as a readability separator.

    See: https://schema.org/Number
    Model depth: 5
    """
    valid_name: ClassVar[str] = "Number"
    type_: str = Field("Number", alias='@type')
    



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
