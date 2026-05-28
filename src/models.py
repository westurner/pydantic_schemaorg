from typing import Optional, List

from pydantic import BaseModel, ConfigDict, field_validator


class PydanticBase(BaseModel):
    name: str
    description: str
    valid_name: Optional[str] = None

    from pydantic import model_validator

    @model_validator(mode="before")
    def set_valid_name(cls, values):
        name = values.get("name")
        valid_name = values.get("valid_name")
        if not name:
            raise ValueError("name is required")
        if not valid_name:
            if name in {"class", "def", "from", "import", "return", "yield", "True", "False"}:
                valid_name = f"{name}_"
            elif name[0].isdigit():
                valid_name = f"_{name}"
            else:
                valid_name = name
            values["valid_name"] = valid_name
        return values

    model_config = ConfigDict(validate_assignment=True)


class PydanticField(PydanticBase):
    type: str


class Import(BaseModel):
    type: str
    classPath: str
    classes_: set


class PydanticClass(PydanticBase):
    fields: List[PydanticField]
    parents: List['PydanticClass']
    depth: int = 1
    parent_imports: List[Import]
    field_imports: List[Import]
    pydantic_imports: List[Import] = []
    forward_refs: List[Import] = []
    filename: str = ""

    @field_validator("filename", mode="after")
    def filename_val(cls, v, values) -> str:
        if not values["valid_name"]:
            raise ValueError()
        filename = values["valid_name"]
        if filename in {
            "class",
            "def",
            "from",
            "import",
            "return",
            "yield",
        }:
            return f'{filename}_'
        return values['valid_name']


#PydanticClass.model_rebuild()
