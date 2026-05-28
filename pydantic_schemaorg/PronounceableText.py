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
from pydantic_schemaorg.Text import Text


class PronounceableText(Text):
    """Data type: PronounceableText.

    See: https://schema.org/PronounceableText
    Model depth: 6
    """
    valid_name: ClassVar[str] = "PronounceableText"
    type_: str = Field("PronounceableText", alias='@type')
    textValue: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Text value being annotated.",
    )
    phoneticText: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Representation of a text [[textValue]] using the specified [[speechToTextMarkup]]."
     "For example the city name of Houston in IPA: /ˈhjuːstən/.",
    )
    speechToTextMarkup: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Form of markup used. eg. [SSML](https://www.w3.org/TR/speech-synthesis11) or [IPA](https://www.wikidata.org/wiki/Property:P898).",
    )
    inLanguage: Optional[Union[List[Union[str, 'Text', 'Language']], str, 'Text', 'Language']] = Field(
        default=None,
        description="The language of the content or performance or used in an action. Please use one of the language"
     "codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also"
     "[[availableLanguage]].",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Language import Language


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
