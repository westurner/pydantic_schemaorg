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
from pydantic_schemaorg.CreativeWork import CreativeWork


class EducationalOccupationalCredential(CreativeWork):
    """An educational or occupational credential. A diploma, academic degree, certification,"
     "qualification, badge, etc., that may be awarded to a person or other entity that meets"
     "the requirements defined by the credentialer.

    See: https://schema.org/EducationalOccupationalCredential
    Model depth: 3
    """
    valid_name: ClassVar[str] = "EducationalOccupationalCredential"
    type_: str = Field("EducationalOccupationalCredential", alias='@type')
    recognizedBy: Optional[Union[List[Union['Organization', str]], 'Organization', str]] = Field(
        default=None,
        description="An organization that acknowledges the validity, value or utility of a credential. Note:"
     "recognition may include a process of quality assurance or accreditation.",
    )
    credentialCategory: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'DefinedTerm']], AnyUrl, 'URL', str, 'Text', 'DefinedTerm']] = Field(
        default=None,
        description="The category or type of credential being described, for example \"degree”, “certificate”,"
     "“badge”, or more specific term.",
    )
    validFor: Optional[Union[List[Union['Duration', str]], 'Duration', str]] = Field(
        default=None,
        description="The duration of validity of a permit or similar thing.",
    )
    educationalLevel: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'DefinedTerm']], AnyUrl, 'URL', str, 'Text', 'DefinedTerm']] = Field(
        default=None,
        description="The level in terms of progression through an educational or training context. Examples"
     "of educational levels include 'beginner', 'intermediate' or 'advanced', and formal"
     "sets of level indicators.",
    )
    competencyRequired: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'DefinedTerm']], AnyUrl, 'URL', str, 'Text', 'DefinedTerm']] = Field(
        default=None,
        description="Knowledge, skill, ability or personal attribute that must be demonstrated by a person"
     "or other entity in order to do something such as earn an Educational Occupational Credential"
     "or understand a LearningResource.",
    )
    validIn: Optional[Union[List[Union['AdministrativeArea', str]], 'AdministrativeArea', str]] = Field(
        default=None,
        description="The geographic area where the item is valid. Applies for example to a [[Permit]], a [[Certification]],"
     "or an [[EducationalOccupationalCredential]].",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.DefinedTerm import DefinedTerm
    from pydantic_schemaorg.Duration import Duration
    from pydantic_schemaorg.AdministrativeArea import AdministrativeArea


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
