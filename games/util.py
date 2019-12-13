
from collections.abc import Hashable
from abc import ABC, abstractproperty, abstractmethod
from uuid import uuid4


class UUIDHash(ABC, Hashable):

    def __init__(self):
        self._uuid = uuid4()

    def __hash__(self):
        return hash(self._uuid)

    def __eq__(self, other):
        return self._uuid == other._uuid

    def __repr__(self):
        return f'{self.__class__.__name__} {hex(hash(self._uuid))}'
