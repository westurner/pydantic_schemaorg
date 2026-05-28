from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from pydantic import StrictInt, StrictFloat
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.OrganizationRole import OrganizationRole


class EmployeeRole(OrganizationRole):
    """A subclass of OrganizationRole used to describe employee relationships.

    See: https://schema.org/EmployeeRole
    Model depth: 5
    """
    valid_name: ClassVar[str] = "EmployeeRole"
    type_: str = Field("EmployeeRole", alias='@type')
    baseSalary: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', 'PriceSpecification', 'MonetaryAmount', str]], StrictInt, StrictFloat, 'Number', 'PriceSpecification', 'MonetaryAmount', str]] = Field(
        default=None,
        description="The base salary of the job or of an employee in an EmployeeRole.",
    )
    salaryCurrency: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The currency (coded using [ISO 4217](http://en.wikipedia.org/wiki/ISO_4217))"
     "used for the main salary information in this job posting or for this employee.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.PriceSpecification import PriceSpecification
    from pydantic_schemaorg.MonetaryAmount import MonetaryAmount
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
