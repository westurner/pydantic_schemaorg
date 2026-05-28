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
from pydantic_schemaorg.Physician import Physician


class IndividualPhysician(Physician):
    """An individual medical practitioner. For their official address use [[address]], for"
     "affiliations to hospitals use [[hospitalAffiliation]]. The [[practicesAt]] property"
     "can be used to indicate [[MedicalOrganization]] hospitals, clinics, pharmacies etc."
     "where this physician practices.

    See: https://schema.org/IndividualPhysician
    Model depth: 5
    """
    valid_name: ClassVar[str] = "IndividualPhysician"
    type_: str = Field("IndividualPhysician", alias='@type')
    practicesAt: Optional[Union[List[Union['MedicalOrganization', str]], 'MedicalOrganization', str]] = Field(
        default=None,
        description="A [[MedicalOrganization]] where the [[IndividualPhysician]] practices.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.MedicalOrganization import MedicalOrganization


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
