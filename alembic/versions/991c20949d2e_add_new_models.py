"""add new models

Revision ID: 991c20949d2e
Revises: 94072883f627
Create Date: 2024-06-04 18:36:47.485235

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '991c20949d2e'
down_revision: Union[str, None] = '94072883f627'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
