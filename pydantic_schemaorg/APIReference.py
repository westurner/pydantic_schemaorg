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
from pydantic_schemaorg.TechArticle import TechArticle


class APIReference(TechArticle):
    """Reference documentation for application programming interfaces (APIs).

    See: https://schema.org/APIReference
    Model depth: 5
    """
    valid_name: ClassVar[str] = "APIReference"
    type_: str = Field("APIReference", alias='@type')
    executableLibraryName: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Library file name, e.g., mscorlib.dll, system.web.dll.",
    )
    targetPlatform: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Type of app development: phone, Metro style, desktop, XBox, etc.",
    )
    programmingModel: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Indicates whether API is managed or unmanaged.",
    )
    assembly: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Library file name, e.g., mscorlib.dll, system.web.dll.",
    )
    assemblyVersion: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Associated product/technology version. E.g., .NET Framework 4.5.",
    )
    


if TYPE_CHECKING:
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
