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
from pydantic_schemaorg.MediaObject import MediaObject
from pydantic_schemaorg.Legislation import Legislation


class LegislationObject(MediaObject, Legislation):
    """A specific object or file containing a Legislation. Note that the same Legislation can"
     "be published in multiple files. For example, a digitally signed PDF, a plain PDF and an"
     "HTML version.

    See: https://schema.org/LegislationObject
    Model depth: 4
    """
    valid_name: ClassVar[str] = "LegislationObject"
    type_: str = Field("LegislationObject", alias='@type')
    legislationLegalValue: Optional[Union[List[Union['LegalValueLevel', str]], 'LegalValueLevel', str]] = Field(
        default=None,
        description="The legal value of this legislation file. The same legislation can be written in multiple"
     "files with different legal values. Typically a digitally signed PDF have a \"stronger\""
     "legal value than the HTML file of the same act.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.LegalValueLevel import LegalValueLevel


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
