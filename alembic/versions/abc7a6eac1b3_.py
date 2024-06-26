"""empty message

Revision ID: abc7a6eac1b3
Revises: 
Create Date: 2024-06-09 14:18:01.977236

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'abc7a6eac1b3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('auto',
    sa.Column('vin_code', sa.String(length=255), nullable=True),
    sa.Column('mark', sa.String(length=255), nullable=True),
    sa.Column('model', sa.String(length=255), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('mileage', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('carpost',
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('time_to_begin', sa.Time(), nullable=True),
    sa.Column('time_to_end', sa.Time(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('master',
    sa.Column('first_name', sa.String(length=255), nullable=False),
    sa.Column('last_name', sa.String(length=255), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('email', sa.String(length=320), nullable=False),
    sa.Column('hashed_password', sa.String(length=1024), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=False),
    sa.Column('is_verified', sa.Boolean(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_table('workorder',
    sa.Column('dt_to_create', sa.DateTime(), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('client',
    sa.Column('phone_number', sa.String(length=30), nullable=False),
    sa.Column('auto_id', sa.Integer(), nullable=True),
    sa.Column('first_name', sa.String(length=255), nullable=False),
    sa.Column('last_name', sa.String(length=255), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['auto_id'], ['auto.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reservation',
    sa.Column('dt_to_reserve', sa.Date(), nullable=True),
    sa.Column('time_from_reserve', sa.Time(), nullable=True),
    sa.Column('time_to_reserve', sa.Time(), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('work_order', sa.Integer(), nullable=True),
    sa.Column('car_post', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['car_post'], ['carpost.id'], ),
    sa.ForeignKeyConstraint(['work_order'], ['workorder.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('work',
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('master_id', sa.Integer(), nullable=True),
    sa.Column('work_order_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['master_id'], ['master.id'], ),
    sa.ForeignKeyConstraint(['work_order_id'], ['workorder.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('work')
    op.drop_table('reservation')
    op.drop_table('client')
    op.drop_table('workorder')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_table('master')
    op.drop_table('carpost')
    op.drop_table('auto')
    # ### end Alembic commands ###
