from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from typing import List, Optional, Union
from datetime import date, datetime
from pydantic import AnyUrl, StrictInt, StrictFloat


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class EducationalOccupationalProgram(Intangible):
    """A program offered by an institution which determines the learning progress to achieve"
     "an outcome, usually a credential like a degree or certificate. This would define a discrete"
     "set of opportunities (e.g., job, courses) that together constitute a program with a"
     "clear start, end, set of requirements, and transition to a new occupational opportunity"
     "(e.g., a job), or sometimes a higher educational opportunity (e.g., an advanced degree).

    See: https://schema.org/EducationalOccupationalProgram
    Model depth: 3
    """
    valid_name: ClassVar[str] = "EducationalOccupationalProgram"
    type_: str = Field("EducationalOccupationalProgram", alias='@type')
    termDuration: Optional[Union[List[Union['Duration', str]], 'Duration', str]] = Field(
        default=None,
        description="The amount of time in a term as defined by the institution. A term is a length of time where"
     "students take one or more classes. Semesters and quarters are common units for term.",
    )
    numberOfCredits: Optional[Union[List[Union[int, 'Integer', 'StructuredValue', str]], int, 'Integer', 'StructuredValue', str]] = Field(
        default=None,
        description="The number of credits or units awarded by a Course or required to complete an EducationalOccupationalProgram.",
    )
    applicationStartDate: Optional[Union[List[Union[date, 'Date', str]], date, 'Date', str]] = Field(
        default=None,
        description="The date at which the program begins collecting applications for the next enrollment"
     "cycle.",
    )
    offers: Optional[Union[List[Union['Demand', 'Offer', str]], 'Demand', 'Offer', str]] = Field(
        default=None,
        description="An offer to provide this item&#x2014;for example, an offer to sell a product, rent the"
     "DVD of a movie, perform a service, or give away tickets to an event. Use [[businessFunction]]"
     "to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can"
     "also be used to describe a [[Demand]]. While this property is listed as expected on a number"
     "of common types, it can be used in others. In that case, using a second type, such as Product"
     "or a subtype of Product, can clarify the nature of the offer.",
    )
    educationalCredentialAwarded: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'EducationalOccupationalCredential']], AnyUrl, 'URL', str, 'Text', 'EducationalOccupationalCredential']] = Field(
        default=None,
        description="A description of the qualification, award, certificate, diploma or other educational"
     "credential awarded as a consequence of successful completion of this course or program.",
    )
    dayOfWeek: Optional[Union[List[Union['DayOfWeek', str]], 'DayOfWeek', str]] = Field(
        default=None,
        description="The day of the week for which these opening hours are valid.",
    )
    provider: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="The service provider, service operator, or service performer; the goods producer."
     "Another party (a seller) may offer those services or goods on behalf of the provider."
     "A provider may also serve as the seller.",
    )
    financialAidEligible: Optional[Union[List[Union[str, 'Text', 'DefinedTerm']], str, 'Text', 'DefinedTerm']] = Field(
        default=None,
        description="A financial aid type or program which students may use to pay for tuition or fees associated"
     "with the program.",
    )
    programPrerequisites: Optional[Union[List[Union[str, 'Text', 'EducationalOccupationalCredential', 'AlignmentObject', 'Course']], str, 'Text', 'EducationalOccupationalCredential', 'AlignmentObject', 'Course']] = Field(
        default=None,
        description="Prerequisites for enrolling in the program.",
    )
    endDate: Optional[Union[List[Union[datetime, 'DateTime', date, 'Date', str]], datetime, 'DateTime', date, 'Date', str]] = Field(
        default=None,
        description="The end date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).",
    )
    hasCourse: Optional[Union[List[Union['Course', str]], 'Course', str]] = Field(
        default=None,
        description="A course or class that is one of the learning opportunities that constitute an educational"
     "/ occupational program. No information is implied about whether the course is mandatory"
     "or optional; no guarantee is implied about whether the course will be available to everyone"
     "on the program.",
    )
    occupationalCategory: Optional[Union[List[Union[str, 'Text', 'CategoryCode']], str, 'Text', 'CategoryCode']] = Field(
        default=None,
        description="A category describing the job, preferably using a term from a taxonomy such as [BLS O*NET-SOC](http://www.onetcenter.org/taxonomy.html),"
     "[ISCO-08](https://www.ilo.org/public/english/bureau/stat/isco/isco08/) or"
     "similar, with the property repeated for each applicable value. Ideally the taxonomy"
     "should be identified, and both the textual label and formal code for the category should"
     "be provided. Note: for historical reasons, any textual label and formal code provided"
     "as a literal may be assumed to be from O*NET-SOC.",
    )
    typicalCreditsPerTerm: Optional[Union[List[Union[int, 'Integer', 'StructuredValue', str]], int, 'Integer', 'StructuredValue', str]] = Field(
        default=None,
        description="The number of credits or units a full-time student would be expected to take in 1 term however"
     "'term' is defined by the institution.",
    )
    startDate: Optional[Union[List[Union[datetime, 'DateTime', date, 'Date', str]], datetime, 'DateTime', date, 'Date', str]] = Field(
        default=None,
        description="The start date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).",
    )
    occupationalCredentialAwarded: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'EducationalOccupationalCredential']], AnyUrl, 'URL', str, 'Text', 'EducationalOccupationalCredential']] = Field(
        default=None,
        description="A description of the qualification, award, certificate, diploma or other occupational"
     "credential awarded as a consequence of successful completion of this course or program.",
    )
    maximumEnrollment: Optional[Union[List[Union[int, 'Integer', str]], int, 'Integer', str]] = Field(
        default=None,
        description="The maximum number of students who may be enrolled in the program.",
    )
    timeToComplete: Optional[Union[List[Union['Duration', str]], 'Duration', str]] = Field(
        default=None,
        description="The expected length of time to complete the program if attending full-time.",
    )
    applicationDeadline: Optional[Union[List[Union[date, 'Date', str, 'Text']], date, 'Date', str, 'Text']] = Field(
        default=None,
        description="The date on which the program stops collecting applications for the next enrollment"
     "cycle. Flexible application deadlines (for example, a program with rolling admissions)"
     "can be described in a textual string, rather than as a DateTime.",
    )
    timeOfDay: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The time of day the program normally runs. For example, \"evenings\".",
    )
    trainingSalary: Optional[Union[List[Union['MonetaryAmountDistribution', str]], 'MonetaryAmountDistribution', str]] = Field(
        default=None,
        description="The estimated salary earned while in the program.",
    )
    programType: Optional[Union[List[Union[str, 'Text', 'DefinedTerm']], str, 'Text', 'DefinedTerm']] = Field(
        default=None,
        description="The type of educational or occupational program. For example, classroom, internship,"
     "alternance, etc.",
    )
    termsPerYear: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', str]], StrictInt, StrictFloat, 'Number', str]] = Field(
        default=None,
        description="The number of times terms of study are offered per year. Semesters and quarters are common"
     "units for term. For example, if the student can only take 2 semesters for the program in"
     "one year, then termsPerYear should be 2.",
    )
    salaryUponCompletion: Optional[Union[List[Union['MonetaryAmountDistribution', str]], 'MonetaryAmountDistribution', str]] = Field(
        default=None,
        description="The expected salary upon completing the training.",
    )
    educationalProgramMode: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        default=None,
        description="Similar to courseMode, the medium or means of delivery of the program as a whole. The value"
     "may either be a text label (e.g. \"online\", \"onsite\" or \"blended\"; \"synchronous\""
     "or \"asynchronous\"; \"full-time\" or \"part-time\") or a URL reference to a term from"
     "a controlled vocabulary (e.g. https://ceds.ed.gov/element/001311#Asynchronous"
     ").",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Duration import Duration
    from pydantic_schemaorg.Integer import Integer
    from pydantic_schemaorg.StructuredValue import StructuredValue
    from pydantic_schemaorg.Date import Date
    from pydantic_schemaorg.Demand import Demand
    from pydantic_schemaorg.Offer import Offer
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.EducationalOccupationalCredential import EducationalOccupationalCredential
    from pydantic_schemaorg.DayOfWeek import DayOfWeek
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.DefinedTerm import DefinedTerm
    from pydantic_schemaorg.AlignmentObject import AlignmentObject
    from pydantic_schemaorg.Course import Course
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.CategoryCode import CategoryCode
    from pydantic_schemaorg.MonetaryAmountDistribution import MonetaryAmountDistribution
    from pydantic_schemaorg.Number import Number


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
