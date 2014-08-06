"""Migration:
    - Rename work_place table to workplace.
"""

from sqlalchemy import *
from migrate import *

from migrate.changeset import schema

pre_meta = MetaData()
post_meta = MetaData()
work_place = Table('work_place', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=32)),
    Column('start_date', DATETIME),
    Column('end_date', DATETIME),
    Column('address_id', INTEGER),
    Column('user_id', INTEGER),
)

workplace = Table('workplace', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=32)),
    Column('start_date', DateTime),
    Column('end_date', DateTime),
    Column('address_id', Integer),
    Column('user_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['work_place'].drop()
    post_meta.tables['workplace'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['work_place'].create()
    post_meta.tables['workplace'].drop()
