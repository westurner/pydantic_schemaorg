from typing import ForwardRef, Optional, Union, List, Any
from pydantic import AnyUrl
f = ForwardRef("Optional[Union[List[Union[AnyUrl, 'URL', str]], AnyUrl, 'URL', str]]")
class MockURL: pass
localns = {'URL': MockURL, 'AnyUrl': AnyUrl, 'Optional': Optional, 'Union': Union, 'List': List}
print(f._evaluate(globals(), localns, frozenset(), recursive_guard=set()))
