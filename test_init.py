import sys
import os
sys.path.insert(0, '')
from pydantic_schemaorg.WebPage import WebPage
try:
    WebPage.model_rebuild(_types_namespace=WebPage.get_local_ns())
except Exception as e:
    print(e)
print("done")
