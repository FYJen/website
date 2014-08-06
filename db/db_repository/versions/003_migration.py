"""Migrations:
    - Add 'apt_number', 'suite_number' and 'city' columns to Address table.
"""

from sqlalchemy import *
from migrate import *

from migrate.changeset import schema

pre_meta = MetaData()
post_meta = MetaData()
address = Table('address', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('apt_number', String(length=32)),
    Column('suite_number', String(length=32)),
    Column('street_name', String(length=32)),
    Column('city', String(length=32)),
    Column('province', String(length=32)),
    Column('country', String(length=32)),
    Column('postal_code', String(length=32)),
    Column('active', Boolean, default=ColumnDefault(True)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['address'].columns['apt_number'].create()
    post_meta.tables['address'].columns['city'].create()
    post_meta.tables['address'].columns['suite_number'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['address'].columns['apt_number'].drop()
    post_meta.tables['address'].columns['city'].drop()
    post_meta.tables['address'].columns['suite_number'].drop()
