"""Migration:
    - Add a new Tag table with a new relationship between Skill.
"""

from sqlalchemy import *
from migrate import *

from migrate.changeset import schema

pre_meta = MetaData()
post_meta = MetaData()
tag = Table('tag', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=32), nullable=False),
)

skill = Table('skill', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('description', Text),
    Column('selected', Boolean, default=ColumnDefault(True)),
    Column('tag_id', Integer),
    Column('user_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['tag'].create()
    post_meta.tables['skill'].columns['tag_id'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['tag'].drop()
    post_meta.tables['skill'].columns['tag_id'].drop()
