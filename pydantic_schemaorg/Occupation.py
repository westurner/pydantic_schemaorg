from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from typing import List, Optional, Union
from pydantic import StrictInt, StrictFloat


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class Occupation(Intangible):
    """A profession, may involve prolonged training and/or a formal qualification.

    See: https://schema.org/Occupation
    Model depth: 3
    """
    valid_name: ClassVar[str] = "Occupation"
    type_: str = Field("Occupation", alias='@type')
    experienceRequirements: Optional[Union[List[Union[str, 'Text', 'OccupationalExperienceRequirements']], str, 'Text', 'OccupationalExperienceRequirements']] = Field(
        default=None,
        description="Description of skills and experience needed for the position or Occupation.",
    )
    responsibilities: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Responsibilities associated with this role or Occupation.",
    )
    skills: Optional[Union[List[Union[str, 'Text', 'DefinedTerm']], str, 'Text', 'DefinedTerm']] = Field(
        default=None,
        description="A statement of knowledge, skill, ability, task or any other assertion expressing a competency"
     "that is either claimed by a person, an organization or desired or required to fulfill"
     "a role or to work in an occupation.",
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
    qualifications: Optional[Union[List[Union[str, 'Text', 'EducationalOccupationalCredential']], str, 'Text', 'EducationalOccupationalCredential']] = Field(
        default=None,
        description="Specific qualifications required for this role or Occupation.",
    )
    occupationLocation: Optional[Union[List[Union['AdministrativeArea', str]], 'AdministrativeArea', str]] = Field(
        default=None,
        description="The region/country for which this occupational description is appropriate. Note that"
     "educational requirements and qualifications can vary between jurisdictions.",
    )
    educationRequirements: Optional[Union[List[Union[str, 'Text', 'EducationalOccupationalCredential']], str, 'Text', 'EducationalOccupationalCredential']] = Field(
        default=None,
        description="Educational background needed for the position or Occupation.",
    )
    estimatedSalary: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', 'MonetaryAmount', 'MonetaryAmountDistribution', str]], StrictInt, StrictFloat, 'Number', 'MonetaryAmount', 'MonetaryAmountDistribution', str]] = Field(
        default=None,
        description="An estimated salary for a job posting or occupation, based on a variety of variables including,"
     "but not limited to industry, job title, and location. Estimated salaries are often computed"
     "by outside organizations rather than the hiring organization, who may not have committed"
     "to the estimated value.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.OccupationalExperienceRequirements import OccupationalExperienceRequirements
    from pydantic_schemaorg.DefinedTerm import DefinedTerm
    from pydantic_schemaorg.CategoryCode import CategoryCode
    from pydantic_schemaorg.EducationalOccupationalCredential import EducationalOccupationalCredential
    from pydantic_schemaorg.AdministrativeArea import AdministrativeArea
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.MonetaryAmount import MonetaryAmount
    from pydantic_schemaorg.MonetaryAmountDistribution import MonetaryAmountDistribution


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
