from enum import Enum


class ResCode(Enum):
    SUCCESS = 200
    CREATED = 201
    NO_CONTENT = 204
    NOT_FOUND = 404
    CONFLICT = 409
