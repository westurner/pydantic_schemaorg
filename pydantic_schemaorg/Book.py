from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from typing import List, Optional, Union
from pydantic import StrictBool


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class Book(CreativeWork):
    """A book.

    See: https://schema.org/Book
    Model depth: 3
    """
    valid_name: ClassVar[str] = "Book"
    type_: str = Field("Book", alias='@type')
    bookEdition: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The edition of the book.",
    )
    isbn: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The ISBN of the book.",
    )
    bookFormat: Optional[Union[List[Union['BookFormatType', str]], 'BookFormatType', str]] = Field(
        default=None,
        description="The format of the book.",
    )
    numberOfPages: Optional[Union[List[Union[int, 'Integer', str]], int, 'Integer', str]] = Field(
        default=None,
        description="The number of pages in the book.",
    )
    abridged: Optional[Union[List[Union[StrictBool, 'Boolean', str]], StrictBool, 'Boolean', str]] = Field(
        default=None,
        description="Indicates whether the book is an abridged edition.",
    )
    illustrator: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="The illustrator of the book.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.BookFormatType import BookFormatType
    from pydantic_schemaorg.Integer import Integer
    from pydantic_schemaorg.Boolean import Boolean
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
