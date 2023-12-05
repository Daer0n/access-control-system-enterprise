"""Add new models: data

Revision ID: eff541c8d21c
Revises: f9e8f320ed7d
Create Date: 2023-12-05 19:55:16.586372

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eff541c8d21c'
down_revision: Union[str, None] = 'f9e8f320ed7d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Data',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('folder_id', sa.Integer(), nullable=True),
    sa.Column('rights', sa.Enum('READ', 'WRITE', 'DELETE', name='folderaccesstype'), nullable=True),
    sa.ForeignKeyConstraint(['folder_id'], ['Folder.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Data')
    # ### end Alembic commands ###
