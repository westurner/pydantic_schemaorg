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
from pydantic_schemaorg.CreativeWork import CreativeWork


class HyperToc(CreativeWork):
    """A HyperToc represents a hypertext table of contents for complex media objects, such"
     "as [[VideoObject]], [[AudioObject]]. Items in the table of contents are indicated"
     "using the [[tocEntry]] property, and typed [[HyperTocEntry]]. For cases where the"
     "same larger work is split into multiple files, [[associatedMedia]] can be used on individual"
     "[[HyperTocEntry]] items.

    See: https://schema.org/HyperToc
    Model depth: 3
    """
    valid_name: ClassVar[str] = "HyperToc"
    type_: str = Field("HyperToc", alias='@type')
    associatedMedia: Optional[Union[List[Union['MediaObject', str]], 'MediaObject', str]] = Field(
        default=None,
        description="A media object that encodes this CreativeWork. This property is a synonym for encoding.",
    )
    tocEntry: Optional[Union[List[Union['HyperTocEntry', str]], 'HyperTocEntry', str]] = Field(
        default=None,
        description="Indicates a [[HyperTocEntry]] in a [[HyperToc]].",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.MediaObject import MediaObject
    from pydantic_schemaorg.HyperTocEntry import HyperTocEntry


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
