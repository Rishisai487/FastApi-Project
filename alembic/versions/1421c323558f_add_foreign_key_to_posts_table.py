"""add foreign-key to posts table

Revision ID: 1421c323558f
Revises: 2b003e0299a7
Create Date: 2026-02-23 15:06:20.647181

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1421c323558f'
down_revision: Union[str, Sequence[str], None] = '2b003e0299a7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('owner_id',sa.Integer(),nullable=False))
    op.create_foreign_key('posts_users_fk','posts','users',local_cols=['owner_id'],remote_cols=['id'],ondelete="CASCADE")


def downgrade() -> None:
    op.drop_constraint('posts_users_fk',table_name='posts')
    op.drop_column('owner_id')
