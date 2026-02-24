"""create posts table

Revision ID: 398605870941
Revises: 
Create Date: 2026-02-23 14:32:29.842652

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '398605870941'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('posts',sa.Column('id',sa.Integer(),nullable=False)
                    ,sa.Column('title',sa.String(),nullable=False)
                    ,sa.Column('created_at',sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'))
                    ,sa.PrimaryKeyConstraint('id'))


def downgrade():
    op.drop_table('posts')
    pass
