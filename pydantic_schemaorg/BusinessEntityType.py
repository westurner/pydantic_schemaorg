from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class BusinessEntityType(Enumeration):
    """A business entity type is a conceptual entity representing the legal form, the size,"
     "the main line of business, the position in the value chain, or any combination thereof,"
     "of an organization or business person. Commonly used values: * http://purl.org/goodrelations/v1#Business"
     "* http://purl.org/goodrelations/v1#Enduser * http://purl.org/goodrelations/v1#PublicInstitution"
     "* http://purl.org/goodrelations/v1#Reseller

    See: https://schema.org/BusinessEntityType
    Model depth: 4
    """
    valid_name: ClassVar[str] = "BusinessEntityType"
    type_: str = Field("BusinessEntityType", alias='@type')
    



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
