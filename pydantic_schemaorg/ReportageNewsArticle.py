from __future__ import annotations
from typing import ClassVar


from pydantic import Field
from pydantic_schemaorg.NewsArticle import NewsArticle


class ReportageNewsArticle(NewsArticle):
    """The [[ReportageNewsArticle]] type is a subtype of [[NewsArticle]] representing news"
     "articles which are the result of journalistic news reporting conventions. In practice"
     "many news publishers produce a wide variety of article types, many of which might be considered"
     "a [[NewsArticle]] but not a [[ReportageNewsArticle]]. For example, opinion pieces,"
     "reviews, analysis, sponsored or satirical articles, or articles that combine several"
     "of these elements. The [[ReportageNewsArticle]] type is based on a stricter ideal for"
     "\"news\" as a work of journalism, with articles based on factual information either"
     "observed or verified by the author, or reported and verified from knowledgeable sources."
     "This often includes perspectives from multiple viewpoints on a particular issue (distinguishing"
     "news reports from public relations or propaganda). News reports in the [[ReportageNewsArticle]]"
     "sense de-emphasize the opinion of the author, with commentary and value judgements"
     "typically expressed elsewhere. A [[ReportageNewsArticle]] which goes deeper into"
     "analysis can also be marked with an additional type of [[AnalysisNewsArticle]].

    See: https://schema.org/ReportageNewsArticle
    Model depth: 5
    """
    valid_name: ClassVar[str] = "ReportageNewsArticle"
    type_: str = Field("ReportageNewsArticle", alias='@type')
    



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
