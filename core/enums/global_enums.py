from enum import Enum


class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = "Received status code is not equal to expected"


class Statuses(Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
