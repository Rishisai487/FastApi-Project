"""add content column to post table

Revision ID: b8806b2df881
Revises: 398605870941
Create Date: 2026-02-23 14:44:50.120860

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b8806b2df881'
down_revision: Union[str, Sequence[str], None] = '398605870941'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))


def downgrade() -> None:
    op.drop_column('posts','content')
