from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.BookFormatType import BookFormatType


class AudiobookFormat(BookFormatType):
    """Book format: Audiobook. This is an enumerated value for use with the bookFormat property."
     "There is also a type 'Audiobook' in the bib extension which includes Audiobook specific"
     "properties.

    See: https://schema.org/AudiobookFormat
    Model depth: 5
    """
    valid_name: ClassVar[str] = "AudiobookFormat"
    type_: str = Field("AudiobookFormat", alias='@type')
    



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
