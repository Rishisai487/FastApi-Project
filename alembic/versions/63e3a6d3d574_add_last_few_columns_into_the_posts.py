"""add last few columns into the posts

Revision ID: 63e3a6d3d574
Revises: ba44c1af9aea
Create Date: 2026-02-23 15:43:13.673114

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '63e3a6d3d574'
down_revision: Union[str, Sequence[str], None] = 'ba44c1af9aea'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
