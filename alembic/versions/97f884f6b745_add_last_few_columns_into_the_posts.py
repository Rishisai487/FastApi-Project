"""add last few columns into the posts

Revision ID: 97f884f6b745
Revises: 1421c323558f
Create Date: 2026-02-23 15:12:33.730507

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '97f884f6b745'
down_revision: Union[str, Sequence[str], None] = '1421c323558f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('published',sa.Boolean(),server_default='TRUE'))


def downgrade() -> None:
    op.drop_column('posts','published')
