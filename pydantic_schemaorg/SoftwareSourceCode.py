from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from typing import List, Optional, Union
from pydantic import AnyUrl


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class SoftwareSourceCode(CreativeWork):
    """Computer programming source code. Example: Full (compile ready) solutions, code snippet"
     "samples, scripts, templates.

    See: https://schema.org/SoftwareSourceCode
    Model depth: 3
    """
    valid_name: ClassVar[str] = "SoftwareSourceCode"
    type_: str = Field("SoftwareSourceCode", alias='@type')
    targetProduct: Optional[Union[List[Union['SoftwareApplication', str]], 'SoftwareApplication', str]] = Field(
        default=None,
        description="Target Operating System / Product to which the code applies. If applies to several versions,"
     "just the product name can be used.",
    )
    runtime: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Runtime platform or script interpreter dependencies (example: Java v1, Python 2.3,"
     ".NET Framework 3.0).",
    )
    runtimePlatform: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Runtime platform or script interpreter dependencies (example: Java v1, Python 2.3,"
     ".NET Framework 3.0).",
    )
    codeRepository: Optional[Union[List[Union[AnyUrl, 'URL', str]], AnyUrl, 'URL', str]] = Field(
        default=None,
        description="Link to the repository where the un-compiled, human readable code and related code is"
     "located (SVN, GitHub, CodePlex).",
    )
    sampleType: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="What type of code sample: full (compile ready) solution, code snippet, inline code,"
     "scripts, template.",
    )
    programmingLanguage: Optional[Union[List[Union[str, 'Text', 'ComputerLanguage']], str, 'Text', 'ComputerLanguage']] = Field(
        default=None,
        description="The computer programming language.",
    )
    codeSampleType: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="What type of code sample: full (compile ready) solution, code snippet, inline code,"
     "scripts, template.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.SoftwareApplication import SoftwareApplication
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.ComputerLanguage import ComputerLanguage


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
