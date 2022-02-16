"""add_foreignkey_to_posts

Revision ID: 959ac55184fc
Revises: 0b170add8e5b
Create Date: 2022-02-16 19:58:02.001071

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '959ac55184fc'
down_revision = '0b170add8e5b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table='posts', referent_table='users', local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
