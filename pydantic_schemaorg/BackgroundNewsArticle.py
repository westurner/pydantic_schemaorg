from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.NewsArticle import NewsArticle


class BackgroundNewsArticle(NewsArticle):
    """A [[NewsArticle]] providing historical context, definition and detail on a specific"
     "topic (aka \"explainer\" or \"backgrounder\"). For example, an in-depth article or"
     "frequently-asked-questions ([FAQ](https://en.wikipedia.org/wiki/FAQ)) document"
     "on topics such as Climate Change or the European Union. Other kinds of background material"
     "from a non-news setting are often described using [[Book]] or [[Article]], in particular"
     "[[ScholarlyArticle]]. See also [[NewsArticle]] for related vocabulary from a learning/education"
     "perspective.

    See: https://schema.org/BackgroundNewsArticle
    Model depth: 5
    """
    valid_name: ClassVar[str] = "BackgroundNewsArticle"
    type_: str = Field("BackgroundNewsArticle", alias='@type')
    



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
