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
from pydantic_schemaorg.Service import Service


class GovernmentService(Service):
    """A service provided by a government organization, e.g. food stamps, veterans benefits,"
     "etc.

    See: https://schema.org/GovernmentService
    Model depth: 4
    """
    valid_name: ClassVar[str] = "GovernmentService"
    type_: str = Field("GovernmentService", alias='@type')
    jurisdiction: Optional[Union[List[Union[str, 'Text', 'AdministrativeArea']], str, 'Text', 'AdministrativeArea']] = Field(
        default=None,
        description="Indicates a legal jurisdiction, e.g. of some legislation, or where some government"
     "service is based.",
    )
    serviceOperator: Optional[Union[List[Union['Organization', str]], 'Organization', str]] = Field(
        default=None,
        description="The operating organization, if different from the provider. This enables the representation"
     "of services that are provided by an organization, but operated by another organization"
     "like a subcontractor.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.AdministrativeArea import AdministrativeArea
    from pydantic_schemaorg.Organization import Organization


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
