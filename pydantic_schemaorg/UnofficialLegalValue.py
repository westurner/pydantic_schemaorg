from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.LegalValueLevel import LegalValueLevel


class UnofficialLegalValue(LegalValueLevel):
    """Indicates that a document has no particular or special standing (e.g. a republication"
     "of a law by a private publisher).

    See: https://schema.org/UnofficialLegalValue
    Model depth: 5
    """
    valid_name: ClassVar[str] = "UnofficialLegalValue"
    type_: str = Field("UnofficialLegalValue", alias='@type')
    



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
