"""Migrations:
   - Add two new columns, initial, position_title to workplace relation.
   - Add one new column, floor, and rename two existing columns, postal_code and
     province.
"""

from sqlalchemy import *
from migrate import *

from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
workplace = Table('workplace', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=32)),
    Column('initial', String(length=32)),
    Column('position_title', String(length=32)),
    Column('start_date', DateTime),
    Column('end_date', DateTime),
    Column('address_id', Integer),
    Column('user_id', Integer),
)

address = Table('address', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('street_name', VARCHAR(length=32)),
    Column('province', VARCHAR(length=32)),
    Column('country', VARCHAR(length=32)),
    Column('postal_code', VARCHAR(length=32)),
    Column('active', BOOLEAN),
    Column('apt_number', VARCHAR(length=32)),
    Column('city', VARCHAR(length=32)),
    Column('suite_number', VARCHAR(length=32)),
)

address = Table('address', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('apt_number', String(length=32)),
    Column('suite_number', String(length=32)),
    Column('floor', String(length=32)),
    Column('street_name', String(length=32)),
    Column('city', String(length=32)),
    Column('province_state', String(length=32)),
    Column('country', String(length=32)),
    Column('postalcode_zip', String(length=32)),
    Column('active', Boolean, default=ColumnDefault(True)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['workplace'].columns['initial'].create()
    post_meta.tables['workplace'].columns['position_title'].create()
    pre_meta.tables['address'].columns['postal_code'].drop()
    pre_meta.tables['address'].columns['province'].drop()
    post_meta.tables['address'].columns['floor'].create()
    post_meta.tables['address'].columns['postalcode_zip'].create()
    post_meta.tables['address'].columns['province_state'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['workplace'].columns['initial'].drop()
    post_meta.tables['workplace'].columns['position_title'].drop()
    pre_meta.tables['address'].columns['postal_code'].create()
    pre_meta.tables['address'].columns['province'].create()
    post_meta.tables['address'].columns['floor'].drop()
    post_meta.tables['address'].columns['postalcode_zip'].drop()
    post_meta.tables['address'].columns['province_state'].drop()
