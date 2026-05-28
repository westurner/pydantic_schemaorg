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
from pydantic_schemaorg.HowTo import HowTo


class Recipe(HowTo):
    """A recipe. For dietary restrictions covered by the recipe, a few common restrictions"
     "are enumerated via [[suitableForDiet]]. The [[keywords]] property can also be used"
     "to add more detail.

    See: https://schema.org/Recipe
    Model depth: 4
    """
    valid_name: ClassVar[str] = "Recipe"
    type_: str = Field("Recipe", alias='@type')
    recipeCuisine: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The cuisine of the recipe (for example, French or Ethiopian).",
    )
    recipeInstructions: Optional[Union[List[Union[str, 'Text', 'CreativeWork', 'ItemList']], str, 'Text', 'CreativeWork', 'ItemList']] = Field(
        default=None,
        description="A step in making the recipe, in the form of a single item (document, video, etc.) or an ordered"
     "list with HowToStep and/or HowToSection items.",
    )
    ingredients: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="A single ingredient used in the recipe, e.g. sugar, flour or garlic.",
    )
    nutrition: Optional[Union[List[Union['NutritionInformation', str]], 'NutritionInformation', str]] = Field(
        default=None,
        description="Nutrition information about the recipe or menu item.",
    )
    recipeIngredient: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="A single ingredient used in the recipe, e.g. sugar, flour or garlic.",
    )
    recipeCategory: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The category of the recipe—for example, appetizer, entree, etc.",
    )
    cookingMethod: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The method of cooking, such as Frying, Steaming, ...",
    )
    recipeYield: Optional[Union[List[Union[str, 'Text', 'QuantitativeValue']], str, 'Text', 'QuantitativeValue']] = Field(
        default=None,
        description="The quantity produced by the recipe (for example, number of people served, number of"
     "servings, etc).",
    )
    suitableForDiet: Optional[Union[List[Union['RestrictedDiet', str]], 'RestrictedDiet', str]] = Field(
        default=None,
        description="Indicates a dietary restriction or guideline for which this recipe or menu item is suitable,"
     "e.g. diabetic, halal etc.",
    )
    cookTime: Optional[Union[List[Union['Duration', str]], 'Duration', str]] = Field(
        default=None,
        description="The time it takes to actually cook the dish, in [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601).",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.CreativeWork import CreativeWork
    from pydantic_schemaorg.ItemList import ItemList
    from pydantic_schemaorg.NutritionInformation import NutritionInformation
    from pydantic_schemaorg.QuantitativeValue import QuantitativeValue
    from pydantic_schemaorg.RestrictedDiet import RestrictedDiet
    from pydantic_schemaorg.Duration import Duration


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
