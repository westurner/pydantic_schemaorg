from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.Rating import Rating


class EndorsementRating(Rating):
    """An EndorsementRating is a rating that expresses some level of endorsement, for example"
     "inclusion in a \"critic's pick\" blog, a \"Like\" or \"+1\" on a social network. It can"
     "be considered the [[result]] of an [[EndorseAction]] in which the [[object]] of the"
     "action is rated positively by some [[agent]]. As is common elsewhere in schema.org,"
     "it is sometimes more useful to describe the results of such an action without explicitly"
     "describing the [[Action]]. An [[EndorsementRating]] may be part of a numeric scale"
     "or organized system, but this is not required: having an explicit type for indicating"
     "a positive, endorsement rating is particularly useful in the absence of numeric scales"
     "as it helps consumers understand that the rating is broadly positive.

    See: https://schema.org/EndorsementRating
    Model depth: 4
    """
    valid_name: ClassVar[str] = "EndorsementRating"
    type_: str = Field("EndorsementRating", alias='@type')
    



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
