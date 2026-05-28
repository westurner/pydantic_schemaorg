from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.ActionStatusType import ActionStatusType


class ActiveActionStatus(ActionStatusType):
    """An in-progress action (e.g., while watching the movie, or driving to a location).

    See: https://schema.org/ActiveActionStatus
    Model depth: 6
    """
    valid_name: ClassVar[str] = "ActiveActionStatus"
    type_: str = Field("ActiveActionStatus", alias='@type')
    



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
