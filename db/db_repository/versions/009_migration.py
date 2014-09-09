from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
work_place = Table('work_place', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=32), nullable=False),
    Column('initial', String(length=32)),
    Column('web_link', String(length=64)),
    Column('position_title', String(length=32), nullable=False),
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
    post_meta.tables['work_place'].columns['web_link'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['work_place'].columns['web_link'].drop()
