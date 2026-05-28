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


class AlignmentObject(Intangible):
    """An intangible item that describes an alignment between a learning resource and a node"
     "in an educational framework. Should not be used where the nature of the alignment can"
     "be described using a simple property, for example to express that a resource [[teaches]]"
     "or [[assesses]] a competency.

    See: https://schema.org/AlignmentObject
    Model depth: 3
    """
    valid_name: ClassVar[str] = "AlignmentObject"
    type_: str = Field("AlignmentObject", alias='@type')
    targetName: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The name of a node in an established educational framework.",
    )
    targetDescription: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The description of a node in an established educational framework.",
    )
    educationalFramework: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The framework to which the resource being described is aligned.",
    )
    alignmentType: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="A category of alignment between the learning resource and the framework node. Recommended"
     "values include: 'requires', 'textComplexity', 'readingLevel', and 'educationalSubject'.",
    )
    targetUrl: Optional[Union[List[Union[AnyUrl, 'URL', str]], AnyUrl, 'URL', str]] = Field(
        default=None,
        description="The URL of a node in an established educational framework.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.URL import URL


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
