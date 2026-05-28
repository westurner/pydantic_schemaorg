from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class ComputerLanguage(Intangible):
    """This type covers computer programming languages such as Scheme and Lisp, as well as other"
     "language-like computer representations. Natural languages are best represented"
     "with the [[Language]] type.

    See: https://schema.org/ComputerLanguage
    Model depth: 3
    """
    valid_name: ClassVar[str] = "ComputerLanguage"
    type_: str = Field("ComputerLanguage", alias='@type')
    



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
