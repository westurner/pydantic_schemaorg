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


from pydantic import Field
from pydantic_schemaorg.StructuredValue import StructuredValue


class PropertyValue(StructuredValue):
    """A property-value pair, e.g. representing a feature of a product or place. Use the 'name'"
     "property for the name of the property. If there is an additional human-readable version"
     "of the value, put that into the 'description' property. Always use specific schema.org"
     "properties when a) they exist and b) you can populate them. Using PropertyValue as a substitute"
     "will typically not trigger the same effect as using the original, specific property.

    See: https://schema.org/PropertyValue
    Model depth: 4
    """
    valid_name: ClassVar[str] = "PropertyValue"
    type_: str = Field("PropertyValue", alias='@type')
    unitText: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="A string or text indicating the unit of measurement. Useful if you cannot provide a standard"
     "unit code for <a href='unitCode'>unitCode</a>.",
    )
    minValue: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', str]], StrictInt, StrictFloat, 'Number', str]] = Field(
        default=None,
        description="The lower value of some characteristic or property.",
    )
    value: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', str, 'Text', StrictBool, 'Boolean', 'StructuredValue']], StrictInt, StrictFloat, 'Number', str, 'Text', StrictBool, 'Boolean', 'StructuredValue']] = Field(
        default=None,
        description="The value of a [[QuantitativeValue]] (including [[Observation]]) or property value"
     "node. * For [[QuantitativeValue]] and [[MonetaryAmount]], the recommended type for"
     "values is 'Number'. * For [[PropertyValue]], it can be 'Text', 'Number', 'Boolean',"
     "or 'StructuredValue'. * Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030)"
     "to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols. * Use"
     "'.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid"
     "using these symbols as a readability separator.",
    )
    measurementTechnique: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'MeasurementMethodEnum', 'DefinedTerm']], AnyUrl, 'URL', str, 'Text', 'MeasurementMethodEnum', 'DefinedTerm']] = Field(
        default=None,
        description="A technique, method or technology used in an [[Observation]], [[StatisticalVariable]]"
     "or [[Dataset]] (or [[DataDownload]], [[DataCatalog]]), corresponding to the method"
     "used for measuring the corresponding variable(s) (for datasets, described using [[variableMeasured]];"
     "for [[Observation]], a [[StatisticalVariable]]). Often but not necessarily each"
     "[[variableMeasured]] will have an explicit representation as (or mapping to) an property"
     "such as those defined in Schema.org, or other RDF vocabularies and \"knowledge graphs\"."
     "In that case the subproperty of [[variableMeasured]] called [[measuredProperty]]"
     "is applicable. The [[measurementTechnique]] property helps when extra clarification"
     "is needed about how a [[measuredProperty]] was measured. This is oriented towards scientific"
     "and scholarly dataset publication but may have broader applicability; it is not intended"
     "as a full representation of measurement, but can often serve as a high level summary for"
     "dataset discovery. For example, if [[variableMeasured]] is: molecule concentration,"
     "[[measurementTechnique]] could be: \"mass spectrometry\" or \"nmr spectroscopy\""
     "or \"colorimetry\" or \"immunofluorescence\". If the [[variableMeasured]] is \"depression"
     "rating\", the [[measurementTechnique]] could be \"Zung Scale\" or \"HAM-D\" or \"Beck"
     "Depression Inventory\". If there are several [[variableMeasured]] properties recorded"
     "for some given data object, use a [[PropertyValue]] for each [[variableMeasured]]"
     "and attach the corresponding [[measurementTechnique]]. The value can also be from"
     "an enumeration, organized as a [[MeasurementMetholdEnumeration]].",
    )
    propertyID: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        default=None,
        description="A commonly used identifier for the characteristic represented by the property, e.g."
     "a manufacturer or a standard code for a property. propertyID can be (1) a prefixed string,"
     "mainly meant to be used with standards for product properties; (2) a site-specific,"
     "non-prefixed string (e.g. the primary key of the property or the vendor-specific ID"
     "of the property), or (3) a URL indicating the type of the property, either pointing to"
     "an external vocabulary, or a Web resource that describes the property (e.g. a glossary"
     "entry). Standards bodies should promote a standard prefix for the identifiers of properties"
     "from their standards.",
    )
    measurementMethod: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text', 'MeasurementMethodEnum', 'DefinedTerm']], AnyUrl, 'URL', str, 'Text', 'MeasurementMethodEnum', 'DefinedTerm']] = Field(
        default=None,
        description="A subproperty of [[measurementTechnique]] that can be used for specifying specific"
     "methods, in particular via [[MeasurementMethodEnum]].",
    )
    maxValue: Optional[Union[List[Union[StrictInt, StrictFloat, 'Number', str]], StrictInt, StrictFloat, 'Number', str]] = Field(
        default=None,
        description="The upper value of some characteristic or property.",
    )
    valueReference: Optional[Union[List[Union[str, 'Text', 'Enumeration', 'QualitativeValue', 'PropertyValue', 'QuantitativeValue', 'StructuredValue', 'DefinedTerm', 'MeasurementTypeEnumeration']], str, 'Text', 'Enumeration', 'QualitativeValue', 'PropertyValue', 'QuantitativeValue', 'StructuredValue', 'DefinedTerm', 'MeasurementTypeEnumeration']] = Field(
        default=None,
        description="A secondary value that provides additional information on the original value, e.g."
     "a reference temperature or a type of measurement.",
    )
    unitCode: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        default=None,
        description="The unit of measurement given using the UN/CEFACT Common Code (3 characters) or a URL."
     "Other codes than the UN/CEFACT Common Code may be used with a prefix followed by a colon.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.Number import Number
    from pydantic_schemaorg.Boolean import Boolean
    from pydantic_schemaorg.StructuredValue import StructuredValue
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.MeasurementMethodEnum import MeasurementMethodEnum
    from pydantic_schemaorg.DefinedTerm import DefinedTerm
    from pydantic_schemaorg.Enumeration import Enumeration
    from pydantic_schemaorg.QualitativeValue import QualitativeValue
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.MeasurementTypeEnumeration import MeasurementTypeEnumeration


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
