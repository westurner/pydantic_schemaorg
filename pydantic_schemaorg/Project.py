from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.Organization import Organization


class Project(Organization):
    """An enterprise (potentially individual but typically collaborative), planned to achieve"
     "a particular aim. Use properties from [[Organization]], [[subOrganization]]/[[parentOrganization]]"
     "to indicate project sub-structures.

    See: https://schema.org/Project
    Model depth: 3
    """
    valid_name: ClassVar[str] = "Project"
    type_: str = Field("Project", alias='@type')
    



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
