from pydantic import BaseModel
from typing import Optional, List, ForwardRef
import gc

class A(BaseModel):
    b: Optional[ForwardRef("B")] = None

class B(BaseModel):
    a: Optional[List[A]] = None
    c: Optional[ForwardRef("C")] = None

class C(BaseModel):
    b: Optional[B] = None

B.model_rebuild()
print("Success B")
A.model_rebuild()
print("Success A")
