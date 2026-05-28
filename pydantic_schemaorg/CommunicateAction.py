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
from pydantic_schemaorg.InteractAction import InteractAction


class CommunicateAction(InteractAction):
    """The act of conveying information to another person via a communication medium (instrument)"
     "such as speech, email, or telephone conversation.

    See: https://schema.org/CommunicateAction
    Model depth: 4
    """
    valid_name: ClassVar[str] = "CommunicateAction"
    type_: str = Field("CommunicateAction", alias='@type')
    about: Optional[Union[List[Union['Thing', str]], 'Thing', str]] = Field(
        default=None,
        description="The subject matter of the content.",
    )
    language: Optional[Union[List[Union['Language', str]], 'Language', str]] = Field(
        default=None,
        description="A sub property of instrument. The language used on this action.",
    )
    inLanguage: Optional[Union[List[Union[str, 'Text', 'Language']], str, 'Text', 'Language']] = Field(
        default=None,
        description="The language of the content or performance or used in an action. Please use one of the language"
     "codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also"
     "[[availableLanguage]].",
    )
    recipient: Optional[Union[List[Union['Audience', 'Person', 'ContactPoint', 'Organization', str]], 'Audience', 'Person', 'ContactPoint', 'Organization', str]] = Field(
        default=None,
        description="A sub property of participant. The participant who is at the receiving end of the action.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Thing import Thing
    from pydantic_schemaorg.Language import Language
    from pydantic_schemaorg.Text import Text
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
