from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('first_name', String(length=32), nullable=False),
    Column('last_name', String(length=32), nullable=False),
    Column('email', String(length=64)),
    Column('alt_email', String(length=64)),
    Column('phone', String(length=32)),
    Column('github', String(length=64)),
    Column('linkedin', String(length=64)),
    Column('skype', String(length=64)),
    Column('intro', Text),
    Column('address_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['user'].columns['alt_email'].create()
    post_meta.tables['user'].columns['skype'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['user'].columns['alt_email'].drop()
    post_meta.tables['user'].columns['skype'].drop()
