from typing import Iterable, Optional
from pydantic import BaseModel, UUID4
from fastapi import HTTPException
from uuid import uuid4

from app.entities.user import UserEntity
from app.repositories import BaseRepository
from app.use_cases import BaseUseCase


def transform(origin: BaseModel) -> UserEntity:
    return UserEntity(**origin.model_dump())


class UserListUseCase(BaseUseCase):
    repo: BaseRepository

    def __init__(self, repo: BaseRepository) -> None:
        self.repo = repo

    def execute(self) -> Iterable[UserEntity]:
        return self.repo.list()

class UserGetUseCase(BaseUseCase):
    repo: BaseRepository

    def __init__(self, repo: BaseRepository) -> None:
        self.repo = repo

    def execute(self, id: UUID4) -> Optional[UserEntity]:
        return self.repo.get(id)

class UserAddUseCase(BaseUseCase):
    repo: BaseRepository

    def __init__(self, repo: BaseRepository) -> None:
        self.repo = repo

    def execute(self, data: BaseModel) -> UserEntity:
        entity = transform(data)
        entity.id = uuid4()
        return self.repo.add(entity)

class UserUpdateUseCase(BaseUseCase):
    repo: BaseRepository

    def __init__(self, repo: BaseRepository) -> None:
        self.repo = repo

    def execute(self, data: BaseModel) -> UserEntity:
        entity = self.repo.get(data.id)
        if entity == None:
            raise HTTPException(status_code=404, detail="User not found")
        return self.repo.update(transform(data))

class UserRemoveUseCase(BaseUseCase):
    repo: BaseRepository

    def __init__(self, repo: BaseRepository) -> None:
        self.repo = repo

    def execute(self, id: UUID4) -> None:
        return self.repo.remove(id)
