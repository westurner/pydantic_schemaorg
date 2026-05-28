from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.BodyMeasurementTypeEnumeration import BodyMeasurementTypeEnumeration


class BodyMeasurementChest(BodyMeasurementTypeEnumeration):
    """Maximum girth of chest. Used, for example, to fit men's suits.

    See: https://schema.org/BodyMeasurementChest
    Model depth: 6
    """
    valid_name: ClassVar[str] = "BodyMeasurementChest"
    type_: str = Field("BodyMeasurementChest", alias='@type')
    



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
