"""initial configuration

Revision ID: 78472c1c0fd7
Revises: 
Create Date: 2024-04-04 21:00:01.568140

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '78472c1c0fd7'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('origins',
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('language', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('text', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('prename', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('gender', sa.String(), nullable=True),
    sa.Column('telephone', sa.String(), nullable=True),
    sa.Column('mail', sa.String(), nullable=True),
    sa.Column('birth', sa.String(), nullable=True),
    sa.Column('birth_location', sa.String(), nullable=True),
    sa.Column('nationality', sa.String(), nullable=True),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('thumbnails', sa.String(), nullable=True),
    sa.Column('is_completed', sa.BOOLEAN(), nullable=True),
    sa.Column('sys_role', sa.String(), nullable=True),
    sa.Column('assigned_language', sa.String(), nullable=True),
    sa.Column('status', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('mail'),
    sa.UniqueConstraint('username')
    )
    op.create_table('inscriptions',
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('dates', sa.TIMESTAMP(), nullable=True),
    sa.Column('code', sa.String(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('latitude', sa.String(), nullable=True),
    sa.Column('longitude', sa.String(), nullable=True),
    sa.Column('device', sa.String(), nullable=True),
    sa.Column('ip_address', sa.String(), nullable=True),
    sa.Column('operating_system', sa.String(), nullable=True),
    sa.Column('navigator', sa.String(), nullable=True),
    sa.Column('status', sa.INTEGER(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('logins',
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('dates', sa.TIMESTAMP(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('latitude', sa.String(), nullable=True),
    sa.Column('longitude', sa.String(), nullable=True),
    sa.Column('device', sa.String(), nullable=True),
    sa.Column('ip_address', sa.String(), nullable=True),
    sa.Column('operating_system', sa.String(), nullable=True),
    sa.Column('navigator', sa.String(), nullable=True),
    sa.Column('refresh_token', sa.TEXT(), nullable=True),
    sa.Column('connection_status', sa.INTEGER(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('origin_audios',
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('audio', sa.String(), nullable=True),
    sa.Column('origin_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['origin_id'], ['origins.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('translations',
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('language', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('text', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('audio', sa.String(), nullable=True),
    sa.Column('origin_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['origin_id'], ['origins.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('translations')
    op.drop_table('origin_audios')
    op.drop_table('logins')
    op.drop_table('inscriptions')
    op.drop_table('users')
    op.drop_table('origins')
    # ### end Alembic commands ###
