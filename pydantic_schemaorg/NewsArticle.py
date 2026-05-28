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
from pydantic_schemaorg.Article import Article


class NewsArticle(Article):
    """A NewsArticle is an article whose content reports news, or provides background context"
     "and supporting materials for understanding the news. A more detailed overview of [schema.org"
     "News markup](/docs/news.html) is also available.

    See: https://schema.org/NewsArticle
    Model depth: 4
    """
    valid_name: ClassVar[str] = "NewsArticle"
    type_: str = Field("NewsArticle", alias='@type')
    printColumn: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The number of the column in which the NewsArticle appears in the print edition.",
    )
    printSection: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="If this NewsArticle appears in print, this field indicates the print section in which"
     "the article appeared.",
    )
    printPage: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="If this NewsArticle appears in print, this field indicates the name of the page on which"
     "the article is found. Please note that this field is intended for the exact page name (e.g."
     "A5, B18).",
    )
    printEdition: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The edition of the print product in which the NewsArticle appears.",
    )
    dateline: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="A [dateline](https://en.wikipedia.org/wiki/Dateline) is a brief piece of text included"
     "in news articles that describes where and when the story was written or filed though the"
     "date is often omitted. Sometimes only a placename is provided. Structured representations"
     "of dateline-related information can also be expressed more explicitly using [[locationCreated]]"
     "(which represents where a work was created, e.g. where a news report was written). For"
     "location depicted or described in the content, use [[contentLocation]]. Dateline"
     "summaries are oriented more towards human readers than towards automated processing,"
     "and can vary substantially. Some examples: \"BEIRUT, Lebanon, June 2.\", \"Paris,"
     "France\", \"December 19, 2017 11:43AM Reporting from Washington\", \"Beijing/Moscow\","
     "\"QUEZON CITY, Philippines\".",
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
