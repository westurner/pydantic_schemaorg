from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class DeliveryMethod(Enumeration):
    """A delivery method is a standardized procedure for transferring the product or service"
     "to the destination of fulfillment chosen by the customer. Delivery methods are characterized"
     "by the means of transportation used, and by the organization or group that is the contracting"
     "party for the sending organization or person. Commonly used values: * http://purl.org/goodrelations/v1#DeliveryModeDirectDownload"
     "* http://purl.org/goodrelations/v1#DeliveryModeFreight * http://purl.org/goodrelations/v1#DeliveryModeMail"
     "* http://purl.org/goodrelations/v1#DeliveryModeOwnFleet * http://purl.org/goodrelations/v1#DeliveryModePickUp"
     "* http://purl.org/goodrelations/v1#DHL * http://purl.org/goodrelations/v1#FederalExpress"
     "* http://purl.org/goodrelations/v1#UPS

    See: https://schema.org/DeliveryMethod
    Model depth: 4
    """
    valid_name: ClassVar[str] = "DeliveryMethod"
    type_: str = Field("DeliveryMethod", alias='@type')
    



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
