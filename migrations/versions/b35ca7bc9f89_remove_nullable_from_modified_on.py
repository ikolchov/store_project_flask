"""remove nullable from modified_on

Revision ID: b35ca7bc9f89
Revises: bb6105c67abe
Create Date: 2022-08-07 16:06:59.090797

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b35ca7bc9f89'
down_revision = 'bb6105c67abe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('products', 'sku',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('products', 'sku',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###