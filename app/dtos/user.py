from pydantic import BaseModel, EmailStr, Field, UUID4


class UserAddRequest(BaseModel):
    name: str = Field(min_length=3, max_length=64)
    email: EmailStr

class UserUpdateRequest(BaseModel):
    id: UUID4
    name: str = Field(min_length=3, max_length=64)
    email: EmailStr


class UserResponse(BaseModel):
    id: UUID4
    name: str = Field(min_length=3, max_length=64)
    email: EmailStr

    class Config:
        from_attributes = True
        populate_by_name = True
