"""fix sku

Revision ID: 0ebba81f141a
Revises: f21485c1ae29
Create Date: 2022-08-25 15:48:11.102331

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "0ebba81f141a"
down_revision = "f21485c1ae29"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, "products", ["sku"])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "products", type_="unique")
    # ### end Alembic commands ###