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
from datetime import date


from pydantic import Field
from pydantic_schemaorg.Thing import Thing


class Organization(Thing):
    """An organization such as a school, NGO, corporation, club, etc.

    See: https://schema.org/Organization
    Model depth: 2
    """
    valid_name: ClassVar[str] = "Organization"
    type_: str = Field("Organization", alias='@type')
    member: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="A member of an Organization or a ProgramMembership. Organizations can be members of"
     "organizations; ProgramMembership is typically for individuals.",
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
    serviceArea: Optional[Union[List[Union['Place', 'GeoShape', 'AdministrativeArea', str]], 'Place', 'GeoShape', 'AdministrativeArea', str]] = Field(
        default=None,
        description="The geographic area where the service is provided.",
    )
    alumni: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="Alumni of an organization.",
    )
    diversityPolicy: Optional[Union[List[Union[AnyUrl, 'URL', 'CreativeWork', str]], AnyUrl, 'URL', 'CreativeWork', str]] = Field(
        default=None,
        description="Statement on diversity policy by an [[Organization]] e.g. a [[NewsMediaOrganization]]."
     "For a [[NewsMediaOrganization]], a statement describing the newsroom’s diversity"
     "policy on both staffing and sources, typically providing staffing data.",
    )
    reviews: Optional[Union[List[Union['Review', str]], 'Review', str]] = Field(
        default=None,
        description="Review of the item.",
    )
    duns: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The Dun & Bradstreet DUNS number for identifying an organization or business person.",
    )
    review: Optional[Union[List[Union['Review', str]], 'Review', str]] = Field(
        default=None,
        description="A review of the item.",
    )
    members: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="A member of this organization.",
    )
    email: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Email address.",
    )
    keywords: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'DefinedTerm']], AnyUrl, 'URL', str, 'Text', 'DefinedTerm']] = Field(
        default=None,
        description="Keywords or tags used to describe some item. Multiple textual entries in a keywords list"
     "are typically delimited by commas, or by repeating the property.",
    )
    founders: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="A person who founded this organization.",
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
    unnamedSourcesPolicy: Optional[Union[List[Union[AnyUrl, 'URL', 'CreativeWork', str]], AnyUrl, 'URL', 'CreativeWork', str]] = Field(
        default=None,
        description="For an [[Organization]] (typically a [[NewsMediaOrganization]]), a statement about"
     "policy on use of unnamed sources and the decision process required.",
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
    dissolutionDate: Optional[Union[List[Union[date, 'Date', str]], date, 'Date', str]] = Field(
        default=None,
        description="The date that this organization was dissolved.",
    )
    hasShippingService: Optional[Union[List[Union['ShippingService', str]], 'ShippingService', str]] = Field(
        default=None,
        description="Specification of a shipping service offered by the organization.",
    )
    skills: Optional[Union[List[Union[str, 'Text', 'DefinedTerm']], str, 'Text', 'DefinedTerm']] = Field(
        default=None,
        description="A statement of knowledge, skill, ability, task or any other assertion expressing a competency"
     "that is either claimed by a person, an organization or desired or required to fulfill"
     "a role or to work in an occupation.",
    )
    nonprofitStatus: Optional[Union[List[Union['NonprofitType', str]], 'NonprofitType', str]] = Field(
        default=None,
        description="nonprofitStatus indicates the legal status of a non-profit organization in its primary"
     "place of business.",
    )
    employee: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="Someone working for this organization.",
    )
    founder: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="A person or organization who founded this organization.",
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
    legalRepresentative: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="One or multiple persons who represent this organization legally such as CEO or sole administrator.",
    )
    actionableFeedbackPolicy: Optional[Union[List[Union[AnyUrl, 'URL', 'CreativeWork', str]], AnyUrl, 'URL', 'CreativeWork', str]] = Field(
        default=None,
        description="For a [[NewsMediaOrganization]] or other news-related [[Organization]], a statement"
     "about public engagement activities (for news media, the newsroom’s), including involving"
     "the public - digitally or otherwise -- in coverage decisions, reporting and activities"
     "after publication.",
    )
    event: Optional[Union[List[Union['Event', str]], 'Event', str]] = Field(
        default=None,
        description="Upcoming or past event associated with this place, organization, or action.",
    )
    ownershipFundingInfo: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'CreativeWork', 'AboutPage']], AnyUrl, 'URL', str, 'Text', 'CreativeWork', 'AboutPage']] = Field(
        default=None,
        description="For an [[Organization]] (often but not necessarily a [[NewsMediaOrganization]]),"
     "a description of organizational ownership structure; funding and grants. In a news/media"
     "setting, this is with particular reference to editorial independence. Note that the"
     "[[funder]] is also available and can be used to make basic funder information machine-readable.",
    )
    foundingDate: Optional[Union[List[Union[date, 'Date', str]], date, 'Date', str]] = Field(
        default=None,
        description="The date that this organization was founded.",
    )
    legalName: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The official name of the organization, e.g. the registered company name.",
    )
    knowsAbout: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'Thing']], AnyUrl, 'URL', str, 'Text', 'Thing']] = Field(
        default=None,
        description="Of a [[Person]], and less typically of an [[Organization]], to indicate a topic that"
     "is known about - suggesting possible expertise but not implying it. We do not distinguish"
     "skill levels here, or relate this to educational content, events, objectives or [[JobPosting]]"
     "descriptions.",
    )
    areaServed: Optional[Union[List[Union[str, 'Text', 'Place', 'GeoShape', 'AdministrativeArea']], str, 'Text', 'Place', 'GeoShape', 'AdministrativeArea']] = Field(
        default=None,
        description="The geographic area where a service or offered item is provided.",
    )
    iso6523Code: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="An organization identifier as defined in [ISO 6523(-1)](https://en.wikipedia.org/wiki/ISO/IEC_6523)."
     "The identifier should be in the `XXXX:YYYYYY:ZZZ` or `XXXX:YYYYYY`format. Where `XXXX`"
     "is a 4 digit _ICD_ (International Code Designator), `YYYYYY` is an _OID_ (Organization"
     "Identifier) with all formatting characters (dots, dashes, spaces) removed with a maximal"
     "length of 35 characters, and `ZZZ` is an optional OPI (Organization Part Identifier)"
     "with a maximum length of 35 characters. The various components (ICD, OID, OPI) are joined"
     "with a colon character (ASCII `0x3a`). Note that many existing organization identifiers"
     "defined as attributes like [leiCode](https://schema.org/leiCode) (`0199`), [duns](https://schema.org/duns)"
     "(`0060`) or [GLN](https://schema.org/globalLocationNumber) (`0088`) can be expressed"
     "using ISO-6523. If possible, ISO-6523 codes should be preferred to populating [vatID](https://schema.org/vatID)"
     "or [taxID](https://schema.org/taxID), as ISO identifiers are less ambiguous.",
    )
    employees: Optional[Union[List[Union['Person', str]], 'Person', str]] = Field(
        default=None,
        description="People working for this organization.",
    )
    numberOfEmployees: Optional[Union[List[Union['QuantitativeValue', str]], 'QuantitativeValue', str]] = Field(
        default=None,
        description="The number of employees in an organization, e.g. business.",
    )
    foundingLocation: Optional[Union[List[Union['Place', str]], 'Place', str]] = Field(
        default=None,
        description="The place where the Organization was founded.",
    )
    address: Optional[Union[List[Union[str, 'Text', 'PostalAddress']], str, 'Text', 'PostalAddress']] = Field(
        default=None,
        description="Physical address of the item.",
    )
    contactPoints: Optional[Union[List[Union['ContactPoint', str]], 'ContactPoint', str]] = Field(
        default=None,
        description="A contact point for a person or organization.",
    )
    events: Optional[Union[List[Union['Event', str]], 'Event', str]] = Field(
        default=None,
        description="Upcoming or past events associated with this place or organization.",
    )
    department: Optional[Union[List[Union['Organization', str]], 'Organization', str]] = Field(
        default=None,
        description="A relationship between an organization and a department of that organization, also"
     "described as an organization (allowing different urls, logos, opening hours). For"
     "example: a store with a pharmacy, or a bakery with a cafe.",
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
    leiCode: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="An organization identifier that uniquely identifies a legal entity as defined in ISO"
     "17442.",
    )
    taxID: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The Tax / Fiscal ID of the organization or person, e.g. the TIN in the US or the CIF/NIF in"
     "Spain.",
    )
    hasMerchantReturnPolicy: Optional[Union[List[Union['MerchantReturnPolicy', str]], 'MerchantReturnPolicy', str]] = Field(
        default=None,
        description="Specifies a MerchantReturnPolicy that may be applicable.",
    )
    legalAddress: Optional[Union[List[Union['PostalAddress', str]], 'PostalAddress', str]] = Field(
        default=None,
        description="The legal address of an organization which acts as the officially registered address"
     "used for legal and tax purposes. The legal address can be different from the place of operations"
     "of a business and other addresses can be part of an organization.",
    )
    correctionsPolicy: Optional[Union[List[Union[AnyUrl, 'URL', 'CreativeWork', str]], AnyUrl, 'URL', 'CreativeWork', str]] = Field(
        default=None,
        description="For an [[Organization]] (e.g. [[NewsMediaOrganization]]), a statement describing"
     "(in news media, the newsroom’s) disclosure and correction policy for errors.",
    )
    hasGS1DigitalLink: Optional[Union[List[Union[AnyUrl, 'URL', str]], AnyUrl, 'URL', str]] = Field(
        default=None,
        description="The <a href=\"https://www.gs1.org/standards/gs1-digital-link\">GS1 digital"
     "link</a> associated with the object. This URL should conform to the particular requirements"
     "of digital links. The link should only contain the Application Identifiers (AIs) that"
     "are relevant for the entity being annotated, for instance a [[Product]] or an [[Organization]],"
     "and for the correct granularity. In particular, for products:<ul><li>A Digital Link"
     "that contains a serial number (AI <code>21</code>) should only be present on instances"
     "of [[IndividualProduct]]</li><li>A Digital Link that contains a lot number (AI <code>10</code>)"
     "should be annotated as [[SomeProduct]] if only products from that lot are sold, or [[IndividualProduct]]"
     "if there is only a specific product.</li><li>A Digital Link that contains a global model"
     "number (AI <code>8013</code>) should be attached to a [[Product]] or a [[ProductModel]].</li></ul>"
     "Other item types should be adapted similarly.",
    )
    makesOffer: Optional[Union[List[Union['Offer', str]], 'Offer', str]] = Field(
        default=None,
        description="A pointer to products or services offered by the organization or person.",
    )
    parentOrganization: Optional[Union[List[Union['Organization', str]], 'Organization', str]] = Field(
        default=None,
        description="The larger organization that this organization is a [[subOrganization]] of, if any.",
    )
    hasMemberProgram: Optional[Union[List[Union['MemberProgram', str]], 'MemberProgram', str]] = Field(
        default=None,
        description="MemberProgram offered by an Organization, for example an eCommerce merchant or an airline.",
    )
    slogan: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="A slogan or motto associated with the item.",
    )
    contactPoint: Optional[Union[List[Union['ContactPoint', str]], 'ContactPoint', str]] = Field(
        default=None,
        description="A contact point for a person or organization.",
    )
    location: Optional[Union[List[Union[str, 'Text', 'VirtualLocation', 'PostalAddress', 'Place']], str, 'Text', 'VirtualLocation', 'PostalAddress', 'Place']] = Field(
        default=None,
        description="The location of, for example, where an event is happening, where an organization is located,"
     "or where an action takes place.",
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
    funder: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="A person or organization that supports (sponsors) something through some kind of financial"
     "contribution.",
    )
    diversityStaffingReport: Optional[Union[List[Union[AnyUrl, 'URL', 'Article', str]], AnyUrl, 'URL', 'Article', str]] = Field(
        default=None,
        description="For an [[Organization]] (often but not necessarily a [[NewsMediaOrganization]]),"
     "a report on staffing diversity issues. In a news context this might be for example ASNE"
     "or RTDNA (US) reports, or self-reported.",
    )
    companyRegistration: Optional[Union[List[Union['Certification', str]], 'Certification', str]] = Field(
        default=None,
        description="The official registration number of a business including the organization that issued"
     "it such as Company House or Chamber of Commerce.",
    )
    subOrganization: Optional[Union[List[Union['Organization', str]], 'Organization', str]] = Field(
        default=None,
        description="A relationship between two organizations where the first includes the second, e.g.,"
     "as a subsidiary. See also: the more specific 'department' property.",
    )
    owns: Optional[Union[List[Union['Product', 'OwnershipInfo', str]], 'Product', 'OwnershipInfo', str]] = Field(
        default=None,
        description="Products owned by the organization or person.",
    )
    logo: Optional[Union[List[Union[AnyUrl, 'URL', 'ImageObject', str]], AnyUrl, 'URL', 'ImageObject', str]] = Field(
        default=None,
        description="An associated logo.",
    )
    acceptedPaymentMethod: Optional[Union[List[Union[str, 'Text', 'LoanOrCredit', 'PaymentMethod']], str, 'Text', 'LoanOrCredit', 'PaymentMethod']] = Field(
        default=None,
        description="The payment method(s) that are accepted in general by an organization, or for some specific"
     "demand or offer.",
    )
    faxNumber: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The fax number.",
    )
    ethicsPolicy: Optional[Union[List[Union[AnyUrl, 'URL', 'CreativeWork', str]], AnyUrl, 'URL', 'CreativeWork', str]] = Field(
        default=None,
        description="Statement about ethics policy, e.g. of a [[NewsMediaOrganization]] regarding journalistic"
     "and publishing practices, or of a [[Restaurant]], a page describing food source policies."
     "In the case of a [[NewsMediaOrganization]], an ethicsPolicy is typically a statement"
     "describing the personal, organizational, and corporate standards of behavior expected"
     "by the organization.",
    )
    hasCredential: Optional[Union[List[Union['EducationalOccupationalCredential', str]], 'EducationalOccupationalCredential', str]] = Field(
        default=None,
        description="A credential awarded to the Person or Organization.",
    )
    aggregateRating: Optional[Union[List[Union['AggregateRating', str]], 'AggregateRating', str]] = Field(
        default=None,
        description="The overall rating, based on a collection of reviews or ratings, of the item.",
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
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.InteractionCounter import InteractionCounter
    from pydantic_schemaorg.Place import Place
    from pydantic_schemaorg.GeoShape import GeoShape
    from pydantic_schemaorg.AdministrativeArea import AdministrativeArea
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.CreativeWork import CreativeWork
    from pydantic_schemaorg.Review import Review
    from pydantic_schemaorg.DefinedTerm import DefinedTerm
    from pydantic_schemaorg.Grant import Grant
    from pydantic_schemaorg.ProgramMembership import ProgramMembership
    from pydantic_schemaorg.MemberProgramTier import MemberProgramTier
    from pydantic_schemaorg.Date import Date
    from pydantic_schemaorg.ShippingService import ShippingService
    from pydantic_schemaorg.NonprofitType import NonprofitType
    from pydantic_schemaorg.Event import Event
    from pydantic_schemaorg.AboutPage import AboutPage
    from pydantic_schemaorg.Thing import Thing
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.PostalAddress import PostalAddress
    from pydantic_schemaorg.ContactPoint import ContactPoint
    from pydantic_schemaorg.MerchantReturnPolicy import MerchantReturnPolicy
    from pydantic_schemaorg.Offer import Offer
    from pydantic_schemaorg.MemberProgram import MemberProgram
    from pydantic_schemaorg.VirtualLocation import VirtualLocation
    from pydantic_schemaorg.Demand import Demand
    from pydantic_schemaorg.Article import Article
    from pydantic_schemaorg.Certification import Certification
    from pydantic_schemaorg.Product import Product
    from pydantic_schemaorg.OwnershipInfo import OwnershipInfo
    from pydantic_schemaorg.ImageObject import ImageObject
    from pydantic_schemaorg.LoanOrCredit import LoanOrCredit
    from pydantic_schemaorg.PaymentMethod import PaymentMethod
    from pydantic_schemaorg.EducationalOccupationalCredential import EducationalOccupationalCredential
    from pydantic_schemaorg.AggregateRating import AggregateRating
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
