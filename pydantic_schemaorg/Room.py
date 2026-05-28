from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.Accommodation import Accommodation


class Room(Accommodation):
    """A room is a distinguishable space within a structure, usually separated from other spaces"
     "by interior walls (source: Wikipedia, the free encyclopedia, see <a href=\"http://en.wikipedia.org/wiki/Room\">http://en.wikipedia.org/wiki/Room</a>)."
     "<br /><br /> See also the <a href=\"/docs/hotels.html\">dedicated document on the"
     "use of schema.org for marking up hotels and other forms of accommodations</a>.

    See: https://schema.org/Room
    Model depth: 4
    """
    valid_name: ClassVar[str] = "Room"
    type_: str = Field("Room", alias='@type')
    



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
