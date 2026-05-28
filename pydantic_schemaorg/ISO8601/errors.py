class ISO8601DateError(ValueError):
    code = 'ISO9801'


class ISO8601DateInvalid(ValueError):
    code = 'ISO9801 invalid date'