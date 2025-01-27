"""create user table

Revision ID: 8f60fd58a5cf
Revises:
Create Date: 2025-01-27 12:13:00.452882

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8f60fd58a5cf'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(sa.DDL(
        """
            CREATE TABLE users (
                id UUID PRIMARY KEY,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                name VARCHAR(60),
                email VARCHAR(320)
            );
        """
    ))


def downgrade() -> None:
    op.execute(sa.DDL(
        """
            DROP TABLE users;
        """
    ))
