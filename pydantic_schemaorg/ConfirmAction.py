from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.InformAction import InformAction


class ConfirmAction(InformAction):
    """The act of notifying someone that a future event/action is going to happen as expected."
     "Related actions: * [[CancelAction]]: The antonym of ConfirmAction.

    See: https://schema.org/ConfirmAction
    Model depth: 6
    """
    valid_name: ClassVar[str] = "ConfirmAction"
    type_: str = Field("ConfirmAction", alias='@type')
    



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
