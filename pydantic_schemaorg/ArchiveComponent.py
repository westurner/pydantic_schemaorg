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


class ArchiveComponent(CreativeWork):
    """An intangible type to be applied to any archive content, carrying with it a set of properties"
     "required to describe archival items and collections.

    See: https://schema.org/ArchiveComponent
    Model depth: 3
    """
    valid_name: ClassVar[str] = "ArchiveComponent"
    type_: str = Field("ArchiveComponent", alias='@type')
    itemLocation: Optional[Union[List[Union[str, 'Text', 'PostalAddress', 'Place']], str, 'Text', 'PostalAddress', 'Place']] = Field(
        default=None,
        description="Current location of the item.",
    )
    holdingArchive: Optional[Union[List[Union['ArchiveOrganization', str]], 'ArchiveOrganization', str]] = Field(
        default=None,
        description="[[ArchiveOrganization]] that holds, keeps or maintains the [[ArchiveComponent]].",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.PostalAddress import PostalAddress
    from pydantic_schemaorg.Place import Place
    from pydantic_schemaorg.ArchiveOrganization import ArchiveOrganization


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
