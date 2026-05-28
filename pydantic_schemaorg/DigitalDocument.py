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


class DigitalDocument(CreativeWork):
    """An electronic file or document.

    See: https://schema.org/DigitalDocument
    Model depth: 3
    """
    valid_name: ClassVar[str] = "DigitalDocument"
    type_: str = Field("DigitalDocument", alias='@type')
    hasDigitalDocumentPermission: Optional[Union[List[Union['DigitalDocumentPermission', str]], 'DigitalDocumentPermission', str]] = Field(
        default=None,
        description="A permission related to the access to this document (e.g. permission to read or write"
     "an electronic document). For a public document, specify a grantee with an Audience with"
     "audienceType equal to \"public\".",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.DigitalDocumentPermission import DigitalDocumentPermission


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
