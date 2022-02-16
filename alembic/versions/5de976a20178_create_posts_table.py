"""Create posts table

Revision ID: 5de976a20178
Revises: 
Create Date: 2022-02-15 23:54:00.808838

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5de976a20178'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer, nullable=False, primary_key=True), sa.Column('title', sa.String, nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
