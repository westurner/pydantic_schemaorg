from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.ReturnFeesEnumeration import ReturnFeesEnumeration


class FreeReturn(ReturnFeesEnumeration):
    """Specifies that product returns are free of charge for the customer.

    See: https://schema.org/FreeReturn
    Model depth: 5
    """
    valid_name: ClassVar[str] = "FreeReturn"
    type_: str = Field("FreeReturn", alias='@type')
    



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
