"""Create tables Client, Product and Request

Revision ID: aa05ed58c2fc
Revises: 
Create Date: 2020-11-19 01:32:01.893706

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aa05ed58c2fc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'client',
        sa.Column('id', sa.Integer, primary_key=True, nullable=False),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('cpf', sa.String,  nullable=False),
        sa.Column('email', sa.String, nullable=False),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_client')),
        sa.UniqueConstraint('cpf', name=op.f('uq_client_cpf')),
        sa.UniqueConstraint('email', name=op.f('uq_client_email'))
    )
    op.create_table(
        'product',
        sa.Column('id', sa.Integer, primary_key=True, nullable=False),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('code', sa.Integer, nullable=False),
        sa.Column('price', sa.Float, nullable=False),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_product')),
        sa.UniqueConstraint('code', name=op.f('uq_product_code'))
    )
    op.create_table('client_product',
                    sa.Column('client_id', sa.Integer(), nullable=True),
                    sa.Column('product_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['client_id'], ['client.id'], name=op.f('fk_client_product_client_id')),
                    sa.ForeignKeyConstraint(['product_id'], ['product.id'],
                                            name=op.f('fk_client_product_product_id_product'))
                    )


def downgrade():
    op.drop_table('client')
    op.drop_table('product')
    op.drop_table('client_product')
