from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.LegalValueLevel import LegalValueLevel


class OfficialLegalValue(LegalValueLevel):
    """All the documents published by an official publisher should have at least the legal value"
     "level \"OfficialLegalValue\". This indicates that the document was published by an"
     "organisation with the public task of making it available (e.g. a consolidated version"
     "of a EU directive published by the EU Office of Publications).

    See: https://schema.org/OfficialLegalValue
    Model depth: 5
    """
    valid_name: ClassVar[str] = "OfficialLegalValue"
    type_: str = Field("OfficialLegalValue", alias='@type')
    



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
