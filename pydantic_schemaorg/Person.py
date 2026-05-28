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
from datetime import date


from pydantic import Field
from pydantic_schemaorg.Thing import Thing


class Person(Thing):
    """A person (alive, dead, undead, or fictional).

    See: https://schema.org/Person
    Model depth: 2
    """
    valid_name: ClassVar[str] = "Person"
    type_: str = Field("Person", alias='@type')
    jobTitle: Optional[Union[List[Union[str, 'Text', 'DefinedTerm']], str, 'Text', 'DefinedTerm']] = Field(
        default=None,
        description="The job title of the person (for example, Financial Manager).",
    )
    award: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="An award won by or for this item.",
    )
    isicV4: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The International Standard of Industrial Classification of All Economic Activities"
     "(ISIC), Revision 4 code for a particular organization, business person, or place.",
    )
    agentInteractionStatistic: Optional[Union[List[Union['InteractionCounter', str]], 'InteractionCounter', str]] = Field(
        default=None,
        description="The number of completed interactions for this entity, in a particular role (the 'agent'),"
     "in a particular action (indicated in the statistic), and in a particular context (i.e."
     "interactionService).",
    )
    duns: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The Dun & Bradstreet DUNS number for identifying an organization or business person.",
    )
    colleague: Optional[Union[List[Union[AnyUrl, 'URL', 'Person', str]], AnyUrl, 'URL', 'Person', str]] = Field(
        default=None,
        description="A colleague of the person.",
    )
    additionalName: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="An additional name for a Person, can be used for a middle name.",
    )
    email: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Email address.",
    )
    parents: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="A parents of the person.",
    )
    parent: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="A parent of this person.",
    )
    gender: Optional[Union[List[Union[str, 'Text', 'GenderType']], str, 'Text', 'GenderType']] = Field(
        default=None,
        description="Gender of something, typically a [[Person]], but possibly also fictional characters,"
     "animals, etc. While https://schema.org/Male and https://schema.org/Female may"
     "be used, text strings are also acceptable for people who are not a binary gender. The [[gender]]"
     "property can also be used in an extended sense to cover e.g. the gender of sports teams."
     "As with the gender of individuals, we do not try to enumerate all possibilities. A mixed-gender"
     "[[SportsTeam]] can be indicated with a text value of \"Mixed\".",
    )
    publishingPrinciples: Optional[Union[List[Union[AnyUrl, 'URL', 'CreativeWork', str]], AnyUrl, 'URL', 'CreativeWork', str]] = Field(
        default=None,
        description="The publishingPrinciples property indicates (typically via [[URL]]) a document describing"
     "the editorial principles of an [[Organization]] (or individual, e.g. a [[Person]]"
     "writing a blog) that relate to their activities as a publisher, e.g. ethics or diversity"
     "policies. When applied to a [[CreativeWork]] (e.g. [[NewsArticle]]) the principles"
     "are those of the party primarily responsible for the creation of the [[CreativeWork]]."
     "While such policies are most typically expressed in natural language, sometimes related"
     "information (e.g. indicating a [[funder]]) can be expressed using schema.org terminology.",
    )
    colleagues: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="A colleague of the person.",
    )
    funding: Optional[Union[List[Union['Grant', str]], 'Grant', str]] = Field(
        default=None,
        description="A [[Grant]] that directly or indirectly provide funding or sponsorship for this item."
     "See also [[ownershipFundingInfo]].",
    )
    memberOf: Optional[Union[List[Union['Organization', 'ProgramMembership', 'MemberProgramTier', str]], 'Organization', 'ProgramMembership', 'MemberProgramTier', str]] = Field(
        default=None,
        description="An Organization (or ProgramMembership) to which this Person or Organization belongs.",
    )
    worksFor: Optional[Union[List[Union['Organization', str]], 'Organization', str]] = Field(
        default=None,
        description="Organizations that the person works for.",
    )
    height: Optional[Union[List[Union['QuantitativeValue', 'Distance', str]], 'QuantitativeValue', 'Distance', str]] = Field(
        default=None,
        description="The height of the item.",
    )
    skills: Optional[Union[List[Union[str, 'Text', 'DefinedTerm']], str, 'Text', 'DefinedTerm']] = Field(
        default=None,
        description="A statement of knowledge, skill, ability, task or any other assertion expressing a competency"
     "that is either claimed by a person, an organization or desired or required to fulfill"
     "a role or to work in an occupation.",
    )
    givenName: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Given name. In the U.S., the first name of a Person.",
    )
    naics: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The North American Industry Classification System (NAICS) code for a particular organization"
     "or business person.",
    )
    awards: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Awards won by or for this item.",
    )
    interactionStatistic: Optional[Union[List[Union['InteractionCounter', str]], 'InteractionCounter', str]] = Field(
        default=None,
        description="The number of interactions for the CreativeWork using the WebSite or SoftwareApplication."
     "The most specific child type of InteractionCounter should be used.",
    )
    telephone: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The telephone number.",
    )
    netWorth: Optional[Union[List[Union['PriceSpecification', 'MonetaryAmount', str]], 'PriceSpecification', 'MonetaryAmount', str]] = Field(
        default=None,
        description="The total financial value of the person as calculated by subtracting the total value"
     "of liabilities from the total value of assets.",
    )
    deathDate: Optional[Union[List[Union[date, 'Date', str]], date, 'Date', str]] = Field(
        default=None,
        description="Date of death.",
    )
    affiliation: Optional[Union[List[Union['Organization', str]], 'Organization', str]] = Field(
        default=None,
        description="An organization that this person is affiliated with. For example, a school/university,"
     "a club, or a team.",
    )
    workLocation: Optional[Union[List[Union['Place', 'ContactPoint', str]], 'Place', 'ContactPoint', str]] = Field(
        default=None,
        description="A contact location for a person's place of work.",
    )
    siblings: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="A sibling of the person.",
    )
    knowsAbout: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'Thing']], AnyUrl, 'URL', str, 'Text', 'Thing']] = Field(
        default=None,
        description="Of a [[Person]], and less typically of an [[Organization]], to indicate a topic that"
     "is known about - suggesting possible expertise but not implying it. We do not distinguish"
     "skill levels here, or relate this to educational content, events, objectives or [[JobPosting]]"
     "descriptions.",
    )
    pronouns: Optional[Union[List[Union[str, 'Text', 'DefinedTerm', 'StructuredValue']], str, 'Text', 'DefinedTerm', 'StructuredValue']] = Field(
        default=None,
        description="A short string listing or describing pronouns for a person. Typically the person concerned"
     "is the best authority as pronouns are a critical part of personal identity and expression."
     "Publishers and consumers of this information are reminded to treat this data responsibly,"
     "take country-specific laws related to gender expression into account, and be wary of"
     "out-of-date data and drawing unwarranted inferences about the person being described."
     "In English, formulations such as \"they/them\", \"she/her\", and \"he/him\" are commonly"
     "used online and can also be used here. We do not intend to enumerate all possible micro-syntaxes"
     "in all languages. More structured and well-defined external values for pronouns can"
     "be referenced using the [[StructuredValue]] or [[DefinedTerm]] values.",
    )
    address: Optional[Union[List[Union[str, 'Text', 'PostalAddress']], str, 'Text', 'PostalAddress']] = Field(
        default=None,
        description="Physical address of the item.",
    )
    performerIn: Optional[Union[List[Union['Event', str]], 'Event', str]] = Field(
        default=None,
        description="Event that this person is a performer or participant in.",
    )
    contactPoints: Optional[Union[List[Union['ContactPoint', str]], 'ContactPoint', str]] = Field(
        default=None,
        description="A contact point for a person or organization.",
    )
    hasPOS: Optional[Union[List[Union['Place', str]], 'Place', str]] = Field(
        default=None,
        description="Points-of-Sales operated by the organization or person.",
    )
    globalLocationNumber: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The [Global Location Number](http://www.gs1.org/gln) (GLN, sometimes also referred"
     "to as International Location Number or ILN) of the respective organization, person,"
     "or place. The GLN is a 13-digit number used to identify parties and physical locations.",
    )
    taxID: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The Tax / Fiscal ID of the organization or person, e.g. the TIN in the US or the CIF/NIF in"
     "Spain.",
    )
    children: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="A child of the person.",
    )
    makesOffer: Optional[Union[List[Union['Offer', str]], 'Offer', str]] = Field(
        default=None,
        description="A pointer to products or services offered by the organization or person.",
    )
    hasOccupation: Optional[Union[List[Union['Occupation', str]], 'Occupation', str]] = Field(
        default=None,
        description="The Person's occupation. For past professions, use Role for expressing dates.",
    )
    contactPoint: Optional[Union[List[Union['ContactPoint', str]], 'ContactPoint', str]] = Field(
        default=None,
        description="A contact point for a person or organization.",
    )
    birthPlace: Optional[Union[List[Union['Place', str]], 'Place', str]] = Field(
        default=None,
        description="The place where the person was born.",
    )
    sibling: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="A sibling of the person.",
    )
    vatID: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The Value-added Tax ID of the organization or person.",
    )
    seeks: Optional[Union[List[Union['Demand', str]], 'Demand', str]] = Field(
        default=None,
        description="A pointer to products or services sought by the organization or person (demand).",
    )
    sponsor: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="A person or organization that supports a thing through a pledge, promise, or financial"
     "contribution. E.g. a sponsor of a Medical Study or a corporate sponsor of an event.",
    )
    relatedTo: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="The most generic familial relation.",
    )
    knows: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="The most generic bi-directional social/work relation.",
    )
    spouse: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="The person's spouse.",
    )
    honorificSuffix: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="An honorific suffix following a Person's name such as M.D./PhD/MSCSW.",
    )
    nationality: Optional[Union[List[Union['Country', str]], 'Country', str]] = Field(
        default=None,
        description="Nationality of the person.",
    )
    funder: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="A person or organization that supports (sponsors) something through some kind of financial"
     "contribution.",
    )
    birthDate: Optional[Union[List[Union[date, 'Date', str]], date, 'Date', str]] = Field(
        default=None,
        description="Date of birth.",
    )
    owns: Optional[Union[List[Union['Product', 'OwnershipInfo', str]], 'Product', 'OwnershipInfo', str]] = Field(
        default=None,
        description="Products owned by the organization or person.",
    )
    alumniOf: Optional[Union[List[Union['EducationalOrganization', 'Organization', str]], 'EducationalOrganization', 'Organization', str]] = Field(
        default=None,
        description="An organization that the person is an alumni of.",
    )
    weight: Optional[Union[List[Union['QuantitativeValue', 'Mass', str]], 'QuantitativeValue', 'Mass', str]] = Field(
        default=None,
        description="The weight of the product or person.",
    )
    faxNumber: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The fax number.",
    )
    hasCredential: Optional[Union[List[Union['EducationalOccupationalCredential', str]], 'EducationalOccupationalCredential', str]] = Field(
        default=None,
        description="A credential awarded to the Person or Organization.",
    )
    follows: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="The most generic uni-directional social relation.",
    )
    familyName: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Family name. In the U.S., the last name of a Person.",
    )
    callSign: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="A [callsign](https://en.wikipedia.org/wiki/Call_sign), as used in broadcasting"
     "and radio communications to identify people, radio and TV stations, or vehicles.",
    )
    hasCertification: Optional[Union[List[Union['Certification', str]], 'Certification', str]] = Field(
        default=None,
        description="Certification information about a product, organization, service, place, or person.",
    )
    brand: Optional[Union[List[Union['Brand', 'Organization', str]], 'Brand', 'Organization', str]] = Field(
        default=None,
        description="The brand(s) associated with a product or service, or the brand(s) maintained by an organization"
     "or business person.",
    )
    knowsLanguage: Optional[Union[List[Union[str, 'Text', 'Language']], str, 'Text', 'Language']] = Field(
        default=None,
        description="Of a [[Person]], and less typically of an [[Organization]], to indicate a known language."
     "We do not distinguish skill levels or reading/writing/speaking/signing here. Use"
     "language codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47).",
    )
    hasOfferCatalog: Optional[Union[List[Union['OfferCatalog', str]], 'OfferCatalog', str]] = Field(
        default=None,
        description="Indicates an OfferCatalog listing for this Organization, Person, or Service.",
    )
    honorificPrefix: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="An honorific prefix preceding a Person's name such as Dr/Mrs/Mr.",
    )
    deathPlace: Optional[Union[List[Union['Place', str]], 'Place', str]] = Field(
        default=None,
        description="The place where the person died.",
    )
    homeLocation: Optional[Union[List[Union['Place', 'ContactPoint', str]], 'Place', 'ContactPoint', str]] = Field(
        default=None,
        description="A contact location for a person's residence.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.DefinedTerm import DefinedTerm
    from pydantic_schemaorg.InteractionCounter import InteractionCounter
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.GenderType import GenderType
    from pydantic_schemaorg.CreativeWork import CreativeWork
    from pydantic_schemaorg.Grant import Grant
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.ProgramMembership import ProgramMembership
    from pydantic_schemaorg.MemberProgramTier import MemberProgramTier
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.Distance import Distance
    from pydantic_schemaorg.PriceSpecification import PriceSpecification
    from pydantic_schemaorg.MonetaryAmount import MonetaryAmount
    from pydantic_schemaorg.Date import Date
    from pydantic_schemaorg.Place import Place
    from pydantic_schemaorg.ContactPoint import ContactPoint
    from pydantic_schemaorg.Thing import Thing
    from pydantic_schemaorg.StructuredValue import StructuredValue
    from pydantic_schemaorg.PostalAddress import PostalAddress
    from pydantic_schemaorg.Event import Event
    from pydantic_schemaorg.Offer import Offer
    from pydantic_schemaorg.Occupation import Occupation
    from pydantic_schemaorg.Demand import Demand
    from pydantic_schemaorg.Country import Country
    from pydantic_schemaorg.Product import Product
    from pydantic_schemaorg.OwnershipInfo import OwnershipInfo
    from pydantic_schemaorg.EducationalOrganization import EducationalOrganization
    from pydantic_schemaorg.Mass import Mass
    from pydantic_schemaorg.EducationalOccupationalCredential import EducationalOccupationalCredential
    from pydantic_schemaorg.Certification import Certification
    from pydantic_schemaorg.Brand import Brand
    from pydantic_schemaorg.Language import Language
    from pydantic_schemaorg.OfferCatalog import OfferCatalog


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
