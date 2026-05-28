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


class MemberProgramTier(Intangible):
    """A MemberProgramTier specifies a tier under a loyalty (member) program, for example"
     "\"gold\".

    See: https://schema.org/MemberProgramTier
    Model depth: 3
    """
    valid_name: ClassVar[str] = "MemberProgramTier"
    type_: str = Field("MemberProgramTier", alias='@type')
    hasTierBenefit: Optional[Union[List[Union['TierBenefitEnumeration', str]], 'TierBenefitEnumeration', str]] = Field(
        default=None,
        description="A member benefit for a particular tier of a loyalty program.",
    )
    membershipPointsEarned: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', 'QuantitativeValue', str]], StrictInt, StrictFloat, 'Number', 'QuantitativeValue', str]] = Field(
        default=None,
        description="The number of membership points earned by the member. If necessary, the unitText can"
     "be used to express the units the points are issued in. (E.g. stars, miles, etc.)",
    )
    hasTierRequirement: Optional[Union[List[Union[str, 'Text', 'MonetaryAmount', 'UnitPriceSpecification', 'CreditCard']], str, 'Text', 'MonetaryAmount', 'UnitPriceSpecification', 'CreditCard']] = Field(
        default=None,
        description="A requirement for a user to join a membership tier, for example: a CreditCard if the tier"
     "requires sign up for a credit card, A UnitPriceSpecification if the user is required"
     "to pay a (periodic) fee, or a MonetaryAmount if the user needs to spend a minimum amount"
     "to join the tier. If a tier is free to join then this property does not need to be specified.",
    )
    isTierOf: Optional[Union[List[Union['MemberProgram', str]], 'MemberProgram', str]] = Field(
        default=None,
        description="The member program this tier is a part of.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.TierBenefitEnumeration import TierBenefitEnumeration
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.MonetaryAmount import MonetaryAmount
    from pydantic_schemaorg.UnitPriceSpecification import UnitPriceSpecification
    from pydantic_schemaorg.CreditCard import CreditCard
    from pydantic_schemaorg.MemberProgram import MemberProgram


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
