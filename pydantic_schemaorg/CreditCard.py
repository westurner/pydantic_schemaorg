from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.LoanOrCredit import LoanOrCredit
from pydantic_schemaorg.PaymentCard import PaymentCard


class CreditCard(LoanOrCredit, PaymentCard):
    """A card payment method of a particular brand or name. Used to mark up a particular payment"
     "method and/or the financial product/service that supplies the card account. Commonly"
     "used values: * http://purl.org/goodrelations/v1#AmericanExpress * http://purl.org/goodrelations/v1#DinersClub"
     "* http://purl.org/goodrelations/v1#Discover * http://purl.org/goodrelations/v1#JCB"
     "* http://purl.org/goodrelations/v1#MasterCard * http://purl.org/goodrelations/v1#VISA

    See: https://schema.org/CreditCard
    Model depth: 5
    """
    valid_name: ClassVar[str] = "CreditCard"
    type_: str = Field("CreditCard", alias='@type')
    



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
