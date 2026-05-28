from pydantic import BaseModel, ConfigDict

class A(BaseModel):
    model_config = ConfigDict(defer_build=True)
print(A.model_config)
