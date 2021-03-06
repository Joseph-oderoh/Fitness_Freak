"""Initial Migration

Revision ID: 0123c1ad42b0
Revises: b0fdda3b1c00
Create Date: 2022-05-18 15:02:52.372296

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0123c1ad42b0'
down_revision = 'b0fdda3b1c00'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('post_id', sa.Integer(), nullable=True))
    op.drop_constraint('comments_blog_id_fkey', 'comments', type_='foreignkey')
    op.create_foreign_key(None, 'comments', 'posts', ['post_id'], ['id'])
    op.drop_column('comments', 'blog_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('blog_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.create_foreign_key('comments_blog_id_fkey', 'comments', 'posts', ['blog_id'], ['id'])
    op.drop_column('comments', 'post_id')
    # ### end Alembic commands ###
