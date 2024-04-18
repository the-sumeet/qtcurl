from collections import namedtuple
from enum import Enum, auto

NameValue = namedtuple('NameValue', ['name', 'value'])


class Method(Enum):
    GET = auto()
    HEAD = auto()
    POST = auto()
    PUT = auto()
    PATCH = auto()
    DELETE = auto()
    OPTIONS = auto()

    @property
    def index(self):
        return list(Method).index(self)
