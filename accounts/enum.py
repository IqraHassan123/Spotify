# accounts/enums.py

from enum import Enum

class UserRole(Enum):
    ARTIST = "artist"
    DISTRIBUTOR = "distributor"
    RECORD_LABEL = "record_label"

    @classmethod
    def choices(cls):
        return [(role.value, role.name.replace("_", " ").title()) for role in cls]
