import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), '..')))
from pydantic_schemaorg.WebPage import WebPage
print(WebPage.model_fields['about'].annotation)
