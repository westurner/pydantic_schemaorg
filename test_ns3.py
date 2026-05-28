import inspect
from pydantic import BaseModel
print(inspect.signature(BaseModel.model_rebuild))
