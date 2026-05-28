from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class Language(Intangible):
    """Natural languages such as Spanish, Tamil, Hindi, English, etc. Formal language code"
     "tags expressed in [BCP 47](https://en.wikipedia.org/wiki/IETF_language_tag)"
     "can be used via the [[alternateName]] property. The Language type previously also covered"
     "programming languages such as Scheme and Lisp, which are now best represented using"
     "[[ComputerLanguage]].

    See: https://schema.org/Language
    Model depth: 3
    """
    valid_name: ClassVar[str] = "Language"
    type_: str = Field("Language", alias='@type')
    



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
