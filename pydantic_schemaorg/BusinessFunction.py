from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class BusinessFunction(Enumeration):
    """The business function specifies the type of activity or access (i.e., the bundle of rights)"
     "offered by the organization or business person through the offer. Typical are sell,"
     "rental or lease, maintenance or repair, manufacture / produce, recycle / dispose, engineering"
     "/ construction, or installation. Proprietary specifications of access rights are"
     "also instances of this class. Commonly used values: * http://purl.org/goodrelations/v1#ConstructionInstallation"
     "* http://purl.org/goodrelations/v1#Dispose * http://purl.org/goodrelations/v1#LeaseOut"
     "* http://purl.org/goodrelations/v1#Maintain * http://purl.org/goodrelations/v1#ProvideService"
     "* http://purl.org/goodrelations/v1#Repair * http://purl.org/goodrelations/v1#Sell"
     "* http://purl.org/goodrelations/v1#Buy

    See: https://schema.org/BusinessFunction
    Model depth: 4
    """
    valid_name: ClassVar[str] = "BusinessFunction"
    type_: str = Field("BusinessFunction", alias='@type')
    



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
