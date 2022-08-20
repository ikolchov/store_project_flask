"""adjust table rev add column for fk right

Revision ID: 841cadb96972
Revises: 01617ac91686
Create Date: 2022-08-18 21:13:32.962876

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '841cadb96972'
down_revision = '01617ac91686'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('product_reviews_item_fkey', 'product_reviews', type_='foreignkey')
    op.create_foreign_key(None, 'product_reviews', 'products', ['item'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'product_reviews', type_='foreignkey')
    op.create_foreign_key('product_reviews_item_fkey', 'product_reviews', 'users', ['item'], ['id'])
    # ### end Alembic commands ###