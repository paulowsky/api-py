from abc import ABCMeta, abstractmethod
from typing import Any


class BaseAdapter(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def from_entity(cls, entity: Any):
        ...

    @abstractmethod
    def to_entity(self):
        ...
