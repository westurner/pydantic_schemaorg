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
from pydantic_schemaorg.BioChemEntity import BioChemEntity


class MolecularEntity(BioChemEntity):
    """Any constitutionally or isotopically distinct atom, molecule, ion, ion pair, radical,"
     "radical ion, complex, conformer etc., identifiable as a separately distinguishable"
     "entity.

    See: https://schema.org/MolecularEntity
    Model depth: 3
    """
    valid_name: ClassVar[str] = "MolecularEntity"
    type_: str = Field("MolecularEntity", alias='@type')
    inChIKey: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="InChIKey is a hashed version of the full InChI (using the SHA-256 algorithm).",
    )
    molecularWeight: Optional[Union[List[Union[str, 'Text', 'QuantitativeValue']], str, 'Text', 'QuantitativeValue']] = Field(
        default=None,
        description="This is the molecular weight of the entity being described, not of the parent. Units should"
     "be included in the form '&lt;Number&gt; &lt;unit&gt;', for example '12 amu' or as '&lt;QuantitativeValue&gt;.",
    )
    smiles: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="A specification in form of a line notation for describing the structure of chemical species"
     "using short ASCII strings. Double bond stereochemistry \ indicators may need to be escaped"
     "in the string in formats where the backslash is an escape character.",
    )
    molecularFormula: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The empirical formula is the simplest whole number ratio of all the atoms in a molecule.",
    )
    potentialUse: Optional[Union[List[Union['DefinedTerm', str]], 'DefinedTerm', str]] = Field(
        default=None,
        description="Intended use of the BioChemEntity by humans.",
    )
    iupacName: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Systematic method of naming chemical compounds as recommended by the International"
     "Union of Pure and Applied Chemistry (IUPAC).",
    )
    chemicalRole: Optional[Union[List[Union['DefinedTerm', str]], 'DefinedTerm', str]] = Field(
        default=None,
        description="A role played by the BioChemEntity within a chemical context.",
    )
    inChI: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Non-proprietary identifier for molecular entity that can be used in printed and electronic"
     "data sources thus enabling easier linking of diverse data compilations.",
    )
    monoisotopicMolecularWeight: Optional[Union[List[Union[str, 'Text', 'QuantitativeValue']], str, 'Text', 'QuantitativeValue']] = Field(
        default=None,
        description="The monoisotopic mass is the sum of the masses of the atoms in a molecule using the unbound,"
     "ground-state, rest mass of the principal (most abundant) isotope for each element instead"
     "of the isotopic average mass. Please include the units in the form '&lt;Number&gt; &lt;unit&gt;',"
     "for example '770.230488 g/mol' or as '&lt;QuantitativeValue&gt;.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.DefinedTerm import DefinedTerm


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
