from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.Article import Article


class SatiricalArticle(Article):
    """An [[Article]] whose content is primarily [[satirical]](https://en.wikipedia.org/wiki/Satire)"
     "in nature, i.e. unlikely to be literally true. A satirical article is sometimes but not"
     "necessarily also a [[NewsArticle]]. [[ScholarlyArticle]]s are also sometimes satirized.

    See: https://schema.org/SatiricalArticle
    Model depth: 4
    """
    valid_name: ClassVar[str] = "SatiricalArticle"
    type_: str = Field("SatiricalArticle", alias='@type')
    



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
