from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.MedicineSystem import MedicineSystem


class TraditionalChinese(MedicineSystem):
    """A system of medicine based on common theoretical concepts that originated in China and"
     "evolved over thousands of years, that uses herbs, acupuncture, exercise, massage,"
     "dietary therapy, and other methods to treat a wide range of conditions.

    See: https://schema.org/TraditionalChinese
    Model depth: 6
    """
    valid_name: ClassVar[str] = "TraditionalChinese"
    type_: str = Field("TraditionalChinese", alias='@type')
    



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
