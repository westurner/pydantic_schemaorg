from pydantic import BaseModel, ConfigDict
import sys

print(getattr(ConfigDict, "defer_build", "Not Found"))
