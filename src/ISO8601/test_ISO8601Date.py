#    Year:
#       YYYY (eg 1997)
#    Year and month:
#       YYYY-MM (eg 1997-07)
#    Complete date:
#       YYYY-MM-DD (eg 1997-07-16)
#    Complete date plus hours and minutes:
#       YYYY-MM-DDThh:mmTZD (eg 1997-07-16T19:20+01:00)
#    Complete date plus hours, minutes and seconds:
#       YYYY-MM-DDThh:mm:ssTZD (eg 1997-07-16T19:20:30+01:00)
#    Complete date plus hours, minutes, seconds and a decimal fraction of a
# second
#       YYYY-MM-DDThh:mm:ss.sTZD (eg 1997-07-16T19:20:30.45+01:00)
import pytest
from pydantic import BaseModel

from pydantic_schemaorg.ISO8601.ISO8601Date import ISO8601Date


class ISO8601DateModel(BaseModel):
    testDate: ISO8601Date


test_dates = {'1997', '1997-07', '1997-07-16', '1997-07-16T19:20+01:00', '1997-07-16T19:20:30+01:00',
              '1997-07-16T19:20:30.45+01:00'}


@pytest.mark.parametrize("test_date", sorted(test_dates))
def test_iso8601_date_accepts_valid_values(test_date):
    ISO8601DateModel(testDate=test_date)
