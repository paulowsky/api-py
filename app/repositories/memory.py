from abc import ABC
from typing import Iterable
from typing import Optional

from app.entities import BaseEntity
from app.repositories import BaseRepository


class MemoryRepository(BaseRepository, ABC):
    def __init__(self) -> None:
        self.data: list[BaseEntity] = []

    def get(self, id: str) -> Optional[BaseEntity]:
        id = str(id)
        return next((e for e in self.data if e.id == id), None)

    def list(self) -> Iterable[BaseEntity]:
        return self.data

    def add(self, other: BaseEntity) -> BaseEntity:
        other.id = str(other.id)
        self.data.append(other)
        return other

    def update(self, other: BaseEntity) -> BaseEntity:
        id = str(other.id)
        existing_entity = self.get(id)
        if not existing_entity:
            return existing_entity
        for attr, value in vars(other).items():
            if attr != "id":
                if value is not None:  # Only update non-None values
                    setattr(existing_entity, attr, value)
        return existing_entity

    def remove(self, id: str) -> None:
        id = str(id)
        self.data = list(filter(lambda e: e.id != id, self.data))

    def commit(self) -> None: ...
