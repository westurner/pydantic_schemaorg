from pydantic_schemaorg import __types__
import importlib
mod = importlib.import_module(__types__.types['URL'][1])
URL = getattr(mod, 'URL')
print(type(URL))
print(URL)
