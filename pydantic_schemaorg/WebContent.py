from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class WebContent(CreativeWork):
    """WebContent is a type representing all [[WebPage]], [[WebSite]] and [[WebPageElement]]"
     "content. It is sometimes the case that detailed distinctions between Web pages, sites"
     "and their parts are not always important or obvious. The [[WebContent]] type makes it"
     "easier to describe Web-addressable content without requiring such distinctions to"
     "always be stated. (The intent is that the existing types [[WebPage]], [[WebSite]] and"
     "[[WebPageElement]] will eventually be declared as subtypes of [[WebContent]].)

    See: https://schema.org/WebContent
    Model depth: 3
    """
    valid_name: ClassVar[str] = "WebContent"
    type_: str = Field("WebContent", alias='@type')
    



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
