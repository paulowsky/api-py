from sqlalchemy.orm import declarative_base
from abc import abstractmethod
from typing import Optional
from abc import ABCMeta

from pydantic.dataclasses import dataclass


@dataclass
class BaseEntity(metaclass=ABCMeta):
    id: Optional[str]

    @classmethod
    @abstractmethod
    def from_dict(cls, other: dict): ...

    @abstractmethod
    def to_dict(self): ...


BaseModel = declarative_base()
