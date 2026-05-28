from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.LodgingBusiness import LodgingBusiness


class Resort(LodgingBusiness):
    """A resort is a place used for relaxation or recreation, attracting visitors for holidays"
     "or vacations. Resorts are places, towns or sometimes commercial establishments operated"
     "by a single company (source: Wikipedia, the free encyclopedia, see <a href=\"http://en.wikipedia.org/wiki/Resort\">http://en.wikipedia.org/wiki/Resort</a>)."
     "<br /><br /> See also the <a href=\"/docs/hotels.html\">dedicated document on the"
     "use of schema.org for marking up hotels and other forms of accommodations</a>.

    See: https://schema.org/Resort
    Model depth: 5
    """
    valid_name: ClassVar[str] = "Resort"
    type_: str = Field("Resort", alias='@type')
    



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
