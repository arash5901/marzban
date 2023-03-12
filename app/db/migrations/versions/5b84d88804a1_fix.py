"""fix

Revision ID: 5b84d88804a1
Revises: 7cbe9d91ac11
Create Date: 2023-03-08 15:41:25.827671

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b84d88804a1'
down_revision = '7cbe9d91ac11'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('hosts') as batch_op:
        batch_op.alter_column('sni',
                              existing_type=sa.VARCHAR(length=256),
                              nullable=True)
        batch_op.alter_column('host',
                              existing_type=sa.VARCHAR(length=256),
                              nullable=True)
    with op.batch_alter_table('users') as batch_op:
        batch_op.alter_column('status',
                              existing_type=sa.VARCHAR(length=8),
                              nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users') as batch_op:
        batch_op.alter_column('status',
                              existing_type=sa.VARCHAR(length=8),
                              nullable=True)
    with op.batch_alter_table('hosts') as batch_op:
        batch_op.alter_column('host',
                              existing_type=sa.VARCHAR(length=256),
                              nullable=False)
        batch_op.alter_column('sni',
                              existing_type=sa.VARCHAR(length=256),
                              nullable=False)
    # ### end Alembic commands ###