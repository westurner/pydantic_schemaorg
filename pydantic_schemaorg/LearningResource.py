from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from typing import List, Optional, Union
from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class LearningResource(CreativeWork):
    """The LearningResource type can be used to indicate [[CreativeWork]]s (whether physical"
     "or digital) that have a particular and explicit orientation towards learning, education,"
     "skill acquisition, and other educational purposes. [[LearningResource]] is expected"
     "to be used as an addition to a primary type such as [[Book]], [[VideoObject]], [[Product]]"
     "etc. [[EducationEvent]] serves a similar purpose for event-like things (e.g. a [[Trip]])."
     "A [[LearningResource]] may be created as a result of an [[EducationEvent]], for example"
     "by recording one.

    See: https://schema.org/LearningResource
    Model depth: 3
    """
    valid_name: ClassVar[str] = "LearningResource"
    type_: str = Field("LearningResource", alias='@type')
    educationalAlignment: Optional[Union[List[Union['AlignmentObject', str]], 'AlignmentObject', str]] = Field(
        default=None,
        description="An alignment to an established educational framework. This property should not be used"
     "where the nature of the alignment can be described using a simple property, for example"
     "to express that a resource [[teaches]] or [[assesses]] a competency.",
    )
    educationalUse: Optional[Union[List[Union[str, 'Text', 'DefinedTerm']], str, 'Text', 'DefinedTerm']] = Field(
        default=None,
        description="The purpose of a work in the context of education; for example, 'assignment', 'group"
     "work'.",
    )
    assesses: Optional[Union[List[Union[str, 'Text', 'DefinedTerm']], str, 'Text', 'DefinedTerm']] = Field(
        default=None,
        description="The item being described is intended to assess the competency or learning outcome defined"
     "by the referenced term.",
    )
    teaches: Optional[Union[List[Union[str, 'Text', 'DefinedTerm']], str, 'Text', 'DefinedTerm']] = Field(
        default=None,
        description="The item being described is intended to help a person learn the competency or learning"
     "outcome defined by the referenced term.",
    )
    educationalLevel: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'DefinedTerm']], AnyUrl, 'URL', str, 'Text', 'DefinedTerm']] = Field(
        default=None,
        description="The level in terms of progression through an educational or training context. Examples"
     "of educational levels include 'beginner', 'intermediate' or 'advanced', and formal"
     "sets of level indicators.",
    )
    learningResourceType: Optional[Union[List[Union[str, 'Text', 'DefinedTerm']], str, 'Text', 'DefinedTerm']] = Field(
        default=None,
        description="The predominant type or kind characterizing the learning resource. For example, 'presentation',"
     "'handout'.",
    )
    competencyRequired: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'DefinedTerm']], AnyUrl, 'URL', str, 'Text', 'DefinedTerm']] = Field(
        default=None,
        description="Knowledge, skill, ability or personal attribute that must be demonstrated by a person"
     "or other entity in order to do something such as earn an Educational Occupational Credential"
     "or understand a LearningResource.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.AlignmentObject import AlignmentObject
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.DefinedTerm import DefinedTerm
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
