"""Add content Column to posts

Revision ID: 656f30cb9d7e
Revises: 5de976a20178
Create Date: 2022-02-16 00:06:36.319713

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '656f30cb9d7e'
down_revision = '5de976a20178'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
