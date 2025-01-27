from typing import Optional
from typing import TypedDict
from uuid import uuid4

from app.entities import BaseEntity
from app.repositories.memory import MemoryRepository

class Dummy(TypedDict):
    id: Optional[str]
    field: Optional[str]


class DummyEntity(BaseEntity):
    @classmethod
    def from_dict(cls, other: dict):
        return cls(id=other["id"])

    def to_dict(self):
        return {"id": self.id}


def test_memory_repository_add_and_list():
    repo = MemoryRepository()
    entity = DummyEntity(id=str(uuid4()))
    other = repo.add(entity)
    entities = repo.list()

    assert any(e.id == other.id for e in entities)


def test_memory_repository_remove_and_list():
    repo = MemoryRepository()
    entity = DummyEntity(id=str(uuid4()))
    added_entity = repo.add(entity)
    repo.remove(added_entity.id)
    entities = repo.list()

    assert all(e.id != added_entity.id for e in entities)


def test_memory_repository_update_and_get():
    repo = MemoryRepository()
    original_entity = DummyEntity(id=str(uuid4()))
    original_entity.field = "old"
    added_entity = repo.add(original_entity)

    updated_entity = DummyEntity(id=str(added_entity.id))
    updated_entity.field = "new"

    result = repo.update(updated_entity)
    fetched_entity = repo.get(updated_entity.id)

    assert result == fetched_entity
    assert fetched_entity.field == "new"
