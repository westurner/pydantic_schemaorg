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


class Article(CreativeWork):
    """An article, such as a news article or piece of investigative report. Newspapers and magazines"
     "have articles of many different types and this is intended to cover them all. See also"
     "[blog post](http://blog.schema.org/2014/09/schemaorg-support-for-bibliographic_2.html).

    See: https://schema.org/Article
    Model depth: 3
    """
    valid_name: ClassVar[str] = "Article"
    type_: str = Field("Article", alias='@type')
    pageStart: Optional[Union[List[Union[int, 'Integer', str, 'Text']], int, 'Integer', str, 'Text']] = Field(
        default=None,
        description="The page on which the work starts; for example \"135\" or \"xiii\".",
    )
    wordCount: Optional[Union[List[Union[int, 'Integer', str]], int, 'Integer', str]] = Field(
        default=None,
        description="The number of words in the text of the CreativeWork such as an Article, Book, etc.",
    )
    pagination: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Any description of pages that is not separated into pageStart and pageEnd; for example,"
     "\"1-6, 9, 55\" or \"10-12, 46-49\".",
    )
    pageEnd: Optional[Union[List[Union[int, 'Integer', str, 'Text']], int, 'Integer', str, 'Text']] = Field(
        default=None,
        description="The page on which the work ends; for example \"138\" or \"xvi\".",
    )
    speakable: Optional[Union[List[Union[AnyUrl, 'URL', 'SpeakableSpecification', str]], AnyUrl, 'URL', 'SpeakableSpecification', str]] = Field(
        default=None,
        description="Indicates sections of a Web page that are particularly 'speakable' in the sense of being"
     "highlighted as being especially appropriate for text-to-speech conversion. Other"
     "sections of a page may also be usefully spoken in particular circumstances; the 'speakable'"
     "property serves to indicate the parts most likely to be generally useful for speech."
     "The *speakable* property can be repeated an arbitrary number of times, with three kinds"
     "of possible 'content-locator' values: 1.) *id-value* URL references - uses *id-value*"
     "of an element in the page being annotated. The simplest use of *speakable* has (potentially"
     "relative) URL values, referencing identified sections of the document concerned."
     "2.) CSS Selectors - addresses content in the annotated page, e.g. via class attribute."
     "Use the [[cssSelector]] property. 3.) XPaths - addresses content via XPaths (assuming"
     "an XML view of the content). Use the [[xpath]] property. For more sophisticated markup"
     "of speakable sections beyond simple ID references, either CSS selectors or XPath expressions"
     "to pick out document section(s) as speakable. For this we define a supporting type, [[SpeakableSpecification]]"
     "which is defined to be a possible value of the *speakable* property.",
    )
    backstory: Optional[Union[List[Union[str, 'Text', 'CreativeWork']], str, 'Text', 'CreativeWork']] = Field(
        default=None,
        description="For an [[Article]], typically a [[NewsArticle]], the backstory property provides"
     "a textual summary giving a brief explanation of why and how an article was created. In"
     "a journalistic setting this could include information about reporting process, methods,"
     "interviews, data sources, etc.",
    )
    articleSection: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Articles may belong to one or more 'sections' in a magazine or newspaper, such as Sports,"
     "Lifestyle, etc.",
    )
    articleBody: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The actual body of the article.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Integer import Integer
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.SpeakableSpecification import SpeakableSpecification
    from pydantic_schemaorg.CreativeWork import CreativeWork


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
