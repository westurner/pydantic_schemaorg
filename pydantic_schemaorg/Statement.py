from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class Statement(CreativeWork):
    """A statement about something, for example a fun or interesting fact. If known, the main"
     "entity this statement is about can be indicated using mainEntity. For more formal claims"
     "(e.g. in Fact Checking), consider using [[Claim]] instead. Use the [[text]] property"
     "to capture the text of the statement.

    See: https://schema.org/Statement
    Model depth: 3
    """
    valid_name: ClassVar[str] = "Statement"
    type_: str = Field("Statement", alias='@type')
    



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
