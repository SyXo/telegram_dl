"""add profile_photo table

Revision ID: 977a5c5a397c
Revises: ccf4b069fbe3
Create Date: 2020-02-05 16:40:26.060974

"""
from alembic import op
import sqlalchemy as sa

import sqlalchemy_utils

from telegram_dl import db_model as dbm
from telegram_dl import db_model_enums as dbme


# revision identifiers, used by Alembic.
revision = '977a5c5a397c'
down_revision = 'ccf4b069fbe3'
branch_labels = None
depends_on = None


def upgrade():

    op.create_table('profile_photo',
        sa.Column('profile_photo_id', sa.Integer(), nullable=False),
        sa.Column('tg_profile_photo_id', sa.Integer(), nullable=True),
        sa.Column('big_id', sa.Integer(), nullable=True),
        sa.Column('small_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['big_id'], ['file.file_id'], ),
        sa.ForeignKeyConstraint(['small_id'], ['file.file_id'], ),
        sa.PrimaryKeyConstraint('profile_photo_id', name='PK-profile_photo-profile_photo_id')
    )

def downgrade():

    op.drop_table('profile_photo')
