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


from pydantic import Field
from pydantic_schemaorg.Intangible import Intangible


class FinancialIncentive(Intangible):
    """<p>Represents financial incentives for goods/services offered by an organization"
     "(or individual).</p> <p>Typically contains the [[name]] of the incentive, the [[incentivizedItem]],"
     "the [[incentiveAmount]], the [[incentiveStatus]], [[incentiveType]], the [[provider]]"
     "of the incentive, and [[eligibleWithSupplier]].</p> <p>Optionally contains criteria"
     "on whether the incentive is limited based on [[purchaseType]], [[purchasePriceLimit]],"
     "[[incomeLimit]], and the [[qualifiedExpense]].

    See: https://schema.org/FinancialIncentive
    Model depth: 3
    """
    valid_name: ClassVar[str] = "FinancialIncentive"
    type_: str = Field("FinancialIncentive", alias='@type')
    incentivizedItem: Optional[Union[List[Union['Product', 'DefinedTerm', str]], 'Product', 'DefinedTerm', str]] = Field(
        default=None,
        description="The type or specific product(s) and/or service(s) being incentivized. <p>DefinedTermSets"
     "are used for product and service categories such as the United Nations Standard Products"
     "and Services Code:</p> { \"@type\": \"DefinedTerm\", \"inDefinedTermSet\": \"https://www.unspsc.org/\","
     "\"termCode\": \"261315XX\", \"name\": \"Photovoltaic module\" } <p>For a specific"
     "product or service, use the Product type:</p> { \"@type\": \"Product\", \"name\":"
     "\"Kenmore White 17\" Microwave\", } For multiple different incentivized items, use"
     "multiple [[DefinedTerm]] or [[Product]].",
    )
    purchasePriceLimit: Optional[Union[List[Union['MonetaryAmount', str]], 'MonetaryAmount', str]] = Field(
        default=None,
        description="Optional. The maximum price the item can have and still qualify for this offer.",
    )
    incentiveStatus: Optional[Union[List[Union['IncentiveStatus', str]], 'IncentiveStatus', str]] = Field(
        default=None,
        description="The status of the incentive (active, on hold, retired, etc.).",
    )
    purchaseType: Optional[Union[List[Union['PurchaseType', str]], 'PurchaseType', str]] = Field(
        default=None,
        description="Optional. The type of purchase the consumer must make in order to qualify for this incentive.",
    )
    provider: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="The service provider, service operator, or service performer; the goods producer."
     "Another party (a seller) may offer those services or goods on behalf of the provider."
     "A provider may also serve as the seller.",
    )
    validFrom: Optional[Union[List[Union[datetime, 'DateTime', date, 'Date', str]], datetime, 'DateTime', date, 'Date', str]] = Field(
        default=None,
        description="The date when the item becomes valid.",
    )
    areaServed: Optional[Union[List[Union[str, 'Text', 'Place', 'GeoShape', 'AdministrativeArea']], str, 'Text', 'Place', 'GeoShape', 'AdministrativeArea']] = Field(
        default=None,
        description="The geographic area where a service or offered item is provided.",
    )
    eligibleWithSupplier: Optional[Union[List[Union['Organization', str]], 'Organization', str]] = Field(
        default=None,
        description="The supplier of the incentivized item/service for which the incentive is valid for such"
     "as a utility company, merchant, or contractor.",
    )
    qualifiedExpense: Optional[Union[List[Union['IncentiveQualifiedExpenseType', str]], 'IncentiveQualifiedExpenseType', str]] = Field(
        default=None,
        description="Optional. The types of expenses that are covered by the incentive. For example some incentives"
     "are only for the goods (tangible items) but the services (labor) are excluded.",
    )
    incentiveAmount: Optional[Union[List[Union['LoanOrCredit', 'QuantitativeValue', 'UnitPriceSpecification', str]], 'LoanOrCredit', 'QuantitativeValue', 'UnitPriceSpecification', str]] = Field(
        default=None,
        description="Describes the amount that can be redeemed from this incentive. <p>[[QuantitativeValue]]:"
     "Use this for incentives based on price (either raw amount or percentage-based). For"
     "a raw amount example, \"You can claim $2,500 - $7,500 from the total cost of installation\""
     "would be represented as the following:</p> { \"@type\": \"QuantitativeValue\", “minValue”:"
     "2500, “maxValue”: 7500, \"unitCode\": \"USD\" } <p>[[QuantitivateValue]] can also"
     "be used for percentage amounts. In such cases, value is used to represent the incentive’s"
     "percentage, while maxValue represents a limit (if one exists) to that incentive. The"
     "unitCode should be 'P1' and the unitText should be '%', while valueReference should"
     "be used for holding the currency type. For example, \"You can claim up to 30% of the total"
     "cost of installation, up to a maximum of $7,500\" would be:</p> { \"@type\": \"QuantitativeValue\","
     "\"value\": 30, \"unitCode\": \"P1\", \"unitText\": \"%\", “maxValue”: 7500, “valueReference”:"
     "“USD” } <p>[[UnitPriceSpecification]]: Use this for incentives that are based on amounts"
     "rather than price. For example, a net metering rebate that pays $10/kWh, up to $1,000:</p>"
     "{ \"@type\": \"UnitPriceSpecification\", \"price\": 10, \"priceCurrency\": \"USD\","
     "\"referenceQuantity\": 1, \"unitCode\": \"DO3\", \"unitText\": \"kw/h\", \"maxPrice\":"
     "1000, \"description\": \"$10 / kwh up to $1000\" } <p>[[LoanOrCredit]]: Use for incentives"
     "that are loan based. For example, a loan of $4,000 - $50,000 with a repayment term of 10"
     "years, interest free would look like:</p> { \"@type\": \"LoanOrCredit\", \"loanTerm\":"
     "{ \"@type\":\"QuantitativeValue\", \"value\":\"10\", \"unitCode\": \"ANN\" },"
     "\"amount\":[ { \"@type\": \"QuantitativeValue\", \"Name\":\"fixed interest rate\","
     "\"value\":\"0\", }, ], \"amount\":[ { \"@type\": \"MonetaryAmount\", \"Name\":\"min"
     "loan amount\", \"value\":\"4000\", \"currency\":\"CAD\" }, { \"@type\": \"MonetaryAmount\","
     "\"Name\":\"max loan amount\", \"value\":\"50000\", \"currency\":\"CAD\" } ], }"
     "In summary: <ul><li>Use [[QuantitativeValue]] for absolute/percentage-based incentives"
     "applied on the price of a good/service.</li> <li>Use [[UnitPriceSpecification]]"
     "for incentives based on a per-unit basis (e.g. net metering).</li> <li>Use [[LoanOrCredit]]"
     "for loans/credits.</li> </ul>.",
    )
    incentiveType: Optional[Union[List[Union['IncentiveType', str]], 'IncentiveType', str]] = Field(
        default=None,
        description="The type of incentive offered (tax credit/rebate, tax deduction, tax waiver, subsidies,"
     "etc.).",
    )
    incomeLimit: Optional[Union[List[Union[str, 'Text', 'MonetaryAmount']], str, 'Text', 'MonetaryAmount']] = Field(
        default=None,
        description="Optional. Income limit for which the incentive is applicable for. <p>If MonetaryAmount"
     "is specified, this should be based on annualized income (e.g. if an incentive is limited"
     "to those making <$114,000 annually):</p> { \"@type\": \"MonetaryAmount\", \"maxValue\":"
     "114000, \"currency\": \"USD\", } Use Text for incentives that are limited based on other"
     "criteria, for example if an incentive is only available to recipients making 120% of"
     "the median poverty income in their area.",
    )
    publisher: Optional[Union[List[Union['Person', 'Organization', str]], 'Person', 'Organization', str]] = Field(
        default=None,
        description="The publisher of the article in question.",
    )
    validThrough: Optional[Union[List[Union[datetime, 'DateTime', date, 'Date', str]], datetime, 'DateTime', date, 'Date', str]] = Field(
        default=None,
        description="The date after when the item is not valid. For example the end of an offer, salary period,"
     "or a period of opening hours.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Product import Product
    from pydantic_schemaorg.DefinedTerm import DefinedTerm
    from pydantic_schemaorg.MonetaryAmount import MonetaryAmount
    from pydantic_schemaorg.IncentiveStatus import IncentiveStatus
    from pydantic_schemaorg.PurchaseType import PurchaseType
    from pydantic_schemaorg.Person import Person
    from pydantic_schemaorg.Organization import Organization
    from pydantic_schemaorg.DateTime import DateTime
    from pydantic_schemaorg.Date import Date
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Place import Place
    from pydantic_schemaorg.GeoShape import GeoShape
    from pydantic_schemaorg.AdministrativeArea import AdministrativeArea
    from pydantic_schemaorg.IncentiveQualifiedExpenseType import IncentiveQualifiedExpenseType
    from pydantic_schemaorg.LoanOrCredit import LoanOrCredit
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.UnitPriceSpecification import UnitPriceSpecification
    from pydantic_schemaorg.IncentiveType import IncentiveType


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
