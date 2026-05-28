from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from typing import List, Optional, Union
from pydantic import AnyUrl


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class EntryPoint(Intangible):
    """An entry point, within some Web-based protocol.

    See: https://schema.org/EntryPoint
    Model depth: 3
    """
    valid_name: ClassVar[str] = "EntryPoint"
    type_: str = Field("EntryPoint", alias='@type')
    httpMethod: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="An HTTP method that specifies the appropriate HTTP method for a request to an HTTP EntryPoint."
     "Values are capitalized strings as used in HTTP.",
    )
    actionPlatform: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'DigitalPlatformEnumeration']], AnyUrl, 'URL', str, 'Text', 'DigitalPlatformEnumeration']] = Field(
        default=None,
        description="The high level platform(s) where the Action can be performed for the given URL. To specify"
     "a specific application or operating system instance, use actionApplication.",
    )
    actionApplication: Optional[Union[List[Union['SoftwareApplication', str]], 'SoftwareApplication', str]] = Field(
        default=None,
        description="An application that can complete the request.",
    )
    urlTemplate: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="An url template (RFC6570) that will be used to construct the target of the execution of"
     "the action.",
    )
    encodingType: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The supported encoding type(s) for an EntryPoint request.",
    )
    contentType: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The supported content type(s) for an EntryPoint response.",
    )
    application: Optional[Union[List[Union['SoftwareApplication', str]], 'SoftwareApplication', str]] = Field(
        default=None,
        description="An application that can complete the request.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.DigitalPlatformEnumeration import DigitalPlatformEnumeration
    from pydantic_schemaorg.SoftwareApplication import SoftwareApplication


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
