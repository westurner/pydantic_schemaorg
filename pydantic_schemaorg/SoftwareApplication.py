from __future__ import annotations
from typing import ClassVar
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field

from pydantic import AnyUrl, StrictBool, StrictInt, StrictFloat
from typing import List, Optional, Union


from pydantic import Field
from pydantic_schemaorg.CreativeWork import CreativeWork


class SoftwareApplication(CreativeWork):
    """A software application.

    See: https://schema.org/SoftwareApplication
    Model depth: 3
    """
    valid_name: ClassVar[str] = "SoftwareApplication"
    type_: str = Field("SoftwareApplication", alias='@type')
    screenshot: Optional[Union[List[Union[AnyUrl, 'URL', 'ImageObject', str]], AnyUrl, 'URL', 'ImageObject', str]] = Field(
        default=None,
        description="A link to a screenshot image of the app.",
    )
    downloadUrl: Optional[Union[List[Union[AnyUrl, 'URL', str]], AnyUrl, 'URL', str]] = Field(
        default=None,
        description="If the file can be downloaded, URL to download the binary.",
    )
    operatingSystem: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Operating systems supported (Windows 7, OS X 10.6, Android 1.6).",
    )
    requirements: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        default=None,
        description="Component dependency requirements for application. This includes runtime environments"
     "and shared libraries that are not included in the application distribution package,"
     "but required to run the application (examples: DirectX, Java or .NET runtime).",
    )
    softwareHelp: Optional[Union[List[Union['CreativeWork', str]], 'CreativeWork', str]] = Field(
        default=None,
        description="Software application help.",
    )
    permissions: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Permission(s) required to run the app (for example, a mobile app may require full internet"
     "access or may run only on wifi).",
    )
    installUrl: Optional[Union[List[Union[AnyUrl, 'URL', str]], AnyUrl, 'URL', str]] = Field(
        default=None,
        description="URL at which the app may be installed, if different from the URL of the item.",
    )
    applicationCategory: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        default=None,
        description="Type of software application, e.g. 'Game, Multimedia'.",
    )
    memoryRequirements: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        default=None,
        description="Minimum memory requirements.",
    )
    fileSize: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Size of the application / package (e.g. 18MB). In the absence of a unit (MB, KB etc.), KB"
     "will be assumed.",
    )
    applicationSubCategory: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        default=None,
        description="Subcategory of the application, e.g. 'Arcade Game'.",
    )
    softwareVersion: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Version of the software instance.",
    )
    applicationSuite: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="The name of the application suite to which the application belongs (e.g. Excel belongs"
     "to Office).",
    )
    storageRequirements: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        default=None,
        description="Storage requirements (free space required).",
    )
    countriesSupported: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Countries for which the application is supported. You can also provide the two-letter"
     "ISO 3166-1 alpha-2 country code.",
    )
    countriesNotSupported: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Countries for which the application is not supported. You can also provide the two-letter"
     "ISO 3166-1 alpha-2 country code.",
    )
    softwareRequirements: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        default=None,
        description="Component dependency requirements for application. This includes runtime environments"
     "and shared libraries that are not included in the application distribution package,"
     "but required to run the application (examples: DirectX, Java or .NET runtime).",
    )
    releaseNotes: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        default=None,
        description="Description of what changed in this version.",
    )
    processorRequirements: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Processor architecture required to run the application (e.g. IA64).",
    )
    supportingData: Optional[Union[List[Union['DataFeed', str]], 'DataFeed', str]] = Field(
        default=None,
        description="Supporting data for a SoftwareApplication.",
    )
    softwareAddOn: Optional[Union[List[Union['SoftwareApplication', str]], 'SoftwareApplication', str]] = Field(
        default=None,
        description="Additional content for a software application.",
    )
    availableOnDevice: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Device required to run the application. Used in cases where a specific make/model is"
     "required to run the application.",
    )
    featureList: Optional[Union[List[Union[AnyUrl, 'URL', str, 'Text']], AnyUrl, 'URL', str, 'Text']] = Field(
        default=None,
        description="Features or modules provided by this application (and possibly required by other applications).",
    )
    device: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        default=None,
        description="Device required to run the application. Used in cases where a specific make/model is"
     "required to run the application.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.URL import URL
    from pydantic_schemaorg.ImageObject import ImageObject
    from pydantic_schemaorg.Text import Text
    from pydantic_schemaorg.CreativeWork import CreativeWork
    from pydantic_schemaorg.DataFeed import DataFeed


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
