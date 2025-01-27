from sqlalchemy import String, Column, DateTime, UUID
from datetime import datetime

from app.entities import BaseModel


class UserEntity(BaseModel):
    __tablename__ = "users"

    id = Column(UUID(), primary_key=True)
    created_at = Column(DateTime(), default=datetime.now)
    updated_at = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    name = Column(String(60))
    email = Column(String(320))

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, email={self.email!r})"
