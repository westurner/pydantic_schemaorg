from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class Play(CreativeWork):
    """A play is a form of literature, usually consisting of dialogue between characters, intended"
     "for theatrical performance rather than just reading. Note: A performance of a Play would"
     "be a [[TheaterEvent]] or [[BroadcastEvent]] - the *Play* being the [[workPerformed]].

    See: https://schema.org/Play
    Model depth: 3
    """
    valid_name: ClassVar[str] = "Play"
    type_: str = Field("Play", alias='@type')
    



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
