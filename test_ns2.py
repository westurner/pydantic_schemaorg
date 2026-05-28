import inspect
from pydantic._internal._typing_extra import NsResolver
print(inspect.signature(NsResolver.__init__))
from pydantic._internal._model_construction import complete_model_class
print(inspect.signature(complete_model_class))
