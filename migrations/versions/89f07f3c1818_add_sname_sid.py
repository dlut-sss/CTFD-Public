"""add_sname_sid

Revision ID: 89f07f3c1818
Revises: 46a278193a94
Create Date: 2022-04-28 11:38:30.893856

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "89f07f3c1818"
down_revision = "46a278193a94"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("users", sa.Column("sid", sa.String(length=20), nullable=True))
    op.add_column("users", sa.Column("sname", sa.String(length=20), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("users", "sname")
    op.drop_column("users", "sid")
    # ### end Alembic commands ###
