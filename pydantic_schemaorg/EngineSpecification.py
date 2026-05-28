from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from pydantic import AnyUrl
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.StructuredValue import StructuredValue


class EngineSpecification(StructuredValue):
    """Information about the engine of the vehicle. A vehicle can have multiple engines represented"
     "by multiple engine specification entities.

    See: https://schema.org/EngineSpecification
    Model depth: 4
    """
    valid_name: ClassVar[str] = "EngineSpecification"
    type_: str = Field("EngineSpecification", alias='@type')
    fuelType: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'QualitativeValue']], AnyUrl, 'URL', str, 'Text', 'QualitativeValue']] = Field(
        default=None,
        description="The type of fuel suitable for the engine or engines of the vehicle. If the vehicle has only"
     "one engine, this property can be attached directly to the vehicle.",
    )
    enginePower: Optional[Union[List[Union['QuantitativeValue', str]], 'QuantitativeValue', str]] = Field(
        default=None,
        description="The power of the vehicle's engine. Typical unit code(s): KWT for kilowatt, BHP for brake"
     "horsepower, N12 for metric horsepower (PS, with 1 PS = 735,49875 W) * Note 1: There are"
     "many different ways of measuring an engine's power. For an overview, see [http://en.wikipedia.org/wiki/Horsepower#Engine\_power\_test\_codes](http://en.wikipedia.org/wiki/Horsepower#Engine_power_test_codes)."
     "* Note 2: You can link to information about how the given value has been determined using"
     "the [[valueReference]] property. * Note 3: You can use [[minValue]] and [[maxValue]]"
     "to indicate ranges.",
    )
    engineType: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'QualitativeValue']], AnyUrl, 'URL', str, 'Text', 'QualitativeValue']] = Field(
        default=None,
        description="The type of engine or engines powering the vehicle.",
    )
    torque: Optional[Union[List[Union['QuantitativeValue', str]], 'QuantitativeValue', str]] = Field(
        default=None,
        description="The torque (turning force) of the vehicle's engine. Typical unit code(s): NU for newton"
     "metre (N m), F17 for pound-force per foot, or F48 for pound-force per inch * Note 1: You"
     "can link to information about how the given value has been determined (e.g. reference"
     "RPM) using the [[valueReference]] property. * Note 2: You can use [[minValue]] and [[maxValue]]"
     "to indicate ranges.",
    )
    engineDisplacement: Optional[Union[List[Union['QuantitativeValue', str]], 'QuantitativeValue', str]] = Field(
        default=None,
        description="The volume swept by all of the pistons inside the cylinders of an internal combustion"
     "engine in a single movement. Typical unit code(s): CMQ for cubic centimeter, LTR for"
     "liters, INQ for cubic inches * Note 1: You can link to information about how the given value"
     "has been determined using the [[valueReference]] property. * Note 2: You can use [[minValue]]"
     "and [[maxValue]] to indicate ranges.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.QualitativeValue import QualitativeValue
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue


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
