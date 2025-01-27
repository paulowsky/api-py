from fastapi import APIRouter, Path, HTTPException
from typing import List, Annotated, Optional
from uuid import UUID

from app.repositories.user_postgres import PostgresRepository
from app.dtos.user import UserAddRequest, UserUpdateRequest, UserResponse
from app.use_cases.user import (
    UserListUseCase,
    UserGetUseCase,
    UserAddUseCase,
    UserUpdateUseCase,
    UserRemoveUseCase,
)


repo = PostgresRepository()
router = APIRouter()


@router.get("/user/")
async def list_user() -> List[UserResponse]:
    return [UserResponse.model_validate(e) for e in UserListUseCase(repo).execute()]


@router.get("/user/{id}")
async def get_users(
    id: Annotated[UUID, Path(title="The ID of the user")]
) -> Optional[UserResponse]:
    entity = UserGetUseCase(repo).execute(id)
    if entity is None:
        raise HTTPException(status_code=404, detail="User not found")
    return UserResponse.model_validate(entity)


@router.post("/user/")
async def add_user(user: UserAddRequest) -> UserResponse:
    entity = UserAddUseCase(repo).execute(user)
    return UserResponse.model_validate(entity)


@router.put("/user/")
async def update_user(user: UserUpdateRequest) -> UserResponse:
    entity = UserUpdateUseCase(repo).execute(user)
    return UserResponse.model_validate(entity)


@router.delete("/user/{id}")
async def remove_user(id: Annotated[UUID, Path(title="The ID of the user")]) -> dict:
    UserRemoveUseCase(repo).execute(id)
    return {}
