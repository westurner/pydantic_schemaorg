import re
from typing import no_type_check, Optional, Dict, cast, Any, Pattern, TYPE_CHECKING, Generator, AnyStr, Union

from pydantic_schemaorg.ISO8601 import errors

_url_regex_cache: Union[Pattern[AnyStr], None] = None


def ISO8601Date_regex() -> Pattern[str]:
    global _url_regex_cache
    if _url_regex_cache is None:
        _url_regex_cache = re.compile(
            r'(?P<year>-?(?:[1-9][0-9]*)?[0-9]{4})-?(?P<month>1[0-2]|0[1-9])?-?(?P<day>3[01]|0[1-9]|[12][0-9])?(T(?P<hour>(2[0-3]|[01][0-9])))?(\:(?P<minute>[0-5][0-9]))?(\:(?P<second>[0-5][0-9]))?(\.(?P<microsecond>[0-9]+))?([+-](?P<timezone>([0-9]{2}\:[0-9]{2})|Z))?',
            re.IGNORECASE
        )
        return _url_regex_cache
    else:
        return _url_regex_cache


class ISO8601Date(str):
    @classmethod
    def __get_pydantic_core_schema__(cls, source_type, handler):
        import pydantic
        from pydantic import GetCoreSchemaHandler
        from pydantic_core import core_schema
        def validate_iso8601(value):
            if isinstance(value, cls):
                return value
            value = str(value)
            m = ISO8601Date_regex().match(value)
            if not m:
                raise ValueError(f"Invalid ISO8601 date: {value}")
            return cls(value)
        return core_schema.no_info_plain_validator_function(validate_iso8601)
    strip_whitespace = True
    min_length = 1
    max_length = 2 ** 16

    __slots__ = ('date', 'year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond', 'tz')

    @no_type_check
    def __new__(cls, date: Optional[str], **kwargs) -> object:
        obj = str.__new__(cls, cls.build(**kwargs) if date is None else date)
        # Optionally, parse and attach fields here if needed
        return obj

    @classmethod
    def __get_pydantic_core_schema__(cls, source_type, handler):
        from pydantic_core import core_schema
        def validate_iso8601(value):
            if isinstance(value, cls):
                return value
            value = str(value)
            m = ISO8601Date_regex().match(value)
            if not m:
                raise ValueError(f"Invalid ISO8601 date: {value}")
            return cls(value)
        return core_schema.json_or_python_schema(
            core_schema.no_info_plain_validator_function(validate_iso8601),
            core_schema.no_info_plain_validator_function(validate_iso8601)
        )

    @classmethod
    def build(
            cls,
            date: str,
            *,
            year: int,
            month: Optional[int] = None,
            day: Optional[int] = None,
            hour: Optional[int] = None,
            minute: Optional[int] = None,
            second: Optional[int] = None,
            microsecond: Optional[int] = None,
            tz: Optional[str] = None,
    ) -> str:
        date = ''
        # TODO: put this in while loop
        if year:
            date += str(year)
            if month:
                date += '-' + str(month)
                if day:
                    date += '-' + str(month)
                    if hour:
                        date += 'T' + str(hour)
                        if minute:
                            date += ':' + str(minute)
                            if second:
                                date += ':' + str(second)
                                if microsecond:
                                    date += '.' + str(microsecond)
        return date

<<<<<<< HEAD
    @classmethod
    def __get_pydantic_core_schema__(cls, source_type, handler) -> Any:
        from pydantic_core import core_schema
        def validate_iso8601(value):
            if isinstance(value, cls):
                return value
            value = str(value)
            if cls.strip_whitespace:
                value = value.strip()
            m = ISO8601Date_regex().match(value)
            if not m:
                raise ValueError(f"Invalid ISO8601 date: {value}")
            return cls(value)
        return core_schema.json_or_python_schema(
            core_schema.no_info_plain_validator_function(validate_iso8601),
            core_schema.no_info_plain_validator_function(validate_iso8601)
        )

    @classmethod
    def __get_pydantic_json_schema__(cls, core_schema, handler) -> Any:
=======

    @classmethod
    def __get_pydantic_json_schema__(cls, core_schema, handler):
>>>>>>> c251655 (REF:  utilities for dynamic model building, ISO8601Date class and error handling;)
        schema = handler(core_schema)
        schema.update({
            "minLength": cls.min_length,
            "maxLength": cls.max_length,
            "format": "ISO8601"
        })
        return schema

<<<<<<< HEAD
    @classmethod
    def validate_parts(cls, parts: Dict[str, str]) -> Dict[str, Union[str, int]]:
=======
    def validate_iso_date(self, value: Any):
        value = str(value)
        if self.__class__.strip_whitespace:
            value = value.strip()
        m = ISO8601Date_regex().match(value)
        assert m, 'ISO8601Date regex failed unexpectedly'
        parts = m.groupdict()
        parts = self.__class__.validate_parts(parts)

    @no_type_check
    def __new__(cls, date: Optional[str], **kwargs) -> object:
        obj = str.__new__(cls, cls.build(**kwargs) if date is None else date)
        return obj
>>>>>>> c251655 (REF:  utilities for dynamic model building, ISO8601Date class and error handling;)
        """
