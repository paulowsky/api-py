from abc import ABC, abstractmethod
from typing import Iterable, Optional

from app.entities import BaseModel


class ContextManagerRepository(ABC):
    @abstractmethod
    def commit(self):
        ...

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs) -> None:
        self.commit()


class BaseReadOnlyRepository(ABC):
    @abstractmethod
    def get(self, id: str) -> Optional[BaseModel]:
        ...

    @abstractmethod
    def list(self) -> Iterable[BaseModel]:
        ...


class BaseWriteOnlyRepository(ContextManagerRepository):
    @abstractmethod
    def add(self, other: BaseModel) -> BaseModel:
        ...

    @abstractmethod
    def update(self, other: BaseModel) -> BaseModel:
        ...

    @abstractmethod
    def remove(self, id: str) -> bool:
        ...


class BaseRepository(BaseReadOnlyRepository, BaseWriteOnlyRepository, ABC):
    ...
