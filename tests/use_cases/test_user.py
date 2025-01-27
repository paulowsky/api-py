from uuid import UUID

from app.dtos.user import UserAddRequest, UserUpdateRequest
from app.repositories.memory import MemoryRepository
from app.use_cases.user import UserAddUseCase, UserGetUseCase, UserListUseCase, UserUpdateUseCase, UserRemoveUseCase


def test_user_add_use_case():
    # Add a user
    repo = MemoryRepository()
    add_use_case = UserAddUseCase(repo)
    data = { "name": "test", "email": "me@test.com" }
    user = UserAddRequest(**data)
    added_user = add_use_case.execute(user)

    # Assertions
    try:
        uuid_obj = UUID(added_user.id, version=4)
        assert str(uuid_obj) == added_user.id
    except ValueError:
        assert False, f"ID {added_user.id} is not a valid UUID"
    assert added_user.name == data["name"]
    assert added_user.email == data["email"]


def test_user_get_use_case():
    # Add a user
    repo = MemoryRepository()
    add_use_case = UserAddUseCase(repo)
    user_data = {"name": "test", "email": "me@test.com"}
    user = UserAddRequest(**user_data)
    added_user = add_use_case.execute(user)

    # Get the user
    get_use_case = UserGetUseCase(repo)
    fetched_user = get_use_case.execute(str(added_user.id))

    # Assertions
    assert fetched_user.id == added_user.id
    assert fetched_user.name == user_data["name"]
    assert fetched_user.email == user_data["email"]


def test_user_list_use_case():
    # Add multiple users
    repo = MemoryRepository()
    add_use_case = UserAddUseCase(repo)
    users_data = [
        {"name": "user1", "email": "user1@test.com"},
        {"name": "user2", "email": "user2@test.com"},
    ]
    for user_data in users_data:
        user = UserAddRequest(**user_data)
        add_use_case.execute(user)

    # List users
    list_use_case = UserListUseCase(repo)
    users = list_use_case.execute()

    # Assertions
    assert len(users) == len(users_data)
    for i, user in enumerate(users):
        assert user.name == users_data[i]["name"]
        assert user.email == users_data[i]["email"]


def test_user_update_use_case():
    # Add a user
    repo = MemoryRepository()
    add_use_case = UserAddUseCase(repo)
    user_data = {"name": "test", "email": "me@test.com"}
    user = UserAddRequest(**user_data)
    added_user = add_use_case.execute(user)

    # Update the user
    update_use_case = UserUpdateUseCase(repo)
    updated_user_data = {"id": str(added_user.id), "name": "updated_name", "email": "updated@test.com"}
    updated_user = UserUpdateRequest(**updated_user_data)
    result = update_use_case.execute(updated_user)

    # Get the updated user
    fetched_user = repo.get(str(added_user.id))

    # Assertions
    assert result.id == added_user.id
    assert result.name == updated_user_data["name"]
    assert result.email == updated_user_data["email"]
    assert fetched_user.name == updated_user_data["name"]
    assert fetched_user.email == updated_user_data["email"]


def test_user_remove_use_case():
    # Add a user
    repo = MemoryRepository()
    add_use_case = UserAddUseCase(repo)
    user_data = {"name": "test", "email": "me@test.com"}
    user = UserAddRequest(**user_data)
    added_user = add_use_case.execute(user)

    # Remove the user
    remove_use_case = UserRemoveUseCase(repo)
    remove_use_case.execute(added_user.id)

    # Assertions
    assert repo.get(added_user.id) is None
    assert all(u.id != added_user.id for u in repo.list())
