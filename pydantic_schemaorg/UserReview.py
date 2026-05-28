from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.Review import Review


class UserReview(Review):
    """A review created by an end-user (e.g. consumer, purchaser, attendee etc.), in contrast"
     "with [[CriticReview]].

    See: https://schema.org/UserReview
    Model depth: 4
    """
    valid_name: ClassVar[str] = "UserReview"
    type_: str = Field("UserReview", alias='@type')
    



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
