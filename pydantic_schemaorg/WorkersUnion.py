from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.Organization import Organization


class WorkersUnion(Organization):
    """A Workers Union (also known as a Labor Union, Labour Union, or Trade Union) is an organization"
     "that promotes the interests of its worker members by collectively bargaining with management,"
     "organizing, and political lobbying.

    See: https://schema.org/WorkersUnion
    Model depth: 3
    """
    valid_name: ClassVar[str] = "WorkersUnion"
    type_: str = Field("WorkersUnion", alias='@type')
    



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
