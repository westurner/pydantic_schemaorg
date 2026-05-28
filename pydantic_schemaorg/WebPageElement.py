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


class WebPageElement(CreativeWork):
    """A web page element, like a table or an image.

    See: https://schema.org/WebPageElement
    Model depth: 3
    """
    valid_name: ClassVar[str] = "WebPageElement"
    type_: str = Field("WebPageElement", alias='@type')
    xpath: Optional[Union[List[Union[str, 'XPathType']], str, 'XPathType']] = Field(
        default=None,
        description="An XPath, e.g. of a [[SpeakableSpecification]] or [[WebPageElement]]. In the latter"
     "case, multiple matches within a page can constitute a single conceptual \"Web page element\".",
    )
    cssSelector: Optional[Union[List[Union[str, 'CssSelectorType']], str, 'CssSelectorType']] = Field(
        default=None,
        description="A CSS selector, e.g. of a [[SpeakableSpecification]] or [[WebPageElement]]. In the"
     "latter case, multiple matches within a page can constitute a single conceptual \"Web"
     "page element\".",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.XPathType import XPathType
    from pydantic_schemaorg.CssSelectorType import CssSelectorType


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
