"""add-column-to-posts

Revision ID: 841dc1fc8c76
Revises: 977acf5468fb
Create Date: 2022-07-24 15:05:51.090935

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '841dc1fc8c76'
down_revision = '977acf5468fb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts",sa.Column("share",sa.Integer,nullable=False))


def downgrade() -> None:
    op.drop_column("posts","share")
