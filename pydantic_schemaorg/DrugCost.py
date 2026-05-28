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
from pydantic_schemaorg.MedicalEntity import MedicalEntity


class DrugCost(MedicalEntity):
    """The cost per unit of a medical drug. Note that this type is not meant to represent the price"
     "in an offer of a drug for sale; see the Offer type for that. This type will typically be used"
     "to tag wholesale or average retail cost of a drug, or maximum reimbursable cost. Costs"
     "of medical drugs vary widely depending on how and where they are paid for, so while this"
     "type captures some of the variables, costs should be used with caution by consumers of"
     "this schema's markup.

    See: https://schema.org/DrugCost
    Model depth: 3
    """
    valid_name: ClassVar[str] = "DrugCost"
    type_: str = Field("DrugCost", alias='@type')
    costCategory: Optional[Union[List[Union['DrugCostCategory', str]], 'DrugCostCategory', str]] = Field(
        default=None,
        description="The category of cost, such as wholesale, retail, reimbursement cap, etc.",
    )
    costCurrency: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The currency (in 3-letter) of the drug cost. See: http://en.wikipedia.org/wiki/ISO_4217.",
    )
    drugUnit: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The unit in which the drug is measured, e.g. '5 mg tablet'.",
    )
    costOrigin: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Additional details to capture the origin of the cost data. For example, 'Medicare Part"
     "B'.",
    )
    applicableLocation: Optional[Union[List[Union['AdministrativeArea', str]], 'AdministrativeArea', str]] = Field(
        default=None,
        description="The location in which the status applies.",
    )
    costPerUnit: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', str, 'Text', 'QualitativeValue']], StrictInt, StrictFloat, 'Number', str, 'Text', 'QualitativeValue']] = Field(
        default=None,
        description="The cost per unit of the drug.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.DrugCostCategory import DrugCostCategory
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.AdministrativeArea import AdministrativeArea
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.QualitativeValue import QualitativeValue


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
