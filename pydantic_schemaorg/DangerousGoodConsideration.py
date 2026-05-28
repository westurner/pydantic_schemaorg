from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.AdultOrientedEnumeration import AdultOrientedEnumeration


class DangerousGoodConsideration(AdultOrientedEnumeration):
    """The item is dangerous and requires careful handling and/or special training of the user."
     "See also the [UN Model Classification](https://unece.org/DAM/trans/danger/publi/unrec/rev17/English/02EREv17_Part2.pdf)"
     "defining the 9 classes of dangerous goods such as explosives, gases, flammables, and"
     "more.

    See: https://schema.org/DangerousGoodConsideration
    Model depth: 5
    """
    valid_name: ClassVar[str] = "DangerousGoodConsideration"
    type_: str = Field("DangerousGoodConsideration", alias='@type')
    



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
