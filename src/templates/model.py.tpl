from __future__ import annotations
from typing import ClassVar
{%- if model.pydantic_imports %}
from typing import Any, List, Optional, Union, TYPE_CHECKING
from pydantic import StrictInt, StrictFloat, AnyUrl
from datetime import date, datetime, time
from decimal import Decimal
from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date
from pydantic import Field
{%- endif %}
{% if model.field_imports %}
{%- for import_ in model.field_imports %}
from {{import_.classPath}} import {{import_.classes_ | sort | join(', ')}}
{%- endfor %}
{% endif %}
{% for import_ in model.parent_imports%}
from {{import_.classPath}} import {{import_.classes_ | sort|join(', ')}}
{%- endfor %}


class {{ model.valid_name }}({{model.parents| sort(attribute='depth', reverse=True) | map(attribute='valid_name') | join(', ')}}):
    """{{ model.description | replace('\\n','\n') | format_description}}

    See: https://schema.org/{{ model.name }}
    Model depth: {{model.depth}}
    """
    valid_name: ClassVar[str] = "{{ model.valid_name }}"
    type_: str = Field("{{ model.name }}", alias='@type')
    {% for field in model.fields -%}
    {{ field.valid_name }}: {{ field.type }} = Field(
        default=None,
        {%- if field.valid_name != field.name -%} alias="{{ field.name }}",{% endif %}
        description="{{ field.description | replace('\\n','\n') | format_description }}",
    )
    {% endfor %}

{% if model.pydantic_imports %}
if TYPE_CHECKING:
{%- for import_ in model.pydantic_imports %}
    from {{import_.classPath}} import {{import_.classes_ | join(', ')}}
{%- endfor %}
{% endif %}

def __getattr__(name: str) -> Any:
    from pydantic_schemaorg.__types__ import types
    if name in types:
        import sys
        mod_name = types[name][1]
        mod = sys.modules.get(mod_name)
        if not mod:
            __import__(mod_name, fromlist=[name])
            mod = sys.modules[mod_name]
        val = getattr(mod, name)
        globals()[name] = val
        return val
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
