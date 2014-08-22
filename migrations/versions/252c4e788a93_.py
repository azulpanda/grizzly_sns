"""empty message

Revision ID: 252c4e788a93
Revises: None
Create Date: 2014-08-07 23:02:14.556000

"""

# revision identifiers, used by Alembic.
revision = '252c4e788a93'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=60), nullable=True),
    sa.Column('username', sa.String(length=45), nullable=True),
    sa.Column('gender', sa.Enum('F', 'M'), nullable=True),
    sa.Column('password', sa.String(length=100), nullable=True),
    sa.Column('mobile', sa.String(length=15), nullable=True),
    sa.Column('birthday', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('created_time', sa.DateTime(), nullable=True),
    sa.Column('edited_time', sa.DateTime(), nullable=True),
    sa.Column('is_edited', sa.Boolean(), nullable=True),
    sa.Column('is_secret', sa.Boolean(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('wall_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['wall_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('created_time', sa.DateTime(), nullable=True),
    sa.Column('edited_time', sa.DateTime(), nullable=True),
    sa.Column('is_edited', sa.Boolean(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comment')
    op.drop_table('post')
    op.drop_table('user')
    ### end Alembic commands ###
