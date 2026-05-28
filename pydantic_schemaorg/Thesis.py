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


class Thesis(CreativeWork):
    """A thesis or dissertation document submitted in support of candidature for an academic"
     "degree or professional qualification.

    See: https://schema.org/Thesis
    Model depth: 3
    """
    valid_name: ClassVar[str] = "Thesis"
    type_: str = Field("Thesis", alias='@type')
    inSupportOf: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Qualification, candidature, degree, application that Thesis supports.",
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
