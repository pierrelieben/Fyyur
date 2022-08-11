"""empty message

Revision ID: e34b0a9c6e74
Revises: e7d1b140d871
Create Date: 2022-08-11 11:12:53.722330

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e34b0a9c6e74'
down_revision = 'e7d1b140d871'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artist', sa.Column('seeking_venue', sa.Boolean(), nullable=True))
    op.drop_column('artist', 'seeking_talent')
    op.add_column('venue', sa.Column('seeking_talent', sa.Boolean(), nullable=True))
    op.add_column('venue', sa.Column('seeking_description', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('venue', 'seeking_description')
    op.drop_column('venue', 'seeking_talent')
    op.add_column('artist', sa.Column('seeking_talent', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column('artist', 'seeking_venue')
    # ### end Alembic commands ###
