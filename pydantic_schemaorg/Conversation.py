from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class Conversation(CreativeWork):
    """One or more messages between organizations or people on a particular topic. Individual"
     "messages can be linked to the conversation with isPartOf or hasPart properties.

    See: https://schema.org/Conversation
    Model depth: 3
    """
    valid_name: ClassVar[str] = "Conversation"
    type_: str = Field("Conversation", alias='@type')
    



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
