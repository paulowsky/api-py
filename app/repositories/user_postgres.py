from abc import ABC
from uuid import UUID
from typing import Iterable
from typing import Optional
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config.env import settings
from app.entities import BaseModel
from app.entities.user import UserEntity
from app.repositories import BaseRepository


class PostgresRepository(BaseRepository, ABC):
    def __init__(self) -> None:
        engine = create_engine(settings.postgres_url, isolation_level="SERIALIZABLE")
        BaseModel.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.db_session = Session()

    def get(self, id: UUID) -> Optional[UserEntity]:
        return self.db_session.query(UserEntity).filter(UserEntity.id == id).first()

    def list(self) -> Iterable[UserEntity]:
        return self.db_session.query(UserEntity).all()

    def add(self, other: UserEntity) -> UserEntity:
        self.db_session.add(other)
        self.commit()
        return other

    def update(self, other: UserEntity) -> UserEntity:
        self.db_session.query(UserEntity).filter(UserEntity.id == other.id)\
            .update({
                UserEntity.name: other.name,
                UserEntity.email: other.email,
            })
        self.commit()
        return other

    def remove(self, id: UUID) -> None:
        self.db_session.query(UserEntity).filter(UserEntity.id == id).delete()
        self.commit()

    def commit(self) -> None:
        self.db_session.commit()
