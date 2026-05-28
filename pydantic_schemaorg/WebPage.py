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
from datetime import date, datetime


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class WebPage(CreativeWork):
    """A web page. Every web page is implicitly assumed to be declared to be of type WebPage, so"
     "the various properties about that webpage, such as <code>breadcrumb</code> may be"
     "used. We recommend explicit declaration if these properties are specified, but if they"
     "are found outside of an itemscope, they will be assumed to be about the page.

    See: https://schema.org/WebPage
    Model depth: 3
    """
    valid_name: ClassVar[str] = "WebPage"
    type_: str = Field("WebPage", alias='@type')
    mainContentOfPage: Optional[Union[List[Union['WebPageElement', str]], 'WebPageElement', str]] = Field(
        default=None,
        description="Indicates if this web page element is the main subject of the page.",
    )
    specialty: Optional[Union[List[Union['Specialty', str]], 'Specialty', str]] = Field(
        default=None,
        description="One of the domain specialities to which this web page's content applies.",
    )
    significantLink: Optional[Union[List[Union[AnyUrl, 'URL', str]], AnyUrl, 'URL', str]] = Field(
        default=None,
        description="One of the more significant URLs on the page. Typically, these are the non-navigation"
     "links that are clicked on the most.",
    )
    relatedLink: Optional[Union[List[Union[AnyUrl, 'URL', str]], AnyUrl, 'URL', str]] = Field(
        default=None,
        description="A link related to this web page, for example to other related web pages.",
    )
    primaryImageOfPage: Optional[Union[List[Union['ImageObject', str]], 'ImageObject', str]] = Field(
        default=None,
        description="Indicates the main image on the page.",
    )
    significantLinks: Optional[Union[List[Union[AnyUrl, 'URL', str]], AnyUrl, 'URL', str]] = Field(
        default=None,
        description="The most significant URLs on the page. Typically, these are the non-navigation links"
     "that are clicked on the most.",
    )
    breadcrumb: Optional[Union[List[Union[str, 'Text', 'BreadcrumbList']], str, 'Text', 'BreadcrumbList']] = Field(
        default=None,
        description="A set of links that can help a user understand and navigate a website hierarchy.",
    )
    reviewedBy: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="People or organizations that have reviewed the content on this web page for accuracy"
     "and/or completeness.",
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
    lastReviewed: Optional[Union[List[Union[date, 'Date', str]], date, 'Date', str]] = Field(
        default=None,
        description="Date on which the content on this web page was last reviewed for accuracy and/or completeness.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.WebPageElement import WebPageElement
    from pydantic_schemaorg.Specialty import Specialty
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.ImageObject import ImageObject
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.BreadcrumbList import BreadcrumbList
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.SpeakableSpecification import SpeakableSpecification
    from pydantic_schemaorg.Date import Date


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
