from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class WarrantyScope(Enumeration):
    """A range of services that will be provided to a customer free of charge in case of a defect"
     "or malfunction of a product. Commonly used values: * http://purl.org/goodrelations/v1#Labor-BringIn"
     "* http://purl.org/goodrelations/v1#PartsAndLabor-BringIn * http://purl.org/goodrelations/v1#PartsAndLabor-PickUp

    See: https://schema.org/WarrantyScope
    Model depth: 4
    """
    valid_name: ClassVar[str] = "WarrantyScope"
    type_: str = Field("WarrantyScope", alias='@type')
    



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
