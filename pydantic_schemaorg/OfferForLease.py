from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.Offer import Offer


class OfferForLease(Offer):
    """An [[OfferForLease]] in Schema.org represents an [[Offer]] to lease out something,"
     "i.e. an [[Offer]] whose [[businessFunction]] is [lease out](http://purl.org/goodrelations/v1#LeaseOut.)."
     "See [Good Relations](https://en.wikipedia.org/wiki/GoodRelations) for background"
     "on the underlying concepts.

    See: https://schema.org/OfferForLease
    Model depth: 4
    """
    valid_name: ClassVar[str] = "OfferForLease"
    type_: str = Field("OfferForLease", alias='@type')
    



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
