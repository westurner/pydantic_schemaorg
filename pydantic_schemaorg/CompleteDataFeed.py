from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.DataFeed import DataFeed


class CompleteDataFeed(DataFeed):
    """A [[CompleteDataFeed]] is a [[DataFeed]] whose standard representation includes"
     "content for every item currently in the feed. This is the equivalent of Atom's element"
     "as defined in Feed Paging and Archiving [RFC 5005](https://tools.ietf.org/html/rfc5005),"
     "for example (and as defined for Atom), when using data from a feed that represents a collection"
     "of items that varies over time (e.g. \"Top Twenty Records\") there is no need to have newer"
     "entries mixed in alongside older, obsolete entries. By marking this feed as a CompleteDataFeed,"
     "old entries can be safely discarded when the feed is refreshed, since we can assume the"
     "feed has provided descriptions for all current items.

    See: https://schema.org/CompleteDataFeed
    Model depth: 5
    """
    valid_name: ClassVar[str] = "CompleteDataFeed"
    type_: str = Field("CompleteDataFeed", alias='@type')
    



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
