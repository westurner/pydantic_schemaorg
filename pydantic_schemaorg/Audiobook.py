from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.AudioObject import AudioObject
from pydantic_schemaorg.Book import Book


class Audiobook(AudioObject, Book):
    """An audiobook.

    See: https://schema.org/Audiobook
    Model depth: 4
    """
    valid_name: ClassVar[str] = "Audiobook"
    type_: str = Field("Audiobook", alias='@type')
    duration: Optional[Union[List[Union['QuantitativeValue', 'Duration', str]], 'QuantitativeValue', 'Duration', str]] = Field(
        default=None,
        description="The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 duration"
     "format](http://en.wikipedia.org/wiki/ISO_8601).",
    )
    readBy: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="A person who reads (performs) the audiobook.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.Duration import Duration
    from pydantic_schemaorg.Person import Person


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
