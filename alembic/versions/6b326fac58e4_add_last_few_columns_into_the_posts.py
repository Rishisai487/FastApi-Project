"""add last few columns into the posts

Revision ID: 6b326fac58e4
Revises: 270221920fac
Create Date: 2026-02-23 15:44:26.100232

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6b326fac58e4'
down_revision: Union[str, Sequence[str], None] = '270221920fac'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
