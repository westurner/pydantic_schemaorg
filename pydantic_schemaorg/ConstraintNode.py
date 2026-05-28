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


class ConstraintNode(Intangible):
    """The ConstraintNode type is provided to support usecases in which a node in a structured"
     "data graph is described with properties which appear to describe a single entity, but"
     "are being used in a situation where they serve a more abstract purpose. A [[ConstraintNode]]"
     "can be described using [[constraintProperty]] and [[numConstraints]]. These constraint"
     "properties can serve a variety of purposes, and their values may sometimes be understood"
     "to indicate sets of possible values rather than single, exact and specific values.

    See: https://schema.org/ConstraintNode
    Model depth: 3
    """
    valid_name: ClassVar[str] = "ConstraintNode"
    type_: str = Field("ConstraintNode", alias='@type')
    numConstraints: Optional[Union[List[Union[int, 'Integer', str]], int, 'Integer', str]] = Field(
        default=None,
        description="Indicates the number of constraints property values defined for a particular [[ConstraintNode]]"
     "such as [[StatisticalVariable]]. This helps applications understand if they have"
     "access to a sufficiently complete description of a [[StatisticalVariable]] or other"
     "construct that is defined using properties on template-style nodes.",
    )
    constraintProperty: Optional[Union[List[Union[AnyUrl, 'URL', 'Property', str]], AnyUrl, 'URL', 'Property', str]] = Field(
        default=None,
        description="Indicates a property used as a constraint. For example, in the definition of a [[StatisticalVariable]]."
     "The value is a property, either from within Schema.org or from other compatible (e.g."
     "RDF) systems such as DataCommons.org or Wikidata.org.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Integer import Integer
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Property import Property


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
