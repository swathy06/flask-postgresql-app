"""empty message

Revision ID: 32b48058cd02
Revises: 791cd7d80402
Create Date: 2017-05-02 17:00:45.486682

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32b48058cd02'
down_revision = '791cd7d80402'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('guests', sa.Column('partysize', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('guests', 'partysize')
    # ### end Alembic commands ###
