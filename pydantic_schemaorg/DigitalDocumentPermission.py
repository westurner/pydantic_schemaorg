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
from pydantic_schemaorg.Intangible import Intangible


class DigitalDocumentPermission(Intangible):
    """A permission for a particular person or group to access a particular file.

    See: https://schema.org/DigitalDocumentPermission
    Model depth: 3
    """
    valid_name: ClassVar[str] = "DigitalDocumentPermission"
    type_: str = Field("DigitalDocumentPermission", alias='@type')
    permissionType: Optional[Union[List[Union['DigitalDocumentPermissionType', str]], 'DigitalDocumentPermissionType', str]] = Field(
        default=None,
        description="The type of permission granted the person, organization, or audience.",
    )
    grantee: Optional[Union[List[Union['Audience', 'Person', 'ContactPoint', 'Organization', str]], 'Audience', 'Person', 'ContactPoint', 'Organization', str]] = Field(
        default=None,
        description="The person, organization, contact point, or audience that has been granted this permission.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.DigitalDocumentPermissionType import DigitalDocumentPermissionType
    from pydantic_schemaorg.Audience import Audience
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.ContactPoint import ContactPoint
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
