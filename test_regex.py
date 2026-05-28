import re
from typing import ForwardRef
f = ForwardRef("Optional[Union[List[Union[AnyUrl, 'URL', str]], AnyUrl, 'URL', str]]")
print(re.findall(r"'([A-Za-z0-9_]+)'", f.__forward_arg__))
print(re.findall(r"\b([A-Z][A-Za-z0-9_]+)\b", f.__forward_arg__))
