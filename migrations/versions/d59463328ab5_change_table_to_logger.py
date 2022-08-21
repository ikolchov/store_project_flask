"""change table to logger

Revision ID: d59463328ab5
Revises: 123832d66958
Create Date: 2022-08-21 21:35:41.923162

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd59463328ab5'
down_revision = '123832d66958'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_products_logger',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.Column('order_create_date', sa.Date(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('qty', sa.Integer(), nullable=False),
    sa.Column('discount', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['item_id'], ['products.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('user_products')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_products',
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('product_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], name='user_products_product_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='user_products_user_id_fkey')
    )
    op.drop_table('user_products_logger')
    # ### end Alembic commands ###
