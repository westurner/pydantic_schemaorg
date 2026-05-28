from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from pydantic import AnyUrl
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class DefinedTerm(Intangible):
    """A word, name, acronym, phrase, etc. with a formal definition. Often used in the context"
     "of category or subject classification, glossaries or dictionaries, product or creative"
     "work types, etc. Use the name property for the term being defined, use termCode if the"
     "term has an alpha-numeric code allocated, use description to provide the definition"
     "of the term.

    See: https://schema.org/DefinedTerm
    Model depth: 3
    """
    valid_name: ClassVar[str] = "DefinedTerm"
    type_: str = Field("DefinedTerm", alias='@type')
    inDefinedTermSet: Optional[Union[List[Union[AnyUrl, 'URL', 'DefinedTermSet', str]], AnyUrl, 'URL', 'DefinedTermSet', str]] = Field(
        default=None,
        description="A [[DefinedTermSet]] that contains this term.",
    )
    termCode: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="A code that identifies this [[DefinedTerm]] within a [[DefinedTermSet]].",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.DefinedTermSet import DefinedTermSet
    from pydantic_schemaorg.Text import Text


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
