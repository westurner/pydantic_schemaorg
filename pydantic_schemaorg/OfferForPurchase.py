from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.Offer import Offer


class OfferForPurchase(Offer):
    """An [[OfferForPurchase]] in Schema.org represents an [[Offer]] to sell something,"
     "i.e. an [[Offer]] whose [[businessFunction]] is [sell](http://purl.org/goodrelations/v1#Sell.)."
     "See [Good Relations](https://en.wikipedia.org/wiki/GoodRelations) for background"
     "on the underlying concepts.

    See: https://schema.org/OfferForPurchase
    Model depth: 4
    """
    valid_name: ClassVar[str] = "OfferForPurchase"
    type_: str = Field("OfferForPurchase", alias='@type')
    



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
