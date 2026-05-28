from typing import Any, Optional

from pydantic import (
    BaseModel,
    Field,
    ConfigDict,
)


class SchemaOrgBase(BaseModel):
    # JSON-LD fields
    reverse_: Optional[Any] = Field(default=None, alias="@reverse")
    id_: Optional[Any] = Field(default=None, alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    def dict(self, *args, **kwargs):
        defaults = {"exclude_none": True, "by_alias": True}
        return super().dict(*args, **dict(defaults, **kwargs))

    def json(self, *args, **kwargs):
        defaults = {"exclude_none": True, "by_alias": True}
        return super().json(*args, **dict(defaults, **kwargs))

    model_config = ConfigDict(populate_by_name=True)

    @classmethod
    def _get_referenced_types(cls):
        from pydantic_schemaorg.utils import get_referenced_types

        return get_referenced_types(cls)

    @classmethod
    def _get_transitive_referenced_types(cls, visited=None):
        from pydantic_schemaorg.utils import get_transitive_referenced_types

        return get_transitive_referenced_types(cls, visited)

    @classmethod
    def model_rebuild(cls, **kwargs: Any) -> None:
        from pydantic_schemaorg.utils import rebuild_model

        rebuild_model(cls, **kwargs)

    def __init__(__pydantic_self__, **data: Any) -> None:
        type(__pydantic_self__).model_rebuild()
        super().__init__(**data)
