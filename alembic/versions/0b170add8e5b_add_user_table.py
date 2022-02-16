"""add_user_table

Revision ID: 0b170add8e5b
Revises: 656f30cb9d7e
Create Date: 2022-02-16 19:43:50.937203

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b170add8e5b'
down_revision = '656f30cb9d7e'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users', sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'))
    
    pass


def downgrade():
    op.drop_table('users')
    pass
