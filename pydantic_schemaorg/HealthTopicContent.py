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
from pydantic_schemaorg.WebContent import WebContent


class HealthTopicContent(WebContent):
    """[[HealthTopicContent]] is [[WebContent]] that is about some aspect of a health topic,"
     "e.g. a condition, its symptoms or treatments. Such content may be comprised of several"
     "parts or sections and use different types of media. Multiple instances of [[WebContent]]"
     "(and hence [[HealthTopicContent]]) can be related using [[hasPart]] / [[isPartOf]]"
     "where there is some kind of content hierarchy, and their content described with [[about]]"
     "and [[mentions]] e.g. building upon the existing [[MedicalCondition]] vocabulary.

    See: https://schema.org/HealthTopicContent
    Model depth: 4
    """
    valid_name: ClassVar[str] = "HealthTopicContent"
    type_: str = Field("HealthTopicContent", alias='@type')
    hasHealthAspect: Optional[Union[List[Union['HealthAspectEnumeration', str]], 'HealthAspectEnumeration', str]] = Field(
        default=None,
        description="Indicates the aspect or aspects specifically addressed in some [[HealthTopicContent]]."
     "For example, that the content is an overview, or that it talks about treatment, self-care,"
     "treatments or their side-effects.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.HealthAspectEnumeration import HealthAspectEnumeration


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
